# bibtex_utils
Python scripts to operate with BibTeX files

# Dependencies
* bibtexparser (https://bibtexparser.readthedocs.io/en/master/).
You can install the library with pip as follows:

<code>pip install bibtexparser</code>

# Utilities

1. bibdiff. This script removes from database1 (first parameter) the entities the databases included as (second parameter).

Use:

<code>bibdiff -min bibtex1 -sub bibtex2 ... -o bibtexresult </code>

Example:

<code>bibdiff -min acm.bib -sub acm1.bib -o acmres.bib</code>
