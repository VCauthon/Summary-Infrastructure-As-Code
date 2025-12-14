# Micro stack

This section introduces an example of how infrastructure code can be organized using the **Micro Stack** pattern.

> A detailed explanation of this pattern can be found in this [section](../../../docs/2-infrastructure-stacks/chapters/1-building-infrastructure-stacks-as-code.md#pattern-micro-stack).

With the Micro Stack approach, infrastructure resources are split into **small, highly focused stacks**, where each stack represents a single infrastructure responsibility.

In this exercise, we define separate stacks for the following infrastructure components:
- **Networking**
- **ECS Cluster**
- **Databases**
- **ECS Services**
- **Lambdas**

This structure maximizes isolation and reusability, but also increases the number of stacks that need to be managed and coordinated.