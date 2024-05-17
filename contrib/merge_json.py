#!/usr/bin/python3

import argparse
import json
import os
import sys


def main():
    parser = argparse.ArgumentParser(os.path.basename(sys.argv[0]))
    parser.add_argument(
        "--delete", default="", help="Remove keys from json, comma separated"
    )
    parser.add_argument("--output", required=True, help="Write output to file")
    parser.add_argument("input", nargs="+", help="Chrome extension key")
    args = parser.parse_args()

    output = {}
    for file in args.input:
        with open(file, "r") as fp:
            data = json.load(fp)
            for key in args.delete.split(","):
                if key in data:
                    del data[key]

            output = {**output, **data}

    with open(args.output, "w") as fp:
        json.dump(output, fp, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
