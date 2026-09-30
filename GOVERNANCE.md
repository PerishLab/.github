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

A Bug separates directly observed facts, inferred causes, and unresolved
diagnosis. Name the existing contract and the exact consumer or execution
context. An unsupported explanation is not an observed defect: reproduce or
verify it before making that explanation the repair scope.

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

## Issue quality checks

An Issue that fails a quality check carries a label in the `needs:`
namespace, named for what it needs: `needs:<check>`. While any such label is
present, the Issue cannot be worked: Concord refuses to start a Member on it or
to deliver it, and names the labels. Resolving the check and removing the label
is the only way back; the label records the finding, and removing it is the
explicit affirmation that the finding was answered. Only the operated Issue's
own labels count, never a parent's. Labels outside the namespace carry no such
effect.

Concord knows only this label contract. Which checks exist, when a label is
applied and who applies it are organization policy, recorded here. The checks
are a closed set:

- `needs:revalidation`: the Issue's Member has existed for 7 days without
  landing. Re-affirm that the outcome is still wanted and correctly bounded,
  then remove the label; that renewal lasts until 14 days after the Member
  started. Past 14 days the Issue is closed. Either a new Issue with a rewritten
  body supersedes it, or the work is dropped; in both cases its branch is
  deleted.

Applying labels belongs to organization patrol, which is designed separately.
A human may apply or resolve any check by hand with the same effect.

## Declared acceptance and comment closure

The first acceptance targets are `acceptance:source` and
`acceptance:release`. An adopted Issue has exactly one of these labels.
The label declares the promised endpoint; it is not progress, readiness,
identity, or permission. Keep it after completion. Native relationships still
own hierarchy and blocking. Consumer or deployment targets are not introduced
in this phase.

- **source** promises the repository result: the bounded change is merged and
  the applicable checks, documentation and other source acceptance are
  settled. It makes no claim that an installed consumer has the capability.
- **release** includes the source result and a containing stable marker whose
  Wharf distribution record is complete. Record how that exact marker includes
  the change. When acceptance names an installed consumer, identify its
  artifact/version and directly verify the promised behavior there. A newer
  version number or a release URL alone proves neither inclusion nor usability.

The target does not replace the Issue's detailed acceptance conditions. State
the consumption endpoint, required evidence, and obligations remaining after
merge in existing Outcome, Scope, Acceptance, or Evidence fields. For example,
a new CLI command can be merged after the current stable tag: source delivery
is then true, but that installed stable still lacks the command. Verify its
release ancestry and help/behavior before diagnosing a manager defect.

Concord is the operational writer for this label family and its declarations.
Permission hardening is a separate concern; label history is observable, but
does not by itself prove a valid declaration or closure. Preserve unrelated
labels. Adopt an existing Issue when active work resumes, not through batch
labeling or rewriting closed history.

Declarations, amendments and closure judgments live in GitHub Issue comments.
Reuse Concord's existing automatic session association; its execution fields
are environment observations, not authenticated identity or authority. There
is no second acceptance ledger. The Concord implementation owns the exact
versioned marker grammar. It must identify the comment purpose, target,
declaration reference, judgment and evidence references, with prose explaining
the result. A declaration identifies itself by its provider comment identity;
amendments and closure comments point to the declaration they evaluate.

The manual closure flow is:

1. Declare the target and concrete promise through Concord, retaining one
   current declaration and the matching label.
2. Record progress as evidence arrives without treating merge, a label or a
   green check as completion of remaining acceptance.
3. Amend a changed promise explicitly: reference its predecessor and explain
   the reason. An amendment supersedes that declaration and invalidates closure
   against it. Reopened acceptance or material expansion requires a fresh
   review even when the label is unchanged.
4. Review every current acceptance condition. Publish a closure judgment
   referencing the current declaration, exact source/release/consumer evidence,
   remaining conditions, and the strength of verification. Manual review is
   valid in this phase when named as manual review; do not present it as an
   automated proof.
5. Close the Issue manually only when every condition is settled and the
   current successful closure comment is present. Leave unmet or unknown
   acceptance open. Automatic close/reopen is outside this phase.

Label and comment writes are not a provider transaction. If one write succeeds
and another fails, inspect the actual timeline, labels and comment identities
before completing or correcting the operation; never blindly repeat it.
Conflicting targets, a missing or stale declaration/closure, unsupported marker
versions, provider failure or truncated reads are not successful closure.
Report unmet facts separately from unknown facts.

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

For adopted acceptance, a closing reference additionally requires successful
closure against the current declaration. Ordinary Refs pull requests may merge
while release acceptance is outstanding; neither the label nor the checker
turns source delivery into installed capability. Changes to a pull request's
references or an Issue's labels, body, declarations or closure invalidate a
stale successful check and require current evaluation. Read-only CI checks
consume GitHub facts without local Concord execution state or session context.
Introduce them observationally before making a narrow closing-reference check
required, following the canary rule below.

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

The workflow installs the current Plumb and Ectropy stable rather than a
pinned release. Guard evidence binds the Plumb and Ectropy that actually ran,
so every commit still records exactly what judged it. A stable that tightens a
law therefore reddens affected pull requests as soon as it is distributed;
that is the intended signal, not a reason to pin.

A change to the required gate is complete only after one real `plumb land` on
PerishLab/plumb succeeds under it, so the first merge to fail under a new rule
is the rollout owner's canary rather than another session's delivery:

- A ruleset or required-workflow change first targets only PerishLab/plumb.
  After a real `plumb land` succeeds under it, it widens to its full
  repository selection.
- A Plumb or Ectropy stable changes the gate everywhere at once. The releaser
  lands on PerishLab/plumb under the organization Guard right after the stable
  is distributed; the window until that land is accepted.
- When no Plumb change is pending, the next one to land serves as the canary.
  The Issue carrying the change stays open until its canary pull request is
  recorded on it.

A ruleset requires a workflow by path and SHA, so a pull request opened before
the ruleset moves needs a fresh event (push, or close and reopen); a rerun
keeps its original workflow identity.

Every workflow action reference is immutable. The GitHub-hosted runner class
is declared explicitly, while Guard evidence binds the actual execution world;
a digest-pinned full-Guard image is a separately tracked enhancement and bakes
in no Plumb or Ectropy version.

## Repository defaults

The issue forms and pull-request template in this repository are the PerishLab
defaults. Blank Issue creation is disabled. Product repositories do not copy or
override the forms or template. A repository-level exception requires a change
to this organization policy rather than a private template fork.

Repository `AGENTS.md` files contain only product-specific constraints and
exceptions plus an explicit route to this canonical governance document. Read
that document at work start and again before delivery or Issue closure. A root
entry must make the route discoverable without assuming a product Skill will
supply it. They do not copy this organization-wide protocol. If the canonical
document cannot be read, report that missing authority rather than reconstruct
it from memory.

## Maintenance

This repository is maintained manually. It contains no product-local workflow,
release lifecycle, generated projection, or Plumb configuration. GitHub owns
issue types and relationships; this repository owns the default forms,
organization-governance workflow sources, and the human-readable protocol they
project.
