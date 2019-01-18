from collector_kickstarts.utility import FileUtility


def test_get_yaml():

    fu = FileUtility('resources/file_utility_yaml_test.yml')
    yaml_data = fu.get_yaml()
    assert isinstance(yaml_data, list)
    assert len(yaml_data) == 2
    assert len(yaml_data[0]) == 2
    assert len(yaml_data[1]) == 2


def test_get_file_string():
    fu = FileUtility('resources/file_string_test_data.txt')
    expected_string = """this is the first line
this is the second line, followed by a newline
"""
    assert fu.get_file_string() == expected_string


def test_get_file_list_of_lines():
    fu = FileUtility('resources/file_string_test_data.txt')
    expected_list = ["this is the first line",
                     "this is the second line, followed by a newline",
                     ""]
    assert fu.get_file_list_of_lines() == expected_list
