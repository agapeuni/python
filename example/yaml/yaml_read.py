import yaml

with open('data/sample.yml') as f:
    yaml_data = yaml.load(f, Loader=yaml.FullLoader)
    for item in yaml_data:
        print(item)