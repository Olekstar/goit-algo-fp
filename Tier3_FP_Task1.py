class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_merge(self, other):
        result = LinkedList()
        current1 = self.head
        current2 = other.head

        while current1 and current2:
            if current1.data < current2.data:
                result.append(current1.data)
                current1 = current1.next
            else:
                result.append(current2.data)
                current2 = current2.next

        while current1:
            result.append(current1.data)
            current1 = current1.next

        while current2:
            result.append(current2.data)
            current2 = current2.next

        return result

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Приклад використання:
if __name__ == "__main__":
    # Створення списку 1
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)
    list1.append(7)

    # Створення списку 2
    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)
    list2.append(8)

    print("Перший список:")
    list1.print_list()

    print("\nДругий список:")
    list2.print_list()

    # Злиття відсортованих списків
    merged_list = list1.sorted_merge(list2)
    print("\nЗлитий список:")
    merged_list.print_list()

    # Реверс списку
    merged_list.reverse()
    print("\nРеверсований злитий список:")
    merged_list.print_list()
