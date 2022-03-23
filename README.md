# bibtex_utils
Python scripts to operate with BibTeX files

# Dependencies
* bibtexparser (https://bibtexparser.readthedocs.io/en/master/).
You can install the library with pip as follows:

<code>pip install bibtexparser</code>

# Utilities

1. **bibdiff**. This script removes from database1 (first parameter) the entities the databases included as second parameter. If no -field is provided, the substraction is made by the id field of the bibtext. If the field is provided, then the substraction is made according to this field.

	Use:

	<code>bibdiff -min bibtex1 -sub bibtex2 ... -field fieldname -o bibtexresult </code>

	Examples:

	<code>bibdiff -min acm.bib -sub acm1.bib -o output.bib</code>
	<code>bibdiff -min acm.bib -sub acm1.bib acm2.bib-o output.bib</code>
	<code>bibdiff -min scopus.bib -sub scopus1.bib -field "url" -o output.bib</code>
	

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
  
	
	```
	Stats for  acm2.bib
	Number of entries: 61
	Entries per type: Counter({'inproceedings': 54, 'article': 7})
	```