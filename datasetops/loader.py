import pandas as pd
from .cleaning import CleaningMixin
from .transformation import TransformationMixin
from .analysis import AnalysisMixin
from .visualization import VisualizationMixin
from .export import ExportMixin


class DatasetOps(CleaningMixin, TransformationMixin, AnalysisMixin, VisualizationMixin, ExportMixin):

    def __init__(self, filepath=None):
        self.df = None
        self._original = None
        self.filepath = filepath
        if filepath:
            self.load_csv(filepath)

    def load_csv(self, filepath):
        self.df = pd.read_csv(filepath)
        self._original = self.df.copy()
        print(f"Dataset loaded successfully")
        print(f"Rows: {self.df.shape[0]}, Columns: {self.df.shape[1]}")

    def load_excel(self, filepath):
        self.df = pd.read_excel(filepath)
        self._original = self.df.copy()
        print(f"Dataset loaded successfully")
        print(f"Rows: {self.df.shape[0]}, Columns: {self.df.shape[1]}")

    def load_json(self, filepath):
        self.df = pd.read_json(filepath)
        self._original = self.df.copy()
        print(f"Dataset loaded successfully")
        print(f"Rows: {self.df.shape[0]}, Columns: {self.df.shape[1]}")

    def reload_dataset(self):
        self.df = self._original.copy()
        print("Dataset reloaded to original state.")

    def summary(self):
        print("=" * 40)
        print("DATASET SUMMARY")
        print("=" * 40)
        print(f"Rows        : {self.df.shape[0]}")
        print(f"Columns     : {self.df.shape[1]}")
        print(f"Memory Usage: {self.df.memory_usage(deep=True).sum() / 1024:.2f} KB")
        print(f"Duplicates  : {self.df.duplicated().sum()}")
        print(f"Missing     : {self.df.isnull().sum().sum()}")
        print("=" * 40)

    def head(self, n=5):
        return self.df.head(n)

    def tail(self, n=5):
        return self.df.tail(n)

    def shape(self):
        print(f"Shape: {self.df.shape}")

    def column_names(self):
        print("Columns:", list(self.df.columns))

    def column_types(self):
        print(self.df.dtypes)

    def describe_stats(self):
        return self.df.describe(include='all')
