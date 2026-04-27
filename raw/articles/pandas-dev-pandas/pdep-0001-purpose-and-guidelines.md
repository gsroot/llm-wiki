# PDEP-1: Purpose and guidelines

- Created: 3 August 2022
- Status: Accepted
- Discussion: #47444, #51417
- Author: Marc Garcia (datapythonista), Noa Tamir (noatamir)
- Revision: 3

## PDEP definition, purpose and scope

A PDEP (pandas enhancement proposal) is a proposal for a **major** change in pandas, in a similar way as a Python PEP or a NumPy NEP.

Bug fixes and conceptually minor changes (e.g. adding a parameter to a function) are out of the scope of PDEPs. A PDEP should be used for changes that are not immediate and not obvious, when everybody in the pandas community needs to be aware of the possibility of an upcoming change.

PDEPs are appropriate for user facing changes, internal changes and significant discussions. Examples:
- substantial API changes
- breaking behavior changes
- moving a module from pandas to a separate repository
- refactoring of the pandas block manager

## Target audience

- The core development team (final decision)
- Contributors to pandas and other related projects, and experienced users
- The wider pandas community (users)

## PDEP States

- Draft
- Under discussion
- Accepted
- Implemented
- Rejected
- Withdrawn

## PDEP Discussion Timeline

- Discussion remains open for **up to 60 days**
- Voting period: **15 days**
- Notifications at: ready / 30-day mark (15 days remaining) / 45-day mark (15 days to vote) / vote start / 10 vote days (5 remaining)
- Authors can close discussion preemptively after 30 days if 15 days passed without unaddressed comments

## Casting Votes

A VOTE issue is created. Each voting member may comment:
- **+1**: approve
- **0**: abstain (one-sentence reason required)
- **-1**: disapprove (one-sentence reason required, prior participation in PDEP discussion required)

Tally format: w-x-y-z (approving, abstaining, disapproving, no-response)

## Quorum and Majority

- Quorum: lower of (11 voting members, 50% of voting members) — abstentions count toward quorum
- Majority: 70% of non-abstaining votes (approving + disapproving)
- If quorum not reached → PDEP rejected

## States

### Accepted PDEP
Open-ended completion timeline. Companies/individuals can help by hiring or sponsoring.

### Implemented PDEP
Status `Implemented` set when merged into main. Header gets `Implemented: vX.Y.Z`.

### Rejected PDEP
Merged with Status: Rejected (visibility on what was discussed). Author can withdraw before final decision.

### Invalid PDEP
PR closed (not merged) for improper documentation or out-of-scope content.

## Evolution of PDEPs

Most PDEPs don't change after acceptance. But procedural PDEPs (like this one) can be revised — `Revision: X` increments and history note added.

## Examples of PDEP-worthy issues (from history)

- numeric_only deprecation (#28900)
- Categorical (#7217, #8074), StringDtype (#8640), ArrowDtype
- Copy/view changes (#36195) — became PDEP-7 Copy-on-Write
- pandas-stubs creation (#43197, #45253)
- New required dependency
- Moving rarely used I/O connectors to separate repository (#28409)
- Build system change to meson (#49115)

## PDEP-1 History

- 2022-08-03: Initial version (#47938)
- 2023-02-15: v2 — clarifies scope and adds examples (#51417)
- 2023-06-09: v3 — defines structured decision making process (#53576)

---

원본: https://github.com/pandas-dev/pandas/blob/main/web/pandas/pdeps/0001-purpose-and-guidelines.md
SHA: ed084a730ecdcb71535a0e59fcd8fe9d233fd0c6 (size 15,052 bytes)
수집일: 2026-04-27
