class Node:
    """Represents a single node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Manages the singly linked list."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Appends a node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Appended {data} as the head node.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Appended {data} to the end of the list.")

    def print_list(self):
        """Prints all elements in the list."""
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Deletes the nth node (1-based index) from the list."""
        try:
            if not self.head:
                raise Exception("Cannot delete from an empty list.")

            if n <= 0:
                raise IndexError("Index should be a positive integer.")

            if n == 1:
                deleted_data = self.head.data
                self.head = self.head.next
                print(f"Deleted node {n} (value: {deleted_data})")
                return

            current = self.head
            count = 1

            while current and count < n - 1:
                current = current.next
                count += 1

            if not current or not current.next:
                raise IndexError("Index out of range.")

            deleted_data = current.next.data
            current.next = current.next.next
            print(f"Deleted node {n} (value: {deleted_data})")

        except Exception as e:
            print(f"Error: {e}")


# -------------------------------
# Sample usage / test case
# -------------------------------
if __name__ == "__main__":
    ll = LinkedList()

    # Add sample data
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)

    # Print current list
    ll.print_list()

    # Delete 3rd node
    ll.delete_nth_node(3)
    ll.print_list()

    # Attempt to delete node out of range
    ll.delete_nth_node(10)

    # Delete first node
    ll.delete_nth_node(1)
    ll.print_list()

    # Delete remaining nodes
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)

    # Try deleting from empty list
    ll.delete_nth_node(1)
