import numpy as np
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
    for i in range(num,17):
        blocking_list.append(messages[i][1])
    block = float(max(blocking_list))
    # print(block)

    LHS = block
    Q = block
    RHS = 0
    while (1<2):
        RHS = 0
        for i in range(0,num):
            RHS += np.ceil((Q+tau)/float(messages[i][2]))*float(messages[i][1])
            print(RHS)    
        RHS += block
        print(RHS)
        if LHS == RHS:
            break
        LHS = RHS
        Q = RHS
    return RHS+float(messages[num][1])

if __name__  == "__main__":
    with open('output.txt', 'w', newline='') as f:
        for i in range(17): 
            f.writelines(str(worstwaitingtime(i))+'\n')
     