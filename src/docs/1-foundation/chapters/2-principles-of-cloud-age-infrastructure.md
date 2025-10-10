[__🧭 BACK TO MODULE__](../README.md)

> [⬅️ PREVIOUS CHAPTER](./1-infrastructure-as-code.md) __|__ [NEXT CHAPTER ➡️](./3-infrastructure-as-platform.md)

---

# Principles of Cloud Age Infrastructure 

There are several principles for designing and implementing infrastructure on cloud platforms. THese principles articulate the reasoning for using the three core practices. 

There are also several common pitfalls that teams make with dynamic infrastructure.

Below is a list of principles and pitfalls identified within the IaC framework.

## Principles

### Assume Systems Are Unreliable

In the Iron Age, we assumed our systems were running on reliable hardware. In the Cloud Age, you need to assume your system runs on unreliable hardware.

This gives you many advantages, because once you’ve written reliability into your software you can scale out with cheap hardware without spending more on reliability per unit, while if you’re using reliable hardware then each unit needs to include reliability (typically in the form of redundant components), which quickly gets very expensive.

> The last quote its from Sam Johnston article Simplifying Cloud: Reliability ([link](https://samjohnston.org/2012/03/08/simplifying-cloud-reliability/))

Cloud scale infrastructure involves hundreds of thousands of devices, if not more. At this scale, failures happen even when using reliable hardware. ANd most cloud vendors use cheap, less reliable hardware, detecting and replacing it when it breaks.

You must design for uninterrupted service when underlying resources change.

### Make Everything Reproducible

One way to make a system recoverable is to make sure you can rebuild its parts effortlessly and reliably.

Effortlessly means that there is no need to make any decisions about how to build things. You should define things such as:

- Configuration settings
- Software versions
- Dependencies as code

Rebuilding is then a simple "yes/no" decision.

Not only does reproducibility make it easy to recover a failed system, but it also helps you to:

- Make testing environments consistent with production
- Replicate systems across regions for availability
- Add instances on demand to cope with high load
- Replicate systems to give each customer a dedicated instance

### Create Disposable Things

Building a system that can cope with dynamic infrastructure is one level. The next level is building a system that is itself dynamic. You should be able to gracefully add, remove, start, stop, change, and move the parts of your system.

Doing this creates operational flexibility, availability, and scalability.

### Minimize Variation

As systems grow, they become harder to understand, change, and fix. Complexity increases not only with the number of components but also with their variety.

To keep systems manageable, reduce variation. It’s easier to manage 100 identical servers than 5 completely different ones.

Defining simple components and replicating them makes systems easier to maintain. But any change must be applied to all instances—otherwise, configuration drift occurs.

Common sources of variation include:
- Different software for the same purpose (OS, runtime, database)
- Multiple software versions
- Different package versions

Organizations must balance giving teams freedom to choose tools with keeping system variation under control.

### Ensure That You Can Repeat Any Process

Building on the reproducibility principle, you should be able to repeat anything you do to your infrastructure. **It's easier to repeat actions using scripts and configuration management tools than to do it by hand**. But automation can be a lot of work, specially if you're not used to it.

For example, let's say I have to partition a hard drive as a one-off task. Writing and testing a script is much more work than just logging in and running the `fdisk` command. So i do it by hand.

## Pitfalls

### Snowflake Systems

A snowflake system is one that’s hard to rebuild or differs unexpectedly from similar environments, like staging.

These systems aren’t created on purpose—they emerge naturally when:

You build with a new tool, learn through mistakes, and can’t rebuild once others depend on it.

Changes are made inconsistently across environments.

Knowledge gaps cause people to modify systems independently.

You know a system is a snowflake when it’s risky to change or upgrade, and hard to fix when broken. Over time, people stop touching it, leaving it outdated and fragile.

It’s usually worth replacing snowflakes with reproducible systems. If it’s not worth improving, it may not be worth keeping.

The best approach is to write code that can recreate the system, run it in parallel, and use automated tests and pipelines to ensure it’s correct, reproducible, and easy to change.
