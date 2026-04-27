## Source: tool_use/memory_cookbook.ipynb

# Context Editing & Memory for Long-Running Agents

AI agents that run across multiple sessions or handle long-running tasks face two key challenges: they lose learned patterns between conversations, and context windows fill up during extended interactions.

This cookbook demonstrates how to address these challenges using Claude's memory tool and context editing capabilities.

---

## Table of Contents

1. [Introduction: Why Memory Matters](#introduction)
2. [Use Cases](#use-cases)
3. [Quick Start Examples](#quick-start)
4. [How It Works](#how-it-works)
5. [Code Review Assistant Demo](#demo)
6. [Real-World Applications](#real-world)
7. [Best Practices](#best-practices)

---

## Prerequisites

**Required Knowledge:**
- Python fundamentals (functions, classes, async/await basics)
- Basic understanding of REST APIs and JSON

**Required Tools:**
- Python 3.10 or higher
- Anthropic API key ([get one here](https://console.anthropic.com/))

**Recommended:**
- Familiarity with concurrent programming concepts (threads, async)
- Basic understanding of context windows in LLMs

## Setup

### For VSCode Users

```bash
# 1. Create virtual environment
python -m venv .venv

# 2. Activate it
source .venv/bin/activate  # macOS/Linux
# or: .venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. In VSCode: Select .venv as kernel (top right)
```

### API Key

```bash
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

Get your API key from: https://console.anthropic.com/

---

## 1. Introduction: Why Memory Matters {#introduction}

This cookbook demonstrates practical implementations of the context engineering patterns described in [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). That post covers why context is a finite resource, how attention budgets work, and strategies for building effective agents—the techniques you'll see in action here.

### The Problem

Large language models have finite context windows (200k tokens for the Claude 4 family of models). While this seems large, several challenges emerge:

- **Context limits**: Long conversations or complex tasks can exceed available context
- **Computational cost**: Processing large contexts is expensive - attention mechanisms scale quadratically
- **Repeated patterns**: Similar tasks across conversations require re-explaining context every time
- **Information loss**: When context fills up, earlier important information gets lost

### The Solution

Claude 4 models introduce powerful context management capabilities:

1. **Memory Tool** (`memory_20250818`): Enables cross-conversation learning
   - Claude can write down what it learns for future reference
   - File-based system under `/memories` directory
   - Client-side implementation gives you full control

2. **Context Editing**: Automatically manages context with two strategies:
   - **Tool use clearing** (`clear_tool_uses_20250919`): Clears old tool results when context grows large
   - **Thinking management** (`clear_thinking_20251015`): Manages extended thinking blocks (requires thinking enabled)
   - Configurable triggers and retention policies

### The Benefit

Build AI agents that **get better at your specific tasks over time**:

- **Session 1**: Claude solves a problem, writes down the pattern
- **Session 2**: Claude applies the learned pattern immediately (faster!)
- **Long sessions**: Context editing keeps conversations manageable

Think of it as giving Claude a notebook to take notes and refer back to - just like humans do.

### What You'll Learn

By the end of this cookbook, you will be able to:
- **Implement** the memory tool for cross-conversation learning
- **Configure** context editing to manage long-running sessions
- **Apply** best practices for memory security and organization

---

## 1. Introduction: Why Memory Matters {#introduction}

This cookbook demonstrates practical implementations of the context engineering patterns described in [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). That post covers why context is a finite resource, how attention budgets work, and strategies for building effective agents—the techniques you'll see in action here.

### The Problem

Large language models have finite context windows (200k tokens for Claude 4). While this seems large, several challenges emerge:

- **Context limits**: Long conversations or complex tasks can exceed available context
- **Computational cost**: Processing large contexts is expensive - attention mechanisms scale quadratically
- **Repeated patterns**: Similar tasks across conversations require re-explaining context every time
- **Information loss**: When context fills up, earlier important information gets lost

### The Solution

Claude Sonnet 4.6 introduces two powerful capabilities:

1. **Memory Tool** (`memory_20250818`): Enables cross-conversation learning
   - Claude can write down what it learns for future reference
   - File-based system under `/memories` directory
   - Client-side implementation gives you full control

**Supported Models**: Claude Opus 4.1 (`claude-opus-4-1`), Claude Opus 4 (`claude-opus-4`), Claude Sonnet 4.6 (`claude-sonnet-4-6`), Claude Sonnet 4 (`claude-sonnet-4`), and Claude Haiku 4.5 (`claude-haiku-4-5`)

### The Benefit

Build AI agents that **get better at your specific tasks over time**:

- **Session 1**: Claude solves a problem, writes down the pattern
- **Session 2**: Claude applies the learned pattern immediately (faster!)
- **Long sessions**: Context editing keeps conversations manageable

Think of it as giving Claude a notebook to take notes and refer back to - just like humans do.

---

## 2. Use Cases {#use-cases}

Memory and context management enable powerful new workflows:

### 🔍 Code Review Assistant
- Learns debugging patterns from past reviews
- Recognizes similar bugs instantly in future sessions
- Builds team-specific code quality knowledge
- **Production ready**: Integrate with [claude-code-action](https://github.com/anthropics/claude-code-action) for GitHub PR reviews

### 📚 Research Assistant
- Accumulates knowledge on topics over multiple sessions
- Connects insights across different research threads
- Maintains bibliography and source tracking

### 💬 Customer Support Bot
- Learns user preferences and communication style
- Remembers common issues and solutions
- Builds product knowledge base from interactions

### 📊 Data Analysis Helper
- Remembers dataset patterns and anomalies
- Stores analysis techniques that work well
- Builds domain-specific insights over time

**Supported Models**: Claude Opus 4.1 (`claude-opus-4-1`) and Claude Sonnet 4.6 (`claude-sonnet-4-6`)

**This cookbook focuses on the Code Review Assistant** as it clearly demonstrates both memory (learning patterns) and context editing (handling long reviews).

---

## 3. Quick Start Examples {#quick-start}

Let's see memory and context management in action with simple examples.

---

### Setup

First, install dependencies and configure your environment:

---

**⚠️ Important**: Create a `.env` file in this directory:

```bash
# Copy .env.example to .env and add your API key
cp .env.example .env
```

Then edit `.env` to add your Anthropic API key from https://console.anthropic.com/

---

### Example 1: Basic Memory Usage

Let's see Claude use memory to store information for future reference.

---

**Helper Functions**

These examples use helper functions from `demo_helpers.py`:

- **`run_conversation_loop()`**: Handles the API conversation loop
  - Calls Claude's API with memory tool enabled
  - Executes tool uses (memory operations)
  - Continues until Claude stops using tools
  - Returns the final response

- **`run_conversation_turn()`**: Single turn (used in Example 3)
  - Same as above but returns after one API call
  - Useful when you need fine-grained control

- **`print_context_management_info()`**: Displays context clearing stats
  - Shows tokens saved, tool uses cleared
  - Helps visualize when context editing triggers

---

**⚠️ Note on Memory Clearing**

The following cell clears all memory files to provide a clean slate for this demonstration. This is useful for running the notebook multiple times to see consistent results.

**In production applications**, you should carefully consider whether to clear all memory, as it permanently removes learned patterns. Consider using selective deletion or organizing memory into project-specific directories instead.

---

**What happened?**

1. Claude checked its memory (empty on first run)
2. Identified the bug: **race condition** - multiple threads modifying shared state (`self.results` and `self.failed_urls`) without synchronization
3. Stored the concurrency pattern in memory for future reference

Now let's see the magic - Claude applying this learned pattern in a **new conversation**:

---

### Example 2: Cross-Conversation Learning

Start a completely new conversation - memory persists!

---

**Notice the difference:**

- Claude **immediately checked memory** and found the thread-safety/concurrency pattern
- Recognized the similar issue in async code **instantly** without re-learning
- Response was **faster** because it applied stored knowledge about shared mutable state

This is **cross-conversation learning** in action!

---

### Example 3: Context Clearing While Preserving Memory

What happens during a **long review session** with many code files?

- Context fills up with tool results from previous reviews
- But memory (learned patterns) must persist!

Let's trigger **context editing** to see how Claude manages this automatically.

**Note on configuration:** We use `clear_at_least: 50` tokens because memory tool operations have small results (~50-150 tokens each). In production with larger tool results (like web search or code execution), you'd use higher values like 3000-5000 tokens.

---

**What just happened?**

As context grew during multiple reviews with extended thinking enabled, context editing was applied:
1. **Thinking blocks cleared** - Old thinking from previous turns removed first
2. **Tool results cleared** - Old memory tool results removed when threshold exceeded
3. **Memory files intact** - Claude can still query learned patterns
4. **Token usage managed** - Saved tokens from both thinking and tool results

This demonstrates the key benefit:
- **Short-term memory** (conversation context + thinking) → Cleared to save space
- **Long-term memory** (stored patterns) → Persists across sessions

Let's verify memory survived the clearing:

---

## 4. How It Works {#how-it-works}

### Memory Tool Architecture

The memory tool is **client-side** - you control the storage. Claude makes tool calls, your application executes them.

#### Memory Tool Commands

| Command | Description | Example |
|---------|-------------|---------|
| `view` | Show directory or file contents | `{"command": "view", "path": "/memories"}` |
| `create` | Create or overwrite a file | `{"command": "create", "path": "/memories/notes.md", "file_text": "..."}` |
| `str_replace` | Replace text in a file | `{"command": "str_replace", "path": "...", "old_str": "...", "new_str": "..."}` |
| `insert` | Insert text at line number | `{"command": "insert", "path": "...", "insert_line": 2, "insert_text": "..."}` |
| `delete` | Delete a file or directory | `{"command": "delete", "path": "/memories/old.txt"}` |
| `rename` | Rename or move a file | `{"command": "rename", "old_path": "...", "new_path": "..."}` |

See `memory_tool.py` for the complete implementation with path validation and security measures.

---

### Thinking Management (`clear_thinking_20251015`)

When using extended thinking, thinking blocks accumulate and consume tokens. The `clear_thinking` strategy manages these automatically.

**Important**: This strategy requires `thinking` to be enabled in your API call.

**API Call Pattern** (with extended thinking enabled):

```python
response = client.beta.messages.create(
    betas=["context-management-2025-06-27"],  # Required beta flag
    model="claude-sonnet-4-6",
    messages=messages,
    tools=[{"type": "memory_20250818", "name": "memory"}],
    thinking={"type": "enabled", "budget_tokens": 10000},  # Enable thinking
    context_management={  # Context editing config
        "edits": [
            {
                "type": "clear_thinking_20251015",
                "keep": {"type": "thinking_turns", "value": 1}  # Keep last turn only
            },
            {
                "type": "clear_tool_uses_20250919",
                "trigger": {"type": "input_tokens", "value": 35000},
                "keep": {"type": "tool_uses", "value": 5}
            }
        ]
    },
    max_tokens=2048
)
```

**Key points:**
- `clear_thinking` must come **first** when combining strategies
- Requires extended thinking to be enabled (`thinking={"type": "enabled", ...}`)
- Use `"keep": "all"` to preserve all thinking blocks for maximum cache hits
- Trigger is optional for thinking (clears based on `keep` value)

---

### Understanding the Demo Code

Key implementation details from `code_review_demo.py`:

```python
class CodeReviewAssistant:
    def __init__(self, memory_storage_path="./memory_storage"):
        self.client = Anthropic()
        self.memory_handler = MemoryToolHandler(base_path=memory_storage_path)
        self.messages = []
    
    def review_code(self, code, filename, description=""):
        # 1. Add user message
        self.messages.append({...})
        
        # 2. Conversation loop with tool execution
        while True:
            response = self.client.beta.messages.create(
                model=MODEL,
                system=self._create_system_prompt(),
                messages=self.messages,
                tools=[{"type": "memory_20250818", "name": "memory"}],
                betas=["context-management-2025-06-27"],
                context_management=CONTEXT_MANAGEMENT
            )
            
            # 3. Execute tool uses
            tool_results = []
            for content in response.content:
                if content.type == "tool_use":
                    result = self._execute_tool_use(content)
                    tool_results.append({...})
            
            # 4. Continue if there are tool uses, otherwise done
            if tool_results:
                self.messages.append({"role": "user", "content": tool_results})
            else:
                break
```

**The key pattern**: Keep calling the API while there are tool uses, executing them and feeding results back.

---

### What Claude Actually Learns

This is what makes memory powerful - **semantic pattern recognition**, not just syntax:

**Session 1: Thread-Based Web Scraper**

```python
# Bug: Race condition
class WebScraper:
    def __init__(self):
        self.results = []  # Shared state!
    
    def scrape_urls(self, urls):
        with ThreadPoolExecutor() as executor:
            for future in as_completed(futures):
                self.results.append(future.result())  # RACE!
```

**What Claude Stores in Memory** (example file: `/memories/concurrency_patterns/thread_safety.md`):

When Claude encounters this pattern, it stores the following insights to its memory files:
- **Symptom**: Inconsistent results in concurrent operations
- **Cause**: Shared mutable state (lists/dicts) modified from multiple threads
- **Solution**: Use locks, thread-safe data structures, or return results instead
- **Red flags**: Instance variables in thread callbacks, unused locks, counter increments

---

**Session 2: Async API Client** (New conversation!)

Claude checks memory FIRST, finds the thread-safety pattern, then:
1. **Recognizes** similar pattern in async code (coroutines can interleave too)
2. **Applies** the solution immediately (no re-learning needed)
3. **Explains** with reference to stored knowledge

```python
# Claude spots this immediately:
async def fetch_all(self, endpoints):
    for coro in asyncio.as_completed(tasks):
        self.responses.append(await coro)  # Same pattern!
```

---

**Why This Matters:**

- ❌ **Syntax checkers** miss race conditions entirely
- ✅ **Claude learns** architectural patterns and applies them across contexts
- ✅ **Cross-language**: Pattern applies to Go, Java, Rust concurrency too
- ✅ **Gets better**: Each review adds to the knowledge base

---

### Sample Code Files

The demo uses these sample files (all have concurrency/thread-safety bugs):

- `memory_demo/sample_code/web_scraper_v1.py` - Race condition: threads modifying shared state
- `memory_demo/sample_code/api_client_v1.py` - Similar concurrency bug in async context
- `memory_demo/sample_code/data_processor_v1.py` - Multiple concurrency issues for long session demo

Let's look at one:

---

**`memory_demo/sample_code/web_scraper_v1.py`**

```python
"""
Concurrent web scraper with a race condition bug.
Multiple threads modify shared state without synchronization.
"""

import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict

import requests


class WebScraper:
    """Web scraper that fetches multiple URLs concurrently."""

    def __init__(self, max_workers: int = 10):
        self.max_workers = max_workers
        self.results = []  # BUG: Shared mutable state accessed by multiple threads!
        self.failed_urls = []  # BUG: Another race condition!

    def fetch_url(self, url: str) -> Dict[str, any]:
        """Fetch a single URL and return the result."""
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return {
                "url": url,
                "status": response.status_code,
                "content_length": len(response.content),
            }
        except requests.exceptions.RequestException as e:
            return {"url": url, "error": str(e)}

    def scrape_urls(self, urls: List[str]) -> List[Dict[str, any]]:
        """
        Scrape multiple URLs concurrently.

        BUG: self.results is accessed from multiple threads without locking!
        This causes race conditions where results can be lost or corrupted.
        """
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(self.fetch_url, url) for url in urls]

            for future in as_completed(futures):
                result = future.result()

                # RACE CONDITION: Multiple threads append to self.results simultaneously
                if "error" in result:
                    self.failed_urls.append(result["url"])  # RACE CONDITION
                else:
                    self.results.append(result)  # RACE CONDITION

        return self.results
```

---

**Bug**: Multiple threads modify `self.results` and `self.failed_urls` without locking!

Claude will:
1. Identify the race conditions
2. Store the pattern in `/memories/concurrency_patterns/thread_safety.md`
3. Apply this concurrency pattern to async code in Session 2

---

### Demo Overview

We've built a complete Code Review Assistant. The implementation is in `memory_demo/code_review_demo.py`.

**To run the interactive demo:**
```bash
python memory_demo/code_review_demo.py
```

The demo demonstrates:
1. **Session 1**: Review Python code with a bug → Claude learns the pattern
2. **Session 2**: Review similar code (new conversation) → Claude applies the pattern
3. **Session 3**: Long review session → Context editing keeps it manageable

---

## 7. Best Practices & Security {#best-practices}

### Memory Management

**Do:**
- ✅ Store task-relevant patterns, not conversation history
- ✅ Organize with clear directory structure
- ✅ Use descriptive file names
- ✅ Periodically review and clean up memory

**Don't:**
- ❌ Store sensitive information (passwords, API keys, PII)
- ❌ Let memory grow unbounded
- ❌ Store everything indiscriminately

### Security: Path Traversal Protection

**Critical**: Always validate paths to prevent directory traversal attacks. See `memory_tool.py` for implementation.

### Security: Memory Poisoning

**⚠️ Critical Risk**: Memory files are read back into Claude's context, making them a potential vector for prompt injection.

**Mitigation strategies:**
1. **Content Sanitization**: Filter dangerous patterns before storing
2. **Memory Scope Isolation**: Per-user/per-project isolation  
3. **Memory Auditing**: Log and scan all memory operations
4. **Prompt Engineering**: Instruct Claude to ignore instructions in memory

See `memory_tool.py` for complete security implementation and tests in `tests/`.

---

## Conclusion

### What You Accomplished

In this cookbook, you learned to:
- ✅ **Implement the memory tool** for cross-conversation learning (Sessions 1 & 2 showed pattern recognition persisting)
- ✅ **Configure context editing** with token triggers and retention policies (Session 3 demonstrated automatic clearing)
- ✅ **Apply security best practices** including path validation and memory poisoning prevention

### Applying These Patterns

**For your projects:**
1. Start with a single memory file for patterns (e.g., `/memories/patterns.md`)
2. Set context editing triggers at 30-40k tokens for production use
3. Implement per-project memory isolation to prevent cross-contamination

**Other applications:**
- **Customer support**: Store user preferences and common issue resolutions
- **Research assistants**: Accumulate domain knowledge across sessions
- **Data analysis**: Remember dataset characteristics and successful techniques

### Next Steps

- **Production deployment**: Use [claude-code-action](https://github.com/anthropics/claude-code-action) for GitHub PR reviews
- **Security hardening**: Review the memory poisoning mitigations in `memory_tool.py`
- **Extended thinking**: Explore thinking management for compute-intensive tasks

### Resources

- [Memory tool documentation](https://docs.claude.com/en/docs/agents-and-tools/tool-use/memory-tool)
- [Claude API reference](https://docs.claude.com/en/api/messages)
- [Support](https://support.claude.com)

Memory and context management are in **beta**. Share your feedback to help us improve!

---

