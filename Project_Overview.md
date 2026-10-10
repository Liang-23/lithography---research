
# Project Overview


## 1. Project Title

Physics-aware High-dimensional AI Surrogate for Advanced Node Computational Lithography

中文：

面向先进节点计算光刻的物理感知高维 AI 代理模型


## 2. Research Domain

- Computational Lithography
- AI-based Lithography Simulation
- Physics-aware Machine Learning
- High-dimensional Surrogate Modeling


## 3. Fundamental Problem
> Current AI surrogate models for computational lithography face a challenge in effectively incorporating physical knowledge without sacrificing prediction performance.

> Pure data-driven surrogate models have strong representation capability and can learn complex high-dimensional lithography transformations, but their prediction reliability may degrade when data availability is limited or when encountering unseen physical conditions.

> Conventional physics-informed approaches attempt to improve surrogate performance by directly embedding physical constraints into the training process. However, continuously enforcing physical constraints during optimization may restrict neural representation learning and introduce conflicts between data-driven learning objectives and physics-based constraints.

> Recent studies suggest that applying physical correction after neural prediction through projection onto a physically valid solution space can be more effective than directly incorporating physical terms into the training loss.

> Therefore, the fundamental challenge is:

**How can physical knowledge be incorporated into AI surrogate models in a way that improves prediction performance while preserving the representation capability of high-dimensional neural networks?**


## 4. Research Motivation
Advanced semiconductor lithography requires accurate physical simulation of aerial images, resist behavior, and wafer patterns. However, high-fidelity physics simulators are computationally expensive, limiting large-scale simulation and practical deployment.

AI surrogate models provide an opportunity to significantly accelerate lithography simulation by approximating expensive physics-based computations.

However, achieving accurate and efficient surrogate modeling remains challenging, especially under limited high-fidelity data conditions in advanced-node lithography.

Existing approaches mainly focus on either increasing neural representation capability through data-driven learning or incorporating physical knowledge through physics-informed constraints. These strategies may involve a trade-off between model flexibility, training effectiveness, and final prediction performance.

Therefore, the key research challenge is how to effectively integrate physical knowledge into AI surrogate models to improve prediction performance while maintaining the ability of neural networks to learn complex high-dimensional lithography transformations.


## 5. Core Research Question
How can physical knowledge be effectively integrated into an end-to-end high-dimensional AI surrogate to improve lithography prediction performance without limiting the representation capability of neural networks?


## 6. Research Hypothesis
This project hypothesizes that the effectiveness of physics integration depends on where and how physical knowledge is introduced into the surrogate learning process.

Instead of continuously enforcing physical constraints during neural network optimization, physical knowledge may be introduced after neural prediction through a physically meaningful correction mechanism.

The corrected solutions can then be transferred back into the surrogate model through knowledge distillation or other learning strategies, enabling the model to gradually acquire physics-guided prediction capability while preserving its representation flexibility.


## 7. Proposed Research Direction
This project explores a new physics-guided surrogate learning paradigm:

High-dimensional neural representation learning

↓

Physical knowledge-based correction of surrogate outputs

↓

Knowledge transfer back into the surrogate model


The physical correction mechanism may involve:

- Physics-defined solution space projection
- Projection-based knowledge distillation
- Event-triggered discrete correction for non-differentiable or discontinuous physical relationships


The final objective is to develop an end-to-end AI surrogate capable of directly predicting high-dimensional lithography outputs with improved prediction performance and significantly reduced computational cost.


## 8. Key Idea

Learn complex representations freely, integrate physical knowledge effectively, and improve surrogate performance..


## 9. Scope Boundary

This project focuses on:

- Forward computational lithography simulation
- Physics-guided AI surrogate modeling


Input:

- Mask layout
- Optical conditions
- Process parameters (if available)


Output:

- Aerial image
- Resist image
- Wafer image


This project does NOT include:

- Inverse Lithography Technology (ILT)
- Mask optimization
- Mask generation
- Gradient trust certification

