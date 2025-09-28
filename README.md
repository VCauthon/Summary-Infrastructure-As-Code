# Summary-Infrastructure-As-Code
Summary of everything learned about infrastructure as code


# Foundations

How current infrastructures are managed

## What is Infrastructure as code

Which are the characteristics of the current infrastructures and what are the Cloud Age and the Iron Age.

Define the three core practices for implementing Infrastructure as Code:
- Define everything as code
- Continuously test
- Deliver everything as you work, and build your system from small, loosely coupled pieces

## Principles of Cloud Age Infrastructure 

Designing principles and implementing infrastructure on cloud platforms. These principles articulate the reasoning for using the three core practices.

It also defines several common pitfalls that teams make with dynamic infrastructure

## Infrastructure as platform

There is a vast landscape of tools relating in some way to modern cloud infrastructure. The question of which technologies to select and how to fit them together can be overwhelming. This chapter presents a model for thinking about the higher-level concerns of your platform the capabilities it provides, and the infrastructure resources you my assemble to provide those capabilities.

## Core practice: Define everything as code

This chapter delves into the first of these core practices, starting with the banal question. Why would you want to define your Infrastructure as Code? What type of things can and should you define as code?

---

# Working with Infrastructure Stacks

Defines the terminology used in IaC and patterns used to deploy and test the builded infrastructure

## Building Infrastructure Stacks as Code

This chapter describes patterns for grouping infrastructure resources in stacks

## Building Environment with Stacks

The last chapter described an infrastructure stack as a collection of infrastructure resources that you manage as a single unit. An environment is also a collection of infrastructure resources. So is a stack the same thing as an environment? This chapter explains that maybe it is, but maybe it isn't.

## Configuring Stack Instances

In this chapter it describes ways on which you can send configuration to a concrete stack. This configuration helps you to instance the infrastructure with a sets of settings that let you handle different use cases (for example, a production and a development environment). 

## Core practice: Continuously and Deliver

This chapter focuses on fundamental challenges and approaches for testing infrastructure

## Testing Infrastructure Stacks

This chapter builds on the latter one with specific guidances on testing infrastructure stack code.

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

# Designing Infrastructure

Define practices that enable the generation of scalable and maintainable code over time.

## Core practice: Small, Simple pieces

This chapter draws on design principles for modularity learned from decades of software design considering them from the point of viw of code-driven infrastructure. It then looks at different types of components in an infrastructure system, with an eye to how we can leverage them for better modularity.

## Building Stacks from Components

This chapter focuses on modularizing infrastructure stacks; that is, breaking stacks into smaller pieces of code.

## Using Stacks as Components

This chapter explores different approaches from a viewpoint of how the infrastructure its been defined affects on coupling.

---

# Delivering Infrastructure


## Organizing Infrastructure Code

Defines which are the best patterns when organizing the project across repositories. Do infrastructure and applications code belong together, or should they by separated? How should you organize code for an estate with multiple parts?

## Delivering Infrastructure Code

This chapters enters more in details on how all the releases are been deployed using IaC.

## Team Workflows

This chapter focuses on what people do in their workflows, while the following one looks at ways of organizing and managing infrastructure codebases.

## Safely Changing Infrastructure

Making frequent changes to infrastructure imposes challenges for delivering uninterrupted services. This chapter explores these challenges and techniques for addressing them.

---

## Sources
- [Infrastructure as Code](https://www.oreilly.com/library/view/infrastructure-as-code/9781491924334/) - By Kief Morris
