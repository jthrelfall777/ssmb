#!/bin/bash
MULTI_MODEL_NOTEBOOK="multi-model-v5.ipynb"
SCATTER_SEARCH_NOTEBOOK="scatter-search-v5.ipynb"
RUNS="acute-inflammations-diagnosis"
cd $RUNS
echo "Running $RUNS"
echo "Notebook multi model running....."
jupyter nbconvert --to notebook --execute $MULTI_MODEL_NOTEBOOK #--output "multi-model-v5-result.ipynb"
echo "Notebook scatter search running....."
jupyter nbconvert --to notebook --execute $SCATTER_SEARCH_NOTEBOOK
cd ..
#######################################################################################################
RUNS="breast-cancer"
cd $RUNS
echo "Running $RUNS"
echo "Notebook multi model running....."
jupyter nbconvert --to notebook --execute $MULTI_MODEL_NOTEBOOK #--output "multi-model-v5-result.ipynb"
echo "Notebook scatter search running....."
jupyter nbconvert --to notebook --execute $SCATTER_SEARCH_NOTEBOOK
cd ..
#######################################################################################################
RUNS="breast-cancer-wisconsin"
cd $RUNS
echo "Running $RUNS"
echo "Notebook multi model running....."
jupyter nbconvert --to notebook --execute $MULTI_MODEL_NOTEBOOK
echo "Notebook scatter search running....."
jupyter nbconvert --to notebook --execute $SCATTER_SEARCH_NOTEBOOK
#######################################################################################################
RUNS="cryotherapy"
cd $RUNS
echo "Running $RUNS"
echo "Notebook multi model running....."
jupyter nbconvert --to notebook --execute $MULTI_MODEL_NOTEBOOK
echo "Notebook scatter search running....."
jupyter nbconvert --to notebook --execute $SCATTER_SEARCH_NOTEBOOK
#######################################################################################################
RUNS="fertility_Diagnosis"
cd $RUNS
echo "Running $RUNS"
echo "Notebook multi model running....."
jupyter nbconvert --to notebook --execute $MULTI_MODEL_NOTEBOOK
echo "Notebook scatter search running....."
jupyter nbconvert --to notebook --execute $SCATTER_SEARCH_NOTEBOOK
#######################################################################################################
RUNS="parkinsons"
cd $RUNS
echo "Running $RUNS"
echo "Notebook multi model running....."
jupyter nbconvert --to notebook --execute $MULTI_MODEL_NOTEBOOK
echo "Notebook scatter search running....."
jupyter nbconvert --to notebook --execute $SCATTER_SEARCH_NOTEBOOK
