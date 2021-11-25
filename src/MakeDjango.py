#!/usr/bin/env python
import argparse
import os

from core.processor import Main

__version__: str = "0.0.0"

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="Make Django",
        description="Quick creation of Django project template",
        epilog="Good Luck...",
    )
    
    # optional arguments:
    parser.add_argument("-v", "--version", action="store_true", help="dst version")
    # positional arguments:
    parser.add_argument("name", nargs="?", help="project name")
    parser.add_argument("framework", nargs="?", choices=("rest", "graphql", "django"), help="select your framework")
    parser.add_argument("appnames", nargs="*", help="app names create apps")
    # modes:
    modes = parser.add_mutually_exclusive_group(required=False)
    modes.add_argument("-a", "--auto", action="store_true", help="Auto Template")
    modes.add_argument("-c", "--custom", action="store_true", help="Custom Template")
    # other:
    other = parser.add_argument_group(title="other options:")
    other.add_argument("-p", "--path", nargs=1, default=os.getcwd(), help="project directory path")

    args = parser.parse_args()

    if not vars(args)["version"]:
        Main(parser, **vars(args))
    else:
        print(f"MakeDjango Version: {__version__}")

if __name__ == "__main__":
    main()
