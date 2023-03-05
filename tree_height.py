# python3 221RDB438

import sys
import threading
import numpy

counted=[]

def node_height(array, index, height):
    if array[index]==-1:
        counted[index]=1
        return 1
    elif counted[array[index]]==0:
        counted[array[index]]=node_height(array, array[index], height)
    counted[index]=counted[array[index]]+1
    return counted[index]

def compute_height(array,number):
    # Write this function
    # Your code here
    max_height=0
    for index in range(number):
        height=node_height(array, index, 1)
        if height>max_height:
            max_height=height
    return max_height


def main():
    # implement input form keyboard and from files
    userInput=input("")
    if "I" in userInput.capitalize():
    #     # input from keyboard
        number = int(input(""))
        line=input().split(" ")
        array = [0 for i in range(len(line))]
        for index in range(len(line)):
            array[index] = int(line[index])
    else:
        # input from file
        try:
            with open("test/"+input()) as file:
                number = int(file.readline())
                line=file.readline().split(" ")
                array = [0 for i in range(len(line))]
                for index in range(len(line)):
                    array[index] = int(line[index])
        except:
            print("JOJO")
            return
    #print(array)
    for index in range(len(array)):
        counted.append(0)
    print(compute_height(array, number))
     
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