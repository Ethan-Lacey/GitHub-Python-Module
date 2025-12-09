import sys
import argparse
from blacklist.functions import blockHost, removeHost, getHostPath

def commandLine():
    hostsPath = getHostPath()


    parser= argparse.ArgumentParser(
        description="Blackholing Utility for blocking suspicious hosts."
    )

    subparsers = parser.add_subparsers(dest="command", required=True, help="What do you want to do?")
    
    blockParser = subparsers.add_parser("block", help="Block a Fully Qualified Domain Name")
    blockParser.add_argument("FQDN", type=str, help="Enter the Fully Qualified Domain Name you wish to block.")

    unblockParser = subparsers.add_parser("unblock", help="Unblock a Fully Qualified Domain Name")
    unblockParser.add_argument("FQDN", type=str, help="Enter the Fully Qualified Domain Name you wish to unblock.")

    args = parser.parse_args()

    try:
        if args.command == "block":
            blockHost(args.FQDN, hostsPath)
            print("The host has been successfully blocked")
        
        elif args.command == "unblock":
            removeHost(args.FQDN, hostsPath)
            print("The Host has been succesfully unblocked")
    
    except (FileNotFoundError) as error:
        print(f"Error: {error}", file=sys.stderr)
        SystemExit(1)
        
if __name__ == "__main__":
    commandLine()