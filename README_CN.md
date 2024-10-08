# SPARKE-GENREPORT
本项目是一个通过人工智能与工具等智能体的调用自动生成报告的项目，可以仅仅通过配置模板就能自动生成您想要的各种报告，在自动化的同时也通过不同的配置选项，能够自由设置其中小章节的内容。

## 项目配置
本项目需要配置几个基础的参数，主要包含使用的大模型和工具。目前支持的大模型如下，其他工具和大模型正在持续的接入。
模型列表：

| 模型名称 | 是否支持 | 备注 |
| -------- | -------- | ---- |
| OpenAI   | 👌        |      |
| Claude   | 正在进行 |      |
| 其他     | 正在进行 |      |

工具支持：

| 工具支持   | 是否支持   | 备注            |
| ---------- | ---------- | --------------- |
| google搜索 | 支持Serper | 需要配置API KEY |
|            |            |                 |
|            |            |                 |

## 项目运行
项目运行需要配置好环境变量，具体的环境变量如下：
1、 将.env.template文件复制为.env文件，并配置其中的环境变量
2、 运行项目

## 模板配置
模板配置是本项目的核心，通过配置模板，可以生成不同的报告，模板配置文件在template文件夹下，具体的配置方法如下：
1、 在template文件夹下的reports文件夹下新建一个文件夹，文件夹名称为模板名称，其中的注释部分为后期生成报告的内容
2、 针对每个注释，对应parts文件夹下的配置文件，这个配置文件是生成的核心
3、 配置文件中的内容是一个yaml文件，具体的配置方法如下：
```yaml 
agent:
  name: 名称
  type: 后期生成的类型
  tasks:
    - task_name: 自定义名称
      steps:
        - step_number: 1
          prompt: >
            "用于AI的提示"
          tool:
            name: 固定的工具大类
            action: 工具小类
            settings:
              prompt: 需要传输的参数
```
4、 配置完成后执行main文件，会在output文件夹中生成报告

## 联系我们
如果您有任何问题，请联系我们，我们会尽快回复您。

邮件：liuxudong@limaicloud.com

X: xudongliu1984

QQ: 343152747


