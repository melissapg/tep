from collections import deque, defaultdict


def topological_sort(n, adj_list, in_degree):
    # Inicialize a fila com todos os nós que têm grau de entrada 0
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Se o número de nós no resultado não é n, então há um ciclo no grafo
    if len(result) != n:
        return []  # Indica que não é possível encontrar uma ordenação topológica
    return result


def main():
    while True:
        line = input().strip()
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break

        # Inicialize o grafo
        adj_list = defaultdict(list)
        in_degree = [0] * (n + 1)

        for _ in range(m):
            i, j = map(int, input().strip().split())
            adj_list[i].append(j)
            in_degree[j] += 1

        # Obtenha a ordenação topológica
        order = topological_sort(n, adj_list, in_degree)
        if order:
            print(" ".join(map(str, order)))
        else:
            print("No valid order")


if __name__ == "__main__":
    main()
