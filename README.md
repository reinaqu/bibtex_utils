# bibtex_utils
Python scripts to operate with BibTeX files

# Dependencies
* bibtexparser (https://bibtexparser.readthedocs.io/en/master/).
You can install the library with pip as follows:

<code>pip install bibtexparser</code>

# Utilities

1. **bibdiff**. This script removes from database1 (first parameter) the entities the databases included as (second parameter).

	Use:

	<code>bibdiff -min bibtex1 -sub bibtex2 ... -o bibtexresult </code>

	Example:

	<code>bibdiff -min acm.bib -sub acm1.bib -o output.bib</code>

2. **bibmerge**. This script merges all the BibTeX files given as parameters. The BibTex file obtained as a result has no duplicated entries.

	Use:

	<code>bibmerge -bib bibtex1 bibtex2 ... -o bibtexresult </code>

	Example:

	<code>bibmerge -bib acm1.bib acm2.bib ... -o output.bib</code>

  
3. **bibstats**. This script prints a set of statistics about the BibTeX file given as a parameter. 

	Use:

	<code>bibstats -bib bibtex</code>

	Example:
	
	<code>bibstat -bib acm2.bib</code>
  
	The previous example prints the following statistics:
  
	<code>Stats for  ../data/acm2.bib
	Number of entries: 61
	Entries per type: Counter({'inproceedings': 54, 'article': 7})</code>