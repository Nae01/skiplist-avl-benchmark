import time
import random
from skiplist import SkipList
from avl import AVLTree, AVLNode

N = 100000  

# ------------------ Skip List ------------------
skiplist = SkipList()
t1 = time.time()

for i in range(N):
    skiplist.insert(random.randint(1, 1000000))

for i in range(N):
    skiplist.search(random.randint(1, 1000000))

t2 = time.time()
skip_time = t2 - t1


# ------------------ AVL Tree ------------------
avl = AVLTree()
root = None

t1 = time.time()

for i in range(N):
    root = avl.insert(root, random.randint(1, 1000000))

for i in range(N):
    avl.search(root, random.randint(1, 1000000))

t2 = time.time()
avl_time = t2 - t1


# ------------------ Resultados ------------------
print("===== RESULTADOS DEL BENCHMARK =====")
print(f"Skip List tiempo total: {skip_time:.4f} segundos")
print(f"AVL Tree tiempo total: {avl_time:.4f} segundos")

if skip_time < avl_time:
    print("\n→ La Skip List fue más rápida en esta prueba.")
else:
    print("\n→ El Árbol AVL fue más rápido en esta prueba.")
