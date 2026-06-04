# Concept Overlap Review

Chinese version: [CONCEPT_OVERLAP_REVIEW_ZH.md](./CONCEPT_OVERLAP_REVIEW_ZH.md)

P55 reduces foundation concept overlap identified by P54. It is document-only:
no runtime behavior, lifecycle execution, recall event write, reducer execution,
adapter work, or product surface is introduced.

## Review Method

For each overlap pair, this review records:

- owner: the concept that should own the primary responsibility.
- references: concepts that may be cited as evidence or routing context.
- do not absorb: what the owner must not swallow.
- future work: later RFC or policy work, if needed.

## Overlap Matrix

| Pair | Primary Owner | Allowed References | Do Not Absorb | Resolution |
|---|---|---|---|---|
| Growth Candidate Review vs Claim Graph | Governance Surface | Claims, evidence refs, conflict ids | Claim Graph must not own every meaning shift | Growth review owns cross-layer candidate; Claim Graph owns claim-shaped belief revision. |
| Stateful Memory vs Memory Layer | Memory Layer for storage; Stateful Memory for semantics | Memory ids, lifecycle status, encoding refs | Memory Layer must not become meaning-shift engine | Keep stateful memory as interpretive model, not store. |
| Governance Surface vs Task Hub | Task Hub owns work queues; Governance Surface owns cross-layer review objects | Task ids, review tasks, lifecycle records | Task Hub must not own every review object | Route work through Task Hub, but keep cross-layer objects in Governance Surface. |
| Meaning Shift vs Claim Revision | Meaning Shift owns memory interpretation; Claim Graph owns claim revision | Claim ids, contradiction evidence | Claim Graph must not convert all recall changes into claims | Only claim-shaped shifts enter Claim Graph. |
| Temporal Awareness vs Event Metadata | Event metadata owns timestamps; Temporal Awareness owns future subjective-time semantics | timestamps, elapsed-time candidates | Event Log must not imply temporal subject state | Keep Temporal Awareness future-only until RFC and policy exist. |
| Reconstruction Evidence vs Payload/Diff Capture Policy | Reconstruction Evidence owns vocabulary; Capture Policy owns future target-path treatment | workflow ids, target paths, gaps | Evidence reports must not mutate event schema | Keep reports read-only until policy and reducer contract are reviewed. |

## Detailed Resolutions

### Growth Candidate Review vs Claim Graph

Growth Candidate Review exists because a possible meaning-bearing state
transition can reference memory, tasks, claims, events, and identity risk at the
same time. Claim Graph should participate when the candidate includes explicit
claims, contradictions, support links, or belief revision pressure.

Resolution:

- Growth Candidate Review owns candidate review object.
- Claim Graph owns claim evidence and claim revision.
- Identity Gate owns identity-threatening final review.
- Task Hub may route the review work, but does not own the candidate semantics.

### Stateful Memory vs Memory Layer

Memory Layer owns concrete records: imported, episodic, candidate, semantic,
identity, and archived memory. Stateful Memory is not a seventh memory store.
It is the model that says memory meaning depends on event, encoding state,
recall state, and meaning shift.

Resolution:

- Memory Layer owns storage and lifecycle.
- Stateful Memory owns interpretation vocabulary.
- Meaning Shift does not rewrite stored memory.
- Future minimal encoding policy should define required references without
  creating another memory store.

### Governance Surface vs Task Hub

Task Hub already contains many review queues and decisions. That makes it
operationally useful, but it should not become the conceptual owner of every
cross-layer review object.

Resolution:

- Task Hub owns actionable work state.
- Governance Surface owns cross-layer review semantics.
- Review objects can expose tasks without becoming tasks.
- P56 should test this boundary in a matrix.

### Meaning Shift vs Claim Revision

Meaning Shift is broader than Claim Revision. A memory can be reinforced,
weakened, reinterpreted, or conflicted without producing a formal claim.

Resolution:

- Meaning Shift remains memory-semantics vocabulary.
- Claim Revision begins when a shift changes a claim statement, confidence,
  support, contradiction, or review status.
- Without claim-shaped content, do not force the shift into Claim Graph.

### Temporal Awareness vs Event Metadata

Event metadata records time. Temporal Awareness asks whether elapsed time changes
subject state. These are related but not the same.

Resolution:

- Event metadata owns timestamps and sequence.
- Temporal Awareness remains a future subject-continuity RFC direction.
- P58 may define elapsed-time concepts, but must not implement temporal runtime.

### Reconstruction Evidence vs Payload/Diff Capture Policy

Reconstruction Evidence describes what proof future reconstruction needs.
Payload/Diff Capture Policy decides future treatment by target path. Neither
executes reconstruction.

Resolution:

- Reconstruction Evidence owns vocabulary and gap visibility.
- Capture Policy owns future target-path recommendation.
- Reducer Contract owns future execution interface.
- No report may imply event schema mutation or event compaction.

## Concepts To Merge Or Rename Later

- Some reconstruction review reports may later be grouped under a single
  "Reconstruction Governance" index.
- Governance Surface may need a clearer alias such as "Cross-Layer Review
  Surface" if the name sounds too broad.
- Growth Candidate Review and Productive Drift should remain separate until a
  lifecycle RFC exists.

## P56 Input

P56 should turn these boundaries into a test matrix:

- forbidden owner;
- allowed reference;
- allowed output;
- forbidden output;
- validation or documentation evidence.
