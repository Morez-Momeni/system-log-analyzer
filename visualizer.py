import matplotlib.pyplot as plt

from analyzer import ps_counter

processes = ps_counter()

top_processes = sorted(
    processes.items(),
    key=lambda item: item[1],
    reverse=True
)[:10]

names = [process[0] for process in top_processes]
counts = [process[1] for process in top_processes]

plt.figure(figsize=(10, 6))
def plot():
    bars = plt.barh(names, counts)

    plt.xlabel("Occurrences")
    plt.ylabel("Process")
    plt.title("Top 10 Most Frequent Processes")

    plt.gca().invert_yaxis()

    for bar, count in zip(bars, counts):
        plt.text(
            bar.get_width(),
            bar.get_y() + bar.get_height() / 2,
            f" {count}",
            va="center"
        )

    plt.tight_layout()
    plt.show()