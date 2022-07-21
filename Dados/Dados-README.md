- The journals that served as source for this data collection are avaible in [this link.](https://prorum.com/?qa=7313/quais-sao-fontes-mais-importantes-papers-machine-learning)
- Web of Science is a software for collecting databases on publications in many different areas. This service is provided by the University of Brasilia but it's 
website was blocked for my usual chrome driver. A selenium controlled Chrome driver was able access the website without restrictions. 
The *open_webofscience.py* file opens this Chrome Driver.
- Web of Science has a maximum of 1000 data points for each individual download, so all the data needed is located in the *journals-partial* directory and the code *merge_database*
merges all of them into the *journals.csv* file.
