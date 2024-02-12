class IntNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def set_next(self, next_node):
        self.next = next_node


def count_number(first, num):
    count = 0
    current = first

    while current is not None:
        if current.get_value() == num:
            count += 1
        current = current.get_next()

    return count


def avg(first):
    total_sum = 0
    count = 0
    current = first

    while current is not None:
        total_sum += current.get_value()
        count += 1
        current = current.get_next()

    if count == 0:
        return 0  # Avoid division by zero
    else:
        return total_sum / count


def max_index(first):
    if first is None:
        return -1  # Return -1 if the linked list is empty

    max_value = first.value
    max_index = 0
    current_index = 0
    current = first

    while current is not None:
        if current.value > max_value:
            max_value = current.value
            max_index = current_index
        current = current.next
        current_index += 1

    return max_index


first_node = None
for i in range(4, 0, -1):
    temp_node = IntNode(i, first_node)
    first_node = temp_node


def first_index_num(first, num):
    current = first
    index = 0

    while current is not None:
        if current.value == num:
            return index
        current = current.next
        index += 1

    return -1  # Return -1 if the number is not found in the list


def last_index_num(first, num):
    current = first
    last_index = -1
    index = 0

    while current is not None:
        if current.value == num:
            last_index = index
        current = current.next
        index += 1

    return last_index


num_to_count = 2
result = count_number(first_node, num_to_count)
print(f"The number {num_to_count} appears {result} times in the linked list.")
print(avg(first_node))
print(max_index(first_node))
print(first_index_num(first_node, 3))  # Output: 1 (index of the first occurrence of 1)
print(last_index_num(first_node, 2))
