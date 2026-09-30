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

## Product guidance authorities

A marker-bound product Skill is one declared by `release.skill = true`. Its new
Depot generation contains exactly one regular file named `SKILL.md`. An
installed managed seat contains that file and installer-owned `metadata.json`;
no other content belongs in either shape. Historical Depot generations remain
immutable. The singleton contract applies when consigning a new generation,
and an upgrade removes companion files left by an earlier managed generation.

`SKILL.md` is the durable entry point for a product. It names the product's
responsibility, core objects, invariants, minimal routine flow, and routes to
the authorities needed for further action. It does not duplicate command or
flag catalogues, organization policy, architecture reference material,
dynamic versions or state, or fault-scenario encyclopedias. In particular, a
managed product Skill has no `PATHS.md`, `SCENARIOS.md`, references directory,
or equivalent companion content.

Authority is divided as follows:

- the product CLI's `--help` owns current command and flag grammar;
- a code-addressed Cookbook owns bounded recovery for complex failures;
- repository `AGENTS.md` owns repository-specific delivery constraints;
- this repository owns organization-wide policy;
- judged product source and documentation own architecture; and
- errors, status, and audit output own current operational evidence.

Complex recovery uses the shared `plumb::cookbook::{Code, Entry, Cookbook}`
contract. Every emitted reference names one exact resolvable code; deterministic
Human and JSON presentations carry equivalent entry content. Simple errors
remain self-contained and emit no Cookbook reference. A product with no genuine
complex recovery exposes no empty Cookbook command or placeholder entries.

This contract does not govern application, plugin, template, or domain-knowledge
Skills that are not marker-bound product guidance. Their owning system defines
their shape and lifecycle.

## Distribution

Wharf's distribution record is the authority for how far a release marker has
been distributed. An issue whose acceptance requires a stable release remains
open until that record says the stable marker is complete. A source merge,
release tag, workflow conclusion, or registry observation alone does not close
it. Wharf records distribution and does not manage issue lifecycle.

## Organization workflow

This repository may carry organization-governance workflows selected directly
by GitHub rulesets. Such a workflow owns only the provider trigger and the
fixed invocation of a released control-plane command. It contains no product
gate, repository-shape policy, release lifecycle, path filter, or target-repo
caller.

The source repository itself is outside product governance, so its copy of the
job is skipped there. A ruleset runs the same source in the target repository's
event context.

The organization Guard workflow checks out the exact event SHA and invokes
`plumb guard` under explicit runtime selectors. Its job runs in the public
digest-pinned Images environment, so Rust, Node, pnpm, Python and the common
tool prerequisites are fixed before the job starts. A repository's root
`rust-toolchain.toml` and `package.json` remain the version authorities; Plumb's
bounded executable probes refuse when the image does not satisfy them. The
workflow neither selects a product gate nor installs a shadow toolchain. Build
caching remains under Guard.

The private `@perishlab` npm packages are read through the organization secret
`PERISHLAB_PACKAGES_READ`, a classic `read:packages` token; the job token asks
for no package scope. The public Images environment itself needs no registry
credential. Its digest advances only after Images publishes an immutable
candidate and Rust plus pnpm/mixed canaries pass against that exact digest.

The workflow pins the released Plumb and Ectropy that judge every repository.
A stable that adds or tightens a law advances in one order: affected
repositories are repaired first, the stable is released and installed, then
one change here advances the pins, and the ruleset moves to that commit's SHA.
A ruleset requires a workflow by path and SHA, so a pull request opened before
the move needs a fresh event (push, or close and reopen); a rerun keeps its
original workflow identity.

Every workflow action and released product reference is immutable. The
GitHub-hosted runner class is declared explicitly, while Guard evidence binds
the actual execution world; a digest-pinned full-Guard image is a separately
tracked enhancement.

## Repository defaults

The issue forms and pull-request template in this repository are the PerishLab
defaults. Blank Issue creation is disabled. Product repositories do not copy or
override the forms or template. A repository-level exception requires a change
to this organization policy rather than a private template fork.

Repository `AGENTS.md` files contain only product-specific constraints and
exceptions. They do not restate this organization-wide protocol.

## Maintenance

This repository is maintained manually. It contains no product-local workflow,
release lifecycle, generated projection, or Plumb configuration. GitHub owns
issue types and relationships; this repository owns the default forms,
organization-governance workflow sources, and the human-readable protocol they
project.
