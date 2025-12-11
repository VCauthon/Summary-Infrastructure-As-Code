# Service stack

This section shows an example of how infrastructure code should be organized to create the Application group stack.

> This [section](../../../docs/2-infrastructure-stacks/chapters/1-building-infrastructure-stacks-as-code.md#pattern-service-stack) describes this pattern.

In the service stack, all services are grouped in stacks by applications. In our case, we are going to create 3 stacks because we have 2 where we detect the following services:
- The registry webpage
    - Front-end
    - BackOffice
- ETL workflow