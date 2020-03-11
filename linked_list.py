class Node:
    def __init__(self, name=None, mobile=None):
        self.name = name
        self.mobile = mobile
        self.next_node = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    # 링크드 리스트에 노드를 추가하는 함수
    def add_node(self, name, mobile):
        pass

    # 링크드 리스트 프린트 함수
    def print_linked_list(self):
        printval = self.head
        while printval is not None:
            print("name=", end=""), print (printval.name)
            print("mobile=", end=""), print (printval.mobile)
            printval = printval.next_node

    # Function to remove node
    def remove_node(self, Removekey):
        pass

    def find_by_name(self, name):
        pass
