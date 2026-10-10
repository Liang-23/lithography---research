---
schema_version: "1.0"
id: SRC-0004
type: source-record
title: "PADM: A Physics-aware Diffusion Model for Attenuation Correction"
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
human_audit_status: completed
human_audit_reviewed_by: project-lead
human_audit_approval_ref: "User confirmed the targeted audit was completed and instructed final Evidence materialization, 2026-09-01"
reviewed_by: AI Agent
approved_by: project-lead
approval_ref: "Paper-level exact-version approval, 2026-08-30; Q-0001 Batch 1 item 4"
core_alignment: unknown
parent_source_ids: []
evidence_ids: [EV-0004, EV-0005, EV-0006]
exclude_from_synthesis: false
---

# PADM: A Physics-aware Diffusion Model for Attenuation Correction

## Identity

- Exact local path: `D:\Litho\2-3nm litho\raw\SRC-0004_PADM.pdf`
- Source type: PDF; arXiv preprint
- Authors: Trung Kien Pham, Hoang Minh Vu, Anh Duc Chu, Dac Thai Nguyen, Trung Thanh Nguyen, Thao Nguyen Truong, Mai Hong Son, Thanh Trung Nguyen, Phi Le Nguyen
- Publication/version date: arXiv `2511.06948v1 [cs.CV]`; 2025-11-10
- DOI: `10.48550/arXiv.2511.06948`
- Imported/registered date: 2026-08-30
- Original location: `https://arxiv.org/pdf/2511.06948v1`
- Language: English
- License/access restriction: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (`CC BY-NC-SA 4.0`); lawful arXiv full text
- Version relationship: The approved and admitted artifact is arXiv v1. A later WACV 2026 published version exists, DOI `10.1109/WACV61042.2026.00256`, and was not silently substituted.

## Integrity

- File size: 1,569,889 bytes
- PDF page count: 10
- Hash algorithm: SHA-256
- Content hash: `EC7AAFC92B072C406DE957AB164531D81CFF435D3A34D2D2668EB8740012A3EF`
- Conversion performed: No canonical conversion. Temporary read-only text extraction and page rendering were used for inspection; the PDF was not modified.
- Parent original `SRC-ID`: None
- Conversion tool/version/config: Not applicable to the registered original

## Project admission

- Project relevance: Candidate high-dimensional teacher-student evidence in which CT-informed physics supervision is transferred to a CT-free volumetric attenuation-correction model.
- Allowed use: Source-relative Background/Wiki review and future claim-level verification through the Evidence workflow, with the admitted-version flag preserved.
- Prohibited use: Treating admission as verified Evidence; substituting the WACV version without review; inferring lithography validity; selecting a Physics Constraint, Hypothesis, Method, Experiment, simulator, or dataset; changing Core; or making field-wide novelty claims.
- Prompt-injection/embedded-instruction review: The PDF was treated as source data. No PDF JavaScript, embedded file, or Agent-directed operational instruction was found.
- Provenance issue: Non-blocking version-resolution flag: the approved arXiv v1 predates the later WACV publication.
- Quarantine status/reason: Promoted from Q-0001 after exact-version project-lead approval and lawful acquisition; version flag retained.

## Verification

- Original accessible: Yes
- Identity checked by/date: AI Agent / 2026-08-30
- Content checked by/date: AI Agent / 2026-08-30; complete text review plus visual inspection of the title, architecture, equations, data tables, metrics, and qualitative results
- Notes: Integrity and exact arXiv v1 identity are source-checked. The project lead completed the targeted P1-P4 Human Audit and explicitly approved the current claim wording and applicability boundaries of `EV-0004` through `EV-0006` on 2026-09-01; all three are verified within their recorded boundaries.

## Linked Evidence

- `EV-ID`s: `EV-0004`, `EV-0005`, `EV-0006`; project-lead reviewed and verified on 2026-09-01 within their recorded boundaries.

## Canonical Tier 2 full-text source check

This section records Source-reported content, not independently verified Evidence. Local PDF and manuscript page numbers coincide. The later WACV version was not used.

### Teacher-student and physics-aware mechanism

- The task corrects attenuation in myocardial-perfusion SPECT. CardiAC contains 424 studies with paired non-attenuation-corrected (NAC) and attenuation-corrected (AC) images plus CT-derived attenuation maps. Source volumes are $128\times128\times D$, with $D=25$–$49$, and attenuation maps are $128^3$. [PDF p. 3, Tables 1–2, Section 3]
- The implemented model is slice-level: a $50\times50$ ROI is resized to $256\times256\times1$, with a patient split of 254/84/86. This is high-dimensional 2D image evidence, not joint 3D-volume correction. [PDF pp. 5–7, Sections 4.3 and 5.1]
- Teacher PADM-T receives a NAC slice plus the CT-derived attenuation map through a cross-modality transformer. Student PADM-S uses the same architecture but receives NAC only. [PDF p. 4, Figure 1, Eqs. (3)–(4)]
- Brownian-bridge diffusion operates in image space with paired AC image $x_0$ as its target. A physics module predicts per-angle path-length fields, an attenuation-coefficient field $\mu$, and an auxiliary clean channel, then forms an input-dependent attenuation-correction factor. [PDF pp. 5–6, Eqs. (7)–(15), Algorithms 1–2]
- Student transfer uses attention transfer between normalized aggregated teacher and student attention features; the frozen teacher supplies this feature signal and the student objective is $\mathcal L_{\mathrm{ELBO}}+\lambda\mathcal L_{\mathrm{AT}}$. [PDF p. 6, Eqs. (16)–(18)]

### Training and inference boundary

- This is explicit teacher-student transfer and the deployed student no longer needs the teacher or CT map. The student receives diffusion and attention-transfer gradients.
- It is not corrected-target transfer from an external projector: paired AC ground truth is the diffusion target, while the teacher supplies attention features rather than a projected-output label.
- Reverse-diffusion sampling and the student's physics-aware module remain at inference. Thus inference is student-only relative to the privileged teacher, but not corrector-free or one-pass.
- The artifact does not explicitly analyze whether gradients propagate through every physics-module operation. No gate, accept/reject rule, trust region, fallback, or correction bound is described.

### Major reported results

- PADM-T reports RMSE $0.0217$, SSIM $0.9796$, and PSNR $34.98$; PADM-S reports $0.0218$, $0.9795$, and $34.75$; BBDM reports $0.0256$, $0.9451$, and $33.04$. [PDF p. 7, Table 3]
- For 16 projections, student/teacher metrics are $0.0218/0.9795/34.75$ versus $0.0217/0.9796/34.98$. At 64 projections, student RMSE/SSIM/PSNR are $0.0229/0.9777/34.16$ versus teacher $0.0218/0.9796/34.99$. [PDF p. 7, Table 4]
- PADM-S has the lowest reported RMSE and highest PSNR among Table 5 comparators, while its SSIM $0.9795$ is below UNIT $0.9848$. [PDF p. 7, Table 5]
- Figure 2 shows qualitative HLA/SA/VLA images and error maps. [PDF p. 8, Figure 2]

### Limitations and safe boundary

- The authors call for clinician evaluation of diagnostic quality and downstream tasks. Increasing projection count worsens student-teacher matching in the reported experiment. [PDF pp. 7–8, Section 5.2 and Conclusion]
- The source does not establish exact satisfaction of a physical constraint, accuracy/identifiability of learned path lengths or $\mu$, an isolated physics-module-versus-distillation ablation, statistical significance, external validation, or 3D spatial consistency.
- Prose says the student replicates teacher output, whereas the equations specify attention-feature transfer; attention aggregation/layer choice and differentiation through the physics module are incompletely specified.
- **Bounded relevance:** direct teacher-student precedent on 2D images with privileged CT-input removal. It does not demonstrate external physical projection $\rightarrow$ corrected target $\rightarrow$ corrector-free student, representation-freedom benefit, or safe correction.

## Targeted Human Audit - pivotal claims P1-P4

- Audit date: 2026-09-01
- Audit operator: AI Agent preparation with project-lead completion confirmation; original admitted PDF checked textually and visually
- Selection basis: the project lead's targeted-audit instruction identifies `SRC-0004` as a selected pivotal Source
- Audit state: Human Audit completed; the project lead explicitly approved `EV-0004` through `EV-0006`, which are verified within their recorded boundaries
- Scientific authority: `D:\Litho\2-3nm litho\raw\SRC-0004_PADM.pdf`, arXiv `2511.06948v1`, SHA-256 `EC7AAFC92B072C406DE957AB164531D81CFF435D3A34D2D2668EB8740012A3EF`
- Scope: only P1-P4 and their specified negative boundaries; no repeated admission, Tier 2 ingestion, full-paper summary, novelty analysis, or independent replication

### A. Audit verdict table

| Claim | Verdict | Best locator | Confidence | Important boundary |
|---|---|---|---|---|
| P1 | `verified-with-boundary` | PDF p. 4, Figure 1, Eqs. (3)-(4); p. 5, Eqs. (5)-(6) and the piecewise definition of $C$ | High | The privileged item is specifically the CT-derived attenuation map and its cross-attention conditioning. The Student still uses paired AC targets during training and retains its own physics-aware diffusion architecture. |
| P2 | `verified-with-boundary` | PDF pp. 5-6, Eqs. (7)-(15), Algorithms 1-2; Figure 1(b) | Medium-high | The ACF path is internal to each diffusion denoising step, but module $\mathcal P$, the merge between Eqs. (10) and (14)-(15), and gradient flow through the physics path are incompletely specified. No physical validation of predicted $s_{\phi_m}$ or $\mu$ is reported. |
| P3 | `verified-with-boundary` | PDF p. 6, Section 4.5, Eqs. (16)-(18); Figure 1(a) | Medium-high | The only mathematically specified teacher-dependent transfer term is normalized aggregated-attention matching. `Agg` and the exact feature layers are undefined, $C^S=y$ is called an attention feature, and prose about replicating teacher outputs is broader than the objective shown. |
| P4 | `verified-with-boundary` | PDF pp. 4-6, Figure 1, Eq. (4), piecewise $C$, Algorithm 2, Eqs. (10)-(15); p. 7, Tables 3-4; p. 8, Conclusion | High for Teacher/CT removal and iterative sampling; medium-high for the Student-specific physics-path reconstruction | PADM-S removes PADM-T and CT conditioning, not reverse diffusion or the Student's physics-aware denoising path. The paper reports no measured inference time or speedup, and the Teacher-Student gap grows at higher projection counts. |

### Negative-boundary check

| Item | Classification | PDF basis and boundary |
|---|---|---|
| Exact satisfaction of a physical constraint | `not-established` | Eqs. (11)-(15) impose a formula-shaped ACF computation, but the paper gives no constraint residual, exactness proof, or feasibility test. |
| Physical accuracy or identifiability of predicted path lengths or $\mu$ | `not-established` | The fields are latent U-Net predictions with no direct field supervision, independent measurement, identifiability analysis, or physical-accuracy metric. |
| Formal feasibility guarantee | `not-established` | No theorem, admissible-set definition, convergence guarantee, or feasibility certificate is provided. |
| External projection onto a physical solution space | `explicitly-not-supported` | Figure 1(b) and Section 4.4 place the ACF computation inside every diffusion denoising step; no external solution set or projection operator is defined. |
| Corrected-output distillation | `not-established` | Eqs. (16)-(18) specify attention transfer, while paired AC $x_0$ supplies the diffusion target. The broader prose that the Student replicates Teacher outputs is not instantiated as a Teacher-output label loss. |
| Deployment-time safety gate or fallback | `not-established` | The audited architecture, sampling algorithm, experiments, and Conclusion specify no accept/reject gate, fallback, trust region, or safety check. |
| Physics-module-versus-distillation ablation | `not-established` | Tables 3-5 do not isolate the physics-aware module from attention distillation under a controlled comparison. |
| Demonstrated representation-freedom benefit | `not-established` | No comparison measures representation restriction or freedom against an alternative physics-integration strategy. |

### B. Claim verification

#### P1

**Candidate claim**

PADM uses an explicit teacher-student architecture in which PADM-T receives both the NAC image and a CT-derived attenuation map, while PADM-S receives only the NAC image.

**What the PDF actually establishes**

PADM-T is defined as $\hat I_{AC}^{T}\sim T_\theta(I_{NAC},A)$, where $I_{NAC}$ is a NAC slice and $A$ is a 3D CT-derived attenuation map. PADM-S is defined as $\hat I_{AC}^{S}\sim S_\phi(I_{NAC})$. The reverse-process conditioning is explicit: $C=\operatorname{CrossAttn}(y,A)$ for the Teacher and $C=y$ for the Student. The authors state that the Student performs inference using only NAC slices and has the same architecture as the Teacher. Paired AC $x_0$ remains a training target for both networks; it is not a deployment input. The PDF identifies no other Teacher-only data, Teacher call, or privileged input required for Student deployment.

**Best locator(s)**

- PDF p. 4, Figure 1, Eqs. (3)-(4), Teacher Network and Student Network paragraphs.
- PDF p. 5, Eqs. (5)-(6), Cross-Modality Transformer Attention, and the piecewise definition of $C$.
- PDF p. 6, Section 4.5, Eqs. (16)-(18).
- PDF p. 8, Conclusion.

**Mechanism / textual basis**

- **Explicit author statement:** the Student "performs inference using only NAC slices with the same architecture as the teacher"; the Conclusion states that no CT-based attenuation-map input is required during inference.
- **Equation / algorithm / figure mechanism:** Eqs. (3)-(4) separate Teacher and Student inputs; Figure 1 routes $A$ only through the Teacher cross-modality transformer; the piecewise $C$ supplies `CrossAttn(y,A)` to the Teacher and $y$ to the Student.
- **Reasonable inference:** once PADM-S is trained, neither PADM-T nor its frozen features are needed to execute the Student sampling path. No separate Student-only inference algorithm is printed.
- **Project interpretation:** privileged CT-derived physics information can be used during training and removed from the deployed Student's input boundary, but physics information in the broader sense is not confined to the Teacher because the Student retains learned physics-aware machinery.

**Boundary / non-support**

"Same architecture" is an author statement about PADM-T and PADM-S, while Figure 1 and the piecewise $C$ show different conditioning paths: only the Teacher uses the cross-modality transformer output. Both networks also use paired AC images during training. The PDF does not establish that every training-time signal is Teacher-exclusive, only that the CT-derived attenuation map is absent from Student inference.

**Recommended Evidence wording**

PADM-T conditions its diffusion model on a NAC slice and a CT-derived attenuation map through $C^T=\operatorname{CrossAttn}(y,A)$, whereas the same-architecture PADM-S uses $C^S=y$ and is reported to require only the NAC slice at inference; the CT map and frozen Teacher are training-only for the deployed Student.

#### P2

**Candidate claim**

PADM predicts attenuation-related quantities and uses them to construct an input-dependent attenuation-correction factor inside the predictive model rather than as an external output projector.

**What the PDF actually establishes**

At diffusion step $t$, the physics-aware U-Net receives $z^{(t)}=\operatorname{concat}(x_t,C)$. It predicts $N$ per-angle path-length fields $\{s_{\phi_m,\theta}^{(t)}\}_{m=1}^{N}$, an attenuation-coefficient/attenuation-map field $\mu_\theta^{(t)}$, and an auxiliary clean-image channel $\tilde x_0^{(t)}$. Equation (13) substitutes the predicted $s$ and $\mu$ into an inverse mean of $\exp[-\mu s]$ terms to construct the input-dependent $\operatorname{ACF}_\theta^{(t)}$. Equation (10) defines the denoising output using $y\odot\operatorname{ACF}_\theta^{(t)}$; Eqs. (14)-(15) describe a physics-aware module $\mathcal P$ that turns predicted $s$ and $\mu$ into $\bar x^{(t)}$ and blends it with $\tilde x_0^{(t)}$. Section 4.4 explicitly places this operation at each diffusion step, and Algorithm 2 repeatedly calls the resulting denoiser during reverse sampling.

**Best locator(s)**

- PDF p. 4, Figure 1(b) and caption.
- PDF p. 5, reverse-process definition and Algorithm 1.
- PDF p. 6, Algorithm 2, Section 4.4, Eqs. (10)-(15).

**Mechanism / textual basis**

- **Explicit author statement:** the network operates in image space and approximates physics-aware AC reconstruction at each diffusion step; Section 4.4 says the denoising network is redefined to produce an attenuation-corrected reconstruction.
- **Equation / algorithm / figure mechanism:** Eqs. (12)-(13) predict $s$, $\mu$, and $\tilde x_0$ and construct $\operatorname{ACF}_\theta^{(t)}$; Eqs. (10), (14), and (15) feed the physics-shaped result into the denoising estimate used by the reverse update; Figure 1(b) shows the same internal path.
- **Reasonable inference:** because $X_\theta$ appears inside both $\mathcal L_{ELBO}$ and every Algorithm 2 update, the physics-aware computation participates in prediction rather than being applied only after the final sampled $x_0$. The paper does not expand $\mathcal P$ in the algorithm.
- **Project interpretation:** PADM is precedent for internal, input-dependent physics-shaped computation inside a predictive model, not for an external projection of a completed neural output onto a defined physical solution space.

**Boundary / non-support**

No direct loss, range constraint, ground-truth field comparison, or identifiability test is given for $s_{\phi_m}$ or $\mu$. The PDF does not explicitly document differentiation through $\mathcal P$. It also overloads $\mu_\theta$: p. 5 uses it for the reverse Gaussian mean, while p. 6 uses it for the predicted attenuation field. Equation (10), Eqs. (14)-(15), and Algorithm 2 do not fully spell out one implementation-level composition.

**Recommended Evidence wording**

At each PADM diffusion step, the denoising U-Net predicts per-angle path-length fields, a $\mu$ attenuation field, and an auxiliary clean-image channel; Eqs. (10)-(15) use the predicted $s$ and $\mu$ to construct an input-dependent ACF and a refined denoising estimate inside reverse diffusion, without independently establishing the physical accuracy or identifiability of those predicted fields.

#### P3

**Candidate claim**

PADM transfers privileged physics knowledge from PADM-T to PADM-S through attention-feature matching rather than through corrected-target distillation.

**What the PDF actually establishes**

The mathematically specified Teacher-dependent representation is $Q_T=\operatorname{Agg}(C^T)$, where $C^T=\operatorname{CrossAttn}(y,A)$. The Student representation is $Q_S=\operatorname{Agg}(C^S)$, with $C^S=y$ in Eq. (16). Equation (17) matches the $L_2$-normalized $Q_T$ and $Q_S$ representations. During Student training the Teacher remains frozen, and Student parameters are optimized with $\mathcal L_{Total}=\mathcal L_{ELBO}+\lambda\mathcal L_{AT}$. The paired AC image $x_0$, not a Teacher-corrected output, is the diffusion target in Algorithm 1 and Eq. (9). No equation or algorithm supplies the Teacher's reconstructed AC image as a Student label.

**Best locator(s)**

- PDF p. 4, Figure 1(a), Eq. (4), and the prose continuing onto p. 5.
- PDF p. 5, Algorithm 1, Eq. (9), and the piecewise definition of $C$.
- PDF p. 6, Section 4.5, Eqs. (16)-(18).

**Mechanism / textual basis**

- **Explicit author statement:** Section 4.5 says PADM employs Attention Transfer; the Teacher remains frozen while Student parameters are optimized.
- **Equation / algorithm / figure mechanism:** Eqs. (16)-(17) aggregate, $L_2$-normalize, and match Teacher/Student representations; Eq. (18) adds that term to the Student diffusion loss; Figure 1 labels U-Net feature distillation.
- **Reasonable inference:** the Student receives gradients from its diffusion objective and from $\lambda\mathcal L_{AT}$, while the frozen Teacher supplies a fixed feature target. The paper does not provide an explicit gradient graph.
- **Project interpretation:** the evidenced transfer chain is privileged CT-conditioned Teacher representation $\rightarrow$ attention/feature matching $\rightarrow$ Student, not external physical corrector $\rightarrow$ corrected output label $\rightarrow$ Student.

**Boundary / non-support**

The exact `Agg` operation, source layers, tensor shapes, and whether Figure 1's "U-Net's features" are identical to the $C$ tensors in Eq. (16) are not specified. Equation (16) calls $C^S=y$ the Student's attention features even though $y$ is the NAC image/condition. Prose on pp. 4-5 says the Student replicates Teacher outputs, but the printed objective contains no Teacher-output matching term. Therefore the equations support attention transfer, while the broader output-replication wording remains unresolved rather than proving corrected-output distillation.

**Recommended Evidence wording**

The only mathematically specified Teacher-dependent term in PADM-S training matches $L_2$-normalized aggregated representations $Q_T=\operatorname{Agg}(C^T)$ and $Q_S=\operatorname{Agg}(C^S)$; the Teacher is frozen and the Student is optimized with $\mathcal L_{ELBO}+\lambda\mathcal L_{AT}$, while paired AC $x_0$ remains the diffusion target and no Teacher-corrected output label is specified.

#### P4

**Candidate claim**

PADM-S can operate without PADM-T or the CT-derived attenuation map at inference, but reverse-diffusion sampling and the Student's own physics-aware module remain part of inference; reported Student performance remains close to the Teacher in the principal setting.

**What the PDF actually establishes**

Equation (4), Figure 1, the piecewise definition $C=y$ for the Student, and the Conclusion explicitly establish NAC-only Student inference without the CT-derived attenuation map. Section 4.5 confines the frozen Teacher to Student training. Algorithm 2 starts from $x_T=y$ and iterates from $t=T$ to $1$, so inference is reverse-diffusion sampling rather than one-pass prediction. Section 4.4 redefines the denoising network at each diffusion step through the physics-aware ACF path; combined with the stated same architecture and Student condition $C=y$, this structurally places the Student's physics-aware module in sampling. Table 3 and the 16-projection row of Table 4 report PADM-T/PADM-S as RMSE $0.0217/0.0218$, SSIM $0.9796/0.9795$, and PSNR $34.98/34.75$. Table 4 also reports a larger 64-projection gap: RMSE $0.0218/0.0229$, SSIM $0.9796/0.9777$, and PSNR $34.99/34.16$.

**Best locator(s)**

- PDF p. 4, Figure 1 and Eq. (4).
- PDF p. 5, piecewise $C$ and reverse-process description.
- PDF p. 6, Algorithm 2, Sampling Process, Eqs. (10)-(15), and Section 4.5.
- PDF p. 7, Tables 3-4 and Section 5.2.
- PDF p. 8, Conclusion.

**Mechanism / textual basis**

- **Explicit author statement:** the Student performs inference using only NAC slices; the Conclusion says CT-based attenuation-map input is not required during inference; DDIM is used for sampling.
- **Equation / algorithm / figure mechanism:** Algorithm 2 contains a $T\rightarrow1$ reverse loop; $X_\theta$ is called at every step; Eqs. (10)-(15) define $X_\theta$ through the physics-aware ACF path; Figure 1 shows reverse processes for both Teacher and Student.
- **Reasonable inference:** the Student's own physics-aware module remains active because PADM-S is stated to share the architecture and uses the same denoising definition with $C=y$. The PDF does not print a separate Student-only Algorithm 2 that expands $\mathcal P$.
- **Project interpretation:** PADM demonstrates removal of privileged Teacher/CT conditioning, not removal of physics correction or diffusion machinery and not a corrector-free one-pass surrogate.

**Boundary / non-support**

The paper calls DDIM accelerated sampling relative to standard Markovian diffusion but reports no inference latency, throughput, speedup factor, or one-pass evaluation. The number of inference sampling steps is not separately reported. The close Teacher-Student gap is a reported result on CardiAC without statistical uncertainty, external validation, or a controlled deployment-cost measurement, and it widens with projection count.

**Recommended Evidence wording**

Reported PADM-S inference removes PADM-T and CT-derived attenuation-map conditioning but retains iterative reverse-diffusion sampling and, structurally, the Student's internal physics-aware denoising path; at 16 projections the reported PADM-S metrics differ from PADM-T by $0.0001$ RMSE, $0.0001$ SSIM, and $0.23$ dB PSNR, with no measured inference-time acceleration.

### C. Evidence materialization resolution

| Claim | Materialized ID | Disposition |
|---|---|---|
| P1 | `EV-0004` | Merged with P3 because privileged CT conditioning, the frozen Teacher, and the specified attention-transfer loss are inseparable parts of one transfer mechanism. |
| P2 | `EV-0005` | Materialized as the internal-physics-path claim; physical validity of predicted fields remains an explicit non-support boundary. |
| P3 | `EV-0004` | Merged with P1; no corrected-output-distillation claim was created from the broader prose. |
| P4 | `EV-0006` | Materialized as the structural inference-boundary claim; the 16-projection numerical gap is supporting context inside the same record, not a fourth Evidence record. |

Exactly three permanent records were allocated: `EV-0004`, `EV-0005`, and `EV-0006`. The project lead approved all three on 2026-09-01, and they are verified within their recorded boundaries.

#### Materialized Evidence - `EV-0004`

- Title: Privileged CT-conditioned attention transfer to a CT-free PADM Student
- Atomic claim: PADM-T uses $C^T=\operatorname{CrossAttn}(y,A)$ from NAC and a CT-derived attenuation map, while the frozen Teacher supplies the normalized aggregated representation matched by PADM-S; PADM-S uses $C^S=y$ and requires only NAC at inference.
- Source ID: `SRC-0004`
- Exact locator: PDF p. 4, Figure 1, Eqs. (3)-(4); p. 5, Eqs. (5)-(6), piecewise $C$, Algorithm 1 and Eq. (9); p. 6, Eqs. (16)-(18); p. 8, Conclusion.
- Support type: explicit author statement plus equation/figure mechanism; no Teacher-output label is specified.
- Applicability boundary: reported PADM architecture and CardiAC training only; paired AC remains the diffusion target; exact `Agg` operation and feature layers are unspecified; no corrected-output distillation claim.
- Confidence: Medium-high.
- Project relevance: strong precedent for training-only privileged physics conditioning transferred into a Student whose deployed input boundary excludes that privileged data.

#### Materialized Evidence - `EV-0005`

- Title: Internal input-dependent attenuation-factor computation in PADM denoising
- Atomic claim: at each PADM diffusion step, the denoising U-Net predicts per-angle path-length fields and a $\mu$ attenuation field and uses them through Eqs. (10)-(15) to construct an input-dependent ACF and refined clean-image estimate inside reverse diffusion.
- Source ID: `SRC-0004`
- Exact locator: PDF p. 4, Figure 1(b); PDF pp. 5-6, Algorithms 1-2 and Eqs. (7)-(15).
- Support type: equation/algorithm/figure mechanism plus explicit at-each-step description.
- Applicability boundary: internal model-component claim only; $\mathcal P$, gradient flow, and the final composition are incompletely specified; no physical accuracy, identifiability, exact-feasibility, or external-projection claim.
- Confidence: Medium-high.
- Project relevance: distinguishes internal physics-shaped prediction from external output projection and prevents using PADM as precedent for a separate physical corrector.

#### Materialized Evidence - `EV-0006`

- Title: CT-free PADM Student inference retains iterative diffusion and physics-aware denoising
- Atomic claim: PADM-S inference removes PADM-T and CT-derived attenuation-map conditioning but follows the reverse-diffusion loop and retains the same physics-aware denoising architecture with Student condition $C=y$.
- Source ID: `SRC-0004`
- Exact locator: PDF p. 4, Figure 1 and Eq. (4); p. 5, piecewise $C$ and reverse-process definition; p. 6, Algorithm 2 and Eqs. (10)-(15); p. 8, Conclusion.
- Support type: explicit input-boundary statement plus algorithm/figure structure and bounded inference from the same-architecture statement.
- Applicability boundary: no separate Student sampling algorithm, implementation trace, sampling-step count, latency, throughput, speedup, safety gate, or fallback.
- Confidence: High for Teacher/CT removal and iterative diffusion; medium-high for the Student-specific physics path.
- Project relevance: prevents upgrading Teacher/CT removal into a corrector-free, physics-free, or one-pass deployment claim.

#### Supporting numerical context merged into `EV-0006` - no separate Evidence record

- Disposition: The reported PADM Teacher-Student performance gap is retained as supporting numerical context in `EV-0006`; no fourth Evidence record was created.
- Atomic claim: on CardiAC, PADM-S nearly matches PADM-T at 16 projections in the reported metrics, while the reported gap increases at 64 projections.
- Source ID: `SRC-0004`
- Exact locator: PDF p. 7, Tables 3-4 and Section 5.2.
- Support type: direct table observation plus author-reported interpretation.
- Applicability boundary: reported single-dataset metrics only; no uncertainty, significance test, external validation, or general benchmark claim.
- Confidence: High for the table values.
- Project relevance: establishes the scale and operating-boundary sensitivity of privileged-input removal without claiming deployment acceleration.

### D. Human attention required

1. **Physics-path differentiation:** Eqs. (9)-(15) make a differentiable end-to-end path plausible, but the paper never explicitly states whether gradients traverse every operation in $\mathcal P$ or whether any component is stopped or treated procedurally.
2. **Attention-transfer tensor identity:** `Agg` and the source layers are undefined; Eq. (16) sets $C^S=y$ while calling it a Student attention feature, Figure 1 labels U-Net feature distillation, and the prose says the Student replicates Teacher outputs. The Evidence wording should remain equation-anchored unless the project lead resolves this mismatch differently.
3. **Student inference reconstruction:** Algorithm 2 calls a generic $X_\theta$ and does not expand $\mathcal P$ or print a separate PADM-S sampling algorithm. The Student physics-path conclusion is supported by Figure 1, Section 4.4, the same-architecture statement, and $C=y$, but is partly reconstructed rather than stated in one place.
4. **Physics-variable meaning and implementation composition:** $\mu_\theta$ is overloaded between the reverse Gaussian mean and the attenuation field; Figure 1 calls it "mean"; Eqs. (10) and (14)-(15) do not completely specify how $y\odot\operatorname{ACF}$, $\mathcal P$, and the weighted auxiliary channel become the exact $X_\theta$ used in Algorithm 2. No independent validation establishes that predicted $s_{\phi_m}$ or $\mu$ is physically accurate.

### E. Final pivotal judgment

`retain as pivotal with narrowed role`

`SRC-0004` is strong precedent for using privileged CT-derived physics conditioning during training and transferring its internal representation into a Student that no longer requires the Teacher or CT map at inference. Its project role stops at that teacher-student mechanism: PADM retains internal physics-aware denoising and iterative diffusion during deployment and does not establish external physical projection, corrected-output distillation, a corrector-free one-pass surrogate, or representation-freedom benefit.

## 用户研究偏好与阅读补充 — 2026-09-13

本节记录用户明确要求保存的偏好，由 Agent 整理，`content_origin: ai-assisted`；它不改写上面的 Human Audit 或已验证 Evidence。

用户希望将 PADM 的 conditional diffusion＋U-Net 作为本轮优先候选 framework，特别关注逐步图像重建、内部物理计算，以及 training-only 物理信息向 Student 的 representation transfer。同时保留 correction → 知识回传与减少高保真标签需求两个研究重点。“优先候选”是研究讨论安排，不是选定长期 architecture。

需保留的原文区别：Algorithm 1 使用 paired NAC/AC、随机 timestep 和 Gaussian noise 构造中间训练状态；noise variants 不会自动增加独立 target。Algorithm 2 从条件输入 NAC 开始采样；diffusion timestep 不代表光刻真实物理阶段。Teacher 依赖项为 attention/representation matching，paired AC target 仍在，不能写成 Teacher-corrected output labels。[PDF pp. 5–6, Eqs. (7)、(16)–(18), Algorithms 1–2]

光刻中的 bridge、输出单位与尺度、内部物理关系、可用 privileged input 和计算预算均未确定。对应 draft 研究问题记录于 BG-0002、HYP-0001–HYP-0003；保存这些条件性假设不代表取得新的光刻 Evidence，也不证明 diffusion 优于直接预测。
