# -*- coding: utf-8 -*-
"""
The result is the first database, removing the entities existing in the second database, based on his IDs
This script removes from database1 (first parameter) the entities in database2 (second parameter)

José Miguel Pérez-Álvarez <josemi@us.es>
A. M. Reina Quintero <reinaqu@us.es>

"""
import argparse
from bibtexparser.bibdatabase import BibDatabase
import bibtexparser
from bibtexparser.bparser import BibTexParser
import os.path
from bibutils import *
import logging

def main():

    logging.basicConfig(level=logging.INFO)
    args = parse_arg()
    
    min_database = load_bibtex(args.min[0])
    logging.info(f"Number of entries in the min database bibtex...{num_entries(min_database)}")
    sub_databases = load_bibtexs(args.sub)   
    for i in range (len(sub_databases)):
        logging.info(f"Number of entries in the sub {i+1} database bibtex...{num_entries(sub_databases[i])}" )
     
    if args.field:
        field = args.field
    else:
        field = 'ID'
   
    result = subtract_dbs_by_field(min_database, sub_databases, field)
    entries = result.get_entry_list()
    logging.info("Number of entries in the resulting bibtex..."+ str(len(entries)) )
    
    if args.output:
        write_bibtex(result, args.output)
    else:
        print(writes_bibtex(result))


def parse_arg():
    parser = argparse.ArgumentParser(prog='bibdiffids', description='The result is the first database, removing the '
                                                                 'references existing in the list of databases'
                                                                 'enumerated in the sub param')
    parser.add_argument('-min', nargs=1, type=str)
    parser.add_argument('-sub', nargs='+', type=str)
    parser.add_argument('-field', nargs='?')
    parser.add_argument('-o', '--output', nargs='?', help='file')
    return parser.parse_args()


if __name__ == "__main__":
    main()