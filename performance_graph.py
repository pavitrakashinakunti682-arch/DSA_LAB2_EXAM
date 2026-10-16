
import os
import matplotlib.pyplot as plt

# Save graphs inside the graphs folder
base = os.path.dirname(os.path.abspath(__file__))
graph_folder = os.path.join(base, "graphs")
os.makedirs(graph_folder, exist_ok=True)

# Six dataset sizes
sizes = [1000, 5000, 10000, 50000, 100000, 500000]
positions = [1, 2, 3, 4, 5, 6]

# Example values only — replace with actual measured timings
dictionary_time = [0.001, 0.004, 0.008, 0.035, 0.070, 0.350]
bst_time = [0.002, 0.010, 0.025, 0.150, 0.350, 2.000]
trie_time = [0.003, 0.012, 0.020, 0.100, 0.200, 1.000]

# Additional timing values (example values only)
dictionary_build = [0.001, 0.003, 0.006, 0.025, 0.050, 0.250]
bst_build = [0.002, 0.008, 0.020, 0.120, 0.280, 1.500]
trie_build = [0.002, 0.009, 0.015, 0.070, 0.150, 0.750]

dictionary_search = [0.0005, 0.001, 0.002, 0.008, 0.015, 0.080]
bst_search = [0.001, 0.002, 0.004, 0.020, 0.050, 0.300]
trie_search = [0.001, 0.002, 0.003, 0.015, 0.030, 0.150]

dictionary_print = [0.001, 0.002, 0.004, 0.015, 0.030, 0.150]
bst_print = [0.001, 0.004, 0.008, 0.030, 0.070, 0.400]
trie_print = [0.001, 0.003, 0.006, 0.025, 0.050, 0.250]

dictionary_total = [
    dictionary_build[i] + dictionary_search[i] + dictionary_print[i]
    for i in range(6)
]
bst_total = [
    bst_build[i] + bst_search[i] + bst_print[i]
    for i in range(6)
]
trie_total = [
    trie_build[i] + trie_search[i] + trie_print[i]
    for i in range(6)
]


def make_graph(name, data, filename):
    plt.figure(figsize=(10, 5))

    for label, times in data.items():
        plt.plot(positions, times, marker="o", label=label)

    plt.xticks(
        positions,
        ["1,000", "5,000", "10,000",
         "50,000", "100,000", "500,000"]
    )

    plt.xlabel("Dataset Size (Words)")
    plt.ylabel("Execution Time (Seconds)")
    plt.title(name + " Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    path = os.path.join(graph_folder, filename)
    plt.savefig(path, dpi=150)
    plt.close()

    print("Saved:", path)


# 1. Overall indexing time
make_graph(
    "Overall Indexing",
    {
        "Dictionary": dictionary_time,
        "BST": bst_time,
        "Trie": trie_time
    },
    "dictionary_graph.png"
)

# 2. BST graph
make_graph(
    "BST",
    {"BST": bst_time},
    "bst_graph.png"
)

# 3. Trie graph
make_graph(
    "Trie",
    {"Trie": trie_time},
    "trie_graph.png"
)

# 4. Build time graph
make_graph(
    "Build Time",
    {
        "Dictionary": dictionary_build,
        "BST": bst_build,
        "Trie": trie_build
    },
    "build_time.png"
)

# 5. Search time graph
make_graph(
    "Search Time",
    {
        "Dictionary": dictionary_search,
        "BST": bst_search,
        "Trie": trie_search
    },
    "search_time.png"
)

# 6. Printing time graph
make_graph(
    "Printing Time",
    {
        "Dictionary": dictionary_print,
        "BST": bst_print,
        "Trie": trie_print
    },
    "printing_time.png"
)

# 7. Total time graph
make_graph(
    "Total Time",
    {
        "Dictionary": dictionary_total,
        "BST": bst_total,
        "Trie": trie_total
    },
    "total_time.png"
)

print("\nAll 7 graphs created successfully!")
print("Check the graphs folder inside DSA_Project.")
