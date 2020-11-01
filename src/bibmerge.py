# -*- coding: utf-8 -*-
"""
The result is a BibTeX file that includes all the entries included in
the BibTeX files given with the -bib parameter. The result has not duplicated entries.
A. M. Reina Quintero <reinaqu@us.es>

"""
import argparse
from bibtexparser.bibdatabase import BibDatabase
import bibtexparser
from bibutils import *
import logging

def main():

    logging.basicConfig(level=logging.INFO)
    args = parse_arg()
    databases = load_bibtexs(args.bib)
    result = merge_dbs(databases)
    entries = result.get_entry_list()
    logging.info("Number of entries in the resulting bibtex..."+ str(len(entries)) )
    if args.output:
        write_bibtex(result, args.output)
    else:
        print(writes_bibtex(result))


def parse_arg():
    parser = argparse.ArgumentParser(prog='bibmerge', description='The result is a bibtex with the merge of all the bibtex')
    parser.add_argument('-bib', nargs='+', type=str)
    parser.add_argument('-o', '--output', nargs='?', help='file')
    return parser.parse_args()


if __name__ == "__main__":
    main()