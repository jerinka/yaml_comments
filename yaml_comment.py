import sys
from ruamel.yaml import YAML


# Inspired from blog: https://towardsdatascience.com/writing-yaml-files-with-python-a6a7fc6ed6c3

inp = """\
# example
name:             # details
  family: Smith
  given: Alice    # one of the siblings
"""

yaml = YAML()
code = yaml.load(inp)
code['name']['given'] = 'Bob'

# Dumping to a yaml file
file_name='before.yaml'
with open(file_name, 'w') as fp:
    yaml.dump(code, fp)

#Loading a yaml file
data={}
with open(file_name) as fp:
    data = yaml.load(fp)
yaml.dump(data, sys.stdout)
print()

# Inserting a comment
data['name'].yaml_add_eol_comment(
        key="family",
        comment="new comment inserted!!"
    )
yaml.dump(data, sys.stdout)

# Dumping to a yaml file
file_name='after.yaml'
with open(file_name, 'w') as fp:
    yaml.dump(data, fp)




