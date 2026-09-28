# Delivery governance

PerishLab uses issues as the only durable work ledger and pull requests as the
delivery projection of one bounded unit of that work. An issue owns the problem,
outcome, acceptance, non-goals, decisions, progress, relationships, and
completion of its work. A pull request owns the exact change and verification
that it delivers. Product source and released records remain the authority for
the behavior and distribution they prove.

Concord is not a second project ledger. It coordinates Issue-anchored local
execution: Members, Claims, Boundaries, private Artifacts, session activity,
non-exclusive occupancy, and exact delivery preparation. It may project
bounded GitHub facts for Agents, but it does not copy or own Issue narrative,
relationships, lifecycle, or retained decisions.

## Issues

Every issue names one observable outcome. Use the organization issue type that
matches the work:

- **Feature** requests new or changed product behavior.
- **Bug** describes behavior that contradicts an existing contract.
- **Task** delivers a bounded operational or maintenance result without adding
  a product behavior.

An issue states its outcome, acceptance conditions, and non-goals. A Feature
also states the problem it addresses. A Bug states the observed behavior and
the expected outcome. A Task states its exact scope.

Acceptance names every condition required to close the issue, including
evidence that can exist only after merge or stable distribution. A merged pull
request is evidence for the conditions it proves, not a substitute for the
remaining conditions.

Decisions and progress that affect the bounded outcome are recorded in the
Issue body or timeline. Adjacent work becomes another Issue or sub-issue rather
than an addition in a private ledger. Timeless product law belongs in judged
source or organization policy, with its originating Issue and pull request as
lineage.

Large outcomes use parent and sub-issues. Each deliverable leaf remains
independently closable. Exact ordering and blocking use GitHub's native issue
dependencies; labels do not stand in for relationships.

Before closing an Issue, every acceptance checkbox is settled. When acceptance
extends beyond the merging pull request, the Issue remains open until the
authoritative evidence exists and a final comment records it. Historical closed
Issues are not rewritten to satisfy a later protocol.

## Concord execution

New work begins with an existing typed Issue. Concord may attach local execution
to its stable provider identity, but that attachment introduces no Goal, Focus,
Next, Question, Addition, Phase, dependency, active/retired state, or copied
forge timeline.

Issue and pull-request observations are external facts. They do not silently
authorize, release or remove local execution resources. Provider unavailability
is not evidence of absence.

## Pull requests

A pull request delivers one leaf issue and uses a native non-closing reference
by default. Its body states the resulting outcome, the bounded change, the
verification performed, and the proved write boundary. A native closing
reference is used only when every Issue acceptance condition is decidable and
true at merge time. A pull request does not replace Concord Member, Claim,
Boundary, Git, or repository-specific landing evidence.

One Issue may require more than one pull request. Each pull remains bounded to
that Issue, and merge alone does not claim that release-dependent acceptance is
complete.

## Distribution

Wharf's distribution record is the authority for how far a release marker has
been distributed. An issue whose acceptance requires a stable release remains
open until that record says the stable marker is complete. A source merge,
release tag, workflow conclusion, or registry observation alone does not close
it. Wharf records distribution and does not manage issue lifecycle.

## Repository defaults

The issue forms and pull-request template in this repository are the PerishLab
defaults. Blank Issue creation is disabled. Product repositories do not copy or
override the forms or template. A repository-level exception requires a change
to this organization policy rather than a private template fork.

Repository `AGENTS.md` files contain only product-specific constraints and
exceptions. They do not restate this organization-wide protocol.

## Maintenance

This repository is maintained manually. It contains no product workflow,
release lifecycle, generated projection, or Plumb configuration. GitHub owns
issue types and relationships; this repository owns the default forms and the
human-readable protocol they project.
