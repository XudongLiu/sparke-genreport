# SPARKE-GENREPORT
This project is an automatic report generation tool that leverages artificial intelligence and various intelligent agents like tools. It can automatically generate various types of reports simply by configuring templates. While offering automation, it also allows the freedom to customize the content of specific sections through different configuration options.

## Project Configuration
This project requires the configuration of several basic parameters, primarily including the use of large models and tools. The currently supported large models are listed below, with more models and tools being continuously integrated.
Model list:

| Model Name | Support Status | Remarks |
|------------|----------------|---------|
| OpenAI     | 👌              |         |
| Claude     | In progress    |         |
| Others     | In progress    |         |

Tool support:

| Tool Support   | Support Status | Remarks          |
|----------------|----------------|------------------|
| google search  | Supported Serper | Requires API KEY |
|                |                |                  |
|                |                |                  |

## Project Execution
Running the project requires setting up environment variables as follows:
1. Copy the .env.template file to a .env file and configure the environment variables in it.
2. Run the project.

## Template Configuration
Template configuration is the core of this project. By setting up templates, different reports can be generated. The template configuration files are located in the template folder, and the specific configuration method is as follows:
1. In the reports folder under the template folder, create a new folder with the name of the template, where the comments part will be the content of the report generated later.
2. For each comment, correspond to a configuration file in the parts folder, which is central to generation.
3. The content of the configuration file is a YAML file, and the specific configuration method is as follows:
```yaml
agent:
  name: Name
  type: Type to be generated later
  tasks:
    - task_name: Custom name
      steps:
        - step_number: 1
          prompt: >
            "Prompt for AI"
          tool:
            name: Fixed tool category
            action: Tool subcategory
            settings:
              prompt: Parameters to be passed
```
4. After configuration, execute the main file, which will generate the report in the output folder.

## Contact Us
If you have any questions, please contact us, and we will reply to you as soon as possible.

Email: liuxudong@limaicloud.com

X: xudongliu1984

QQ: 343152747