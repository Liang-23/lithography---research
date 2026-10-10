---
schema_version: "1.0"
id: SRC-0009
type: source-record
title: "Deep Epidemiological Modeling by Black-box Knowledge Distillation: An Accurate Deep Learning Model for COVID-19"
lifecycle_status: active
authority_class: working
authority_scope: source-provenance-and-source-check
created_by: ai
content_origin: external-source
created_at: 2026-08-30
updated_at: 2026-09-13
owner: project-lead
review_status: source-checked
tier2_review_status: agent-complete
human_audit_status: not-started
reviewed_by: AI Agent
approved_by: project-lead
approval_ref: "Paper-level exact-version approval, 2026-08-30; Q-0001 Batch 2 item 7"
core_alignment: unknown
parent_source_ids: []
evidence_ids: []
exclude_from_synthesis: false
---

# Deep Epidemiological Modeling by Black-box Knowledge Distillation: An Accurate Deep Learning Model for COVID-19

## Identity

- Exact local path: `D:\Litho\2-3nm litho\raw\SRC-0009_Deep_Epidemiological_Modeling_Black_Box_KD.pdf`
- Source type: PDF; peer-reviewed conference paper
- Authors: Dongdong Wang, Shunpu Zhang, Liqiang Wang
- Publication/version date: *Proceedings of the AAAI Conference on Artificial Intelligence* 35(17):15424–15430; 2021
- DOI: `10.1609/aaai.v35i17.17812`
- Imported/registered date: 2026-08-30
- Original location: `https://ojs.aaai.org/index.php/AAAI/article/download/17812/17619`
- Language: English
- License/access restriction: Official AAAI PDF is lawfully open to read; copyright remains with AAAI/authors and no permissive reuse license was identified in the artifact.
- Version relationship: The approved and admitted artifact is the AAAI 2021 published version. ArXiv `2101.10280v1` is the related preprint and was not admitted separately.

## Integrity

- File size: 381,425 bytes
- PDF page count: 7
- Hash algorithm: SHA-256
- Content hash: `7F160F3AC13575C131B81634F4AA62EBDAAE479D1DBAA914410031258A0321DB`
- Conversion performed: No canonical conversion. Temporary read-only text extraction and page rendering were used for inspection; the PDF was not modified.
- Parent original `SRC-ID`: None
- Conversion tool/version/config: Not applicable to the registered original

## Project admission

- Project relevance: Candidate black-box teacher-to-student precedent in which a costly epidemiological simulation system supplies synthetic projection sequences for a deployable neural model.
- Allowed use: Source-relative Background/Wiki review and future claim-level verification through the Evidence workflow.
- Prohibited use: Treating admission as verified Evidence; equating epidemiological simulator distillation with physical output projection without support; inferring lithography validity; selecting a Physics Constraint, Hypothesis, Method, Experiment, simulator, or dataset; changing Core; or making field-wide novelty claims.
- Prompt-injection/embedded-instruction review: The PDF was treated as source data. No PDF JavaScript, embedded file, or Agent-directed operational instruction was found.
- Provenance issue: None affecting admission; conference header, title, authors, and DOI identify the approved published version.
- Quarantine status/reason: Promoted from Q-0001 after exact-version project-lead approval and lawful acquisition.

## Verification

- Original accessible: Yes
- Identity checked by/date: AI Agent / 2026-08-30
- Content checked by/date: AI Agent / 2026-08-30; complete text review plus visual inspection of the title and all pivotal method, result, and discussion pages
- Notes: Integrity and published-version identity are source-checked. Scientific claims and reported results remain source-reported and are not independently verified Evidence.

## Linked Evidence

- `EV-ID`s: None

## Canonical Tier 2 full-text source check

This section records Source-reported content, not independently verified Evidence. Local PDF p. 1 corresponds to printed proceedings p. 15424.

### Teacher and transfer mechanism

- The teacher is a mixture-SEIR simulation system with ten host communities, population conservation, and coupled ODEs. The complete scenario space is reported as $(160{,}000)^{10}$; the practical approximate teacher randomly samples $10^7$ scenarios. [PDF p. 3 / printed p. 15426, Eqs. (1)–(2); PDF pp. 4–5]
- The system queries $1{,}000$ boundary-condition, initial-condition, and ODE-parameter keys to obtain teacher observation/projection sequence pairs. Sequence mixup creates a $100{,}000$-pair pool, from which $1{,}000$ pairs train the student. [PDF pp. 3–5, Eqs. (3)–(4)]
- The student is a three-hidden-layer MLP with 80 units per layer, trained for 300 epochs using MSE imitation of teacher output. [PDF pp. 4–5, Eq. (5)]
- Teacher outputs are directly used as student targets, the teacher is query-only, and the trained MLP is reused without repeating teacher search. This is black-box teacher-output $\rightarrow$ student-target $\rightarrow$ teacher-free inference.
- It is not correction of a raw neural prediction: student output is never fed into and repaired by the teacher. The student has no explicit SEIR residual or exact feasibility enforcement. No gate, fallback, or trust region is described.

### Output structure and reported results

- The output is a temporal daily-infection-increase sequence for four countries. Calibration covers 2020-04-06 through 2020-08-23 and projection covers 2020-08-24 through 2020-09-13. Exact vector length is not stated; this is not spatial image/field evidence. [PDF pp. 4–5]
- For the US, projection MAPE is reported as $0.0352$ for the approximate teacher, $0.0433$ for the student, and $0.0727$ for a coarse-grained teacher; RMSE values are $0.209$, $0.218$, and $0.399$ in units of $10^5$. [PDF p. 5 / 15428, Table 1]
- The student slightly outperforms the approximate teacher in Philippines and Brazil MAPE, but the exhaustive teacher is not computed; this cannot establish student superiority over it. [PDF p. 5, Table 1]
- US student weekly MAPE values are reported as $0.0301$, $0.0623$, and $0.0398$, versus CDC Ensemble $0.0608$, $0.1108$, and $0.0581$. [PDF p. 6 / 15429, Table 2]
- Table 3 reports complete teacher $(160{,}000)^{10}$ scenarios, approximate teacher $10^7$, student $10^3$, and coarse teacher $10^5$; reported CPU time per query is approximately $3\times10^4$, $400$, and $300$ seconds for approximate teacher, student, and coarse teacher, with the student number including training. [PDF p. 6, Table 3]
- Reducing the mixup pool from $100{,}000$ to $50{,}000$ and $25{,}000$ worsens US projection MAPE from $0.0433$ to $0.1861$ and $0.2813$. [PDF p. 6, Table 4]

### Limitations and safe boundary

- The discussion says teacher accuracy and complexity are critical and that reduced mixup propagates calibration error into projection. There is no dedicated limitations section. [PDF p. 6]
- The source does not test student SEIR/conservation satisfaction, spatial outputs, OOD validity beyond four countries and a three-week horizon, corrected-prediction feedback, solver gradients, safe correction, or representation freedom.
- Daily training sequences versus weekly plots/evaluation and exact input/output vector dimensions are under-specified.
- **Bounded relevance:** direct precedent for black-box teacher targets and teacher-free inference. It is not external physical correction of a surrogate output and supplies no high-dimensional spatial correction evidence.

## 用户阅读判断 — 2026-09-13

用户要求保存以下学习记录，由 Agent 整理：就当前需要吸收的方法思路而言，SRC-0009 可以理解为熟悉的 Teacher–Student 路径：Teacher 模拟系统生成输入与对应 target，Student 使用这些样本训练，学习输入到预测结果的映射，训练后独立预测。用户认为这一核心机制较常见，目前无需进一步深入，转入 SRC-0011。

本节归类为用户阅读判断与阅读进度，`content_origin: ai-assisted`；“较常见”是用户对当前学习价值的判断，不是整篇论文缺乏创新的科学结论。Teacher 提供的是 output targets，不是把 Student 输出修正后再教回网络。[PDF pp. 3–4, Eq. (5), Algorithm 1] 此记录不代表完成全文 Human Audit；Source claims 仍未验证，未选择任何项目 Method。
