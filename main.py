import argparse
from datacollector import collect_logs
from analyzer import statistics
from visualizer import plot

parser = argparse.ArgumentParser()

parser.add_argument("--collog" , action="store_true")
parser.add_argument("--sholog" , action="store_true")
parser.add_argument("--plot" , action="store_true")
args = parser.parse_args()


if args.collog:

    print("collecting logs from system...")
    collect_logs()
    print("Done")

if args.sholog:
    statistics()


if args.plot:
    plot()