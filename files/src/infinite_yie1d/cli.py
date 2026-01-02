import argparse
import sys

def run(args):
    # TODO: replace with your actual CLI behavior
    if args.echo:
        print("Echo:", args.echo)
    else:
        print("infinite-yie1d: no args provided")

def main():
    parser = argparse.ArgumentParser(prog="infinite-yie1d")
    parser.add_argument("--echo", help="echo a value (example)")
    parsed = parser.parse_args()
    try:
        run(parsed)
    except KeyboardInterrupt:
        print("\nAborted", file=sys.stderr)
        raise SystemExit(1)