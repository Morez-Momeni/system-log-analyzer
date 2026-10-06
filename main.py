import argparse

from datacollector import collect_logs
from analyzer import statistics, special_log, top_ps, tail_ps
from visualizer import (
    plot,
    plot_time,
    plot_session_status,
    plot_sessions_per_user,
    plot_failed_auth
)


parser = argparse.ArgumentParser()


parser.add_argument("--collog", action="store_true")
parser.add_argument("--sholog", action="store_true")
parser.add_argument("--plot", action="store_true")
parser.add_argument("--timeplot", action="store_true")

parser.add_argument("--sessionplot", action="store_true")
parser.add_argument("--userplot", action="store_true")
parser.add_argument("--authplot", action="store_true")

parser.add_argument("--slog")
parser.add_argument("--top", type=int)
parser.add_argument("--tail", type=int)


args = parser.parse_args()


if args.collog:

    print("collecting logs from system...")
    collect_logs()
    print("Done")


if args.sholog:

    statistics()


if args.plot:

    plot()


if args.timeplot:

    plot_time()


if args.sessionplot:

    plot_session_status()


if args.userplot:

    plot_sessions_per_user()


if args.authplot:

    plot_failed_auth()


if args.slog:

    special_log(args.slog)


if args.top:

    top_ps(args.top)


if args.tail:

    tail_ps(args.tail)

