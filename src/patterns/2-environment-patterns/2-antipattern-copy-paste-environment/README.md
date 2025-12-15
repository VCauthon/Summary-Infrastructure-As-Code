# Copy-paste environment stack

This section introduces an example of how infrastructure code can be organized using the **copy-and-paste environment** anti-pattern.

> A detailed explanation of this pattern can be found in this [section](../../../docs/2-infrastructure-stacks/chapters/2-building-environment-with-stacks.md#antipattern-copy-paste-environments).

This anti-pattern describes a stack where each environment is defined using a file that has been copied for each environment, with some values modified to match the expected configuration for that specific environment.

In our case, we are going to create two stacks, each defining a concrete environment. Each stack uses the same base files, with a variation in the `local.tf` file. The only variation is that the locals define the environment in which the code is running.
