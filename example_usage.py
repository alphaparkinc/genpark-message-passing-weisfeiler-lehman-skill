from client import WeisfeilerLehmanGraph

def main():
    print("=== Testing 1-WL Graph Color Refinement ===")
    # Star graph: node 0 connected to nodes 1 and 2
    adj = {0: [1, 2], 1: [0], 2: [0]}
    wl = WeisfeilerLehmanGraph(adj)

    refined = wl.iterate()
    print("1-WL Refined node colors:", refined)

    # Hub node 0 must have different color from peripheral nodes
    assert refined[0] != refined[1]
    # Peripheral nodes 1 and 2 must share identical color
    assert refined[1] == refined[2]
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
