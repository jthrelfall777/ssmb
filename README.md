# Scatter Search Algorithm for Markov Blanket Attribute Selectionand Classification

**A scatter search algorithm to produce a probabilistic graphical model using python and pgmpy. All datasets used can be found at the UCI machine learning repository, link; [https://archive.ics.uci.edu/ml/datasets.php](https://archive.ics.uci.edu/ml/datasets.php)
All jupyter notebooks are grouped into dataset folders, these folders form the workspace to run the jupyter notebooks on the datasets and save transformed data and models into these folders with the datasets.**


## Notebooks
**Each folder contains these three notebooks**

 - discretisation-process.ipynb
 - scatter-search.ipynb
 - multi-model-v2.ipynb
 
## Datasets

**Datasets need to be downloaded into each folder for which they belong. The raw dataset in the folder will be transformed by discretisation-process.ipynb notebook. Once this process has taken place a second dataset will be present in the folder called <dataset-name>-discretized.csv All training will take place on the discretized dataset.**

## Running the notebooks
**The run order of the notebooks is as follows;**

 1. discretisation-process.ipynb
 2. scatter-search.ipynb
 3. multi-model-v2.ipynb

discretisation-process.ipynb - This notebook processes the dataset ready for the machine learning algorithms. A link to download the datasets from UCI can be found in each notebook.

scatter-search.ipynb - This notebook runs the scatter search and reports on the results.

multi-model-v2.ipynb - This notebook runs the benchmarking machine learning methods.
    