#!/usr/bin/env python
import argparse
from init.init import init
from compile import compile

def main():
    parser = argparse.ArgumentParser(description="Hydrazine CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Initialize command
    init_parser = subparsers.add_parser('init', help="Initialize a new project")

    # Compile command
    compile_parser = subparsers.add_parser('compile', help="Compile the project")

    args = parser.parse_args()

    # Initialization
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

    # Compilation
    elif args.command == 'compile':
        print("Compiling Project Files")
        try:
            result = compile()

            if result:
                print("Project compiled successfully.")
            else:
                print("Compilation terminated.")
        except Exception as e:
            print(f"Error during compilation: {str(e)}")

    elif args.command:
        print(f"Unknown command: {args.command}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()