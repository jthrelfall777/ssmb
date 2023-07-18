import sys
import logging
import unittest
import pandas as pd
from datetime import datetime
from results import Experiment_Results

class Test_Experiment_Results(unittest.TestCase):
    def setUp(self):
        self.er = Experiment_Results()
        self.r1 = {'dt': datetime.now(), 'experiment_name': "test1", 'graph': 1, 'runtime': 0.078, 'samples': 43, \
                   'folds': 2, 'accuracy':0.90, 'ROC': 0.5, 'recall': 0.77, 'precision': 0.42, 'TN': 20, 'FN': 1, \
                   'TP': 10, 'FP': 8, 'NPV': 0.9, 'PPV': 0.88, 'sensitivity': 0.77, 'specificity': 0.7, 'PRC': 0.72}
        self.r2 = {'dt': datetime.now(), 'experiment_name': "test2", 'graph': 1, 'runtime': 0.129, 'samples': 100, \
                   'folds': 5, 'accuracy':0.90, 'ROC': 0.5, 'recall': 0.77, 'precision': 0.42, 'TN': 20, 'FN': 1, \
                   'TP': 55, 'FP': 1, 'NPV': 0.3, 'PPV': 0.21, 'sensitivity': 0.85, 'specificity': 0.1, 'PRC': 0.2}
        self.r3 = {'dt': datetime.now(), 'experiment_name': "test3", 'graph': 3, 'runtime': 1.54, 'samples': 75, \
                   'folds': 10, 'accuracy':0.11, 'ROC': 0.1, 'recall': 0.72, 'precision': 0.84, 'TN': 1, 'FN': 309, \
                   'TP': 99, 'FP': 78, 'NPV': 0.1, 'PPV': 0.12, 'sensitivity': 0.01, 'specificity': 0.3, 'PRC': 0.48}
        
    def test_create_df(self):
        df = self.er.create_df()
        assert('experiment_name' in df.columns)
        
    def test_add_row_as_dict(self):
        self.er.create_df()
        self.er.add_row_as_dict(self.r1)
        df = self.er.get_df()
        assert(df.iloc[0]['experiment_name'] is "test1")
        assert(df.iloc[0]['experiment_name'] is not "test")
        self.er.add_row_as_dict(self.r2)
        df = self.er.get_df()
        assert(df.iloc[1]['experiment_name'] is "test2")
        assert(df.iloc[1]['experiment_name'] is not "test1")
        
    def test_save_load_df(self):
        self.er.create_df()
        self.er.add_row_as_dict(self.r1)
        self.er.add_row_as_dict(self.r2)
        self.er.add_row_as_dict(self.r3)
        self.er.save_df("df_results.pkl")
        self.er = Experiment_Results()
        self.er.load_df("df_results.pkl")
        df = self.er.get_df()
        assert(df.iloc[0]['experiment_name'] == "test1")
        assert(df.iloc[1]['experiment_name'] == "test2")
        assert(df.iloc[2]['experiment_name'] == "test3")
        
    def test_save_load_df_as_excel(self):
        self.er.create_df()
        self.er.add_row_as_dict(self.r1)
        self.er.add_row_as_dict(self.r2)
        self.er.add_row_as_dict(self.r3)
        self.er.save_df_as_excel()
        self.er.create_df()
        self.er.load_df_from_excel()
        df = self.er.get_df()
        assert(df.iloc[0]['experiment_name'] == "test1")
        assert(df.iloc[1]['experiment_name'] == "test2")
        assert(df.iloc[2]['experiment_name'] == "test3")
        
        
        