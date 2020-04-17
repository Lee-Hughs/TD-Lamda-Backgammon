#!C:\Users\Lee\AppData\Local\Programs\Python\Python38-32\python.exe
import math

class Network:
    def __init__(self):
        self.layers = []
        self.input = []
        self.alpha = 5
        self.lambd = 0.6
        self.e_trace = 0
    def load_input(self, inputs):
        if(len(inputs) != len(self.layers[0])):
            print("Error loading inputs")
            exit(2)
        for x in range(len(inputs)):
            self.layers[0][x].add_input(inputs[x])

class Neuron:
    def __init__(self):
        self.input = 0
        self.out = 0
        self.out_con = []
        #self.in_con = []
    def add_input(self, x):
        self.input += x
    def send_output(self):
        self.out = (1 / (1 + math.exp(-self.input)))
        for o in self.out_con:
            o.out.add_input(self.out * o.weight)
    def add_connection(self, out, weight):
        self.out_con.append(Axon(self, out, weight))

class Axon:
    def __init__(self, inp, out, weight):
         self.inp = inp
         self.out = out
         self.weight = weight

if __name__ == '__main__':
    print("start program")
    tdg = Network()

    input_layer = [Neuron(), Neuron(), Neuron()]
    hidden_layer = [Neuron(), Neuron()]
    output_layer = [Neuron()]

    for in_node in input_layer:
        for out_node in hidden_layer:
            in_node.add_connection(out_node, 1)

    for in_node in hidden_layer:
        for out_node in output_layer:
            in_node.add_connection(out_node, 1)
    tdg.layers = [input_layer, hidden_layer, output_layer]
    print(vars(tdg))

    #tdg.layers[0][0].add_input(1)
    #tdg.layers[0][1].add_input(2)
    #tdg.layers[0][2].add_input(3)

    tdg.load_input([1,2,3])

    for node in tdg.layers[0]:
        node.send_output()
    for node in tdg.layers[1]:
        node.send_output()

    print("input layer")
    for node in tdg.layers[0]:
        print("This node's input is: ", node.input)
        print("This node's output is: ", node.out)
        for con in node.out_con:
            print("This connection weight is: ", con.weight)
    
    print("The final output is: ", tdg.layers[2][0].input)
