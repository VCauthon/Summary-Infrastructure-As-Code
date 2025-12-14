# Service stack

This section introduces an example of how infrastructure code can be organized using the **Service Stack** pattern.

> A detailed explanation of this pattern can be found in this [section](../../../docs/2-infrastructure-stacks/chapters/1-building-infrastructure-stacks-as-code.md#pattern-service-stack).

With the Service Stack approach, infrastructure resources are grouped by **service**, with each service defined in its own stack.

In this exercise, we define **three stacks**, based on the services identified in the system:
- **Registry webpage**
  - Front-end
  - Back office
- **ETL workflow**
