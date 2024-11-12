#!/usr/bin/env python
import argparse
from init import init


def main():
    parser = argparse.ArgumentParser(description="Hydrazine CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Initialize command
    init_parser = subparsers.add_parser('init', help="Initialize a new project")

    args = parser.parse_args()

    if args.command == 'init':
        print("Initializing new project...")
        try:
            # Call the init function directly
            result = init()

            if result:
                print("Project initialized successfully.")
            else:
                print("Initialization cancelled.")
        except Exception as e:
            print(f"Error during initialization: {str(e)}")

    elif args.command:
        print(f"Unknown command: {args.command}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()