import pytest

@pytest.fixture()
def resource_dir():
    from collector_kickstarts.utility import find_subdir
    return find_subdir('resources')


def test_single_template_output(resource_dir):
    from collector_kickstarts.render import Kickstart
    from collector_kickstarts.utility import FileUtility
    expected_file = FileUtility('/'.join([resource_dir, 'simple_kickstart.good.txt']))
    contents = expected_file.get_file_string()

    config_file = FileUtility('/'.join([resource_dir, 'single_file_yaml_data.yml']))
    config_data = config_file.get_yaml()

    assert contents == Kickstart.render_template_from_dict(template_data=config_data)
