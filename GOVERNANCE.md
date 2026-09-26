# Delivery governance

PerishLab uses issues as the public unit of bounded product work and pull
requests as the delivery projection of one such unit. The issue is the sole
public narrative authority for that outcome and its acceptance. Concord remains
the authority for estate-wide execution state, dependencies, Members, Claims,
Boundaries, Phases, and retained lineage.

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

Large outcomes use parent and sub-issues. Each deliverable leaf remains
independently closable. Exact ordering and blocking use GitHub's native issue
dependencies; labels do not stand in for relationships.

## Concord lineage

An issue may originate from a Concord Task. When it does, record the stable
Task identity in the issue. The Task is a temporary execution envelope; it does
not copy the issue body, discussion, or forge timeline. Keep estate-wide
decisions and retained execution evidence in Concord, and carry only the public
delivery boundary into the issue.

Creating an issue does not prove that its outcome was delivered. A Concord
Task may be retired after transfer only when it retains the issue reference,
has no remaining local responsibility, and says explicitly that the product
gap remains open in GitHub.

## Pull requests

A pull request delivers one leaf issue and uses a native non-closing reference
by default. Its body states the resulting outcome, the bounded change, and the
verification performed. A native closing reference is used only when every
acceptance condition is decidable and true at merge time. A pull request does
not replace Concord Member, Claim, Boundary, Git, or repository-specific
landing evidence.

Issue and pull-request observations are external facts. They do not silently
authorize, settle, finish, release, or otherwise mutate a Concord object.

## Distribution

Wharf's distribution record is the authority for how far a release marker has
been distributed. An issue whose acceptance requires a stable release remains
open until that record says the stable marker is complete. A source merge,
release tag, workflow conclusion, or registry observation alone does not close
it. Wharf records distribution and does not manage issue lifecycle.

## Repository defaults

The issue forms and pull-request template in this repository are the PerishLab
defaults. Product repositories do not copy or override them. A repository-level
exception requires a change to this organization policy rather than a private
template fork.

Repository `AGENTS.md` files contain only product-specific constraints and
exceptions. They do not restate this organization-wide protocol.

## Maintenance

This repository is maintained manually. It contains no product workflow,
release lifecycle, generated projection, or Plumb configuration. GitHub owns
issue types and relationships; this repository owns the default forms and the
human-readable protocol they project.
