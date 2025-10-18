# Anti-pattern: Monolithic Stack

This section shows an example of how infrastructure code should be organized to create the Monolithic Stack anti-pattern.

> This [section](../../docs/2-infrastructure-stacks/chapters/1-building-infrastructure-stacks-as-code.md#anti-patterns-monolithic-stack) describes this pattern.

The goal here is to create a stack that contains three different services, which are grouped together in the same stack and have dependencies among them.

The services included are as follows:
- __Service 1__:
    - A web page that lists links parameterized in a database.
    - When the user selects one of the links, the clicks are recorded in the same database.
- __Service 2__:
    - A database where the links displayed on the web page are stored.
    - Additionally, this database keeps count of how many times each link has been selected.
- __Service 3__:
    - A monitoring web page where you can see how many times each link has been selected.

Relations between services:
- Each service will work with the same database
- All the computer resources will be in the same network
- All the webpages will be made in the same environment
