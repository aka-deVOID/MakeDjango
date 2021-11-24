#!/usr/bin/env python
import argparse
import os
import sys

from core.portal import Main

__version__ = "0.0.0"

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="Django smithing tools",
        description="Quick creation of Django project template",
        epilog="Good Luck...",
    )
    
    # optional arguments:
    parser.add_argument("--version", action="store_true")
    # positional arguments:
    parser.add_argument("path", nargs="?", default=os.getcwd(), help="project directory path")
    # modes
    starter = parser.add_argument_group(title="mode", description="Template making modes")
    starter.add_argument("-a", "--auto", action="store_true", help="Auto Template")
    starter.add_argument("-c", "--custom", action="store_true", help="Custom Template")

    Main(**vars(parser.parse_args()))

if __name__ == "__main__":
    main()