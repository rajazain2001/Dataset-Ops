from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
import pandas as pd


class TransformationMixin:

    def normalize(self):
        numeric_cols = self.df.select_dtypes(include='number').columns
        scaler = MinMaxScaler()
        self.df[numeric_cols] = scaler.fit_transform(self.df[numeric_cols])
        print("Numeric columns normalized to range 0-1.")

    def standardize(self):
        numeric_cols = self.df.select_dtypes(include='number').columns
        scaler = StandardScaler()
        self.df[numeric_cols] = scaler.fit_transform(self.df[numeric_cols])
        print("Numeric columns standardized.")

    def log_transform(self, column):
        import numpy as np
        self.df[column] = np.log1p(self.df[column])
        print(f"Log transform applied to column '{column}'.")

    def encode_categorical(self):
        le = LabelEncoder()
        cat_cols = self.df.select_dtypes(include='object').columns
        for col in cat_cols:
            self.df[col] = le.fit_transform(self.df[col].astype(str))
        print(f"Categorical columns encoded: {list(cat_cols)}")

    def one_hot_encode(self, column):
        self.df = pd.get_dummies(self.df, columns=[column])
        print(f"One-hot encoding applied to column '{column}'.")
