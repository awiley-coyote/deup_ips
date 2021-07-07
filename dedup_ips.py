import argparse as ap
import re

#initializes the parser so that the prgram can accept command line arguments
parser = ap.ArgumentParser(description="Insert descrption here")
parser.add_argument("-f", help="File(s) to be combined and deduped", action="append")
parser.add_argument("--dedup_output", help="File for the deduped ips to be output")
args = parser.parse_args()
#intialize the ips set. Since sets don't allow duplicates, having a set will automatically dedup the set
ips = set()
#create a regex to check each line. Since we don't have to validate the ips, we can use a simple regex
pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
#goes through each file to be deduped and pulls out the IPs
for f in args.f:
    with open(f) as filename:
        for line in filename:
            if(re.search(pattern, line)):
                ips.add(line.strip())

