from typing import List, Dict, Any


def merge_config_data(config_data, partial_template):
    result_list = []  # type: List[Dict[str, Any]]
    for item in partial_template:
        merged = item.copy()
        merged.update(config_data)
        result_list.append(merged)

    return result_list


def encrypt_linux_password(unencrypted_password: str) -> str:
    """given a string, encrypt and return in a format that can be put into shadow


    """
    import crypt
    return crypt.crypt(unencrypted_password, crypt.mksalt(crypt.METHOD_SHA512))


def find_subdir(input_dir):
    """Return the relative path of a directory

    Used by test fixtures to find resource files regardless of where pytests is from from (project_root,
    project_root/tests, etc). This didn't matter when i was just running pytests directly, but tox runs form teh
    project dir so this fixes that problem
    """
    import os
    for root, dirs, files in os.walk("."):
        for d in dirs:
            if d == input_dir:
                return os.path.relpath(os.path.join(root, d), ".")


class FileUtility(object):
    """Common actions for text files based on file types

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    """
    _csv_data: List[Dict[str, str]]
    _file_path: str
    _file_string: str
    _file_list_of_lines: List[str]
    _yaml_data_object: Any

    def __init__(self, file_path=None):
        if not file_path:
            raise RuntimeError("No file path provided")
        self._file_path = file_path
        self._file_string = None
        self._file_list_of_lines = None
        self._yaml_data_object = None
        self._csv_data = None

    def get_yaml(self):
        """load yaml data from file and return it


        """
        if not self._yaml_data_object:
            import yaml
            with open(self._file_path, 'r') as stream:
                yaml_data = yaml.load(stream)
            self._yaml_data_object = yaml_data
        return self._yaml_data_object

    def get_file_string(self):
        """return text file contents as string


        """
        if not self._file_string:
            with open(self._file_path, 'r') as stream:
                string_data = stream.read()
            self._file_string = string_data
        return self._file_string

    def get_file_list_of_lines(self):
        """return text file contents a list of lines


        """
        if not self._file_list_of_lines:
            with open(self._file_path, 'r') as stream:
                lines = stream.readlines()
            self._file_list_of_lines = lines
        return self._file_list_of_lines

    def get_csv_data(self):
        """return data from a csv file

        The data format will be a list of dictionaries. each list item represents a csv ros and the row data is a
        dictionary where the key is the column header and the value is the cell data


        """
        if not self._csv_data:
            import csv
            with open(self._file_path, 'r') as stream:
                csv_data = [{k: v for k, v in row.items()}
                            for row in csv.DictReader(stream, skipinitialspace=True)]
            self._csv_data = csv_data
        return self._csv_data
