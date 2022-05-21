import json
from Catalog.Items.Bench import Bench


class Parser:

    def __init__(self, project_path: str = "Project1.json") -> None:
        self.name = project_path
        self.layers = {}
        self.holes = []
        self.lines = []

    def parse_project(self):
        with open(self.name, "r") as project:
            json_string = json.loads(project.read())
            project.close()
        return json_string

    def set_layers(self):
        for layer in dict(self.parse_project()["layers"]).keys():
            self.layers.update({layer : {"lines" : None, "holes" : None, "items" : None}})

    def get_layers(self):
        return self.parse_project()["layers"]

    def get_items(self):
        items = []
        for layer in self.get_layers().items():
            layer_name = layer[0]
            layer_items = list(layer[1].get("items").items())

            for index, item in enumerate(layer_items):
                properties = item[1].get("properties")
                name = properties.get("name")
                altitude = properties.get("altitude")
                x = properties.get("x")
                y = properties.get("y")
                rotation = properties.get("rotation")

                match item[1].get("type"):
                    case "bench":
                        bench = Bench(x,y,rotation,name,altitude)
                        self.items.append(bench)

            self.layers[layer_name]["items"] = items


    def get_lines(self):
        pass

    def get_holes(self):
        pass
        


p = Parser()
p.get_items()

for index, item in enumerate(p.layers):
    print(item)