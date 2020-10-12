class Node:
    """
    Node class to hold next and previous items in the doubly linked
    circular list.
    """

    def __init__(self, data):
        """
        Create the node.
        Inlcudes reference to node in front and behind current node.
        :param data: data to be held in the list. Can be anything.
        """
        self.next = None  # Next and previous hold node objects.
        self.previous = None
        self.data = data

    def get_next(self):
        """
        Get next item
        :return: The next node.
        """
        return self.next

    def get_previous(self):
        """
        Get item behind current one, for the first item in the list, this
        will reference the node at the end of the list.
        :return: previous node
        """
        return self.previous

    def get_data(self):
        """
        :return: Data inside of node
        """
        return self.data

    def set_next(self, node):
        """
        Set the next item in the list.
        :return: None
        """
        self.next = node

    def set_previous(self, node):
        """
        Set previous Node.
        :param node: new previous node
        :return: None
        """
        self.previous = node

    def __str__(self):
        a_str = '' + str(self.get_data())
        return a_str


class DLCList:
    """
    Doubly linked circular list
    Uses nodes to keep track of the next items in the list.
    """

    def __init__(self):
        """
        Create a new empty DLCList
        """
        self.first = None
        self.last = None
        self.size = 0

    def is_empty(self):
        """
        Check if list is empty
        :return: Boolean true if list is empty.
        """
        empty = False
        if self.size == 0:
            empty = True
        return empty

    def set_last(self, node):
        """
        Set the last node to the new last node.
        :param node: Node to set as last
        """
        self.last = node

    def get_last(self):
        """
        :return: last item in the list
        """
        return self.last

    def get_first(self):
        """
        :return: first item in the list
        """
        return self.first

    def get_size(self):
        """
        :return: size of list
        """
        return self.size

    def set_first(self, node):
        """
        Set the first node to a new first node
        :param node: The new node at the front of the list.
        """
        self.first = node

    def append(self, data):
        """
        Append a piece of data to back of the list.
        :param data: any object the user would like to store in their list.
        :return: None
        """
        new_node = Node(data)
        if self.get_size() == 0:
            self.first = new_node
            self.last = new_node
        else:
            new_node.set_previous(self.get_last())
            new_node.set_next(self.get_first())
            self.first.set_previous(new_node)
            self.last.set_next(new_node)
            self.set_last(new_node)
        self.size += 1

    def remove(self, data):
        """
        remove specific data from a list.
        :param data: Data to remove from the list.
        :return: Error if data doesn't exist in the list.
        """
        found = False
        current = self.first

        while not found:  # Find Node
            if current.get_data() == data:
                found = True
            else:
                if current != self.get_last():
                    current = current.get_next()
                else:  # Break the loop if the data is not in the list
                    raise Exception("Data is not in the list.")

        if current == self.first:  # Need to reassign our list's first instance variable
            self.first.get_next().set_previous(self.last)
            self.last.set_next(self.first.get_next())
            self.first = self.first.get_next()
        elif current == self.last:  # Need to reassign our list's last instance variable
            self.get_last().get_previous().set_next(self.get_first())
            self.get_first().set_previous(self.get_last().get_previous())
            self.set_last(self.get_last().get_previous())
        else:
            current.get_next().set_previous(current.get_previous())
            current.get_previous().set_next(current.get_next())

        self.size -= 1

    def pop(self):
        """
        Remove data at the end of the list.
        :return: Data stored in the node at the end of the list
        """
        tmp = self.get_last().get_data()
        self.get_last().get_previous().set_next(self.get_first())
        self.get_first().set_previous(self.get_last().get_previous())
        self.set_last(self.get_last().get_previous())
        self.size -= 1
        return tmp


    def get_index(self, item):
        """
        Returns the index of specified data
        :param item: Item to get the index of
        :return: int: index of the item.
        """
        current = self.get_first()
        item_index = 0
        found = False

        while not found and self.get_size() > 0:  # Only loop through the list if there are items in it.
            if current.get_data() == item:
                found = True
            else:
                if current.get_next() == self.get_first():  # we have reached the end of the list with no match.
                    raise Exception("Item is not in the list.")
                else:
                    current = current.get_next()
                    item_index += 1

        return item_index

    def get_at_index(self, index):
        """
        return the data at the specified index
        :param index: index you want to get value from
        :return: The node at specified index
        """
        if index == 0:  # Return the first item in the list
            return self.get_first()

        elif index <= self.get_size():
            current = self.get_first()
            for i in range(0, index):
                current = current.get_next()
            return current

        else:
            raise Exception("Index is out of bounds")

    def insert(self, pos, item):
        """
        insert an item at specified index.
        :param pos: index to insert item at, will raise exception if out of bounds.
        :param item: Item to insert into the list
        """
        current = self.get_at_index(pos)
        new_node = Node(item)
        new_node.set_next(current)
        new_node.set_previous(current.get_previous())
        current.get_previous().set_next(new_node)
        current.set_previous(new_node)

        self.size += 1

    def __str__(self):
        list_string = ["["]
        tmp = self.get_first()
        end_of_list = False

        while not end_of_list:
            if tmp.get_next() != self.get_first():  # if there is another item in list add a ,
                list_string.append(str(tmp.get_data()))
                list_string.append(", ")
                tmp = tmp.get_next()
            else:
                list_string.append(str(tmp.get_data()))
                end_of_list = True

        list_string.append(']')
        return ''.join(list_string)


def main():
    my_ll = DLCList()
    my_ll.append("hi")
    my_ll.append("hey")
    my_ll.append('hello')
    my_ll.append('whatsup')
    my_ll.append('hows it goin')
    print(my_ll)
    print(my_ll.insert(2, 'konnichiwa'))
    print(my_ll)
    print(my_ll.pop())
    print(my_ll)
    print(my_ll.get_at_index(2))
    my_ll.remove('konnichiwa')
    print(my_ll)


if __name__ == '__main__':
    main()
