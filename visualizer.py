import matplotlib.pyplot as plt

from analyzer import ps_counter, summry_times


def plot():
    processes = ps_counter()

    top_processes = sorted(
        processes.items(),
        key=lambda item: item[1],
        reverse=True
    )[:10]

    names = [process[0] for process in top_processes]
    counts = [process[1] for process in top_processes]

    plt.figure(figsize=(10, 6))
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



def plot_time():
    times = summry_times()

    labels = []
    counts = []

    for time_range, count in times.items():
        start, finish = time_range

        labels.append(f"{start:02d}:00-{finish:02d}:00")
        counts.append(count)

    plt.figure(figsize=(10, 6))

    bars = plt.bar(labels, counts)

    plt.xlabel("Time")
    plt.ylabel("Occurrences")
    plt.title("System Activity by Hour")

    plt.xticks(rotation=45)

    for bar, count in zip(bars, counts):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            str(count),
            ha="center",
            va="bottom"
        )

    plt.tight_layout()
    plt.show()