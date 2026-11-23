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

- **Last attempted:** Lesson 04 Part 27. Understanding still needs a short explanation in the learner’s own words.
- **Teaching style:** Show a small table or tensor, ask one short shape, node-ID or one-line PyTorch question, and wait for an attempt. Explain the result visually, then advance one concept.
- **Suggested first check:** F6 receives two messages of width four. F9 receives three messages of the same width. Show the groups as rows and ask the learner to predict the shape of F9’s stacked matrix and explain what its first dimension counts. Withhold the expected result until the learner answers.
- **After the answer:** If the axes are clear, proceed one small step toward processing a single receiver’s variable-size message group. If they are unclear, label the rows “incoming Pair” and the columns “feature”, then ask about a different receiver. Record what the learner actually demonstrated.

At the end of a later session, append the lesson/part, exercise, actual attempt, what the learner explained, and one next question. Update “Last attempted” to match that entry.
