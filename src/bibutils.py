# -*- coding: utf-8 -*-
'''
Created on 27 may. 2020

@author: reinaqu_2
'''
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bparser import BibTexParser
import bibtexparser
import os.path
import sys

def load_bibtex(filename):
    
    if not (os.path.isfile(filename)):
        print("input file not found"+ filename, file=sys.stderr)
        exit(0)
        
    parser = BibTexParser(common_strings=True) 
    with open(filename,encoding='utf-8') as bibtex_file:
        database = bibtexparser.load(bibtex_file, parser)
    return database 

def load_bibtexs(filenames):
    ''' Get a sequence of filenames and returns a list of databases one for each filename.
        If any of the files do not exists, the process finishes.
    '''
    return [load_bibtex(filename) for filename in filenames]

def write_bibtex(db, filename):
    '''
    Writes the database into the file named filename
    '''
    with open(filename, 'w', encoding='utf-8') as bibtex_file:
        bibtexparser.dump(db, bibtex_file)

def writes_bibtex(db):
    '''
    Returns a string with the bibtex of the entries contained in the database
    '''
    return bibtexparser.dumps(db)

def merge_dbs (db_list):
    res = BibDatabase()
    for db in db_list:
        for entry in db.entries:
            res.entries.append(entry)       
    return res

def subtract_dbs(db_min, list_dbs_sub):
    """
    The result of the operation is db_min -  union (db_sub_list).
    The result is the db_min without the references included in the list_dbs_sub databases 
    """
    db_subs = merge_dbs(list_dbs_sub)
    db = BibDatabase()
    for entry in db_min.entries:
        if not contains(entry, db_subs):
            db.entries.append(entry)
    return db


def contains(entry, database):
    """
    check if entry exits in the database, based on its ID
    """
    for ent in database.entries:
        if entry['ID'] == ent['ID']:
            return True
    return False

