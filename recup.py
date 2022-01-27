import json


def test():

  with open('perso.json', 'r') as f:
    data = json.load(f)

  # Output: {'name': 'Bob', 'languages': ['English', 'French']}
  print(data)