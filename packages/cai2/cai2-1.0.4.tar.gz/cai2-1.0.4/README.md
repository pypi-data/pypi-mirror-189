### cai2 - Codon Adaptation Index

[![DOI](https://joss.theoj.org/papers/10.21105/joss.00905/status.svg)](https://doi.org/10.21105/joss.00905) [![docs](https://readthedocs.org/projects/cai/badge/?version=latest)](https://cai.readthedocs.io/en/latest/) [![PyPI version](https://badge.fury.io/py/cai2.svg)](https://badge.fury.io/py/cai2)

An implementation of [Sharp and Li's 1987 formulation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC340524/pdf/nar00247-0410.pdf)

of the [codon adaption index](https://en.wikipedia.org/wiki/Codon_Adaptation_Index).

This is an update of [cai](https://pypi.org/project/CAI) providing the same functionality, but now works with all python 3 versions. This version also has more tests, some derived from the Sharp and Li 1987 paper above.  

This module can be installed with the following command:

	
	$ pip install cai2

Use:

Finding the CAI of a sequence is easy:

    from cai2 import CAI
    CAI("ATG...", reference=["ATGTTT...", "ATGCGC...",...])
    0.24948128951724224

Determining which sequences to use as the reference set is left to the user, though the [HEG-DB](http://genomes.urv.cat/HEG-DB/) is a great resource of highly expressed genes.

Citation

---

  

Lee, B. D. (2018). Python Implementation of Codon Adaptation Index.

*Journal of Open Source Software, 3* (30), 905.

[<https://doi.org/10.21105/joss.00905>](https://doi.org/10.21105/joss.00905)

:

  

@article{Lee2018,

doi = {10.21105/joss.00905},

url = {https://doi.org/10.21105/joss.00905},

year = {2018},

month = {oct},

publisher = {The Open Journal},

volume = {3},

number = {30},

pages = {905},

author = {Benjamin D. Lee},

title = {Python Implementation of Codon Adaptation Index},

journal = {Journal of Open Source Software}

---
The original creator was [<benjamin_lee@college.harvard.edu>](mailto:benjamin_lee@college.harvard.edu).  This version was created by Björn Johansson as it is needed for optional functionality for [pydna](https://pypi.org/project/pydna).  

Reference

---------

 Sharp, P. M., & Li, W. H. (1987). The codon adaptation index--a measure
of directional synonymous codon usage bias, and its potential
applications. *Nucleic Acids Research*, 15(3), 1281–1295.