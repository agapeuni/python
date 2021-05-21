import yaml

yaml_data = [
    {
        "Code": "A1",
        "Name": "item1",
        "Date": "2020-09-19"
    },
    {
        "Code": "B2",
        "Name": "item2",
        "Date": "2020-09-20",
        "Memo": {"Hobby1": "Music", "Hobby2": "Movie"}
    }, {
        "Code": "C3",
        "Name": "item3",
        "Date": "2020-09-20"
    },
    {"Code": "D4", "Name": "item4"}
]

with open("data/sample.yml", "w") as f:
    yaml.dump(yaml_data, f)
