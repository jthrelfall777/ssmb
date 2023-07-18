import pickle
import pandas as pd


class Experiment_Results:
    def __init__(self):
        self.field = ['dt', 'experiment_name', 'graph', 'runtime', 'samples', 'folds', 'accuracy', 'ROC', 'recall', 'precision', \
                      'TN', 'FN', 'TP', 'FP', 'NPV', 'PPV', 'sensitivity', 'specificity', 'PRC']
        self.field_mapping = {'dt': pd.Series([], dtype='datetime64[ns]'),
                                'experiment_name': pd.Series([], dtype='string'),
                                'model_name': pd.Series([], dtype='string'),
                                'graph': pd.Series([], dtype='int'),
                                'p_value': pd.Series([], dtype='float'),
                                'refset_size': pd.Series([], dtype='int'),
                                'before_limit_refset_size': pd.Series([], dtype='int'),
                                'vertices': pd.Series([], dtype='int'),
                                'edge': pd.Series([], dtype='int'),
                                'runtime': pd.Series([], dtype='float'),
                                'folds': pd.Series([], dtype='int'),
                                'samples': pd.Series([], dtype='int'),
                                'population': pd.Series([], dtype='int'),
                                'accuracy': pd.Series([], dtype='float'),
                                'ROC': pd.Series([], dtype='float'),
                                'recall': pd.Series([], dtype='float'),
                                'precision': pd.Series([], dtype='float'),
                                'TN': pd.Series([], dtype='float'),
                                'FN': pd.Series([], dtype='float'),
                                'TP': pd.Series([], dtype='float'),
                                'FP': pd.Series([], dtype='float'),
                                'NPV': pd.Series([], dtype='float'),
                                'PPV': pd.Series([], dtype='float'),
                                'sensitivity': pd.Series([], dtype='float'),
                                'specificity': pd.Series([], dtype='float'),
                                'PRC': pd.Series([], dtype='float')}
        self.df = None
        
    def create_df(self):
        self.df = pd.DataFrame(self.field_mapping)
        
        return self.df
    
    def save_df(self, filename):
        fd = open(filename,'wb')
        pickle.dump(self.df, fd)
        fd.close()
        
    def load_df(self, filename):
        fd = open(filename,'rb')
        self.df = pickle.load(fd)
        fd.close
        
    def add_row_as_dict(self, a_row_dict):
        self.df = self.df.append(a_row_dict, ignore_index=True)
        
    def get_df(self):
        return self.df
    
    def save_df_as_excel(self, filename):
        self.df.to_excel(filename)
        
    def load_df_from_excel(self, filename):
        self.df = pd.read_excel(filename, index_col=0)
    