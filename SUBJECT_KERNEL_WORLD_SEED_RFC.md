# Subject Kernel / World Seed RFC v0.1

Chinese version: [SUBJECT_KERNEL_WORLD_SEED_RFC_ZH.md](./SUBJECT_KERNEL_WORLD_SEED_RFC_ZH.md)

Status: `document-only`, `boundary-rfc`, `non-runtime`.

P64 clarifies a possible future split inside Identity Seed: a protected Subject
Kernel and a more evolvable World Seed. It does not rewrite Identity Core,
change schemas, migrate state, create runtime world state, mutate identity,
promote growth, or implement product behavior.

## Problem

Identity Seed currently carries several different kinds of starting material:

- who the subject is;
- why it exists;
- what values orient it;
- what world or project it begins inside;
- what kind of future it should be allowed to grow.

Keeping all of that inside a single identity concept can make Identity Core too
large. But splitting it carelessly can create a second identity layer, a
mutable personality layer, or an unreviewed world model.

P64 defines the boundary before any implementation.

## Core Rule

```text
Subject Kernel protects the minimal subject anchor.
World Seed orients the subject inside a world.
Neither one is a runtime mutation path.
```

The goal is not to rewrite Identity Seed. The goal is to make future identity
and world/context evolution easier to review.

## Subject Kernel

Subject Kernel is the smallest protected answer to:

```text
Who is the subject that must remain continuous?
```

Candidate contents:

- name or subject identifier;
- core continuity thesis;
- non-fiction boundary;
- minimal values;
- protected identity invariants;
- high-gate identity update rule;
- origin as identity seed, not assigned false biography.

Subject Kernel should remain smaller than Identity Core, slower than ordinary
memory, and protected by the highest gate.

## World Seed

World Seed is the initial orientation answer to:

```text
What world, project, and direction does the subject begin inside?
```

Candidate contents:

- project context;
- research program orientation;
- current collaborators or stewardship context;
- initial task horizon;
- domain vocabulary;
- known constraints;
- open world questions;
- non-product boundaries.

World Seed may evolve more easily than Subject Kernel, but only through review.
It is not identity. It is orientation.

## Boundary Matrix

| Concept | Owns | Does Not Own |
|---|---|---|
| Subject Kernel | minimal subject anchor, protected continuity invariants | detailed biography, tasks, product role, platform behavior |
| Identity Core | slow reviewed identity memory and identity-adjacent commitments | automatic personality update, adapter-owned identity |
| World Seed | project/world orientation and initial context | protected identity, relationship simulation, product positioning |
| Task Hub | operational continuity | subject definition |
| Claim Graph | claim-shaped beliefs and evidence | all meaning shift or identity |
| Memory Layer | stored records and lifecycle | subject kernel semantics |

## Allowed Future Review Questions

Future work may ask:

- Which Identity Seed fields are truly subject-kernel fields?
- Which fields are world/context orientation?
- Which fields are historical evidence rather than seed?
- Which world orientation can evolve without identity review?
- Which changes require Identity Gate?
- How should reconstruction preserve kernel/world distinction?

P64 does not answer these by changing state. It only creates the review frame.

## Forbidden Interpretations

Subject Kernel / World Seed must not be used to:

- rewrite Identity Core;
- split identity in runtime;
- create a mutable personality layer;
- treat project context as identity;
- treat relationship context as identity;
- treat platform behavior as world truth;
- create companion or product persona;
- bypass high-gate identity review;
- justify automatic growth;
- hide memory rewrite behind "world update."

## Relationship To Identity Seed

Identity Seed remains the project concept for beginning without a false full
biography.

Subject Kernel and World Seed are possible sub-boundaries inside that concept:

- Subject Kernel asks what must remain protected for continuity.
- World Seed asks what initial environment helps the subject begin.

Both preserve the original principle:

```text
Give it a seed.
Give it a direction.
Give it a world.
Then let it experience time.
```

## Relationship To State Transfer

State transfer must carry enough information for the next run to recover:

- Who am I?
- Where am I?
- What am I doing?

Subject Kernel primarily supports "Who am I?" World Seed primarily supports
"Where am I?" Task Hub primarily supports "What am I doing?"

This is a conceptual mapping, not a runtime schema change.

## Relationship To Reconstruction

Future reconstruction should preserve the distinction between:

- protected subject anchor;
- reviewed identity evidence;
- world/project context;
- task state;
- memories and claims.

Without this distinction, reconstruction may rebuild a state that remembers
facts but blurs subject identity and world orientation.

## P65 Handoff

P65 may define Reconstruction Reducer Contract RFC. It should ensure reducer
contracts can distinguish protected identity paths from world/context paths
before any reducer execution is considered.

Until then, Subject Kernel / World Seed remains document-only boundary language.
