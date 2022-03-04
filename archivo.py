import json
with open("configuracion.json") as f:
    config = json.load(f)


print(config["texto"])