def dfs(v, adj_list, visited):

    visited[v] = True
    for neighbor in adj_list[v]:
        if not visited[neighbor]:
            dfs(neighbor, adj_list, visited)

def is_connected(n_vertices, n_edges, edges, start_vertex):

    # Inicializa a lista de adjacência
    adj_list = {i: [] for i in range(1, n_vertices + 1)}
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)  # Como o grafo é não direcionado
    
    # Inicializa a lista de vértices visitados
    visited = [False] * (n_vertices + 1)  # Índices de 1 a n_vertices
    
    # Executa DFS a partir do vértice inicial
    dfs(start_vertex, adj_list, visited)
    
    # Verifica se todos os vértices foram visitados
    for vertex in range(1, n_vertices + 1):
        if not visited[vertex]:
            return False
    return True

def main():
    print("Verificação de Conectividade de um Grafo usando DFS")
    
    # Entrada do número de vértices
    while True:
        try:
            n_vertices = int(input("Digite o número de vértices: "))
            if n_vertices <= 0:
                print("O número de vértices deve ser positivo.")
                continue
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
    
    # Entrada do número de arestas
    while True:
        try:
            n_edges = int(input("Digite o número de arestas: "))
            if n_edges < 0:
                print("O número de arestas não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
    
    # Entrada das arestas
    edges = []
    print(f"Digite as {n_edges} arestas no formato 'u v' (vértices separados por espaço):")
    for i in range(n_edges):
        while True:
            try:
                edge_input = input(f"Aresta {i+1}: ").strip()
                u, v = map(int, edge_input.split())
                if u < 1 or u > n_vertices or v < 1 or v > n_vertices:
                    print(f"Os vértices devem estar entre 1 e {n_vertices}.")
                    continue
                edges.append((u, v))
                break
            except ValueError:
                print("Formato inválido. Por favor, insira dois números inteiros separados por espaço.")
    
    # Entrada do vértice inicial
    while True:
        try:
            start_vertex = int(input(f"Digite o vértice inicial (1 a {n_vertices}): "))
            if start_vertex < 1 or start_vertex > n_vertices:
                print(f"O vértice inicial deve estar entre 1 e {n_vertices}.")
                continue
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
    
    # Verificação de conectividade
    if is_connected(n_vertices, n_edges, edges, start_vertex):
        print("O grafo é CONEXO.")
    else:
        print("O grafo NÃO é conexo.")

if __name__ == "__main__":
    main()
