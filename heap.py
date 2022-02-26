"""
데이터에서 최대값, 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리
완전이진트리 : 노드 삽입 시 최하단 왼쪽부터 차례대로 삽입

최대힙과 최소힙이 있음
최대힙 : root = max
최소힙 : root = min
"""


# class Node:
#
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# class MaxHeap:
#
#     def __init__(self, root):
#         # root == max
#         self.root = root
#
#     def insert(self, node):
#         """
#         :param node:
#         :return:
#         """
#
#         parent_node = None
#         current_node = self.root
#
#         # 1번 규칙
#         while True:
#
#             if current_node.left and not current_node.right:
#                 current_node.right = node
#                 break
#
#             elif not current_node.left and not current_node.right:
#                 current_node.left = node
#                 break
#
#             elif current_node.left and current_node.right:
#                 current_node = current_node.left



"""

1. 무조건 완전이진트리의 형태로 집어넣는다
2. 집어넣고 난 다음에 부모>자식 규칙을 어기는지를 판단하여 swap을 진행한다

구현 시 배열을 사용하는 게 일반적임
indexing을 통해서 자식 노드의 위치를 알아내는 방법

자기 index가 현재 n이면
left child = n*2
right child = n*2+1 
parent = n//2

생각의 단순화를 위해서 0번째 index는 비워두는 게 보통임
"""




class Heap:

    def __init__(self, root):
        self.heap_array = [None, root]

    def insert(self, value):

        # 1번 규칙
        self.heap_array.append(value)

        # 2번 규칙
        current_node_index = len(self.heap_array) - 1

        while True:
            # 부모보다 크면 swap
            if current_node_index//2 > 0:
                if self.heap_array[current_node_index] > self.heap_array[current_node_index//2]:
                    self.heap_array[current_node_index//2], self.heap_array[current_node_index] = self.heap_array[current_node_index], self.heap_array[current_node_index//2]
                    current_node_index = current_node_index//2
                else:
                    break
            else:
                break
        return True



heap = Heap(15)
heap.insert(5)
heap.insert(6)
heap.insert(7)
heap.insert(1)
heap.insert(9)
heap.insert(16)
heap.insert(32)
heap.insert(19)
heap.insert(5999)
heap.insert(8)


print(heap.heap_array)














