class node:
    # link is also called pointer
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

class linked_list:
    def __init__(self):
        self.head = None

    # function that adds a node at front
    def add_at_front(self, data):
        self.head = node(data=data, link=self.head)

    # function to check whether the list is empty
    def is_empty(self):
        return self.head == None

    # function to add node at end
    def add_at_end(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.link:
            curr = curr.link
        curr.link = node(data=data)

    # function to delete any node
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.link
        if prev is None:
            self.head = curr.link
        elif curr:
            prev.link = curr.link
            curr.link = None

    # function to get the last node
    def get_last_node(self):
        temp = self.head
        while temp.link:
            temp = temp.link
        return temp.data

    # function to print the list nodes
    def print_list(self):
        node = self.head
        while node != None:
            print(node.data, end=">>")
            node = node.link


