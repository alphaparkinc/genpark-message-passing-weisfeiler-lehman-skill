class WeisfeilerLehmanGraph:
    """
    1-Weisfeiler-Lehman (1-WL) Graph Isomorphism / Expressivity Color Refinement.
    Aggregates sorted multiset of neighbor colors to iteratively refine node embeddings.
    """
    def __init__(self, adj_list):
        self.adj = adj_list
        self.colors = {u: "0" for u in adj_list}

    def iterate(self):
        new_colors = {}
        for u in self.adj:
            neighbor_colors = sorted([self.colors[v] for v in self.adj[u]])
            signature = f"{self.colors[u]}|{','.join(neighbor_colors)}"
            new_colors[u] = str(hash(signature) % 10000)
        self.colors = new_colors
        return self.colors
