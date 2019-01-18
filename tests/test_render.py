def test_single_template_output(tmp_path):
    from collector_kickstarts.render import Kickstart
    from collector_kickstarts.utility import FileUtility
    fu = FileUtility('resources/simple_kickstart.good.txt')
    contents = fu.get_file_string()

    fu = FileUtility('resources/single_file_yaml_data.yml')
    config_data = fu.get_yaml()

    assert contents == Kickstart.render_template_from_dict(template_data=config_data)
