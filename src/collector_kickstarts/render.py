from typing import List, Dict


class Kickstart(object):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = {}
        self.kwargs.update(kwargs)

    @staticmethod
    def render_template_from_dict(template_data=None) -> str:
        """Given a dict, render the template and return as string

        Note that PackageLoader lets me put the template in src and from the template in the package after install
        """
        from jinja2 import Environment, PackageLoader

        env = Environment(loader=PackageLoader('collector_kickstarts', 'templates'),
                          trim_blocks=True, lstrip_blocks=True)
        template = env.get_template('kickstart_template.txt')

        return template.render(template_data)

    @staticmethod
    def render_files(template_data=None) -> List[str]:
        """Render a list of file strings

        iterate on a list of dicts and return a list of strings.  each of the return strings is the contents of a
        kickstart file.
        :type template_data: List[Dict[str, str]]

        """
        output_list = []
        for data in template_data:
            output_list.append(Kickstart.render_template_from_dict(data))
        return output_list




