"""
Árvore Binária de Busca (BST): reconstrução a partir da pré-ordem
e impressão do percurso em pós-ordem.

Entrada: um número inteiro por linha, na ordem de um percurso em pré-ordem
(linha em branco ou fim do arquivo encerra a leitura).
Saída: os mesmos valores no percurso em pós-ordem.

Uso:
    python 05_arvore_binaria_busca.py < entrada.txt
    python 05_arvore_binaria_busca.py          # sem entrada, roda o exemplo
"""
import sys


class Node:
    def __init__(self, element):
        self.element = element
        self.parent = None
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self): return self._size
    def is_empty(self): return self._size == 0
    def root(self): return self._root
    def parent(self, node): return node.parent

    def left_child(self, node): return node.left_child
    def right_child(self, node): return node.right_child

    def is_root(self, node): return self._root == node
    def is_leaf(self, node): return node.left_child is None and node.right_child is None

    def insert_leftchild(self, parent, element):
        new_node = Node(element)
        if self.is_empty():
            self._root = new_node
        else:
            new_node.parent = parent
            parent.left_child = new_node
        self._size += 1
        return new_node

    def insert_rightchild(self, parent, element):
        new_node = Node(element)
        if self.is_empty():
            self._root = new_node
        else:
            new_node.parent = parent
            parent.right_child = new_node
        self._size += 1
        return new_node

    def pre_order(self, node):
        if node is None:
            return
        print(node.element)
        self.pre_order(node.left_child)
        self.pre_order(node.right_child)

    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left_child)
        self.post_order(node.right_child)
        print(node.element)


def bst_insert(tree, root, value):
    """Insere mantendo a propriedade da BST: menores à esquerda, maiores à direita."""
    if value < root.element:
        if root.left_child is None:
            return tree.insert_leftchild(root, value)
        return bst_insert(tree, root.left_child, value)
    if root.right_child is None:
        return tree.insert_rightchild(root, value)
    return bst_insert(tree, root.right_child, value)


def build_from_preorder(values):
    """O primeiro valor da pré-ordem é sempre a raiz; os demais são inseridos na BST."""
    tree = BinaryTree()
    root = None
    for v in values:
        if root is None:
            root = tree.insert_leftchild(None, v)
        else:
            bst_insert(tree, root, v)
    return tree


def read_values():
    values = []
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        values.append(int(line))
    return values


if __name__ == "__main__":
    values = read_values() if not sys.stdin.isatty() else []
    if not values:
        values = [50, 30, 24, 5, 28, 45, 98, 52, 60]  # exemplo
        print("Pré-ordem (exemplo):", values)
        print("Pós-ordem:")
    tree = build_from_preorder(values)
    tree.post_order(tree.root())
