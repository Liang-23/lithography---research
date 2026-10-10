
[[我们要找的是]]

对。你现在已经到了一个非常关键的分界点：

> **Governance 搭建结束，接下来不要继续治理，而要正式开始 scientific discovery。**

而且你的第一步，我不建议马上做实验，也不建议马上搭一个很复杂的 simulator。**第一步应该是有目标地做 literature + Evidence discovery。**

但和以前“去网上看看别人做了什么”不同，现在你读论文必须带着一个非常明确的问题去找答案。

## 你现在真正的第一个科学任务

你当前 Core 的思想可以压缩成：

> **让高维 AI surrogate 自由学习内部 representation，不持续用 physics gradient / physics loss 去约束它；物理知识主要作用在 output / terminal solution 层，再研究如何把 corrected solution 的知识传回 surrogate。**

所以你现在最大的不确定性已经不是：

> “我要不要做 physics-aware surrogate？”

这个已经确定了。

真正不知道的是：

> **到底哪一个 physical relationship 可以作用在 lithography surrogate 的 output 上，而且是 computable、有效、不会破坏 prediction、还能最终服务于 end-to-end surrogate？**

这就是你现在的第一个 research question。

而且这个问题已经和你当前 `Current_State` 里的 unresolved definitions 完全一致：你还没有定义 exact physical relationship、valid solution set、projection operator、variables/units/tensor shape/output stage，也还没有正式的 Data/Simulator contract。Current_State.mdMD

---

# 所以现在不要随机读论文

我建议把第一轮 literature research 收窄成 **三个问题**。

### Q1. 别人到底如何把 physics 放到 neural surrogate 的 output 端？

重点找：

- output projection
- physical manifold projection
- constrained output correction
- terminal correction
- post-prediction physics correction
- projection-based learning
- hard / soft output constraints
- corrected target distillation

而不是再广泛搜索：

> physics-informed neural networks

因为 PINN 太大了，其中大量工作会把 physics residual 直接塞进 training loss，这不是你最想研究的路径。

而且现在已经有非常直接的先例需要你认真读。2025 年一篇 _Communications Physics_ 工作就提出了把 ML surrogate 输出直接 projection 到由 physical laws 定义的 manifold，而且明确把它与把 physics penalty 塞进 training loss 的方法区分开。它使用的是类似

\[ \min_p \|p-f(x;\theta)\|_W^2 \quad \text{s.t.}\quad g(x,p)=0 \]

这样的 output projection。[Nature](https://www.nature.com/articles/s42005-025-02329-1?utm_source=chatgpt.com)

这篇论文对你非常重要。

不是因为它证明你的课题错了，而是因为它意味着：

> **“output projection 本身”已经不能直接作为你的创新点。**

你需要继续问：

> lithography 的 \(g(x,y)\) 到底是什么？  
> 高维 image output 怎么定义 physical solution set？  
> correction 怎样最小破坏 learned spatial structure？  
> 怎样把 correction 再 distill 回 surrogate，使最终 inference 不需要外部 projection？

最后这一层可能才是你真正应该往下挖的位置。

---

# Q2. Lithography 里究竟有哪些可以计算的 output physics？

这是你接下来读 lithography papers 的核心目的。

不要先想着“我要找创新”。

先建立一个候选表：

|Candidate physics|作用在哪个 output|能否计算|需要什么 simulator/data|是否适合 projection|
|---|---|---|---|---|
|PC candidate A|aerial image|?|?|?|
|PC candidate B|resist image|?|?|?|
|PC candidate C|wafer image|?|?|?|

也就是说，你接下来读一篇 lithography paper，不是只写 Summary。

而要问：

> **这篇论文有没有给我一个可以写成 \(R(x,y)=0\)、\(R(x,y)\leq \epsilon\)，或者某种 computable operator 的 physical relation？**

如果没有，它可能是 Background。

如果有，它才有机会往：

`SRC → EV → PC`

这条链走。

---

# Q3. 要测试这些 physics，我需要什么 simulator？

这是第三个问题。

注意这里我暂时不建议：

> “马上正式选 `pylitho.exact.LithoSim` 为 canonical simulator。”

你刚刚模拟三已经很好地证明了，这属于 strategic decision，需要 Evidence。

你现在更适合做：

> **Simulator characterization / contract discovery**

也就是先弄明白：

- simulator input 是什么；
- output 是 aerial / resist / wafer 哪一层；
- physical parameters 是什么；
- units；
- resolution；
- process conditions；
- focus/dose；
- differentiability；
- computational cost；
- 什么东西可以作为 high-fidelity reference；
- 哪些 physical quantities 能从 simulator 中得到。

先把它**描述清楚**，而不是先宣布它是 canonical simulator。

---

# 所以你的第一阶段其实可以叫

## Stage 1 — Physical Constraint Discovery

目标不是训练模型。

目标是找到：

> **第一个值得进入 `PC-0001` 的 computable output-level physical relationship。**

我建议你在这一阶段只做三类工作：

**Literature → Evidence → Simulator understanding**

然后才进入：

**Physics Constraint → Hypothesis → Method → Experiment**

---

# 你现在的完整科学路线

你可以把后面的路线压缩成这一条：

```
① Targeted literature discovery
        ↓
② Register relevant SRC
        ↓
③ Verify important claims → EV
        ↓
④ Characterize Data / Simulator
        ↓
⑤ Candidate physical relationships
        ↓
⑥ PC-0001
        ↓
⑦ HYP-0001
        ↓
⑧ METHOD-0001
        ↓
⑨ EXP-0002
        ↓
⑩ Evidence
        ↓
⑪ Decide whether the idea survives
```

这时候 governance 才真正开始给科研服务，而不是科研给 governance 打工。

---

## 那你现在“明天打开电脑第一件事”具体做什么？

我建议不是训练。

也不是写 simulator。

就是启动一个**定向文献搜索任务**：

> **寻找可以用于 high-dimensional computational lithography forward-surrogate output correction 的 computable physical relationships，以及 output projection / terminal physical correction / corrected-target distillation 的现有方法。**

而且这个搜索要同时完成两件事：

**一条线看 lithography physics。**

寻找：

> “我们究竟可以约束什么？”

**另一条线看 ML methodology。**

寻找：

> “别人已经如何做 output correction / projection / knowledge transfer？”

两条线最后交叉：

```
Lithography
“What physics can be computed?”
               ↓
            PC candidate
               ↑
Machine Learning
“How can output physics be integrated
without constraining representation learning?”
```

这个交叉点，就是你真正课题开始长肉的地方。

---

## 暂时不要做的三件事

**不要马上训练新网络。**

现在训练，你甚至还说不清 physics correction 是什么，训练出来的数据很难回答核心 research question。

**不要马上正式选择 simulator。**

先 characterize，再 Evidence，再决定是否 canonical。

**不要漫无目的地读几十篇论文。**

每篇论文必须回答至少一个明确问题：

> 它提供了什么 physical relationship？  
> 它用了什么 integration mechanism？  
> 它解决了什么 limitation？  
> 它和我的 Core assumption 是 support、conflict，还是 irrelevant？

否则论文越多，你的 Obsidian 会慢慢长成一座漂亮的论文墓园。📚

---

还有一点很重要：按照你之前的 `Next_Action.md`，当 governance review `NA-0005` 完成以后，原本被它阻塞的 **NA-0002 — Admit the first Background sources** 就应该成为自然的下一步。它要求你开始选择 project-relevant original sources，赋予 `SRC-ID` 并记录 provenance/status。Next_Action.mdMD

所以从**治理路线**和**科学路线**两个角度，它们现在恰好汇合了：

> **你的下一步就是 Literature / Source / Evidence discovery。**

而不是继续搭 framework。

如果再具体一点，我会把你接下来的第一个小目标定成：

> **不是“读 20 篇论文”，而是找出 3–5 个值得进一步验证的 output-level lithography Physics Constraint candidates。**

这才是你现在真正应该开始推进的科研任务。




























✅
你可以把“可使用”的标准压缩成一句：

> **规则有唯一 owner，任务能走通，AI 不能越权，小实验不会被行政流程卡死。**

满足这四点，就不需要追求“每一句都完美”。

我反而建议你现在不要继续逐字审全部 governance。再审下去很容易进入“治理治理本身”的循环。更适合的方法是做 **3 个模拟测试**：

- 模拟 1：加入一篇新论文
- 模拟 2：设计一个普通 ablation experiment
- 模拟 3：AI 建议更换长期 canonical simulator

如果这三种任务分别能正确走到：  
`Source/Evidence`、`EXP Plan`、`proposed ADR`  
而且没有多余文件被强制加载，那这个 governance 就已经达到“可以正式使用”的程度。

你甚至可以把治理验收理解成软件测试：**不是证明所有代码都完美，而是证明关键路径不会炸**






✅
### 你现在立刻应该做：NA-0005

也就是：

> **Review corrected governance and Wiki synchronization**

但这里不要再设计新的 Graph system。你需要做的只是检查目前剩下的 governance 文件到底有没有问题，例如：

- `AGENTS.md`
- `Core_Governance.md`
- 文件 status / lifecycle 规则
- source register / evidence register 的基本规则
- Markdown Wiki synchronization rules
- Agent 应该怎么修改 Obsidian Markdown
- 哪些文件可以自动修改，哪些必须经过你确认

然后做一个决定：

**“这套 governance 可以用了。”**

一旦你确认，NA-0005 就从：

`proposed → approved/completed`

这一步的意义不是科研创新，而是把“科研操作系统”冻结下来，避免以后 Agent 又偷偷长出第三套、第四套架构。文件本身也强调 NA-0005 只是 governance review，不应修改 Core scientific meaning。