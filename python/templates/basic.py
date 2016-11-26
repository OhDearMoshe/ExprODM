from jinja2 import Template


class Examper:
    name = ""

template = Template('Hello {{ name }}!')
print template.render(name='John Doe')

e = Examper()
e.name = "Testy"
template = Template('Hello {{ example.name }}!')
print template.render(example=e)
