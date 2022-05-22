import json
from Catalog.Items.Bench import Bench


class Parser:

    def __init__(self, project_path: str) -> None:
        self.name = project_path
        self.layers = {}
        self.holes = []
        self.lines = []
        self.set_layers()

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
        for layer in self.get_layers().items():
            items = []
            layer_name = layer[0]
            layer_items = list(layer[1].get("items").items())

            for index, item in enumerate(layer_items):
                properties = item[1].get("properties")
                name = item[1].get("name")
                altitude = properties.get("altitude")
                x = item[1].get("x")
                y = item[1].get("y")
                rotation = item[1].get("rotation")

                match item[1].get("type"):
                    case "bench":
                        bench = Bench(x,y,rotation,name,Alitude=altitude)
                        items.append(bench)
            
            self.layers[layer_name]["items"] = items


    def get_lines(self):
        pass

    def get_holes(self):
        pass

    def load_project(self):
        self.get_items()
        self.get_lines()
        self.get_holes()
        return self.layers
