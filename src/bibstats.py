# -*- coding: utf-8 -*-
"""
The result is a set of statistics about the file given as a parameter.

A. M. Reina Quintero <reinaqu@us.es>

"""
import argparse
from bibtexparser.bibdatabase import BibDatabase
import bibtexparser
from bibtexparser.bparser import BibTexParser
import os.path
from bibutils import *
import logging

import logging

def main():

    logging.basicConfig(level=logging.INFO)
    args = parse_arg()
            
    db = load_bibtex(args.bib[0])
    print("Stats for ", args.bib[0])
    print_database_stats(db)
 

def parse_arg():
    parser = argparse.ArgumentParser(prog='bibstats', description='Some statistics about the bibtex is printed on console')
    parser.add_argument('-bib', nargs=1, type=str)
    return parser.parse_args()


if __name__ == "__main__":
    main()