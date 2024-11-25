import argparse

# parse command line arguments
parser = argparse.ArgumentParser(description="A script that says hi to someone")
parser.add_argument("name", type=str, help="Name of the person you want to say hi to")
parser.add_argument(
    "--shout", default=False, action="store_true", help="Use this flag to shout"
)
args = parser.parse_args()

# print message
print(args.shout)
text = "Hi " + args.name + "!"
if args.shout:
    text = text.upper()
print(text)
