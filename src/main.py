#!/usr/bin/env python
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(
        prog="Django smithing tools",
        description="Quick creation of Django project template",
        epilog="Good Luck...",
    )
    parser.add_argument("-a", "--auto", metavar=None)
    parser.add_argument("-sp", "--startproject", metavar="sp", type=str, help="Custom Template", choices=("rest", "jinja", "graphql"))

    args = parser.parse_args()
    print(args.sp)

if __name__ == "__main__":
    main()