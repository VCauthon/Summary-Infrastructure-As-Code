# Multiple environment stack

This section introduces an example of how infrastructure code can be organized using the **multiple environment stack** anti-pattern.

> A detailed explanation of this pattern can be found in this [section](../../../docs/2-infrastructure-stacks/chapters/2-building-environment-with-stacks.md#antipattern-mutliple-environment-stack).

This anti-pattern describes a stack in which multiple environments coexist. Using the defined base infrastructure as a foundation, we can create multiple Lambdas within the same stack, simulating different environments.
