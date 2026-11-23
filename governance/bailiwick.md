# Bailiwick

A bailiwick is the smallest unit in which an idea becomes a product. The domain, broadly, is the ideas and products formed while perishcode explores the limits of agent collaboration; narrowly, it is the repositories under the organization, their downstream artifacts, and the solutions built on them. A bailiwick is that sentence's unit: one explored question bound to one landed product.

## Standing

A bailiwick holds five conditions. Missing any one leaves a candidate, not a bailiwick.

| Condition | Meaning |
| --- | --- |
| Explored question | Which capability boundary it probes, and who carried that cost before. Required; may be recorded as unknown with its reason. |
| Landed product | Facades exist that state responsibility, core objects, invariants and the minimal routine flow. |
| Native records | Decisions, progress and acceptance live only in its own records. |
| Non-goals | It states what it does not do. A boundary is defined by exclusions. |
| Exit condition | What ends it: split, handoff or retirement. Required; may be recorded as unknown with its reason. |

## Facades

A bailiwick has exactly one charter and one promise.

| | Charter: `AGENTS.md` | Promise: `SKILL.md` |
| --- | --- | --- |
| Reader | Whoever takes over the iteration | Whoever uses it |
| Goal | Hand over without breaking it | Use it without friction |
| Test question | What must I know so I do not break this? | What may I rely on? |
| Contains | explored question, responsibility, core objects, invariants, non-goals, native record location, verification, exit condition | what it does for the user, entry, minimal routine flow, where to go next |
| Excludes | install and invocation entries, versions, promises | non-goals, native record location, exit condition, verification |

Responsibility and core objects are owned by the charter; the promise cites them and never restates them.

A bailiwick must be statable in one charter and one promise. If it needs two sets that do not cite each other, it is two bailiwicks.

A marker-bound product Skill is delivered through the product's Depot generation and installed as a managed seat; its absence from the repository proves nothing.

## Boundary change

A bailiwick carries no version of its own. The versions of what it ships belong to those artifacts, not to the boundary they were built under.

A boundary change is a change to the charter's or promise's stated responsibility, core objects, non-goals or exit condition, declared by the Issue that makes it. Formatting and spelling corrections are not boundary changes.

## Gaps

A gap found while advancing goes to an Issue. The charter states what is true now, never what is intended. An intention written as a statement is the drift this rule prevents.

## Authority surfaces

The organization-wide division of authority is the single authority. A repository's local surface list is a view of it, naming only the surfaces that repository actually has; any surface it omits is still governed by the organization-wide division.

## Words

`bailiwick` names this unit. It is not the closure of acceptance: that word belongs to the explicit closure judgment on a GitHub Issue and keeps it.

## Judging

To decide whether something is a bailiwick, answer the five conditions from its charter alone, then check that the promise cites rather than restates. Record which condition is unknown and why; an unreadable answer is unknown, never a pass.
