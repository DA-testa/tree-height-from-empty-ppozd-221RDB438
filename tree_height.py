# python3 221RDB438

import sys
import threading
import numpy

c=[]

def node_h(ar, i, h):
    if ar[i]==-1:
        c[i]=1
        return 1
    elif c[ar[i]]==0:
        c[ar[i]]=node_h(ar, ar[i], h)
    c[i]=c[ar[i]]+1
    return c[i]

def compute_h(ar,n):
    # Write this function
    # Your code here
    max_h=0
    for i in range(n):
        h=node_h(ar, i, 1)
        if h>max_h:
            max_h=h
    return max_h


def main():
    # implement input form keyboard and from files
    Input=input("")
    if "I" in Input.capitalize():
    #     # input from keyboard
        n = int(input(""))
        ln=input().split(" ")
        ar = [0 for i in range(len(ln))]
        for i in range(len(ln)):
            ar[i] = int(ln[i])
    else:
        # input from file
        try:
            with open("test/"+input()) as file:
                n = int(file.readline())
                ln=file.readline().split(" ")
                ar = [0 for i in range(len(ln))]
                for i in range(len(ln)):
                    ar[i] = int(ln[i])
        except:
            print("JOJO")
            return
    #print(array)
    for index in range(len(ar)):
        c.append(0)
    print(compute_h(ar, n))
     
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    #print(compute_height([4, -1, 4, 1, 1],1))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))