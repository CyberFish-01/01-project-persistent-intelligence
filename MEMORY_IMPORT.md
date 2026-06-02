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
Manual review / promote
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
- import batch id;
- import timestamp;
- confidence;
- content hash / dedupe key;
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

If you already have clean `.txt`:

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

## 4. Clean Raw Exports

If you have raw AstrBot / Angel Memory exports, clean them into generic text first.

Currently supported:

- `.txt`
- `.json`
- `.jsonl`
- `.csv`
- `.db` / `.sqlite` / `.sqlite3`

Command:

```bash
python3 -m one_core.cli clean-memory raw_astrbot_export.json \
  -o work/imports/astrbot_01_memory.txt
```

Multiple files can be cleaned together:

```bash
python3 -m one_core.cli clean-memory raw_1.json raw_2.jsonl raw_3.csv \
  -o work/imports/astrbot_01_memory.txt
```

Then import:

```bash
python3 -m one_core.cli import-text work/imports/astrbot_01_memory.txt \
  --source-system astrbot_text \
  --source-label astrbot_01_export
```

The cleaner extracts text from common fields:

```text
content, memory, text, message, summary, description, value, fact, memo, note
```

It ignores obvious noise fields:

```text
id, uuid, timestamp, embedding, vector, metadata, session_id
```

For Angel Memory `simple_memory.db`, the cleaner prioritizes:

```text
memory_records.judgment
```

and reads only `is_active = 1` current memories by default.

## 5. Where It Goes

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

## 6. Import Safety Checks

`import-text` now treats every run as an import batch.

The report written to `imports.jsonl` includes:

```yaml
import_batch_id: "import_batch_..."
candidate_count: 4
imported_count: 2
skipped_count: 2
duplicate_count: 1
sensitive_count: 1
filter_report:
  duplicate_items: []
  sensitive_items: []
```

Each imported memory receives:

```yaml
import_batch_id: "import_batch_..."
content_hash: "..."
dedupe_key: "sha256:..."
```

The importer deduplicates within the current batch and against existing `imported_memory`.

It also conservatively filters obvious sensitive material, such as passwords, tokens, API keys, secrets, private keys, and Chinese password/key markers. Filtered sensitive content is not stored as imported memory and is not copied into the report as plaintext or hash; the report keeps only source index and reason for sensitive items.

If every candidate is skipped, `import-text` still writes an import report and audit/trace events, but it does not create a Dream job.

These checks are not a replacement for human review. They are a first safety boundary before Dream review.

## 7. Why Not Identity Core

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

## 8. Recommended Flow

1. Export old memories from AstrBot / Angel Memory.
2. Run `clean-memory` to produce `.txt`.
3. Manually review and remove obvious private data, noise, and plugin internals.
4. Run `import-text`.
5. Check `context` and `status`.
6. Run `dream`.
7. Review Dream candidate memory.
8. After manual approval, use `promote-candidate` to promote it into active semantic memory.
9. Identity updates still require a high gate and must not be auto-approved.

## 9. Current Limits

The first cleaner/importer does not yet:

- read AstrBot databases directly;
- parse Angel Memory proprietary formats;
- judge truth automatically;
- promote to identity memory automatically.

This is intentional.

The importer does one thing:

> Bring external memories safely into 01 Core without allowing external systems to own 01.
