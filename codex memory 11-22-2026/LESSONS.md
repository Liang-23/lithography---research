# Lesson history and current checkpoint

AI-assisted reconstruction from the learner’s FD-GNN sessions. The examples below are teaching examples. Multiple-choice letters alone do not establish understanding. The tutoring sessions referred to `prototypes/fd_gnn/fft_features.py`. Its contents were not verified on this repository’s `main` or `dev/fd-gnn-workbench` branch.

| Lesson | Practiced | One concrete check |
| --- | --- | --- |
| 01 · Frequency Nodes | Binary mask, `torch.fft.fft2`, frequency grids, and `torch.stack(..., dim=-1)` to put four features together at each bin. Flatten only the two grid axes. | For an $8\times8$ grid, `features.reshape(-1, 4)` gives 64 rows. At row 2, column 3, node 19 holds the four features for that bin. |
| 02 · Pair Nodes | Retrieve complex coefficients from `spectrum.reshape(-1)` using square-bracket indexing. Form `A_k * torch.conj(A_l)`. | Swapping the endpoints conjugates the product. For nonzero coefficients its phase is the endpoint phase difference. The flat complex spectrum and the four-column node table answer different lookup questions. |
| 03 · Difference Nodes | Recover row and column with `// W` and `% W`. Compute signed component differences, then map them to bins in a circular-grid exercise. | On the exercise grid, `q_y % H` wraps a negative row difference into a valid index. The canonical modular-versus-padded FFT choice is still open. |
| 04 · Pair-to-Frequency messages | Assemble Pair features, identify which Pair messages reach each receiver, and summarize a variable number of messages. | For F6, make message rows correspond to Pairs incident to F6. Distinguish counting rows from reading feature width. |

## Lesson 04 in more detail

| Parts | What the learner worked through | What to check when needed |
| --- | --- | --- |
| 1–5 | Joined endpoint vectors, split the complex Pair product into real and imaginary channels, and prepared a floating-point difference vector. | `torch.cat([h_k, h_l], dim=0)` joins two 1D vectors. `torch.stack([pair_real, pair_imag])` gives two scalars a new axis. Joining unequal-length 1D feature groups calls for concatenation. |
| 6–14 | Used endpoint IDs for indexing. Flattened endpoint IDs into a receiver list, masked it for F6, and identified the incoming Pair IDs. | Each receiver entry needs its aligned Pair ID. `torch.unique(receiver_ids)` enumerates receivers. Keep the full aligned list for grouping. |
| 15–21 | Practiced elementwise max and receiver-specific attention using supplied toy weights. | Each max output channel can come from a different Pair. A weighted sum uses the weights supplied for the receiver in that example. |
| 22–25 | Collected incoming vectors with `append`, stacked them into `message_matrix`, then read `message_matrix.shape[0]`. | For a nonempty list of equal-width vectors, each row is one incoming message. Different receivers may have different row counts. |
| 26–27 | The learner attempted both checks and chose B. At Part 27 the learner explicitly remained unsure. | The exact prompts and option texts are unavailable here. Recheck the concept with a fresh example before marking progress. |

## Resume here

- **Last attempted:** Lesson 04, Part 27 (fresh recheck, 2026-11-23). Overall stacked shape `[3, 4]` and the link between `3` and the 3 incoming Pair messages were right, while `shape[0]` and `shape[1]` were swapped; one quick receiver check on `F6` is needed before advancing.
- **Teaching style:** Show a small table or tensor, ask one short shape, node-ID or one-line PyTorch question, and wait for an attempt. Explain the result visually, then advance one concept.
- **Suggested first check:** Using the same toy incoming Pair-to-Frequency message table (`F6`: `P0`, `P1`; `F9`: `P2`, `P3`, `P4`; toy feature width $4$), ask: if we stack `f6_messages` with `f6_message_matrix = torch.stack(f6_messages, dim=0)`, what are `f6_message_matrix.shape[0]` and `f6_message_matrix.shape[1]`, and why is `f6_message_matrix.shape[0]` different from `f9_message_matrix.shape[0]`? Withhold the expected result until the learner answers.
- **After the answer:** If `shape[0]` (row count = incoming Pairs) vs. `shape[1]` (column count = feature width) and the per-receiver variation are clear in the learner’s own words, proceed one small step toward processing a single receiver’s variable-size message group. Record what the learner actually demonstrated.

## Session checkpoints

### 2026-11-23 — Lesson 04, Part 27 (fresh recheck via Arm C Drive staging)

- **Lesson and part attempted:** Lesson 04, Part 27 (fresh recheck on `torch.stack(..., dim=0)` shape and axis meaning for `F9`).
- **Exercise and actual learner response:** Given the toy incoming Pair-to-Frequency message table (`F6`: 2 Pairs `P0, P1`; `F9`: 3 Pairs `P2, P3, P4`; width $4$), predicted `f9_message_matrix.shape = [3, 4]` and `f9_message_matrix.shape[0] = 4`, reasoning "because it involving 3 pair messages".
- **What the learner explained correctly:** Correctly predicted the stacked matrix shape `[3, 4]` and connected the `3` to the 3 incoming Pair messages for `F9`.
- **What still needs a check:** Mapping `shape[0]` to the row count (incoming Pairs $= 3$) versus `shape[1]` to the column count (feature width $= 4$), and stating in their own words why `shape[0]` can differ across receiver Frequency Nodes (e.g., `F6` vs. `F9`).
- **Next single question:** Using the same table for `F6` (`P0` and `P1`), if we stack `f6_messages` with `f6_message_matrix = torch.stack(f6_messages, dim=0)`, what are `f6_message_matrix.shape[0]` and `f6_message_matrix.shape[1]`, and why is `f6_message_matrix.shape[0]` different from `f9_message_matrix.shape[0]`?
- **Method decisions touched or left open:** Kept `METHOD-0003` as a draft concept candidate (`method_state: concept`); internal Pair-to-incident-Frequency messages kept distinct from final $q = k - l$ Difference Node rendering; toy feature width $4$ noted as an exercise input only. Left open: attention scoring, normalization, target-specific message orientation, channel widths, exact aggregation equations (attention plus elementwise max remains a working candidate), FFT boundary convention, mode count $R$, and global-context choice (`L0`/`G1`/`G2`).

At the end of a later session, append the lesson/part, exercise, actual attempt, what the learner explained, and one next question. Update “Last attempted” to match that entry.
