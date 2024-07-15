import yaml

class AgentConfig:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        """加载YAML配置文件"""
        with open(self.config_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)



    def get_agent_config(self, agent_name):
        """获取指定agent的配置"""
        for agent in self.config['agents']:
            if agent['name'] == agent_name:
                return agent
        return None

    def execute_function(self, agent_name, function_name):
        """执行指定agent的函数"""
        agent = self.get_agent_config(agent_name)
        if agent:
            for function in agent.get('functions', []):
                if function['name'] == function_name:
                    # 这里可以添加真正执行函数的代码
                    print(f"Executing {function_name} with parameters {function['parameters']}")
                    return True
        return False

    def start_tool(self, agent_name, tool_name):
        """启动指定agent的工具"""
        agent = self.get_agent_config(agent_name)
        if agent:
            for tool in agent.get('tools', []):
                if tool['name'] == tool_name:
                    # 这里可以添加真正启动工具的代码
                    print(f"Starting tool {tool_name} with settings {tool['settings']}")
                    return True
        return False

    # 做一个函数，能够获取整个文件中第一符合这个标签的信息，能够迭代搜索，不需要指定根的名称
    def get_metadata(self, tag_name, root=None):
        """获取指定tag的metadata"""
        # 从根节点进行搜索，直到找到相关的tag
        if root is None:
            root = self.config
        if isinstance(root, dict):
            if tag_name in root:
                return root[tag_name]
            for key, value in root.items():
                result = self.get_metadata(tag_name, value)
                if result:
                    return result
        return None



