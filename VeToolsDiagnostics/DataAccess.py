import os
from typing import Union, Optional
from yaml import CSafeLoader as Loader
import yaml
from infrastructure.PathResolver import resolve_path

basedir = os.path.dirname(__file__)


# noinspection PyMethodMayBeStatic
class DataAccess:
    """
    This class is a system of interacting with the yaml data file. It is used to load the data file,
    and to navigate through the decision tree.
    Each disease in the data.yml file is a tree-like structure. The root node is the disease name,
    and the leaves are the final pages. The intermediate nodes are the questions.
    The data file is loaded into a dictionary, and the dictionary is passed to the class.
    The class then navigates through the dictionary, and returns the data for the current page.

    """
    def __init__(self):
        self.yml_data = self.load_yaml_data()
        self.question_history = []
        self.base_data = None
        self.flag = None
        self.current_data = None
        self.text = None

    def load_yaml_data(self) -> Optional[dict]:
        try:
            with open(resolve_path('data/data.yml')) as fh:
                data = yaml.load(fh, Loader=Loader)
                return data
        except FileNotFoundError:
            return None

    def current_node_flag(self, loaded_yaml: dict, disease: str) -> Union[int, str]:
        return loaded_yaml[disease]['flag']

    def get_disease_root_node(self, loaded_yaml: dict, disease: str) -> dict:
        return loaded_yaml[disease]

    def reset_to_flag(self, disease_root: dict) -> dict:
        """
        This method is used to reset the data to the previous node in the decision tree,
        by popping off the last flag added to the question history.
        :param disease_root: the base data for the disease
        :return: the data at the flag
        """
        # get the flag of the last page
        last_page_flag = self.question_history.pop()

        # loop through base_data until the flag for the last page is found (flag = last_page)
        def traverse_tree(breadth: dict, flag: str) -> dict:
            for k, v in breadth.items():
                if flag in breadth.values():
                    return breadth
                elif isinstance(v, dict):
                    recursive_call = traverse_tree(v, flag)
                    if recursive_call is not None:
                        return recursive_call

        return traverse_tree(disease_root, last_page_flag)

    def update_data(self, action: str):
        """
        This method is used to update the data to the next node in the decision tree.
        :param action: the action to take
        """
        # get the next node's data
        next_data = self.current_data[action]

        # add the current node's flag to the history
        self.question_history.append(self.current_data['flag'])

        # update the current data
        self.current_data = next_data

        # update the text
        self.text = self.current_data['text']

        # update the flag
        self.flag = self.current_data['flag']

    def reset_data(self):
        self.question_history = []
        self.base_data = None
        self.flag = None
        self.current_data = None
        self.text = None
