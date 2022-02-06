class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.pointer = next_node


class NodeMGMT:

    def __init__(self, head):
        self.head = head

    def add(self, node_to_add):
        node = self.head
        while node.pointer:
            node = node.pointer

        node.pointer = node_to_add

    def delete(self, node_value_to_delete):

        if self.head.value == None:
            print("no nodes")
            return

        node_current = self.head
        node_before = None
        while node_current.pointer:
            if node_current.value == node_value_to_delete and node_current == self.head:
                self.head = self.head.pointer
                return

            elif node_current.value == node_value_to_delete and node_current != self.head:
                node_before.pointer = node_current.pointer
                return
            node_before = node_current
            node_current = node_current.pointer

        if node_current.value == node_value_to_delete:
            node_before.pointer = None
        print("no value matched")

    def desc(self):
        node_values = []
        node = self.head
        while node.pointer:
            node_values.append(node.value)
            node = node.pointer
        node_values.append(node.value)
        print(node_values)


node1 = Node(13)
node2 = Node(165)
node3 = Node(123)

node1.pointer = node2
node2.pointer = node3

node_mgmt = NodeMGMT(head=node1)
node_mgmt.add(Node(3))
node_mgmt.add(Node(4))

node_mgmt.desc()

node_mgmt.delete(4)
node_mgmt.desc()

# def add_new_node(value, node):
#     while node.pointer:
#         node = node.pointer
#
#     node.pointer = Node(value)
#
#
# for i in range(3):
#     add_new_node(i, node1)
#
# node = node1
# while node.pointer:
#     print(node.value)
#     node = node.pointer
