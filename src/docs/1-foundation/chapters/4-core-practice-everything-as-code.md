[__🧭 BACK TO MODULE__](../README.md)

> [⬅️ PREVIOUS CHAPTER](./3-infrastructure-as-platform.md)

---

# Core Practice: Define everything as code

This chapter delves into the first of [these core practices](./1-infrastructure-as-code.md#the-core-practices). 

## Understanding why

To better understand the purpose of this practice lets ask ourselves the following questions.

### Why You Should Define Your Infrastructure as Code?

Why do you need to take all this troublesome? I mean, you can actually deploy the entire infrastructure in four clicks through the cloud's provider website, or if you can use its own CLI.

Responding to myself:

Implementing and managing your system as a code enables you to leverage speed to improve quality. This its done because throw code you can automate anything you want to.

Things like:
- Testing that your application works
- Deploy new features of your infrastructure
- Replicate your current environment

### What You Can Define as Code?

Infrastructure code specifies oth the infrastructure elements you want and how you want them configured. YOu run an infrastructure tool to apply your code to an instance of your infrastructure. __The tool either creates new infrastructure, or it modifies existing infrastructure to match what you've defined in your code__.

Some of the things you should define as code include:
- _Infrastructure stack_: A collection of elements provisioned to serve a concrete purpose from your application
- _Server configuration_: Packages, files, user accounts and services
- _Server role_: A group of server configuration modules to apply to a server
- _Server image_: Define server images that will be used for building multiple server instances
- _Application package_: Define how to build a deployable application artifact using containers
- _Deployment pipelines_: Pipelines to deploy new changes into your current infrastructure
- _Monitoring checks_: Checks to know that your environment its working as expected
- _Testing_: Checks you want to follow to validate that your infrastructure its working

## Version control

If you're defining your stuff as code, then putting that code into a version control system (VCS) is simple and powerful.

By doing this, you will get:
- _Traceability_: With VCS you will have a history of changes of your infrastructure.
- _Rollback_: Because you can trace your history of changes you can rollback to an stable version
- _Correlation_: Keeping scripts, specifications, and configuration in VCS helps when tracking and fixing gnarly problems
- _Visibility_: Everyone can see each change committed to the version control system, giving the team situational awareness.
- _Actionability_: The VCS can trigger an action automatically for each change committed (enabling CI/CD).

> Take into account that there are some IaC tools that are Non code. All the definitions of your infrastructure will be saved as data and will be seen throw GUI, API or/and CLI. These are closed-box tools that limit the practices and workflows you can use.

## Coding languages

There are different types of coding languages that allows you to define IaC. Here comes some of it:

### The older ways

Before standard tools appeared for provisioning cloud infrastructure declaratively, __we wrote scripts in general-purpose, procedural languages__ (using Bash, Perl, PowerShell, Ruby and/or Python). Our scripts typically used and SDK to interact with the cloud provider's API.

Here is an example of script that defines a server (it doesn't really work):
```py
import dummy_provider as dp
from time import sleep

# Retrieving the state of the server
network_segment = dp.find_network_segment("private")
app_server = dp.find_server("my_application_server")

# Creating the server if it doesn't exist
if not app_server:
    app_server = dp.create_server(
        name="my_application_server",
        image="dummy-image",
        cpu=2,
        ram="2GB",
        network=network_segment
    )

while app_server.ready is False:
    if not app_server.ok:
        raise Exception("The server isn't working")
    sleep(5)
    app_server.get_state()

app_server.provision(
    provisioner="servermaker",
    role="tomcat_server"
)
```

This scripts mixes what to create and how to create it. This is done because the script will try to check the current state of the infrastructure (using some if statements) and then apply some logic.

Taking into account that these scripts will have to make, over time, more and more validations, makes that some teams turn simplistic script into multipurpose scripts.

### The current way

#### Declarative Infrastructure Languages

Many infrastructure code tools, including Ansible, Chef, CLoudFormation, Puppet and Terraform, uses declarative languages. __Your code defines your desired state for your infrastructure__, such as which packages and users accounts should be on a server or how much RAM and CPU resources it should have.

Declarative infrastructure separate what you want from how yo create it.

This would be a translation of the last code shown in Terraform:
```hcl
resource "DummyProvider" "my_application_server" {
    name="my_application_server"
    source_image="dummy-image"
    cpu=2
    ram="2GB"
    network="private_network_segment"

    provision {
        provisioner="servermaker"
        role="tomcat_server"
    }
}
```

If you compare this code with the one shown [here](#infrastructure-scripting) you can see that this code doesn't check the state of the infrastructure. It just define the desired state of the infrastructure (2CPU, 2GB of ram, the dummy-image, etc...).

Tools that uses declarative languages checks the current attributes of the infrastructure against what is declared, and works out what changes to make to bring the infrastructure in line. For example, if someone changes in the infrastructure the RAM of your server, like going from 2GB to 3GB, the tool will detect that difference and will change again the RAM to 2GB.

> Define the infrastructure declaratively when you want to ensure that the infrastructure ALWAYS has a specific status. For example, and in the previous case, let's say we want there to always be a server with the same characteristics. In this case, greatly simplified, we should opt for the declarative approach.

````markdown
##### Idempotency

Idempotency means that when you apply a given piece of code, it always produces the same result — no matter how many times you run it.  

For example, in the [previous section](#declarative-infrastructure-languages), we saw code that describes a desired state. If the tool implementing that code is designed correctly, it will __always__ produce the same output. This ensures the server remains in the desired state. If someone makes manual changes that are not defined in the code, the tool will detect the configuration drift and automatically correct it by reapplying the desired configuration.

Here’s an example of a shell script that __is not idempotent__:

```sh
echo "spock:*:1010:1010:Spock:/home/spock:/bin/bash" \
    >> /etc/passwd
````

Running this script once will add the user `spock` to the `/etc/passwd` file. However, running it ten times will add ten identical entries for the same user.

An __idempotent__ version of this process would ensure that, no matter how many times the script or tool runs, only a single entry for the user `spock` exists in the `/etc/passwd` file.

#### Imperative Infrastructure Languages

Declarative code is fine when you always want the same outcome. But there are situations where you want different results depending on the circumstances. This type of code is similar to scripting, but not entirely, as it works within a framework that offers features that make it more maintainable.

Newer tools, such as [Pulumi](https://www.pulumi.com/) and the [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html), return to using programmatic languages for infrastructure. Much of their appeal is their support for general-purpose programming languages (it allows you to use TypeScript, JavaScript, Python, Java, C#/.Net, and maybe more).

Rather seeing either declarative or imperative infrastructure languages as the correct paradigm, we should look at which types of concerns each one is mos suited for.

> Define the infrastructure imperatively when you want to control the state of your infrastructure and, based on conditions in the logic itself, define resources in one way or another. For example, returning to the previous case, let's say we want the server to use one configuration or another based on the region. In this case, it would make more sense to use the imperative approach.

### Domain-specific Infrastructure Languages

In addition to being declarative, many infrastructure tools use their own DSL, or [domain-specific-language](https://martinfowler.com/books/dsl.html).

A DSL is a language designed to model a specific domain, in our case infrastructure. This makes it easier to write code, and makes the code easier to understand, because it closely maps the thing you're defining.

MAny stack management tools also use DSLs, including Terraform and CloudFormation. They expose concepts from their own domain, infrastructure platforms, so that you can directly write code that refers to virtual machines, disk volumes, and network routes.

Many infrastructure DSLs are built as extensions of existing markup languages such as YAML (Ansible, CLoudFormation, anything related to K8) and JSON (Packer, and again CloudFormation). Some are internals DSLs, written as a subset (or superset) of a general-purpose programming languages.

> Subset means that that DLS its using some features of a language to implement its logic. And a superset its an extension of an existing language (Typescript its a superset of JavaScript)

Others are external DSLs, which are interpreted by code written in a different language. For example, Terraform HCL is an external DS; the code is not related to the GO language it's interpreter is written in.
