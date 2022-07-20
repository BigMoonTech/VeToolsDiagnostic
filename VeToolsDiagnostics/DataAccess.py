import os
from typing import Union, Optional

import yaml

basedir = os.path.dirname(__file__)

# noinspection PyMethodMayBeStatic
class DataAccess:
    def __init__(self, disease_text: str = Optional[str]):
        self.filepath = basedir + '/Data/data.yml'

        self.yml_data = self.load_data_map()

        self.disease_text = disease_text
        self.question_history = []
        self.base_data = None
        self.flag = None
        self.data = None
        self.text = None

    def load_data_map(self) -> Optional[dict]:
        try:
            with open(self.filepath) as fh:
                data = yaml.safe_load(fh)
                return data
        except FileNotFoundError:
            return None

    def get_current_flag(self, loaded_yaml: dict, disease: str) -> Union[int, str]:
        return loaded_yaml[disease]['flag']

    def get_disease_dict(self, loaded_yaml: dict, disease: str) -> dict:
        return loaded_yaml[disease]

    def reset_to_flag(self, base_data: dict) -> dict:
        # get the flag of the last page
        last_page = self.question_history.pop()

        # # loop through base_data until the flag for the last page is found (flag = last_page)
        def traverse_tree(tree: dict, flag_a: str) -> dict:
            for k, v in tree.items():
                if flag_a in tree.values():
                    return tree
                elif isinstance(v, dict):
                    recursive_call = traverse_tree(v, flag_a)
                    if recursive_call is not None:
                        return recursive_call

        return traverse_tree(base_data, last_page)

    def reset_data(self):
        self.question_history = []
        self.base_data = None
        self.flag = None
        self.data = None
        self.text = None
