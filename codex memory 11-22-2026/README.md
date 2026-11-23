# FD-GNN learning handoff

Start at **Lesson 04, Part 27**. The last recorded attempt was “B” with uncertainty about the reasoning. Ask one fresh question about incoming Pair messages before moving on. [Lesson history and checkpoint](LESSONS.md) · [Antigravity prompts and Gemini tutor brief](WORKFLOW.md)

This AI-assisted handoff combines two records with different purposes. The project summary below comes from the repository. The lesson checkpoint comes from the learner’s FD-GNN tutoring sessions and records practice, questions and attempts. Update the checkpoint when a lesson is actually attempted.

## What the project is trying to predict

The broader project studies an end-to-end surrogate for forward computational lithography. The specific METHOD-0003 question is whether a network can predict an aerial image for an unseen mask in one forward pass, with the optical setup provisionally fixed. Training would use final aerial images as targets. The learned complex effective-mode coefficients have no individual ground-truth labels. The method record classifies this design as a **draft concept candidate**. Its performance and selection remain open.

| Stage | Input and operation | What the next stage receives |
| --- | --- | --- |
| Frequency Nodes | Take the mask FFT. For each bin, collect the real and imaginary coefficient and normalized absolute frequency coordinates. | One initial feature vector per frequency. |
| Pair Nodes | Read the two endpoint states, the known complex product $p_{k,l}=A(k)\overline{A(l)}$, and $q=k-l$. | Hidden Pair messages for incident Frequency Nodes. |
| Frequency update | The working candidate summarizes incoming messages using attention and elementwise max. Two Frequency–Pair–Frequency rounds are proposed for comparison. | Updated frequency features for the effective-mode generator. |
| Mode head | Predict complex effective-mode coefficients per frequency. L0 uses local features. G1 adds pooled graph context. G2 adds full mask-spectrum context. | Mask-conditioned coefficients $b_r(k;M)$ for the renderer. |
| Difference Nodes and rendering | Each final Pair contribution is $C_{k,l}=p_{k,l}\sum_r b_r(k;M)\overline{b_r(l;M)}$. Sum contributions with a common $q=k-l$, then take the inverse FFT. | A spatial aerial-image prediction. |

**Two destinations matter in the lessons.** To update Frequency Node F6, collect messages from Pairs incident to F6. To assemble one output-spectrum bin, collect final Pair contributions sharing its frequency difference. A Pair can send a hidden message to F6 while its rendered contribution belongs to a different Difference Node.

Keep attention scoring, normalization, target-specific message orientation, channel width, and the exact combination of attention and max open. The FFT boundary convention, mode count, and global encoder choice also remain open. Any numeric tensor dimensions or weights in a lesson are exercise inputs.

## Repository sources

Research snapshot consulted on `main` at `1b4a25861d3ece324453bce91a5857efbc508d4d`. For later research decisions, follow the current repository’s context router and reread the live records.

- [METHOD-0003, sections 2–5](../05_Method_Design/METHOD-0003_Mask_Conditioned_Effective_Mode_FD_GNN.md) defines the graph, the working aggregation candidate, the mode head and the renderer.
- [Global context comparison](../08_Project_Status/FD_GNN_Global_Context_Candidates_2026-10-14.md) records which parts L0, G1 and G2 vary.
- [Current State](../08_Project_Status/Current_State.md) and [Context Router](../08_Project_Status/Context_Router.md) identify the project status and authoritative reading route.
