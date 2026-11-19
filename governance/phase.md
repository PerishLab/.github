# Issue Phase

Phase names the main kind of work currently remaining on an Issue. Its truth
is one organization-only native GitHub single-select Issue field, with these
meanings:

- **Clarify:** clarify the outcome, scope, responsibility or decision.
- **Deliver:** produce the deliverable the Issue promises.
- **Verify:** check delivered results against that promise using real evidence.
- **Settle:** complete remaining disposition, handoff and formal settlement.

An Issue may skip a phase or return to an earlier one with a stated basis;
these meanings do not impose a universal sequence. Its native handoff records
the basis, remaining conditions and exact resume conditions. Unset means
unclassified, never Clarify by default. Unavailable reads and invalid or changed
schema remain explicit unknowns or refusals, not empty values.

Phase belongs to the Issue, independently of state/stateReason, readiness,
acceptance targets and detailed promises, blocked-by relationships, `needs:`
labels, and Project-owned priority, cycles and order. Project presentation
attaches the same native Issue field rather than creating another Phase truth.
Qualify exact native field and option identities; a display name alone is not
authority. Configuration may reference those identities, but keeps no Phase
value or history copy. Do not mirror Phase into labels or local execution state.

Phase grants no execution or resource authority, assignment, lock, automatic
routing or closure, or acceptance proof. Auto and unknown Issue types remain
read-only; do not bulk-classify Issues or backfill closed history.
