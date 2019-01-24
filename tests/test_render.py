import pytest
from collector_kickstarts.render import Kickstart
from collector_kickstarts.utility import FileUtility


@pytest.fixture()
def resource_dir():
    from collector_kickstarts.utility import find_subdir
    return find_subdir('resources')


def test_single_template_output(resource_dir):

    expected_file = FileUtility('/'.join([resource_dir, 'simple_kickstart.good.txt']))
    contents = expected_file.get_file_string()

    config_file = FileUtility('/'.join([resource_dir, 'single_file_yaml_data.yml']))
    config_data = config_file.get_yaml()

    output = Kickstart.render_template_from_dict(template_data=config_data)
    assert contents == output


def test_multi_template_output(resource_dir):

    config_file = FileUtility('/'.join([resource_dir, 'render_multiple_files.yml']))
    config_data = config_file.get_yaml()

    assert len(Kickstart.render_files(template_data=config_data)) == 3


def test_create_kickstart_files(resource_dir, tmpdir):
    import os

    # get data from multi yaml file
    fu = FileUtility('/'.join([resource_dir, 'render_multiple_files.yml']))
    yaml_data = fu.get_yaml()

    Kickstart.create_kickstart_files(yaml_data, tmpdir)

    assert os.path.exists('/'.join([tmpdir.dirname, 'first_host_name.ks']))
    assert os.path.exists('/'.join([tmpdir.dirname, 'second_host_name.ks']))
    assert os.path.exists('/'.join([tmpdir.dirname, 'third_host_name.ks']))
