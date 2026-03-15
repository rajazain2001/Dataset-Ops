class AnalysisMixin:

    def correlation_matrix(self):
        return self.df.corr(numeric_only=True)

    def detect_outliers(self, column):
        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1
        outliers = self.df[(self.df[column] < Q1 - 1.5 * IQR) | (self.df[column] > Q3 + 1.5 * IQR)]
        print(f"Outliers detected in '{column}': {len(outliers)}")
        return outliers

    def column_unique_values(self, column):
        return self.df[column].unique()

    def value_counts(self, column):
        return self.df[column].value_counts()

    def group_by(self, column):
        return self.df.groupby(column)

    def aggregate_stats(self, group_col, agg_col, func='mean'):
        return self.df.groupby(group_col)[agg_col].agg(func)

    def top_values(self, column, n=5):
        return self.df[column].value_counts().head(n)

    def data_quality_report(self):
        print("=" * 40)
        print("DATA QUALITY REPORT")
        print("=" * 40)
        print(f"Total Rows       : {self.df.shape[0]}")
        print(f"Total Columns    : {self.df.shape[1]}")
        print(f"Missing Values   : {self.df.isnull().sum().sum()}")
        print(f"Duplicate Rows   : {self.df.duplicated().sum()}")
        print(f"Numeric Columns  : {len(self.df.select_dtypes(include='number').columns)}")
        print(f"Categoric Columns: {len(self.df.select_dtypes(include='object').columns)}")
        print("=" * 40)
