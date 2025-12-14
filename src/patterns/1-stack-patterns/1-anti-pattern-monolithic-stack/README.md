# Monolithic stack

This section introduces an example of how infrastructure code can be organized using the **Monolithic Stack** anti-pattern.

> A detailed explanation of this anti-pattern can be found in this [section](../../../docs/2-infrastructure-stacks/chapters/1-building-infrastructure-stacks-as-code.md#anti-patterns-monolithic-stack).

With the Monolithic Stack approach, **all infrastructure resources are defined within a single stack**.

In this exercise, this means that every resource is deployed together, exactly as defined in the base infrastructure, without any logical separation by service or application.
