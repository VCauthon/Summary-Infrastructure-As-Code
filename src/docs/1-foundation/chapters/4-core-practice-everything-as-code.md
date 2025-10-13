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

### Infrastructure scripting

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

### Declarative Infrastructure Languages


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
