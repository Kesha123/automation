from enum import Enum

class Catalogue(Enum):
    CATALOG = "#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(3)"
    CATALOG_ALTER = "#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(4)"
    BENCH = "div:nth-child(10)"