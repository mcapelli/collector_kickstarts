import pytest
from collector_kickstarts.utility import FileUtility
import yaml


@pytest.fixture()
def resource_dir():
    from collector_kickstarts.utility import find_subdir
    return find_subdir('resources')


def test_get_yaml(resource_dir):

    fu = FileUtility('/'.join([resource_dir, 'render_multiple_files.yml']))

    yaml_data = fu.get_yaml()
    assert isinstance(yaml_data, list)
    assert len(yaml_data) == 3
    assert len(yaml_data[0]) == 8
    assert len(yaml_data[1]) == 8
    assert len(yaml_data[2]) == 8


def test_get_file_string(resource_dir):
    fu = FileUtility('/'.join([resource_dir, 'file_string_test_data.txt']))

    expected_string = """this is the first line
this is the second line, followed by a newline
"""
    assert fu.get_file_string() == expected_string


def test_get_file_list_of_lines(resource_dir):
    fu = FileUtility('/'.join([resource_dir, 'file_string_test_data.txt']))

    expected_list = ["this is the first line\n",
                     "this is the second line, followed by a newline\n"]
    assert fu.get_file_list_of_lines() == expected_list


def test_get_csv_data(resource_dir):
    fu = FileUtility('/'.join([resource_dir, 'file_utility_csv_data.csv']))

    data = fu.get_csv_data()
    assert data[0]['first_name'] == 'nate'
    assert data[0]['last_name'] == 'marks'
    assert data[0]['age'] == '46'
    assert data[1]['first_name'] == 'doug'
    assert data[1]['last_name'] == 'syer'
    assert data[1]['age'] == '32'

def test_merge_config_data(resource_dir):
    from collector_kickstarts.utility import merge_config_data
    config_string = '''
    yum_repo_ip: 44.44.44.44
    network_interface_name: eth55
    encrypted_password:  SOME_ENCRYPTED-PASSWORD
    nameservers:
        - 8.8.8.8
        - 8.8.4.4
    '''
    config_data = yaml.load(config_string)

    partial_string = '''
-   hostname: first_host_name
    host_ip_address: 10.1.1.100
    host_default_gateway: 10.1.1.1
    host_subnet_mask: 255.255.255.0
-   hostname: second_host_name
    host_ip_address: 10.2.2.100
    host_default_gateway: 10.2.2.1
    host_subnet_mask: 255.255.255.0
-   hostname: third_host_name
    host_ip_address: 10.3.3.100
    host_default_gateway: 10.3.3.1
    host_subnet_mask: 255.255.255.0

    '''
    partial_data = yaml.load(partial_string)

    expected_data_string = '''
-   yum_repo_ip: 44.44.44.44
    hostname: first_host_name
    network_interface_name: eth55
    host_ip_address: 10.1.1.100
    host_default_gateway: 10.1.1.1
    host_subnet_mask: 255.255.255.0
    encrypted_password: SOME_ENCRYPTED-PASSWORD
    nameservers:
        - 8.8.8.8
        - 8.8.4.4
-   yum_repo_ip: 44.44.44.44
    hostname: second_host_name
    network_interface_name: eth55
    host_ip_address: 10.2.2.100
    host_default_gateway: 10.2.2.1
    host_subnet_mask: 255.255.255.0
    encrypted_password: SOME_ENCRYPTED-PASSWORD
    nameservers:
        - 8.8.8.8
        - 8.8.4.4
-   yum_repo_ip: 44.44.44.44
    hostname: third_host_name
    network_interface_name: eth55
    host_ip_address: 10.3.3.100
    host_default_gateway: 10.3.3.1
    host_subnet_mask: 255.255.255.0
    encrypted_password: SOME_ENCRYPTED-PASSWORD
    nameservers:
        - 8.8.8.8
        - 8.8.4.4

'''
    expected_data = yaml.load(expected_data_string)
    assert merge_config_data(config_data, partial_data) == expected_data


def test_merge_config_data():
    from collector_kickstarts.utility import reformat_host_name
    input_string = "Crane-002.inframax.ncare"
    expected = "PROD01-ZDEL-CRANE-002"
    assert reformat_host_name(input_string) == expected
