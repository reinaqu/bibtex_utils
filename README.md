# bibtex_utils
Python scripts to operate with BibTeX files

# Dependencies
* bibtexparser (https://bibtexparser.readthedocs.io/en/master/).
You can install the library with pip as follows:

<code>pip install bibtexparser</code>

# Utilities

1. **bibdiff**. This script removes from database1 (first parameter) the entities the databases included as (second parameter).

--- Use:

--- <code>bibdiff -min bibtex1 -sub bibtex2 ... -o bibtexresult </code>

--- Example:

--- <code>bibdiff -min acm.bib -sub acm1.bib -o output.bib</code>

2. **bibmerge**. This script merges all the BibTeX files given as parameters. The BibTex file obtained as a result has no duplicated entries.

--- Use:

--- <code>merge -bib bibtex1 bibtex2 ... -o bibtexresult </code>

--- Example:

--- <code>merge -bib acm1.bib acm2.bib ... -o output.bib</code>

