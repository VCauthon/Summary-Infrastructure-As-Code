# Application group stack

This section introduces an example of how infrastructure code can be organized using the **Application Group Stack** pattern.

> A detailed explanation of this pattern can be found in this [section](../../../docs/2-infrastructure-stacks/chapters/1-building-infrastructure-stacks-as-code.md#pattern-application-group-stack).

With the Application Group Stack approach, infrastructure resources are grouped by **application**, with each application defined in its own stack.

In this exercise, we define **two stacks**, corresponding to the applications identified in the system:
- **Registry webpage**
- **ETL workflow**
