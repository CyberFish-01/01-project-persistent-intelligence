# External Memory Import

Chinese version: [MEMORY_IMPORT_ZH.md](./MEMORY_IMPORT_ZH.md)

01 Core can use old 01 memories from AstrBot as seed material, but it should not depend on AstrBot or Angel Memory internals.

The principle:

```text
External system memory
  ↓
Extract as generic text
  ↓
Import into 01 Core imported_memory
  ↓
Dream review
  ↓
Optional semantic memory candidates
  ↓
No default Identity Core update
```

## 1. Why Generic Text

AstrBot, Angel Memory, bot frameworks, and memory plugins are external carriers.

01 continuity should not be bound to any one carrier.

The importer keeps only:

- memory text;
- source system;
- source label;
- source path;
- import timestamp;
- confidence;
- provenance;
- promotion policy.

It does not preserve external execution logic.

## 2. Text Format

Recommended format: plain `.txt`.

Use blank-line separated blocks:

```text
01 treats continuity as State Transfer, not memory retrieval.

01 and the user are studying Dream Engine, Memory Lifecycle, and Identity Seed.

AstrBot should be an external adapter, not the owner of 01 Core state.
```

Or bullet points:

```text
- 01 treats continuity as State Transfer, not memory retrieval.
- 01 and the user are studying Dream Engine, Memory Lifecycle, and Identity Seed.
- AstrBot should be an external adapter, not the owner of 01 Core state.
```

## 3. Import Command

```bash
python3 -m one_core.cli import-text astrbot_01_memory.txt \
  --source-system astrbot_text \
  --source-label astrbot_01_export
```

For Angel Memory:

```bash
python3 -m one_core.cli import-text angel_memory_export.txt \
  --source-system angel_memory_text \
  --source-label astrbot_angel_memory_export
```

## 4. Where It Goes

Imported content is stored in:

```text
state.json -> memory_stores.imported_memory
imports.jsonl
```

Each imported memory is staged:

```yaml
status: "staged"
promotion_policy:
  default_target: "semantic_memory_candidate"
  requires_dream_review: true
  may_update_identity_core: false
```

Imported memories are external material by default, not identity core.

## 5. Why Not Identity Core

Old memories may contain:

- stale preferences;
- plugin mistakes;
- roleplay content;
- temporary moods;
- AstrBot platform state;
- Angel Memory formatting noise;
- content the user did not intend to preserve forever.

These can be historical materials, but they should not automatically change "Who am I?"

Identity Core updates must pass a high gate.

## 6. Recommended Flow

1. Export old memories from AstrBot / Angel Memory.
2. Clean them into `.txt`.
3. Remove obvious private data, noise, and plugin internals.
4. Run `import-text`.
5. Check `context` and `status`.
6. Run `dream`.
7. Review Dream semantic candidates.
8. Later, add manual approval and identity update gates.

## 7. Current Limits

The first importer does not yet:

- read AstrBot databases directly;
- parse Angel Memory proprietary formats;
- deduplicate automatically;
- judge truth automatically;
- promote to identity memory automatically.

This is intentional.

The importer does one thing:

> Bring external memories safely into 01 Core without allowing external systems to own 01.
