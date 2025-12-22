# Stack environment variable pattern

This section introduces an example of how infrastructure code can be organized using the **stack environment variable** pattern.

> A detailed explanation of this pattern can be found in this [section](../../../docs/2-infrastructure-stacks/chapters/3-configuring-stack-instances.md#pattern-stack-environment-parameters).

This pattern describes a stack where a single, reusable definition is instantiated multiple times, and environment-specific behavior is controlled through **environment variables provided by the execution context**, rather than through duplicated files or environment-specific configuration inside the repository.

In this approach, each environment defines its own configuration using environment variables available on the machine running Terraform (for example, exported shell variables or CI/CD environment variables). The stack reads these values at runtime to determine context such as the environment name, region, or account, while the core infrastructure code remains identical and centrally maintained.

To run this example its needed to run the following command to create the expected environment variables by the exercise.

```bash
export TF_VAR_environment="pro"
```
