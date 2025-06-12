class Node:
    def __init__(self, key, data=None):
        self.key = key  # ключ или полезная нагрузка
        self.data = data  # дополнительные данные (по желанию)
        self.prev = None  # ссылка на предыдущий узел
        self.next = None  # ссылка на следующий узел


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # указатель на голову списка
        self.tail = None  # (опционально) указатель на хвост списка

    def insert_at_head(self, x: Node):
        """
        Вставка узла x в начало списка.
        Если список пуст — x станет и головой, и хвостом.
        """
        x.prev = None
        x.next = self.head
        if self.head is None:
            # список был пуст
            self.tail = x
        else:
            # старой голове теперь предшествует x
            self.head.prev = x
        # x становится новой головой списка
        self.head = x

    def __iter__(self):
        # удобный итератор по ключам для проверки содержимого
        node = self.head
        while node:
            yield node.key
            node = node.next


# --- пример использования ---
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Вставим три элемента в голову
    for key in ["C", "B", "A"]:
        node = Node(key)
        dll.insert_at_head(node)

    # Проверим порядок: должно быть A, B, C
    print(list(dll))  # ['A', 'B', 'C']
