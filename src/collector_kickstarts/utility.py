from typing import List, Dict, Any


class FileUtility(object):
    """Common actions for text files based on file types

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    """
    csv_data: List[Dict[str, str]]
    file_path: str
    file_string: str
    file_list_of_lines: List[str]
    yaml_data_object: Any

    def __init__(self, file_path=None):
        if not file_path:
            raise RuntimeError("No file path provided")
        self.file_path = file_path
        self.file_string = None
        self.file_list_of_lines = None
        self.yaml_data_object = None
        self.csv_data = None

    def get_yaml(self):
        """load yaml data from file and return it


        """
        if not self.yaml_data_object:
            import yaml
            with open(self.file_path, 'r') as stream:
                yaml_data = yaml.load(stream)
            self.yaml_data_object = yaml_data
        return self.yaml_data_object

    def get_file_string(self):
        """return text file contents as string


        """
        if not self.file_string:
            with open(self.file_path, 'r') as stream:
                string_data = stream.read()
            self.file_string = string_data
        return self.file_string

    def get_file_list_of_lines(self):
        """return text file contents a list of lines


        """
        if not self.file_list_of_lines:
            with open(self.file_path, 'r') as stream:
                lines = stream.readlines()
            self.file_list_of_lines = lines
        return self.file_list_of_lines

    def get_csv_data(self):
        """return data from a csv file

        The data format will be a list of dictionaries. each list item represents a csv ros and the row data is a
        dictionary where the key is the column header and the value is the cell data


        """
        if not self.csv_data:
            import csv
            with open(self.file_path, 'r') as stream:
                csv_data = [{k: v for k, v in row.items()}
                            for row in csv.DictReader(stream, skipinitialspace=True)]
            self.csv_data = csv_data
        return self.csv_data
