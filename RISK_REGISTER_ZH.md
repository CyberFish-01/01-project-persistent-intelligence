# Risk Register / 风险台账

English version: [RISK_REGISTER.md](./RISK_REGISTER.md)

状态：`document-only`、`risk-register`、`non-runtime`。

P72 记录 P71 之后的 foundation risks。它不新增 runtime behavior、schemas、CLI commands、
validation rules、policy executors、reducers、payload capture、identity mutation、
memory rewrite、adapters、UI 或 product behavior。

## Register Rule / 台账规则

```text
risk visibility is not risk automation.
mitigation guidance is not policy execution.
blocked runtime work remains blocked.
```

这份 register 的目的，是在 P91 及后续 planning phases 讨论 capability evolution 时，让
foundation layer 保持清醒，同时不批准 runtime work。

## Risk Levels / 风险等级

- `high`：可能破坏 foundation thesis，或制造不安全实现压力。
- `medium`：可能混淆 ownership、documentation 或 future sequencing。
- `low`：需要观察，但当前不威胁 foundation。

## Active Foundation Risks / 当前基础层风险

| ID | Risk | Level | Trigger Signal | Mitigation | Blocked Action |
|---|---|---|---|---|---|
| R1 | Concept inflation | high | 新命名概念增长快于 ownership boundaries | 新增 surface 前优先更新 [CONCEPT_MAP.md](./CONCEPT_MAP.md)、[RFC_INDEX.md](./RFC_INDEX.md) 或本 register | 为概念添加 runtime capability |
| R2 | Review layer over review layer | high | 一个 review object 需要另一个 review object 才能被理解 | 收敛到 [Governance Surface](./CONCEPT_MAP.md) 语言，或 defer | policy executor、growth engine |
| R3 | Reports outnumber mechanisms | medium | 文档增加，但 future implementation contracts 仍模糊 | 让 reports 绑定 open questions、contracts 和 blocked runtime lists | 只凭 reports 声称 readiness |
| R4 | Growth misunderstood as automatic growth | high | productive drift、meaning shift 或 lifecycle labels 被当成 promotion | 重复 Growth Candidate Review 边界和 Identity Gate escalation | growth lifecycle execution、memory promotion |
| R5 | Temporal Awareness implemented too early | high | elapsed-time vocabulary 被当成 event schema 或 salience mutation | 保持 [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) future-only，直到 write policy 和 validation 存在 | temporal runtime、temporal event execution |
| R6 | Recall retrieval becomes write path | high | ordinary retrieval、similarity search 或 context fill 写入 durable events | 遵守 [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md)：ordinary recall is not a write | recall event writes |
| R7 | Memory rewrite pressure | high | missing encoding context 被通过编辑 memory 来“修复” | 使用 [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md)：insufficient context 是安全输出 | memory rewrite |
| R8 | Reconstruction readiness mistaken for reconstruction | high | evidence reports 或 reducer contracts 被当成 rebuild execution | 保持 reducer contract、capture policy 和 execution 分离 | reducer execution、state rebuild |
| R9 | Payload capture slips into schema mutation | high | capture policy recommendations 未经 review 就变成 event fields | 先要求 privacy、schema、compatibility 和 validation review | payload capture、event schema mutation |
| R10 | Identity boundary dilution | high | Subject Kernel、World Seed、memory 或 product context 开始承担 identity | 保持 Identity Core high-gated，Subject Kernel / World Seed 保持 conceptual | Identity Core rewrite |
| R11 | Companion/social layer arrives early | high | exploration、relationship silence 或 product language 变成 companion behavior | exploration 保持 record-only 或 review-only；relationship memory 后推 | companion、relationship memory、UI/product behavior |
| R12 | Adapter or platform owns identity | high | AstrBot、adapter metadata 或 platform sessions 暗示 identity updates | 保持 "01 Core owns state; adapters translate" | adapter integration required、platform-owned identity |
| R13 | Event audit trail weakened | high | retention review、capture policy 或 reconstruction 暗示 compaction/rewrite | Event Log 保持 append-only；使用 reports 和 references | event compaction、event rewrite |
| R14 | Governance Surface becomes too broad | medium | 每个 task、claim 或 memory review 都被路由到 governance | 使用 ownership boundaries：Task Hub 管 work，Claim Graph 管 claims，Memory Layer 管 records | centralizing all review semantics |
| R15 | Bilingual drift | medium | 中英文 docs 对 status 或 blocked actions 表述分叉 | 使用 [BILINGUAL_CONSISTENCY_REVIEW.md](./BILINGUAL_CONSISTENCY_REVIEW.md)，做 consistency pass，并偏好 paired edits | 两种语言矛盾时只信一边 |
| R16 | README entrance overload | medium | 新读者无法区分 stable foundation 与 future-only work | 优化 README entrance 和 indexes，不新增 features | productizing the README |
| R17 | P80 pressure | medium | 为了推进编号而打开 phase | 使用 [FOUNDATION_MAINTENANCE_REVIEW.md](./FOUNDATION_MAINTENANCE_REVIEW.md) 作为 stop condition；如果不能增加清晰度，就 skip、merge 或 stop | opening empty phases |
| R18 | Cloud/AstrBot deployment pressure | medium | local foundation docs 被当成现在更新 cloud 或 AstrBot 的理由 | foundation loop 结束前继续后推 cloud 和 AstrBot | cloud runtime rollout、AstrBot specialization |
| R19 | Tool evolution becomes uncontrolled autonomy | high | tool candidates、verification 和 reuse 被接成 action loop | 保持 [TOOL_FIRST_SELF_EVOLUTION_RFC.md](./TOOL_FIRST_SELF_EVOLUTION_RFC.md) 和 [CAPABILITY_EVOLUTION_BOUNDARY_RFC.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC.md) review-only，直到 verification、safe library 和 human review gates 存在 | tool execution runtime、automatic tool generation |
| R20 | Verification mistaken for authorization | high | passing tool check 被当成 promote 或 reuse 的许可 | 使用 P92 规则：verification does not imply authorization；要求 separate review 和 founder gate | automatic tool promotion、policy executor |
| R21 | Tool library pollution | high | one-off 或 unsafe candidates 积累成 reusable capability | 要求 reproducibility、dependency checks、safety boundary checks、rollback notes、quarantine path 和未来 safe library policy | tool library mutation |
| R22 | Capability growth mistaken for identity growth | high | 更强 task performance 被描述成 subject growth | 使用 P92 规则：capability improvement does not imply identity growth；identity pressure 路由到 Identity Gate | 由 capability evidence 触发 Identity Core mutation |
| R23 | Dependency / network / filesystem risk | high | tool candidates 需要 packages、APIs、files、credentials 或 network access | future execution 前要求 dependency check、safety boundary check、human review 和 explicit authorization | dependency installation、network calls、filesystem mutation |
| R24 | Reusable procedure mistaken for trusted tool | high | repeatable workflow 被当成 safe executable capability | 使用 P92 规则：reusable procedure does not imply trusted tool | trusted tool promotion without review |
| R25 | Self-modifying runtime pressure | high | capability work 提议修改 runtime、prompts、code、memory 或 identity | self-modifying runtime 保持 forbidden，直到 explicit future architecture 和 founder approval 存在 | self-modifying runtime |
| R26 | Lineage contamination | high | instance output、synthetic history、adapter context 或 model self-claims 开始看起来像 Core 原生内容 | 使用 [LINEAGE_BRANCH_GOVERNANCE_RFC.md](./LINEAGE_BRANCH_GOVERNANCE_RFC.md)：不允许 direct instance/research/quarantine merge；只能 candidate -> quarantine -> review -> manual selected return | direct branch merge into Core、tag/branch creation as authorization、synthetic autobiography as Core history |
| R27 | Tagging plan or review mistaken for Git execution | high | candidate tags、branch names、founder-review recommendations 或 manual command drafts 被当成已经创建的 Git objects | 使用 [BASELINE_TAGGING_PLAN.md](./BASELINE_TAGGING_PLAN.md) 和 [BASELINE_TAGGING_FOUNDER_REVIEW.md](./BASELINE_TAGGING_FOUNDER_REVIEW.md)：先 plan/review，之后 founder confirmation，且只能在单独操作中执行 | git tag creation、git branch creation、git history modification、rebuild start |

## Risk Clusters / 风险簇

### Foundation Semantics / 基础语义

风险：R1、R2、R3、R14、R17。

主要控制：保持 [PHASE_INDEX.md](./PHASE_INDEX.md)、[CONCEPT_MAP.md](./CONCEPT_MAP.md)、
[RFC_INDEX.md](./RFC_INDEX.md) 和 [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) 一致。除非新概念能减少
ambiguity，否则不要创建新概念。

### Memory And Growth / 记忆与成长

风险：R4、R6、R7。

主要控制：保持 Stateful Memory、Meaning Shift、Productive Drift、Growth Candidate Review 和
Growth Candidate Lifecycle 分离。Review objects 不执行 subject-state transition。

### Time And Exploration / 时间与探索

风险：R5、R11。

主要控制：Temporal Awareness 和 Exploration / Serendipity 在未来明确 implementation contracts
出现前，保持 future-only、review-only、non-product。

### Reconstruction And Events / 重建与事件

风险：R8、R9、R13。

主要控制：Reconstruction Evidence 不是 reconstruction。Reducer Contract 不是 reducer
execution。Capture Policy 不是 payload capture。Event Log 保持 append-only。

### Identity, Platform, And Lineage Boundary / 身份、平台与谱系边界

风险：R10、R12、R18、R26、R27。

主要控制：Identity Core 保持 high-gated。Subject Kernel / World Seed 保持 conceptual。
Platforms and adapters translate; they do not own identity. Instances may grow, but Core remains
sovereign.

### Capability Evolution And Tools / 能力演化与工具

风险：R19、R20、R21、R22、R23、R24、R25。

主要控制：tool-first self-evolution 保持 review-only capability boundary。Tool improvement 不是
identity growth。Verification evidence 不是 authorization。Candidate review 不是 promotion。

### Lineage And Branch Governance / 谱系与分支治理

风险：R26、R27。

主要控制：保持 Core trunk、baseline、milestone、pre-rebuild checkpoint、instance sandbox、
research、quarantine 和 release/verification branches 分离。selected return 必须经过 quarantine
和 manual review。Tag 和 branch plans 在单独 founder-approved operation 创建 Git objects 前，
都只是 review material。

### Documentation Operations / 文档运维

风险：R15、R16。

主要控制：保持 bilingual docs 同步，降低 README overload，并通过 indexes 让 stable/future/blocked
status 可见。

## Immediate Watch Items For P92-P93 / P92-P93 近期观察项

- P92 Capability Evolution Boundary RFC 必须保持 RFC-only，不能创建 tool execution、automatic tool
  generation、automatic tool promotion、policy execution 或 Identity Core mutation。
- P93 只有在选择窄的 document-only direction 后才应继续，例如 Tool Verification Evidence Model、
  Tool Candidate Review Schema、Procedural Memory Alignment、Safe Tool Library Policy 或
  Capability Growth Evaluation Plan。
- 任何 future implementation phase 都需要 explicit founder approval，以及独立的 no-write、
  no-identity-mutation validation gate。

## Non-Execution Statement / 非执行声明

P72 不实现：

- risk automation；
- policy execution；
- Temporal Awareness runtime；
- recall event writes；
- growth lifecycle execution；
- tool execution runtime；
- automatic tool generation；
- automatic tool promotion；
- tool library mutation；
- self-modifying runtime；
- git tag creation；
- git branch creation；
- automatic merge；
- automatic selected return；
- lineage executor；
- 从 lineage planning 直接启动 rebuild；
- git history modification；
- 从 tagging plan 直接启动 rebuild；
- unreviewed dependency installation；
- uncontrolled filesystem 或 network access；
- identity mutation；
- memory rewrite；
- payload capture；
- event schema mutation；
- reconstruction reducer execution；
- event compaction；
- companion、relationship memory、UI、AstrBot、adapter 或 product layer。
