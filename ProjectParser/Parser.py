import json
import math
from Catalog.Items.Bench import Bench
from Catalog.Lines.Wall import Wall
from Logger.Logger import Logger


class Parser:

    def __init__(self, project_path: str) -> None:
        self.name = project_path
        self.layers = {}
        self.holes = []
        self.vertices = []
        self.set_layers()

    def parse_project(self):
        with open(self.name, "r") as project:
            json_string = json.loads(project.read())
            project.close()
        return json_string

    def set_layers(self):
        for layer in dict(self.parse_project()["layers"]).keys():
            self.layers.update({layer : {"lines" : None, "holes" : None, "items" : None, "vertices": None}})

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

    def get_vertices(self):
        for layer in self.get_layers().items():
            vertices = {}
            layer_name = layer[0]
            layer_vertices = list(layer[1].get("vertices").items())

            for vertex in layer_vertices:
                vertices.update({vertex[0]: {"x":vertex[1].get("x"), "y":vertex[1].get("y")}})
            
            self.layers[layer_name]["vertices"] = vertices

    def get_lines(self):
        self.get_vertices()
        for layer in self.get_layers().items():
            lines = []
            layer_name = layer[0]
            layer_lines = list(layer[1].get("lines").items())

            for line in layer_lines:
                name = line[1].get("name")
                line_vertices = [vert for vert in line[1].get("vertices")]
                x1 = self.layers[layer_name]["vertices"].get(line_vertices[0]).get("x")
                y1 = self.layers[layer_name]["vertices"].get(line_vertices[0]).get("y")
                x2 = self.layers[layer_name]["vertices"].get(line_vertices[1]).get("x")
                y2 = self.layers[layer_name]["vertices"].get(line_vertices[1]).get("y")
                length = math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )
                height = {"length": line[1].get("properties").get("height").get("length"), "unit":"cm"}
                thickness = {"length": line[1].get("properties").get("thickness").get("length"), "unit":"cm"}
                
                match line[1].get("type"):
                    case "wall":
                        textureA = line[1].get("properties").get("textureA")
                        textureB = line[1].get("properties").get("textureB")
                        wall = Wall(name,x1,y1,x2,y2,length,height=height,thickness=thickness,textureA=textureA,textureB=textureB)
                        lines.append(wall)
            
            self.layers[layer_name]["lines"] = lines

    def get_holes(self):
        pass

    def load_project(self):
        self.get_items()
        Logger.info("Items got successfully")
        self.get_lines()
        Logger.info("Lines got successfully")
        self.get_holes()
        Logger.info("Holes got successfully")
        return self.layers
