class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, x: Node):
        x.prev = None
        x.next = self.head
        if self.head is None:
            self.tail = x
        else:
            self.head.prev = x
        self.head = x

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


def test_insert_into_empty_list():
    dll = DoublyLinkedList()
    node = Node("A")
    dll.insert_at_head(node)

    assert dll.head is node, "Head должен указывать на вставленный узел"
    assert dll.tail is node, "Tail должен совпадать с head в однодальном списке"
    assert node.prev is None, "prev нового узла должен быть None"
    assert node.next is None, "next нового узла должен быть None"


def test_multiple_inserts_order_and_links():
    dll = DoublyLinkedList()
    # вставляем C, затем B, затем A
    nodes = [Node(k) for k in ["C", "B", "A"]]
    for n in nodes:
        dll.insert_at_head(n)

    # Проверяем последовательность ключей: A, B, C
    keys = [node.key for node in dll]
    assert keys == ["A", "B", "C"]

    # Проверяем связи prev/next между ними
    a, b, c = nodes[::-1]  # после вставок head=A, потом B, C
    assert dll.head is a
    assert dll.tail is c

    assert a.prev is None
    assert a.next is b

    assert b.prev is a
    assert b.next is c

    assert c.prev is b
    assert c.next is None


def test_head_updates_on_each_insert():
    dll = DoublyLinkedList()
    first = Node(1)
    second = Node(2)

    dll.insert_at_head(first)
    old_head = dll.head

    dll.insert_at_head(second)
    assert dll.head is second
    assert second.next is old_head
    assert old_head.prev is second
