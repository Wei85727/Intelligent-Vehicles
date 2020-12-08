import numpy as np

edges = []
with open('input2.dat', 'r', encoding='UTF-8') as file:
    vertex_num = float(file.readline())
    edge_num = float(file.readline())
    for data in file.readlines():
        data = data.strip()
        data = data.split()
        edges.append(data)
for i in range(len(edges)):
    edges[i][0] = int(edges[i][0])
    edges[i][1] = int(edges[i][1])
# edges = [[0,1],[2,3],[2,4],[6,7]]
a = edges.index([1,3])
print(edges[284],edges[94])
# while (True and a != 100):
#     a+=1
#     print(a)
# a.remove(a[1])
# print(a)