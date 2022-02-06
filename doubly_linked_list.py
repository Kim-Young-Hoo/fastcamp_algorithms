"""
양방향 탐색이 가능한 링크드리스트
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class NodeMGMT:

    def __init__(self, head):
        if not head:
            raise Exception("no head")

        self.head = head
        self.tail = None
        self.length = 1

    def add(self, node_to_add, index):
        """
        python list의 .insert 메소드랑 동일
        :param node_to_add:
        :param index:
        :return:
        """

        if index == 0:
            node_to_add.next = self.head
            self.head.previous = node_to_add
            self.head = node_to_add

        elif index == -1 or index >= self.length:
            node_current = self.head
            while node_current.next:
                node_current = node_current.next
            node_current.next = node_to_add
            node_to_add.previous = node_current
            self.tail = node_to_add

        else:
            node_current = self.head

            for i in range(index):
                node_current = node_current.next

            node_to_add.previous = node_current.previous
            node_to_add.next = node_current
            node_current.previous.next = node_to_add
            node_current.previous = node_to_add

        self.length += 1

    def desc(self, forward=True):
        node_values = []
        if forward:
            node_current = self.head
            while node_current.next:
                node_values.append(node_current.value)
                node_current = node_current.next
            node_values.append(node_current.value)
        else:
            node_current = self.tail
            while node_current.previous:
                node_values.append(node_current.value)
                node_current = node_current.previous
            node_values.append(node_current.value)
        print(node_values)

    def delete(self, index):
        """
        python list remove랑 동일하게
        index가 length/2 기준보다 높으면 역방향
         낮으면 정방향으로
        :param index:
        :return:
        """

        if index <= self.length // 2:
            node_current = self.head
            for i in range(index):
                node_current = node_current.next

            node_current.previous.next = node_current.next
            node_current.next.previous = node_current.previous

        else:
            node_current = self.tail
            for i in range(index):
                node_current = node_current.previous

            node_current.previous.next = node_current.next
            node_current.next.previous = node_current.previous


node_mgmt = NodeMGMT(head=Node(13))
node_mgmt.add(Node(3), 0)
node_mgmt.desc()

node_mgmt.add(Node(4), -1)
node_mgmt.desc()

node_mgmt.add(Node(5), 2)
node_mgmt.desc()

# node_mgmt.desc(forward=False)

node_mgmt.delete(index=2)
node_mgmt.desc()
