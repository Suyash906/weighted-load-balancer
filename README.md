# weighted-load-balancer

### Programming Language
- Python(version 3.7.3)

### Problem approach
- MaxHeap has been used to save the server name and its capacity. It is ordered on the basis of capacity.
- To make the MaxHeap persistent, a text file has been used to save its state after each request.
- For each request the following operations are performed - 
    - Pop the max entry from MaxHeap.
    - Output the sever name on console and also save it in result.txt file.
    - Reduce the capacity and save it in server.txt if the capacity is above 0.
- An additional file initial.txt has been used to save the initial state of the server. After the all the elements are popped out from the MaxHeap the initial state of the load balancer is restored with the help of this file. This gives a cyclic nature to the load balancer

### Steps to run test cases
- Clear the previous configuration to run a new test case
```
    python LoadBalancing.py reset
```
- Initililze or run the load balancer
```
    python LoadBalancing.py X:1 Y:2 Z:3
```

### Output Screenshot