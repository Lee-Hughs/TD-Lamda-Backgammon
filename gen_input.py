#!C:\Users\leehu\AppData\Local\Programs\Python\Python37\python.exe
import random
import json

if __name__ == '__main__':
    input_data = []
    for x in range(198):
        input_data.append(round(random.uniform(-1,1),4))

    with open("input.json","w") as input_file:
        input_file.write(json.dumps(input_data))
        input_file.close()
        



