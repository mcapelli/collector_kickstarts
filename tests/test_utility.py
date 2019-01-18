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
    expected_list = ["this is the first line\n",
                     "this is the second line, followed by a newline\n"]
    assert fu.get_file_list_of_lines() == expected_list


def test_get_csv_data():
    fu = FileUtility('resources/file_utility_csv_data.csv')
    data = fu.get_csv_data()
    assert data[0]['first_name'] == 'nate'
    assert data[0]['last_name'] == 'marks'
    assert data[0]['age'] == '46'
    assert data[1]['first_name'] == 'doug'
    assert data[1]['last_name'] == 'syer'
    assert data[1]['age'] == '32'

