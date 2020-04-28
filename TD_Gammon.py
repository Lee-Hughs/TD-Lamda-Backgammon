#!C:\Users\Lee\AppData\Local\Programs\Python\Python38-32\python.exe
import math
import json

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
    def load_weights(self, weights):
        if(len(self.layers) != len(weights)):
            print("Error loading weights")
            exit(2)
        #for each layer
        for a in range(len(self.layers)):
            #for each node
            for b in range(len(self.layers[a])):
                #for each weight
                for c in range(len(self.layers[a][b].out_con)):
                    self.layers[a][b].out_con[c].weight = weights[a][b][c]

    def load_biases(self, biases):
        for x in range(50):
            self.layers[1][x].bias = biases[x]
        self.layers[2][0].bias = biases[50]

    def clear_inputs(self):
        for layer in self.layers:
            for node in layer:
                node.input = 0
                node.out = 0


class Neuron:
    def __init__(self):
        self.input = 0
        self.bias = 0
        self.out = 0
        self.out_con = []
        self.in_con = []
    def add_input(self, x):
        self.input += x

    def send_output(self):
        self.out = (1 / (1 + math.exp(-(self.bias + self.input))))
        for o in self.out_con:
            o.out.add_input(self.out * o.weight)

    def set_bias(self, b):
        self.bias = b

    def add_connection(self, out, weight):
        self.out_con.append(Axon(self, out, weight))
        out.in_con.append(Axon(self, out, weight))
    def get_output(self):
        return (1 / (1 + math.exp(-(self.bias + self.input))))

class Axon:
    def __init__(self, inp, out, weight):
         self.inp = inp
         self.out = out
         self.weight = weight
def backprop(new, old, target, guess, alpha, lmbda, eTrace):
    #update every weight connecting a hidden layer neuron to the output neuron
    # x = index of the input connection from a hidden layer node to the output layer node
    for x in range(len(new.layers[2][0].in_con)):
        grad = -(target - guess) * guess * (1-guess) * new.layers[2][0].in_con[x].inp.out
        eTrace[1][x] = lmbda*eTrace[1][x] + grad
        new.layers[2][0].in_con[x].inp.out_con[0].weight = new.layers[2][0].in_con[x].inp.out_con[0].weight - (alpha*eTrace[1][x])

    #update everyweight connecting an input layer neron to a hidden layer neuron
    # x = index of the input neuron
    for x in range(len(new.layers[0])):
        # y = index of the connection from the input neuron to the hidden neuron
        for y in range(len(new.layers[0][x].out_con)):
            grad = -(target - guess) * guess * (1-guess) * old.layers[0][x].out_con[y].out.out_con[0].weight * new.layers[0][x].out_con[y].out.out * ( 1 - new.layers[0][x].out_con[y].out.out ) * new.layers[0][x].input
            eTrace[0][x][y] = lmbda*eTrace[0][x][y] + grad
            new.layers[0][x].out_con[y].weight = new.layers[0][x].out_con[y].weight - ( alpha * eTrace[0][x][y] )

    #update the bias on the output neron
    grad = -(target - guess) * guess * (1-guess)
    eTrace[2][50] = lmbda*eTrace[2][50] + grad
    new.layers[2][0].bias = new.layers[2][0].bias - ( alpha * eTrace[2][50] )

    #update each bias in the hidden layer
    for x in range(50):
        grad = -(target - guess) * guess * (1-guess) * old.layers[1][x].out_con[0].weight * old.layers[1][x].out * (1-old.layers[1][x].out)
        eTrace[2][x] = lmbda*eTrace[2][x] + grad
        new.layers[1][x].bias = new.layers[1][x].bias - ( alpha * eTrace[2][x] )

if __name__ == '__main__':
    print("start program")
    tdg = Network()

    input_layer = []
    for x in range(198):
        input_layer.append(Neuron())
    hidden_layer = []
    for x in range(50):
        hidden_layer.append(Neuron())
    output_layer = [Neuron()]

    for in_node in input_layer:
        for out_node in hidden_layer:
            in_node.add_connection(out_node, 1)

    for in_node in hidden_layer:
        for out_node in output_layer:
            in_node.add_connection(out_node, 1)
    tdg.layers = [input_layer, hidden_layer, output_layer]
    #print(vars(tdg))
    with open("weights.json") as json_file:
        data = json.load(json_file)
        tdg.load_weights(data)
    with open("input.json") as json_file:
        data = json.load(json_file)
        tdg.load_input(data)

    #tdg.layers[0][0].add_input(1)
    #tdg.layers[0][1].add_input(2)
    #tdg.layers[0][2].add_input(3)

    #tdg.load_input([1,2,3])

    for node in tdg.layers[0]:
        node.send_output()
    for node in tdg.layers[1]:
        node.send_output()

    print("input layer")
    for node in tdg.layers[0]:
        print("This node's input is: ", node.input)
        print("This node's output is: ", node.out)
        #for con in node.out_con:
            #print("This connection weight is: ", con.weight)
    
    print("The final output is: ", tdg.layers[2][0].get_output())

    print("Output node connections")
    for con in tdg.layers[2][0].in_con:
        print("Connection weight: ", con.weight)
