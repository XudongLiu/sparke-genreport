from tools.serper_search import google_search


def call_tools(tool):
    print(f"Starting tool {tool['name']} with settings {tool['settings']}")
    if tool['action'] == 'google_search':
        prompt = tool['settings']['prompt']
        search_content = google_search(prompt)
        return search_content
    return ""