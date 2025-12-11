# Application group stack

This section shows an example of how infrastructure code should be organized to create the Application group stack.

> This [section](../../../docs/2-infrastructure-stacks/chapters/1-building-infrastructure-stacks-as-code.md#pattern-application-group-stack) describes this pattern.

In the application group, all resources are grouped in stacks by applications. In our case, we are going to create 2 stacks because we have 2 applications which are:
- The registry webpage
- ETL workflow