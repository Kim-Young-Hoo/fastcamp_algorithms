"""
Binary Search Tree - Linked List로 구현하기
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class BinarySearchTree:

    def __init__(self, root):
        self.root = root

    def add_node(self, node):
        current_node = self.root

        while True:
            if node.value > current_node.value:

                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = node
                    break

            elif node.value < current_node.value:

                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = node
                    break

    def search(self, value):
        """
        해당 value가 트리 내에 있는지 탐색
        :param value: 찾고자 하는 value
        :return: boolean
        """
        current_node = self.root

        while True:
            if current_node.value == value:
                return True

            else:
                if current_node.value < value:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        return False
                elif current_node.value > value:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        return False

    def delete_node(self, value):
        """
        value 해당하는 값을 담고 있는 노드를 삭제
        :param value: 삭제하고자 하는 value
        :return: True/False
        """

        parent_node = None
        current_node = self.root

        while True:
            if current_node.value == value:

                """
                0. 루트를 삭제하는 경우 (고려하지 말자)
                    1)삭제할 노드의 오른쪽 자식 중 가장 작은 값이 루트가 됨
                    2)삭제할 노드의 왼쪽 자식 중 가장 큰 값이 루트가 됨
                1. 삭제할 노드의 자식이 1개일 경우
                    1) 삭제할 노드의 자식을 부모 노드가 가리키도록
                2. 삭제할 노드의 자식이 2개일 경우
                    1)삭제할 노드의 오른쪽 자식 중 가장 작은 값을 부모 노드가 가리키도록
                    2)삭제할 노드의 왼쪽 자식 중 가장 큰 값을 부모 노드가 가리키도록
                3. 삭제할 노드가 없을 경우
                    1) False를 리턴
                4. 삭제할 노드의 자식이 없을 경우
                    1) 그냥 삭제해
                """

                # 1번 케이스
                if not current_node.left and current_node.right:
                    parent_node.right = current_node.right
                    return True
                elif not current_node.right and current_node.left:
                    parent_node.left = current_node.left

                # 2번 케이스
                if current_node.right and current_node.left:
                    temp_node = current_node.right
                    while temp_node.left.left:
                        temp_node = temp_node.left
                    replace_node = temp_node.left
                    temp_node.left = None

                    replace_node.left = current_node.left
                    replace_node.right = current_node.right

                    if parent_node.left and parent_node.left.value == value:
                        parent_node.left = replace_node
                        return True
                    elif parent_node.right and parent_node.right.value == value:
                        parent_node.right = replace_node
                        return True

                # 4번 케이스
                if not current_node.left and not current_node.right:
                    if parent_node.left and parent_node.left.value == value:
                        parent_node.left = None
                        return True
                    elif parent_node.right and parent_node.right.value == value:
                        parent_node.right = None
                        return True


            else:
                if current_node.value < value:
                    if current_node.right:
                        parent_node = current_node
                        current_node = current_node.right
                    else:
                        return False
                elif current_node.value > value:
                    if current_node.left:
                        parent_node = current_node
                        current_node = current_node.left
                    else:
                        return False




root_node = Node(10)
bst = BinarySearchTree(root_node)

"""
        10
    8       15
               17
             22  23
                21 25
                  24  
"""
bst.add_node(Node(15))
bst.add_node(Node(17))
bst.add_node(Node(8))
bst.add_node(Node(23))
bst.add_node(Node(22))
bst.add_node(Node(21))
bst.add_node(Node(25))
bst.add_node(Node(24))


print(bst.search(15)) # True
print(bst.search(22)) # True
print(bst.search(50)) # False

print(bst.delete_node(23)) # True
print(bst.search(23))  # False
print(bst.search(24))  # True
print(bst.search(25))  # True

print(bst.delete_node(8)) # True
print(bst.search(8)) # False



