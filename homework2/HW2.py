# from HW1 import worstwaitingtime
# from HW1 import total
import time
import numpy as np
import random
import math

messages = []
with open('input.dat', 'r', encoding='UTF-8') as file:
    numbers = float(file.readline())
    tau = float(file.readline())
    for data in file.readlines():
        data = data.strip()
        data = data.split()
        messages.append(data)
# print(numbers, tau, messages) 

def worstwaitingtime(number):
    num = number
    blocking_list = []
    for element in messages:
        if int(element[0]) >= int(messages[num][0]): 
            blocking_list.append(element[1])
    block = float(max(blocking_list))
    # print(block)

    LHS = block
    Q = block
    RHS = 0
    while True:
        RHS = 0
        
        for i in range(0,int(messages[num][0])):
            a = 0
            for element in messages:
                if int(element[0]) == i:
                    break
                a += 1   
            RHS += np.ceil((Q+tau)/float(messages[a][2]))*float(messages[a][1])
            # print(RHS)    
        RHS += block
        # print(RHS)
        if LHS == RHS:
            break
        LHS = RHS
        Q = RHS
    return RHS+float(messages[num][1])

def total():
    obj = 0
    for i in range(17):
        a = worstwaitingtime(i)
        if a > float(messages[i][2]): 
            obj += 1000  # penality of breaking restrictions
        obj += a    
    return(obj)

if __name__  == "__main__":
    start = time.time()
    T = 100 # initial temp
    S = total() # initial solution
    output = []
    for i in range(17):
        output.append(messages[i][0]) 
    threshold = 0.01 # 機率的臨界值
    a = 0
    while(T>0.01):
        s1 = random.randint(0,16) # pick a random nieghbor
        s2 = random.randint(0,16)
        messages[s1][0],messages[s2][0] = messages[s2][0],messages[s1][0] # 交換priority
        cost = total()
        # if cost <= S:
        if cost <= S or math.exp((S-cost)/T) > threshold:
            S = cost
            output = []
            for i in range(17):
                output.append(messages[i][0]) # 保留最佳解時的priority分配
        T *= 0.999 # r=0.999
        a += 1
    print("跑了", a, "輪", " 最終objective value為:", S, " message_0的priority為:", output[0], " message_1的priority為:", output[1], " message_2的priority為:", output[2])

    with open('output1.txt', 'w', newline='') as f:
        for i in range(17): 
            f.writelines(str(output[i])+'\n')
    with open('output2.txt', 'w', newline='') as f: 
        f.write(str(S))
    end = time.time()
    
    print("runtime:", end-start, "secs")           