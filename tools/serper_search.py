import os

import requests
import json

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv()) # This loads the .env file in the root directory of the project

def google_search(keyword:str):
    url = "https://google.serper.dev/search"

    payload = json.dumps({
        "q": keyword,
        # "gl": "cn",
        # "hl": "zh-cn",
        # "num": 10,
        # "autocorrect": True,
        # "page": 1,
        # "type": "search",
        # "engine": "google"
    })

    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    result = ''

    # 访问返回的数据
    data = json.loads(response.text)
    print(data)
    for key in data['organic']:
        # 将内容写入result，每一个key的title，snippet，url，用横线分开，并且每个前面加上相应标签

        if 'title' in key and key['title']:
            result += 'Title: ' + key['title'] + '\n'
        if 'snippet' in key and key['snippet']:
            result += 'Snippet: ' + key['snippet'] + '\n'
        if 'url' in key and key['url']:
            result += 'URL: ' + key['url'] + '\n'
        result += '------------------------------------\n'

    return result


def googleNewsSearch(keywords,local = 'us',country = 'us'):
    url = "https://google.serper.dev/news"

    # payload = json.dumps({
    #     "q": keyword,
    #     "gl": "cn",
    #     "hl": "zh-cn",
    #     "num": 10,
    #     "autocorrect": True,
    #     "page": 1,
    #     "type": "search",
    #     "engine": "google"
    # })

    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'Content-Type': 'application/json'
    }

    for keyword in keywords:
        keyword['hl'] = local
        keyword['gl'] = country

    payload = json.dumps(keywords)


    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return response.text