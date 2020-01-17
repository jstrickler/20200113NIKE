#!/usr/bin/env python
import fileinput
import sys
import argparse
import re
import logging

logging.basicConfig(filename="fauxgrep.log", level=logging.DEBUG)

logging.info("Starting program")

parser = argparse.ArgumentParser(description="Faux grep")

parser.add_argument("-v", dest="invert", action="store_true",
                    help="print NON-matching lines")

parser.add_argument("-i", dest="ignorecase", action="store_true",
                    help="ignore case")

parser.add_argument("-n", dest="showname", action="store_true",
                    help="display file name")

parser.add_argument('searchterm', help="term to find" )

parser.add_argument('files', nargs='*', help="files to search")


args = parser.parse_args()

if args.ignorecase:
    flag = re.IGNORECASE
else:
    flag = 0

logging.debug(f"flag is {flag}")
logging.debug(f"search term is {args.searchterm}")


for raw_line in fileinput.input(args.files):
    if re.search(args.searchterm, raw_line, flag):
        line = raw_line.rstrip()
        if args.showname:
            print(fileinput.filename(), end=' ')
        print(line)


logging.info("Program finished")
