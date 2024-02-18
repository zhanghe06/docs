# Ansible

[https://docs.ansible.com/](https://docs.ansible.com/)

## Ansible AWX

[https://github.com/ansible/awx](https://github.com/ansible/awx)

参考：[https://cscontents.com/introduction-to-ansible/](https://cscontents.com/introduction-to-ansible/)


## 如何使用 Ansible？
Ansible 是一种无代理自动化工具，我们可以使用它来自动化各种手动任务。为此，我们需要在一台称为控制器机器的机器上安装 Ansible，从这台控制器机器上，我们可以在远程机器上执行各种任务。在这里，我们不需要在远程主机上安装任何类型的代理来让 Ansible 工作。一些任务示例包括部署应用程序、配置 Web 服务器等。

## Ansible 是如何工作的？
要了解 Ansible 的工作原理，您需要查看 Ansible 工作模型的架构。

控制器机器中的各种组件。

- 引擎
- 模块
  - 核心模块——这些是 Ansible 默认附带的模块
  - 自定义模块——这些是我们在所需模块不存在时创建的模块
- 插件
  - 连接插件——此插件用于与远程主机建立通信。
  - 回调插件——此插件用于处理所有输出。
- 清单文件——这是一个普通的文本文件，我们在其中存储远程主机的详细信息。
- Playbook——这是一个YAML文件，我们在其中提到了需要在远程主机上执行的各种任务。

在受控或托管或目标主机中，不需要安装任何类型的代理。

## Ansible 如何与远程主机连接？
**与 Linux 机器的连接**  
为了连接 Linux 机器，Ansible 使用 SSH 协议。

**端口要求**  
SSH 协议使用端口 22。

**与 Windows 机器的连接**  
为了连接 Windows 机器，Ansible 使用WinRM。WinRM是一个用 python 语言编写的软件/客户端，需要安装在 Ansible 控制器机器/节点上。而WinRM使用 WS-Management 协议。

**端口要求**  
默认情况下，Ansible 在使用 WinRM 进行通信时使用端口 5986 (HTTPS)。如果我们想使用 HTTP，那么我们需要特别提到 ansible_port: 5985

## Ansible 如何在多个远程主机上执行各种任务——顺序的还是并行的？
默认情况下，Ansible 在服务器中并行运行任务。例如，如果有 10 个远程服务器，那么 Ansible 将在所有 10 个远程服务器中同时执行任务。

假设在所有远程服务器上总共有 6 个任务要执行。

任务 1 → 任务 2 → 任务 3 → …… → 任务 6

现在，默认情况下，Ansible 将开始在所有 10 个服务器中运行任务 1，并等待所有服务器完成。一旦任务 1 在所有服务器中完成，然后只有 Ansible 将在所有 10 个服务器中启动任务 2，并以这种方式继续进行。

在上述情况下，如果任何任务在任何服务器上失败，那么 Ansible 将跳过该服务器。

## Ansible 控制器节点和托管节点要求
**Ansible 控制器节点：**  
- Ansible 控制器节点必须是 Linux 机器，我们不能使用 Windows 机器作为 Ansible 控制器节点。
- Python 必须安装在 Ansible 控制器节点中。
  - Python 2 >= 版本 2.7
  - Python 3 >= 版本 3.5

**Ansible 受管节点或目标机**  
- 它可以是 Linux 或 Windows 机器
- Python 需要安装在目标机器上，因为默认情况下 Ansible 模块需要 Python。
