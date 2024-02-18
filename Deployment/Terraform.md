# Terraform

[https://github.com/hashicorp/terraform](https://github.com/hashicorp/terraform)

Terraform 是一种开源工具，用于编写“基础设施即代码”。
也就是说，我们可以使用 Terraform 来编写管理基础设施的代码。

## Terraform 使用哪种语言？

有两种语言

- HCL（HashiCorp 配置语言）- 用于编写 terraform 文件 (.tf) 的语言。我们需要学习这个才能使用 terraform。
- GO 语言 - Terraform 的核心部分是用 GO 语言编写的。

## Terraform 在哪里使用？

Terraform 用于管理云平台（主要）上的基础设施以及本地基础设施。

Terraform 支持几乎所有主要的云提供商（例如，Microsoft Azure、AWS、GCP 等），
我们可以在其中使用 Terraform 来管理（提供、删除、修改）基础设施。

## 如何使用 Terraform？

要使用 Terraform，我们需要按照以下步骤操作。

### 第 1 步 – 安装 terraform
我们需要在我们的机器上安装它。根据我们的操作系统，我们可以通过不同的步骤来安装它。以下是安装 terraform 的文档链接：

[https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform)

安装后，我们可以通过运行以下命令检查其版本来验证它。

```
terraform -v
```

### 第 2 步 – 授予对 Terraform 的访问权限
Terraform 应该可以访问云平台，以便它可以管理基础设施。所以我们应该允许访问 terraform

### 第 3 步 – 创建 Terraform 文件
如果您是 terraform 的新手，那么您可以从创建一个“main.tf”文件开始，您可以在其中声明云提供商详细信息（否则您也可以为提供商创建单独的 .tf 文件）和您要创建的资源详细信息。

编写 terraform 文件时需要记住的几个基本要点

- Terraform 将一切都视为“资源”，即基础设施的每个组件都被假定为资源。
- 当我们为任何资源编写代码时，它有两个名称
  - 一个是它的实际名称，我们将在配置后在云门户上看到它。
  - terraform 使用另一个名称。当我们调用 .tf 文件中的任何资源时，将使用此名称。

### 第 4 步 – 运行 terraform 命令
获得所需的 .tf 文件后，我们需要运行 terraform 命令。以下是命令的基本流程

1. 首先，我们需要通过运行“terraform init”来初始化后端
2. 接下来，我们可以运行“terraform plan”来查看计划，它会显示将要进行哪些更改。
3. 接下来，我们需要运行“terraform apply”来配置资源。

这些是我们配置任何资源时的主要命令。还有其他用于销毁和修改资源的命令。

## Terraform和Ansible的对比

Terraform目前更合适你的基础设施创建和管理，如创建你的云主机、负载均衡器等等；

Ansible而是更适合你的云主机创建后，自动化地去初始化你的机器配置、安装组件、部署服务等。

核心 Terraform 工作流程包含三个阶段：
- Write-编写：定义资源，编写声明式配置文件定义资源。这些资源可能跨越多个云提供商和服务。
- Plan-计划： Terraform 创建一个执行计划，描述它将根据现有基础架构和您的配置创建、更新或销毁的基础架构。
- Apply-应用：在批准后，Terraform 会按照正确的顺序执行建议的操作，并尊重任何资源依赖关系。例如，如果您更新 VPC 的属性并更改该 VPC 中的虚拟机数量，Terraform 将在扩展虚拟机之前重新创建 VPC。

## 参考

[Terraform基础(一)-什么是Terraform？](https://blog.csdn.net/qq522044637/article/details/124338418)

[https://cscontents.com/introduction-to-terraform-high-level-information/](https://cscontents.com/introduction-to-terraform-high-level-information/)
