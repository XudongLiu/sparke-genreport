import json
import os
import re
import time
from typing import Any

import yaml

from dotenv import load_dotenv

from models.base_model import create_work_model
from tools.call_tools import call_tools

load_dotenv()

# get prompt from file
# prompt = current_dir = os.getcwd() + '/prompts/work_prompt.txt'

# get parent folder
parent_dir = os.path.dirname(os.getcwd())
current_dir = os.path.dirname(__file__)
template_dir = os.getcwd() + '/template/reports/'
parts_dir = os.getcwd() + '/template/parts/'


def generate_report(template_name):
    llm = create_work_model()
    work_prompt = ""
    # load the work prompt
    # get current working directory

    with open(current_dir + '/prompts/work_prompt.txt', 'r', encoding='utf-8') as f:
        work_prompt = f.read()

    # step 1: get the markdown template file
    with open(template_dir + template_name, 'r', encoding='utf-8') as f:
        template = f.read()

    # step 2: read the annotation tags from the template
    tags = re.findall(r'<!--(.*?)-->', template)

    # step 3: replace the tags with the actual content
    for tag in tags:
        # get the tag name, delete the space
        tag = tag.strip()

        # read the yaml file with the tag's name
        with open(parts_dir + tag + '.yaml', 'r', encoding='utf-8') as f:
            yaml_config = yaml.safe_load(f)
            print(f'Processing tag: {yaml_config}')
            agent_tasks = yaml_config['agent']['tasks']
            for task in agent_tasks:
                content = ""
                tool_response = ""
                for step in task['steps']:
                    if 'tool' in step:
                        # call the tool to process the text
                        tool_response = call_tools(step['tool'])
                    local_prompt = step['prompt'] + tool_response
                    # call llm to process the text
                    response = llm.process_text(work_prompt, model="gpt-3.5-turbo", prompt=local_prompt)

                    content += response

                # replace the tag with the content
                template = template.replace(f'<!--{tag}-->', content)

    # step 4: save the content to a new file
    with open(f'{os.getcwd()}/output/{template_name}.md', 'w', encoding='utf-8') as f:
        f.write(template)
        print(f'File reports/{template_name}.md has been created successfully')















# def nation_report(config: str, nation: str, file_mode: str, file_name: str = None, level: str = None):
#     # 获取当前工作目录的路径
#     current_dir = os.getcwd()
#
#     # 拼接得到配置文件的绝对路径
#     config_file_path = os.path.join(current_dir, 'config/' + config)
#
#     # 读取配置文件内容
#     with open(config_file_path, 'r', encoding='utf-8') as file:
#         config_data = file.read()
#
#     # 进行数据替换
#     # 假设我们要替换的内容是 {PLACEHOLDER}，替换为 'new_value'
#
#     # 浏览replace_params_json每个元素
#     for item in replace_params_json:
#         # 将config_data中的{PLACEHOLDER}替换为new_value
#         old_value = "<<" + item["key"] + ">>"
#         config_data = config_data.replace(old_value, item['value'])
#
#     # 使用yaml加载数据
#     config = yaml.safe_load(config_data)
#
#     # # """加载并解析YAML配置文件"""
#     # with open(config_file_path, 'r', encoding='utf-8') as file:
#     #     config = yaml.safe_load(file)
#
#     print(config)
#
#     # 查看是否有准备的数据
#     if 'prepared_data' in config:
#         prompt_prepare(config['prepared_data'], './prompts/temp_prompt_files')
#
#     # step 1: 获取国别的信息
#
#     nation_name = nation
#
#     # 创建markdown文件
#     if file_name:
#         markdown_file = os.path.join(current_dir, f'reports/{file_name}.md')
#     else:
#         markdown_file = os.path.join(current_dir, f'reports/{nation_name}.md')
#     with open(markdown_file, file_mode, encoding='utf-8') as f:
#         f.write(f'# {nation_name}国别分析报告\n\n')
#         task_name = config['agent']['tasks'][0]['task_name']
#         # 插入标题1
#         f.write(f'## {config["agent"]["name"]}\n\n')
#
#         tasks = config['agent']['tasks']
#
#         step_num = 0
#
#         mulu = [
#             '(一)', '(二)', '(三)', '(四)', '(五)', '(六)', '(七)', '(八)', '(九)', '(十)'
#         ]
#
#         for task in tasks:
#             # step 2: 获取执行的步骤信息
#             steps = task['steps']
#
#             # 获取当前时间的字符串 格式 2024年6月23日
#             present_time = time.strftime('%Y年%m月', time.localtime(time.time()))
#
#             # step 3: 执行步骤
#             f.write(f'### {task["task_type"]}\n\n')
#
#             step_num += 1
#
#             for step in steps:
#
#                 if 'step_name' in step:
#                     f.write(f'#### {step["step_name"]}\n\n')
#
#                 if step['tool']['name'] == 'gb-assistant':
#                     content = process_message(step['prompt'], step['tool']['settings']['parameter1'])
#                     f.write(f'{content}\n\n')
#                     break
#
#                 if step['tool']['action'] == 'insert_table':
#                     df = wb_api_table(indicators, base_url)
#                     # 重塑DataFrame以便更好的阅读
#                     pivot_df = df.pivot(index='指标', columns='年份', values='数值')
#                     # 输出到Markdown
#                     table = pivot_df.to_markdown()
#                     f.write(f'{table}\n\n')
#                     continue
#
#                 if step['tool']['action'] == 'gdp':
#                     addPrompt = step['tool']['settings']['parameter1']
#                     search_content = wb_api_table(indicators, base_url)
#
#                 if step['tool']['action'] == 'perplexity':
#
#                     addPrompt = step['tool']['settings']['parameter1']
#                     if 'reference_urls' in step['tool']['settings']:
#                         addPrompt = addPrompt + ' 可以查阅 ' + step['tool']['settings']['reference_urls']
#                     # 调用perplexity的工具
#                     pplx_prompt = f'''
#                     请分析{nation_name}的信息，根据以下要求进行分析：
#                     {step['prompt']}
#                     {addPrompt}
#                     '''
#                     search_content = pplx_search(pplx_prompt)
#
#                 if step['tool']['action'] == 'google':
#                     search_content = googleSearch(
#                         keyword=present_time + nation_name + step['tool']['settings']['parameter1'])
#
#                     print(search_content)
#
#                 if step['tool']['action'] == 'search_ralated':
#                     search_content = search_related(client, present_time + nation_name + step['prompt'])
#                     googleSearch(keyword=present_time + nation_name + search_content)
#
#                     print(search_content)
#
#                 if step['refine']['status'] == 'yes':
#                     refine_prompt = step['refine']['prompt']
#                     refine = f'''
#                     {search_content}
#                     以上信息是搜索到的信息，根据我的要求进行分析, 现在是{present_time}尽量搜索最新的信息
#                     {refine_prompt}
#                     {addPrompt}
#                     '''
#                     search_content = pplx_search(refine)
#
#                 if 'reference_answer' in step:
#                     reference_answer = step['reference_answer']
#                 else:
#                     reference_answer = 'NO REFERENCE ANSWER PROVIDED'
#
#                 if 'length' in step:
#                     length = step['length']
#                 else:
#                     length = 200
#
#                 # 调用llm工具进行生成
#
#                 # 组合一个prompt
#                 # openai_prompt = f'''
#                 # 本次搜索的国别为{nation_name}
#                 # 请根据我的要求完成工作，要求如下：
#                 # {step['prompt']}，你可以不用搜索，使用我的提供的搜索信息进行分析。
#                 # 我提供的搜索信息如下：
#                 # {search_content}
#                 # 请使用最新的信息，现在是{present_time}，尽量使用最新信息。并且根据你的知识进行扩展和分析。
#                 # 输出的内容请按照段落进行输出，整合数据内容，用一个段落进行输出，不用markdown格式，就正常文字输出即可，语言要精炼，体现专业性。
#                 #
#                 # '''
#                 openai_prompt = f'''
#                          You are an AI assistant tasked with analyzing a given text and providing a summary and sentiment analysis. Please follow the instructions below:
#
#                         <INSTRUCTIONS>
#                         1. Read the text provided between the TEXT delimiters.
#                         2. REF contain the sample， you can use it to help you understand the text. and with your information and TEXT to provide a summary.
#                         3. Provide a summary of the text， keep all the useful information, and make it concise.
#                         4. add more information based your knowledge，and rewrite the text.
#                         5. Give the summary with a few paragraphs.
#                         6. Answer in Chinese. don't output delimiters
#
#                         </INSTRUCTIONS>
#
#                         <REF>
#                         {reference_answer}
#                         </REF>
#
#                         <TEXT>
#                         {search_content}
#                         </TEXT>
#
#                         Please format your response as follows and write more than {length} words:
#
#                         [Your some paragraphs summary here]
#
#                         Answer with Chinese.
#
#                 '''
#
#                 response = client.chat.completions.create(
#                     model="gpt-3.5-turbo",
#                     messages=[
#                         {"role": "system", "content": "You are a useful assistant."},
#                         {"role": "user", "content": openai_prompt},
#                     ]
#                 )
#
#                 print(response.choices[0].message.content)
#
#                 f.write(f'&emsp;&emsp;{response.choices[0].message.content}\n\n')
#
#                 # break
#
#         # 保存文件
#         f.close()