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

    def run(self):
        #Import necessary functions from Jinja2 module
        from jinja2 import Environment, FileSystemLoader

        #Import YAML module
        import yaml

        #Load data from YAML into Python dictionary
        config_data = yaml.load(open('resources/yaml_data.yml'))

        #Load Jinja2 template
        env = Environment(loader = FileSystemLoader('resources/templates'), trim_blocks=True, lstrip_blocks=True)
        template = env.get_template('template.txt')

        #Render the template with data and print the output
        return template.render(config_data)
