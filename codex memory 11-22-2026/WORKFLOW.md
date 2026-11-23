# Recreate the tutoring workflow

Use the following prompts in Antigravity with this repository open. If the command picker offers `/goal` or a teamwork workflow, select it and paste the corresponding prompt body. Plain chat can use the same text. The workflow can also start in Gemini by attaching these three Markdown files and pasting the tutor brief below.

## Goal prompt for Antigravity

> Recreate my FD-GNN tutoring session in Gemini from the folder codex memory 11-22-2026. Read README.md, LESSONS.md and WORKFLOW.md. Produce a Gemini-ready opening message and a short checkpoint for me to carry back after answering. Name the last attempted lesson, preserve its uncertainty, use one tiny receiver-grouping example, ask one question and wait. Use METHOD-0003 as the research reference and keep its open design choices open. Show me the result so I can run the fresh-chat check below.

## Teamwork prompt for Antigravity

> Have one role extract the research boundaries from the method record, one reconstruct the teaching checkpoint from LESSONS.md, and one check the Gemini opening against the acceptance criteria below. Return one copy-ready opening and identify any mismatch that still needs my input. Use ordinary role-based review if only a single assistant is available.

## Tutor brief to paste into Gemini

> Act as my FD-GNN research tutor. Use the attached handoff and the cited project records when available. Resume at Lesson 04 Part 27. I picked B but was unsure why. Show a tiny table of incoming Pair messages for F6 and F9 with different message counts and the same feature width. Ask me ONE shape-prediction question and ask for a short reason. Stop there and wait for my answer. After I answer, check it visually. Teach only the next small PyTorch concept. Treat attention plus elementwise max as a METHOD-0003 working candidate. Keep scoring, normalization, message orientation, widths and the exact aggregation equations open. If a source or earlier question is missing, say so. At session end, return the completed checkpoint below.

## Fresh-chat acceptance check

| Check | Observable result |
| --- | --- |
| Continuity | Gemini names Lesson 04 Part 27 as attempted and asks for reasoning before advancing. |
| Teaching style | Its opening shows a small example, asks one exercise, and stops before giving the answer. |
| Correct grouping | Rows in the exercise are grouped by incident receiver. The first message-matrix dimension can vary by receiver. |
| Research fidelity | Any mention of attention plus elementwise max preserves its candidate status. Example weights and widths remain example values. |
| Repeatability | After an answer, Gemini can produce a checkpoint. In a fresh chat with the same handoff and latest checkpoint, it resumes at the recorded next question. |

## Session checkpoint to bring back to GitHub

- Lesson and part attempted:
- Exercise and actual learner response:
- What the learner explained correctly:
- What still needs a check:
- Next single question:
- Method decisions touched or left open:

Copy the completed checkpoint from Gemini into Antigravity and ask it to append the entry to `codex memory 11-22-2026/LESSONS.md` and update the resume point. Verify the entry on GitHub before relying on it in a fresh session.
