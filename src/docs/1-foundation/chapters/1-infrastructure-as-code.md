# What is Infrastructure as code

This chapter explains the key characteristics of modern infrastructures, contrasting the Cloud Age with the Iron Age, and introduces the three core practices of Infrastructure as Code:

- Define everything as code
- Continuously test
- Deliver continuously through small, loosely coupled components

---

## Infrastructure as code (IaC)

Infrastructure as Code is an approach to infrastructure automation based on practices from software development. It emphasizes consistent, repeatable routines for provisioning and changing system and their configuration. __You make changes to code, then use automaton to test and apply those changes to your systems__.

Given that changes are the biggest risk to a production system, continuous change is inevitable, and making changes is the only way to improve a system, it makes sense to optimize your capability to make changes both rapidly and reliably. Research from the _Accelerate State of DevOps Report_ backs this up. Making changes frequently and reliably is correlated to organization success.

> The Accelerate State of DevOps report can been seen [here](https://dora.dev/research/2024/dora-report/2024-dora-accelerate-state-of-devops-report.pdf) and the metric specified before in the chapter _Performance levels_.

### Benefits of IaC

- Using IT infrastructure as an enabler for rapid delivery of value
- Reducing the effort and risk of making changes to infrastructure
- Enabling users of infrastructure to get the resources they need, when they need it
- Providing common tooling across development, operations, and other stakeholders
- Creating systems that are reliable, secure, and cost affective
- Make governance, security, and compliance controls visible
- Improving the speed to troubleshoot and resolve failures

### Objections to the use of IaC

| Objection | Counterargument |
|---|---|
| __We don't make changes often enough to justify all the automation__ | We want to think that we build a system, adn then its "done". In this view, we don't make many changes, so automating changes is a waste of time. In reality, very few systems stop changing, at least not before they are retired. <br><br>A fundamental truth of the Cloud Age is: Stability comes from making changes.|
| __We should build first and automate later__ | The cost of manually maintaining and fixing the system can escalate quickly. Also if the service it runs is successful, stakeholders will pressure you to expand and add features rather than stopping to rebuild. |
| __We must choose between speed and stability__ | DORA’s research has repeatedly demonstrated that speed and stability are not tradeoffs. In fact, we see that the metrics that the four keys focus on are correlated for most teams. Top performers do well across all four metrics, and low performers do poorly. |

## DORA's software delivery metrics

DORA's Accelerate research team identifies four key metrics for software delivery and operational performance. Its research surveys various measures, and has found that these four have the strongest correlation to how well an organization meets its goals.

These metrics are grouped as follows:
- __Throughput__:
    1. Change lead time: This metric measures the time it takes for a code commit or change to be successfully deployed to production.
    2. Deployment frequency: This metric measures how often application changes are deployed to production.
- __Stability__:
    3. Change fail percentage: This metric measures the percentage of deployments that cause failures in production, requiring hotfixes or rollbacks.
    4. Failed deployment recovery time: This metric measures the time it takes to recover from failed deployment.

> This research can be seen [here](https://dora.dev/guides/dora-metrics-four-keys/)
There are some objections  heard when teams don't

# TODO: Shown an example on which this metrics are measured into a project

## The core practices

There are three core practices for implementing IaC.

### Define everything as code

Defining all your stuff "as code" is a core practice for making changes rapidly and reliably. There are a few reasons why this helps:
- _Reusability_: If you define a thing as code, you can create many instances of it, version it, rebuild it quickly
- _Consistency_: Things built from code are built the same way every time. This makes system behavior predictable
- _Transparency_: Everyone can see how the thing is built by looking at the code. Allowing them to understand it and to suggest improvements

### Continuously test and deliver all work in progress

Effective infrastructure teams are rigorous about testing. They use automation to deploy and test each component of their system, and integrate all the work everyone has in progress.

The idea is to build quality in rather than trying to test quality in.

### Build small, simple pieces that you can change independently 

Teams struggle when their systems are large and tightly coupled. The larger a system is, the harder it is to change, and the easier it is to break.

When you look at the codebase of a high-performing team, you see the difference. The system is composed of small, simple pieces. Each piece is easy to understand and has clearly defined interfaces. The team can easily change each component on its own, and can deploy and test each component in isolation.

