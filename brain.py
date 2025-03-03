from node import Node
from connection import Connection
import random
from typing import List


class Brain:
    def __init__(self, inputs):
        self.connections: List[Connection] = []
        self.nodes:List[Node] = []
        self.inputs = inputs
        self.net:List[Node] = []  # All nodes which appear in the neural Network
        self.layers = 2
        self.OUTPUT_idx = self.inputs +1
        self.BIAS_idx = self.inputs

        # Creation of the input nodes
        for i in range(0, self.inputs):
            self.nodes.append(Node(i))
            self.nodes[i].layer = 0
        # Creation of the bias nodes
        self.nodes.append(Node(self.BIAS_idx))
        self.nodes[self.BIAS_idx].layer = 0
        # Creation of output layer
        self.nodes.append(Node(self.OUTPUT_idx))
        self.nodes[self.OUTPUT_idx].layer = 1

        for i in range(0, self.inputs+1):
            self.connections.append(Connection(self.nodes[i], self.nodes[self.OUTPUT_idx], random.uniform(-1, 1)))

    def connect_nodes(self):
        for i in range(0, len(self.nodes)):
            self.nodes[i].connections = []

        for i in range(0, len(self.connections)):
            self.connections[i].from_node.connections.append(self.connections[i])

    def generate_net(self):
        self.connect_nodes()
        self.net = []
        for j in range(0, self.layers):
            for i in range(0, len(self.nodes)):
                if self.nodes[i].layer == j:
                    self.net.append(self.nodes[i])

    def feed_forward(self,vision):
        for i in range(0, self.inputs):
            self.nodes[i].output_value = vision[i]
        
        self.nodes[self.BIAS_idx].output_value = 1

        for i in range(0,len(self.net)):
            self.net[i].activate()

        output_value = self.nodes[self.OUTPUT_idx].output_value

        for i in range(0, len(self.nodes)):
            self.nodes[i].input_value = 0

        return output_value

        