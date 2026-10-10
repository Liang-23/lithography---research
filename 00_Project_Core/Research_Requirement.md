
# Research Requirements


## 1. Functional Requirement

The proposed method must construct an end-to-end high-dimensional AI surrogate.

The model should directly map lithography inputs to physical outputs without requiring external filtering or post-processing modules during inference.


### Input

The model should support:

- Mask layout
- Optical conditions
- Process parameters (if available)


### Output

The model should predict:

- Aerial image
- Resist image
- Wafer image


## 2. Representation Learning Requirement

The proposed method should preserve the capability of neural networks to learn complex high-dimensional lithography transformations.

The integration of physical knowledge should improve surrogate performance without unnecessarily reducing the flexibility of neural representation learning.


## 3. Lithography Prediction Requirement

The surrogate should accurately predict lithography outputs while maintaining consistency with expected lithographic behavior.

Evaluation should go beyond pixel-level similarity and consider whether the predicted results capture important lithography characteristics, including:

- Spatial frequency behavior
- Edge response behavior
- Process variation response
- Relationship between input geometry and output behavior

## 4. Physics Knowledge Integration Requirement

The research should investigate effective strategies for incorporating physical knowledge into AI surrogate models.

Possible approaches include:

- Output-level physical correction
- Physics-defined solution space projection
- Projection-based knowledge distillation
- Event-triggered correction mechanisms for non-differentiable physical relationships


## 5. Efficiency Requirement

Compared with high-fidelity physics simulators, the surrogate should significantly reduce:

- Inference time
- Computational cost


The final goal is accelerated lithography simulation with improved prediction performance and reduced computational cost.


## 6. Data Constraint Requirement

The proposed method should remain feasible under limited high-fidelity advanced-node lithography data.

The framework should consider:

- Limited high-fidelity simulation samples
- Expensive data generation process
- Effective utilization of available physics knowledge
- Data-efficient learning strategies

## 7. Scientific Contribution Requirement

The contribution should not only be:

- A larger neural network
- A more complex architecture
- Improved prediction accuracy

The research must answer:

How can physical knowledge be integrated into AI surrogate learning to improve prediction performance while preserving the representation capability of high-dimensional neural networks?


## 8. Evaluation Requirement

The evaluation framework should include:


### Prediction Performance

Metrics:

- MSE
- SSIM
- Contour error


### Data Efficiency

Evaluation:

- Performance under limited high-fidelity data
- Sample efficiency


### Lithography Behavior Validation

Metrics:

- Frequency response consistency
- Edge behavior consistency
- Process variation response


### Computational Efficiency

Metrics:

- Simulation speedup
- Memory usage
- Computational cost