import argparse
from models import Attraction
# from context import Config

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("commands", nargs="+")
    args = parser.parse_args()
    route(args.commands)

def route(commands):
    action = commands[0]
    if action == "waittime":
        print Attraction.get(commands)
    else:
        print "INVALID COMMAND"

def args(commands):
    if len(commands) > 1:
        return commands[1:]
    else:
        return []

if __name__ == "__main__":
    main()