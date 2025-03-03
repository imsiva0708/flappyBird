from node import Node

class Connection:
    def __init__(self,from_node, to_node, weight):
        self.from_node:Node = from_node
        self.to_node:Node = to_node
        self.weight = weight