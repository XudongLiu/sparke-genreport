import os
from abc import ABC, abstractmethod
from utils.yaml_tool import AgentConfig

class BaseLLMModel(ABC):

    @abstractmethod
    def process_text(self, text, model, prompt):
        pass



def create_work_model():
    # get the config form config file which is a json file
    # load config file from folder
    current_folder = os.path.dirname(__file__)
    config = AgentConfig(current_folder + '/config/model.json').load_config()

    if config["model_name"] == "openai":
        from models.openai.openai_model import OpenAIModel
        return OpenAIModel()
    else:
        raise ValueError(f"Unknown model type: {config['model']}")