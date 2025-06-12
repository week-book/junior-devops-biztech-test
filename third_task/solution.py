import re


class Node:
    def __init__(self, label):
        self.label = label
        self.children = []

    def __repr__(self):
        return f"Node({self.label!r}, children={self.children})"


def tokenize(s):
    return re.findall(r"\(|\)|[^\s()]+", s)


def parse_nodes(tokens):
    nodes = []
    while tokens and tokens[0] != ")":
        label = tokens.pop(0)
        node = Node(label)
        if tokens and tokens[0] == "(":
            tokens.pop(0)
            node.children = parse_nodes(tokens)
            if tokens and tokens[0] == ")":
                tokens.pop(0)
        nodes.append(node)
    return nodes


def parse(s):
    tokens = tokenize(s)
    if tokens and tokens[0] == "(":
        tokens.pop(0)
        roots = parse_nodes(tokens)
        if tokens and tokens[0] == ")":
            tokens.pop(0)
        return roots[0] if len(roots) == 1 else Node("root", children=roots)
    else:
        return Node(s)


def print_tree(node, prefix="", parent_last=True):
    # всегда используем именно эти 4 символа для "линии" под узел
    connector = "---+"
    # печать текущего узла
    print(f"{prefix}{node.label}{connector if node.children else ''}")

    # длина зоны, на которую надо "съехать" детям:
    indent_zone = len(node.label) + len(connector) - 1
    for idx, child in enumerate(node.children):
        is_last = idx == len(node.children) - 1

        if prefix == "":
            # для первого уровня (дети корня) просто отступ = ширина родителя
            next_prefix = " " * indent_zone
        else:
            if parent_last:
                # если мы были последним ребёнком у родителя — просто пробелы
                next_prefix = prefix + " " * indent_zone
            else:
                # иначе — вертикальная линия на месте первого символа,
                # потом пробелы до следующей зоны
                next_prefix = prefix + "|" + " " * (indent_zone - 1)

        print_tree(child, next_prefix, is_last)


if __name__ == "__main__":
    s = input("Введите дерево в скобках: ").strip()
    root = parse(s)
    print_tree(root)
