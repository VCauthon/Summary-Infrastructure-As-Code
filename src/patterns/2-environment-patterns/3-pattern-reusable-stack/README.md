# Reusable stack

This section introduces an example of how infrastructure code can be organized using the **reusable environment** pattern.

> A detailed explanation of this pattern can be found in this [section](../../../docs/2-infrastructure-stacks/chapters/2-building-environment-with-stacks.md#pattern-reusable-stack).

This pattern describes a stack where a single, reusable definition is shared across multiple environments, and environment-specific behavior is controlled through inputs such as variables, locals, or configuration files rather than duplicated code.

In our case, we define one reusable stack that can be instantiated for multiple environments. Each environment provides its own configuration via `terraform.tfvars` file to specify context such as the environment name, while the core infrastructure code remains identical and centrally maintained.
