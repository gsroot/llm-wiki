## Source: claude_agent_sdk/01_The_chief_of_staff_agent.ipynb

# 01 - The Chief of Staff Agent

#### Introduction

In notebook 00, we built a simple research agent. In this notebook, we'll incrementally introduce key Claude Code SDK features for building comprehensive agents. For each introduced feature, we'll explain:
- **What**: what the feature is
- **Why**: what the feature can do and why you would want to use it
- **How**: a minimal implementation showing how to use it

If you are familiar with Claude Code, you'll notice how the SDK brings feature parity and enables you to leverage all of Claude Code's capabilities in a programmatic headless manner.

#### Scenario

Throughout this notebook, we'll build an **AI Chief of Staff** for a 50-person startup that just raised $10M Series A. The CEO needs data-driven insights to balance aggressive growth with financial sustainability.

Our final Chief of Staff agent will:
- **Coordinate specialized subagents** for different domains
- **Aggregate insights** from multiple sources
- **Provide executive summaries** with actionable recommendations

---

## Basic Features

---

### Feature 0: Memory with [CLAUDE.md](https://www.anthropic.com/engineering/claude-code-best-practices)

**What**: `CLAUDE.md` files serve as persistent memory and instructions for your agent. When present in the project directory, Claude Code automatically reads and incorporates this context when you initialize your agent.

**Why**: Instead of repeatedly providing project context, team preferences, or standards in each interaction, you can define them once in `CLAUDE.md`. This ensures consistent behavior and reduces token usage by avoiding redundant explanations.

**How**: 
- Have a `CLAUDE.md` file in the working directory - in our example: `chief_of_staff_agent/CLAUDE.md`
- Set the `cwd` argument of your ClaudeSDKClient to point to directory of your CLAUDE.md file
- Use explicit prompts to guide the agent when you want it to prefer high-level context over detailed data files

**Important Behavior Note**: When both CLAUDE.md and detailed data files (like CSVs) are available, the agent may prefer to read the more granular data sources to provide precise answers. This is expected behavior - agents naturally seek authoritative data. To ensure the agent uses high-level CLAUDE.md context, use explicit prompt instructions (see example below). This teaches an important lesson: CLAUDE.md provides *context and guidance*, not hard constraints on data sources.

---

#### Understanding Agent Data Source Preferences

**What Just Happened:**
By adding   to our prompt, we guided the agent to rely on the CLAUDE.md context rather than seeking more granular data from CSV files.

**Key Insights:**
1. **CLAUDE.md as Context, Not Constraint**: When you set `cwd`, the CLAUDE.md file is loaded as background context. However, agents will naturally seek the most authoritative data sources available. If detailed CSV files exist, the agent may prefer them for precision.

2. **Prompt Engineering Matters**: The phrasing "high-level financial numbers from context" signals to the agent that you want the simplified executive summary from CLAUDE.md ($500K burn, 20 months runway) rather than the precise month-by-month data from financial_data/burn_rate.csv ($525K gross, $235K net burn).

3. **Architectural Design Choice**: This behavior is actually desirable in production systems - you want agents to find the best data source. CLAUDE.md should contain:
   - High-level context and strategy
   - Company information and standards
   - Pointers to where detailed data lives
   - Guidelines on when to use high-level vs. detailed numbers

4. **Real-World Pattern**: Think of CLAUDE.md as an "onboarding document" that orients the agent, while detailed files are "source systems" the agent can query when precision matters.

---

### Feature 1: The Bash tool for Python Script Execution

**What**: The Bash tool allows your agent to (among other things) run Python scripts directly, enabling access to procedural knowledge, complex computations, data analysis and other integrations that go beyond the agent's native capabilities.

**Why**: Our Chief of Staff might need to process data files, run financial models or generate visualizations based on this data. These are all good scenarios for using the Bash tool.

**How**: Have your Python scripts set-up in a place where your agent can reach them and add some context on what they are and how they can be called. If the scripts are meant for your chief of staff agent, add this context to its CLAUDE.md file and if they are meant for one your subagents, add said context to their MD files (more details on this later). For this tutorial, we added five toy examples to `chief_of_staff_agent/scripts`:
1. `hiring_impact.py`: Calculates how new engineering hires affect burn rate, runway, and cash position. Essential for the `financial-analyst` subagent to model hiring scenarios against the $500K monthly burn and 20-month runway.
2. `talent_scorer.py`: Scores candidates on technical skills, experience, culture fit, and salary expectations using weighted criteria. Core tool for the `recruiter` subagent to rank engineering candidates against TechStart's $180-220K senior engineer benchmarks.
3. `simple_calculation.py`: Performs quick financial calculations for runway, burn rate, and quarterly metrics. Utility script for chief of staff to get instant metrics without complex modeling.
4. `financial_forecast.py`: Models ARR growth scenarios (base/optimistic/pessimistic) given the current $2.4M ARR growing at 15% MoM.Critical for `financial-analyst` to project Series B readiness and validate the $30M fundraising target.
5. `decision_matrix.py`: Creates weighted decision matrices for strategic choices like the SmartDev acquisition or office expansion. Helps chief of staff systematically evaluate complex decisions with multiple stakeholders and criteria.

---

### Feature 2: Output Styles

**What**: Output styles allow you to use different output styles for different audiences. Each style is defined in a markdown file.

**Why**: Your agent might be used by people of different levels of expertise or they might have different priorities. Your output style can help differentiate between these segments without having to create a separate agent.

**How**:
- Configure a markdown file per style in `chief_of_staff_agent/.claude/output-styles/`. For example, check out the Executive Ouput style in `.claude/output-styles/executive.md`. Output styles are defined with a simple frontmatter including two fields: name and description. Note: Make sure the name in the frontmatter matches exactly the file's name (case sensitive)

> **IMPORTANT**: Output styles modify the system prompt that Claude Code has underneath, leaving out the parts focused on software engineering and giving you more control for your specific use case beyond software engineering work.

> **SDK CONFIGURATION NOTE**: Similar to slash commands (covered in Feature 4), output styles are stored on the filesystem in `.claude/output-styles/`. For the SDK to load these files, you **must** include `setting_sources=["project"]` in your `ClaudeAgentOptions`. The `settings` parameter tells the SDK *which* style to use, but `setting_sources` is required to actually *load* the style definitions. This requirement was identified while debugging later sections and applies to all filesystem-based settings.

---

### Feature 3: Plan Mode - Strategic Planning Without Execution

**What**: Plan mode instructs the agent to create a detailed execution plan without performing any actions. The agent analyzes requirements, proposes solutions, and outlines steps, but doesn't modify files, execute commands, or make changes.

**Why**: Complex tasks benefit from upfront planning to reduce errors, enable review and improve coordination. After the planning phase, the agent will have a red thread to follow throughout its execution.

**How**: Just set `permission_mode="plan"`

**Plan Persistence**: Since plans are valuable artifacts for review and decision-making, we'll demonstrate how to capture and save them to persistent markdown files. This enables stakeholders to review plans before approving execution.

> Note: this feature shines in Claude Code but still needs to be fully adapted for headless applications with the SDK. Namely, the agent will try calling its `ExitPlanMode()` tool, which is only relevant in the interactive mode. In this case, you can send up a follow-up query with `continue_conversation=True` for the agent to execute its plan in context.

---

#### Executing the Saved Plan

As mentioned above, the agent will stop after creating its plan. The saved plan file serves as a review artifact for stakeholders.

**To execute the plan after review:**
1. Review the saved plan in `chief_of_staff_agent/plans/plan_*.md`
2. If approved, send a new query with `continue_conversation=True` and remove `permission_mode="plan"` to execute

This workflow enables a "plan → review → approve → execute" cycle, perfect for high-stakes decisions like organizational restructuring or major infrastructure changes.

---

#### How Plan Persistence Works

In the code above, we implemented a **robust multi-source plan capture mechanism** that handles the various ways Plan Mode agents may output their plans:

**The Challenge:**
When using `permission_mode="plan"`, the agent may output the plan in different ways:
1. **Direct text output** in the message stream (ideal case)
2. **Write tool** to save to `~/.claude/plans/` (Claude's internal plan system)
3. **Write tool** to save to a custom path

Our capture mechanism handles all three scenarios with a **priority-based fallback system**:

**Source Priority (in order):**

1. **Message Stream** (Preferred)
   - Capture text blocks from `msg.content` during streaming
   - Extract content between `<plan></plan>` XML tags
   - This is the cleanest approach as content comes directly from the response

2. **Write Tool Capture**
   - Monitor for Write tool calls in the message stream
   - Extract the `content` parameter being written
   - Useful when the agent decides to save despite prompt instructions

3. **Claude's Internal Plan Directory**
   - Check `~/.claude/plans/` for recently created plan files (within 5 minutes)
   - Read and extract content from the most recent file
   - Acts as a safety net when other methods fail

4. **Full Content Fallback**
   - If no XML tags found but substantial content exists (>500 chars), use it directly
   - Prevents empty plan files while preserving partial information

**Key Implementation Details:**

```python
def extract_plan_from_text(text):
    """Extract content between <plan> tags, return None if not found or empty."""
    match = re.search(r'<plan>(.*?)</plan>', text, re.DOTALL)
    if match:
        extracted = match.group(1).strip()
        # Validate minimum content length (a real plan should be substantial)
        if len(extracted) > 200:
            return extracted
    return None
```

**Why Content Validation Matters:**
- Previous versions could produce empty plan files if extraction "succeeded" with no content
- We now require a minimum of 200 characters for XML-tagged content
- This prevents false positives where regex matches empty or trivial content

**Prompt Engineering for Direct Output:**
The prompt explicitly instructs the agent:
- **DO NOT use the Write tool** - prevents file-system detours
- **Output directly in response** - ensures content flows through message stream
- **Use XML tags** - enables clean extraction from potentially verbose responses

This approach gives you:
- **Reliability**: Plans are captured regardless of agent behavior
- **Transparency**: The saved file indicates which source was used
- **Audit Trail**: History of all plans with timestamps and source metadata
- **Debugging**: Clear error messages when extraction fails

Let's view the saved plan:

---

## Advanced Features

---

### Feature 4: Custom Slash Commands

> Note: slash commands are syntactic sugar for users, not new agent capabilities

**What**: Custom slash commands are predefined prompt templates that users can trigger with shorthand syntax (e.g., `/budget-impact`). These are **user-facing shortcuts**, not agent capabilities. Think of them as keyboard shortcuts that expand into full, well-crafted prompts.

**Why**: Your Chief of Staff will handle recurring executive questions. Instead of users typing complex prompts repeatedly, they can use already vetted prompts. This improves consistency and standardization.

**How**:
- Define a markdown file in `.claude/commands/`. For example, we defined one in `.claude/commands/slash-command-test.md`. Notice how the command is defined: frontmatter with two fields (name, description) and the expanded prompt with an option to include arguments passed on in the query.
- You can add parameters to your prompt using `$ARGUMENTS` (for full argument string) or `$1`, `$2`, etc. (for positional arguments)
- The user uses the slash command in their prompt

> **CRITICAL SDK CONFIGURATION**: When using the SDK, you **must** set `setting_sources=["project"]` in your `ClaudeAgentOptions` for slash commands to work. By default, the SDK operates in isolation mode and does NOT load filesystem settings (slash commands, CLAUDE.md, subagents, hooks, etc.). This is different from using Claude Code interactively where these are loaded automatically.

---

### Feature 5: Hooks - Automated Deterministic Actions

**What**: Hooks are Python scripts that you can set to execute automatically, among other events, before (pre) or after (post) specific tool calls. Hooks run **deterministically**, making them perfect for validation and audit trails.

**Why**: Imagine scenarios where you want to make sure that your agent has some guardrails (e.g., prevent dangerous operations) or when you want to have an audit trail. Hooks are ideal in combination with agents to allow them enough freedom to achieve their task, while still making sure that the agents behave in a safe way.

**How**:
- Define hook scripts in `.claude/hooks/` -> _what_ is the behaviour that should be executed when a hook is triggered
- Define hook configuration in `.claude/settings.local.json` -> _when_ should a hook be triggered
- In this case, our hooks are configured to watch specific tool calls (Bash, Write, Edit)
- When those tools are called, the hook script runs after the tool completes (PostToolUse)

> **SDK CONFIGURATION NOTE**: Hooks configured in `.claude/settings.local.json` require `setting_sources=["project", "local"]`. The SDK distinguishes between three setting sources:
> - `"project"` → `.claude/settings.json` (version-controlled, team-shared)
> - `"local"` → `.claude/settings.local.json` (gitignored, local settings like hooks)
> - `"user"` → `~/.claude/settings.json` (global user settings)
>
> Since our hooks are in `settings.local.json`, we must include `"local"` in `setting_sources`.

**Example: Report Tracking for Compliance**

A hook to log Write/Edit operations on financial reports for audit and compliance purposes.
The hook is defined in `chief_of_staff_agent/.claude/hooks/report-tracker.py` and the logic that enforces it is in `chief_of_staff_agent/.claude/settings.local.json`:


```json
"hooks": {
  "PostToolUse": [
    {
      "matcher": "Write",
      "hooks": [
        {
          "type": "command",
          "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/report-tracker.py"
        }
      ]
    },
    {
      "matcher": "Edit",
      "hooks": [
        {
          "type": "command",
          "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/report-tracker.py"
        }
      ]
    }
  ]
}
```

---

If you now navigate to `./chief_of_staff_agent/audit/report_history.json`, you will find that it has logged that the agent has created and/or made changes to your report. The generated report itself you can find at `./chief_of_staff_agent/output_reports/`.

---

### Feature 6: Subagents via Task Tool

**What**: The Task tool enables your agent to delegate specialized work to other subagents. These subagents each have their own instructions, tools, and expertise.

**Why**: Adding subagents opens up a lot of possibilities:
1. Specialization: each subagent is an expert in their domain
2. Separate context: subagents have their own conversation history and tools
3. Parallellization: multiple subagents can work simultaneously on different aspects.

**How**:
- Add `"Task"` to allowed_tools
- Use a system prompt to instruct your agent how to delegate tasks (you can also define this its CLAUDE.md more generally)
- Create a markdown file for each agent in `.claude/agents/`. For example, check the one for `.claude/agents/financial-analyst.md` and notice how a (sub)agent can be defined with such an easy and intuitive markdown file: frontmatter with three fields (name, description, and tools) and its system prompt. The description is useful for the main chief of staff agent to know when to invoke each subagent.

**Visualization Enhancements**: Our `print_activity()` and `visualize_conversation()` utilities have been enhanced to clearly show subagent operations:
- 🚀 indicates when a subagent is being delegated to (with the subagent name)
- 📎 indicates tools being used BY the subagent (indented for visual hierarchy)
- Visual separators clearly mark subagent delegation and completion boundaries
- Task descriptions and prompts are shown in the conversation timeline

---

Here, when our main agent decides to use a subagent, it will:
  1. Call the Task tool with parameters like:
  ```json
    {
      "description": "Analyze hiring impact",
      "prompt": "Analyze the financial impact of hiring 5 engineers...",
      "subagent_type": "financial-analyst"
    }
  ```
  2. The Task tool executes the subagent in a separate context
  3. Return results to main Chief of Staff agent to continue processing

---

## Putting It All Together

---

Let's now put everything we've seen together. We will ask our agent to determine the financial impact of hiring 3 senior engineers and write their insights to `output_reports/hiring_decision.md`. This demonstrates all the features seen above:
- **Bash Tool**: Used to execute the `hiring_impact.py` script to determine the impact of hiring new engineers
- **Memory**: Reads `CLAUDE.md` in directory as context to understand the current budgets, runway, revenue and other relevant information
- **Output style**: Different output styles, defined in `chief_of_staff_agent/.claude/output-styles`
- **Custom Slash Commands**: Uses the shortcut `/budget-impact` that expands to full prompt defined in `chief_of_staff_agent/.claude/commands`
- **Subagents**: Our `/budget_impact` command guides the chief of staff agent to invoke the financial-analyst subagent defined in `chief_of_staff_agent/.claude/agents` 
- **Hooks**: Hooks are defined in `chief_of_staff_agent/.claude/hooks` and configured in `chief_of_staff_agent/.claude/settings.local.json`
    - If one of our agents is updating the financial report, the hook should log this edit/write activity in the `chief_of_staff_agent/audit/report_history.json` logfile
    - If the financial analyst subagent will invoke the `hiring_impact.py` script, this will be logged in `chief_of_staff_agent/audit/tool_usage_log.json` logfile

- **Plan Mode**: If you want the chief of staff to come up with a plan for you to approve before taking any action, uncomment the commented line below

To have this ready to go, we have encapsulated the agent loop in a python file, similar to what we did in the previous notebook. Check out the agent.py file in the `chief_of_staff_agent` subdirectory. 

All in all, our `send_query()` function takes in 4 parameters (prompt, continue_conversation, permission_mode, and output_style), everything else is set up in the agent file, namely: system prompt, max turns, allowed tools, and the working directory.

To better visualize how this all comes together, check out these [flow and architecture diagrams that Claude made for us :)](./chief_of_staff_agent/flow_diagram.md)


---

## Conclusion

We've demonstrated how the Claude Code SDK enables you to build sophisticated multi-agent systems with enterprise-grade features. Starting from basic script execution with the Bash tool, we progressively introduced advanced capabilities including persistent memory with CLAUDE.md, custom output styles for different audiences, strategic planning mode, slash commands for user convenience, compliance hooks for guardrailing, and subagent coordination for specialized tasks.

By combining these features, we created an AI Chief of Staff capable of handling complex executive decision-making workflows. The system delegates financial analysis to specialized subagents, maintains audit trails through hooks, adapts communication styles for different stakeholders, and provides actionable insights backed by data-driven analysis.

This foundation in advanced agentic patterns and multi-agent orchestration prepares you for building production-ready enterprise systems. In the next notebook, we'll explore how to connect our agents to external services through Model Context Protocol (MCP) servers, dramatically expanding their capabilities beyond the built-in tools.

Next: [02_The_observability_agent.ipynb](02_The_observability_agent.ipynb) - Learn how to extend your agents with custom integrations and external data sources through MCP.

---

