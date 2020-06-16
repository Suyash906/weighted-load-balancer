import json
import sys
import os.path
from os import path
from heapq import heapify, heappush, heappop

BASE_FILE_PATH = 'Files/'
SERVER_FILE_PATH = BASE_FILE_PATH + 'server.txt'
INITIAL_FILE_PATH = BASE_FILE_PATH + 'initial.txt'

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def add(self, element):
        heappush(self.heap,element)

    def getMax(self):
        return self.heap[0]
    
    def deleteMax(self):
        x = heappop(self.heap)
        return x
    
    def getHeap(self):
        return self.heap

    def isEmpty(self):
        return True if len(self.heap) ==0 else False

class JsonHelper:
    def json_decode(self, input):
        pass
    def json_encode(self, input):
        pass
    def _isValidJson(self, input):
        try:
            json_object = json.loads(input)
        except ValueError as e:
            return False
        return True

class FileHelper:
    def __init__(self, file_name):
        self.file_name = file_name
    def readFile(self):
        content = []
        with open(self.file_name, 'r') as reader:
            content.append(reader.read())
        res = ''
        if content is not None and len(content) > 0:
            res = json.loads(content[0])
        return res

def read_file(file_name):
    content = []
    with open(file_name, 'r') as reader:
        content.append(reader.read())
    res = ''
    if content is not None and len(content) > 0:
        res = json.loads(content[0])
    return res

def write_file(file_name, content):
    content = json.dumps(content)
    with open(file_name, 'w') as writer:
        writer.write(content)




if __name__ == "__main__":
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))
    if len(sys.argv) < 2:
        print('\nNo arguments passed!! Please add some arguments\n')
        print('1. Reset the load balancer to change the load balancer configuration')
        print('     $ LoadBalancing.py reset')
        print('2. Initililze or run the load balancer')
        print('     $ LoadBalancing.py X:1 Y:3')
    else:
        arguments = sys.argv
        if 'reset' == arguments[1]:
            write_file(INITIAL_FILE_PATH, [])
            write_file(SERVER_FILE_PATH,[])
        else:
            max_heap = MaxHeap()
            load_balancer_details = None
            if path.exists(SERVER_FILE_PATH):
                load_balancer_details = read_file(SERVER_FILE_PATH)
            if load_balancer_details is None: # file is created for the first time
                server_data = arguments[1:]
                for curr in server_data:
                    x, y = curr.split(':')
                    max_heap.add([-int(y), x])
                write_file(INITIAL_FILE_PATH, max_heap.getHeap())
                write_file(SERVER_FILE_PATH, max_heap.getHeap())
            elif len(load_balancer_details) == 0: # server.txt goes empty
                server_data = read_file(INITIAL_FILE_PATH)
                for curr in server_data:
                    x, y = curr.split(':')
                    max_heap.add([-int(y), x])
                write_file(SERVER_FILE_PATH, max_heap.getHeap())
            else: 
                server_data = read_file(SERVER_FILE_PATH)
                print(server_data)
                for curr in server_data:
                    x, y = curr
                    max_heap.add([-int(x), y])
                x, y = max_heap.deleteMax()
                print(y)
                x+=1
                if x > 0:
                    max_heap.add([x,y])
                write_file(SERVER_FILE_PATH,max_heap.getHeap())