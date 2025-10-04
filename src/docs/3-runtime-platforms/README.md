[__🧭 HOME__](../../../README.md)

> [⬅️ PREVIOUS MODULE](../2-infrastructure-stacks/README.md) __|__ [NEXT MODULE ➡️](../4-designing-infrastructure/README.md)

---

# Working with servers and Other Application Runtime Platforms

Define how software that escapes configurations enters IaC, i.e., the code itself that the infrastructure must execute to provide a final service.

## Application Runtimes

This chapter summarizes each of the relationships, focusing on ways to organize infrastructure resources into runtime platforms for applications. It sets the stage for later chapters, which go into more detail on how to define and manage those resources as code.

## Building Servers as Code

This chapter explains approaches to building and managing server configuration as code. It starts with the content of servers (what needs to be configured) and the server life cycle (when configuration activities happen). It then moves on to a view of server configuration code and tools. The central content of this chapter looks at different ways to create server instances, how to pre-build servers so you can create multiple consistent instances, and approaches to applying server configuration across the server life cycle.

## Managing Changes to Servers

This chapter is about how to change things on servers by changing the code that defines where the things comes from adn applying it one way or another. By implementing a reliable, automated change process for your servers, you ensure that you can roll changes out across your state rapidly and reliably. You can keep all of your servers up-to-date with the latest approved pakcage and configuration with minimal effort.

## Server Images as Code

This chapter delves into the best way to create multiple server instances from a single source.

## Building Clusters as Code

You should use code to define and manage your application cluster. You can build an application cluster as one or more application stack as code. In this chapter, its given some examples of what this can look like. Its also shown some different stack topoligies, including a single stack for a whole cluster, and breaking clusters across multiple stacks.

---
