import numpy as np
import networkx as nx

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
# edges[284] = [3, 0]
# edges[94]  = [1, 3]

edge_start_vertex = []
remove_list = []
empty = []

# while(edges != []):
#     edge_start_vertex = []
#     for i in range(len(edges)):
#         edge_start_vertex.append(edges[i][0])
#     s = edges[0][1]
#     v = edges[0][0]
#     while(s in edge_start_vertex): 
#         # print(len(edge_start_vertex),len(edges))
#         idx = edge_start_vertex.index(s)
#         s = edges[idx][1]
#         if s == v :
#             print("cycle!")  
#             print(edges[0])  
#             break        
#         edges.remove(edges[idx])
#         edge_start_vertex.remove(edge_start_vertex[idx]) 
#     edges.remove(edges[0])    
# def cycle():
#     for i in range(len(edges)):
#         edge_start_vertex.append(edges[i][0])
#     for i in range(len(edges)):
#         v_s = [edges[i][0]]
#         s = edges[i][1]
#         a = 0
#         b = [[v_s, s]]
#         c = 0
#         while (s in edge_start_vertex and c != 1024):
#             idx = edge_start_vertex.index(s)
#             b.append(edges[idx])
#             s = edges[idx][1]
#             v_s.append(edges[idx][0])    
#             if s in v_s:
#                 print("there is a cycle")
#                 print("起點為:", edges[i])
#                 print(b)
#                 remove_list.append(edges[i])
#                 edges.remove(edges[i])
#                 break
#         if remove_list != []:
#             break
#     return remove_list

# print(edges.index([0,1])) 
# print(edges.index([1,3])) 
# print(edges.index([3,0])) 
# print(edges.index([0,2])) 
# print(edges.index([2,3])) 

# edges.remove([2,3])
# edges.remove([0,2])
# edges.remove([3,0])
G = nx.DiGraph(edges)
num_of_cycle = 0
for cycle in nx.simple_cycles(G):
    print(cycle)
    num_of_cycle += 1
print("總共有", num_of_cycle, "個cycle")    
  

# print(vertex_num, edge_num, edges)

# if __name__=='__main__':
#     result = [1]
#     remove_edge = []
#     while(result != []):
#         result = cycle()
#         remove_edge.append(result)
#     print("remove", result_edge, "edge可以使graph acyclic")    