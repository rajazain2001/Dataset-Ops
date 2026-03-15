class CleaningMixin:

    def missing_report(self):
        missing = self.df.isnull().sum()
        missing = missing[missing > 0]
        if missing.empty:
            print("No missing values found.")
        else:
            print("Missing Values:")
            print(missing)

    def missing_percentage(self):
        pct = (self.df.isnull().sum() / len(self.df)) * 100
        pct = pct[pct > 0]
        if pct.empty:
            print("No missing values found.")
        else:
            print("Missing Value Percentage:")
            print(pct)

    def fill_missing_mean(self):
        numeric_cols = self.df.select_dtypes(include='number').columns
        self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].mean())
        print("Missing numeric values filled with mean.")

    def fill_missing_median(self):
        numeric_cols = self.df.select_dtypes(include='number').columns
        self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].median())
        print("Missing numeric values filled with median.")

    def fill_missing_mode(self):
        for col in self.df.columns:
            self.df[col] = self.df[col].fillna(self.df[col].mode()[0])
        print("Missing values filled with mode.")

    def fill_missing_value(self, value):
        self.df = self.df.fillna(value)
        print(f"Missing values filled with: {value}")

    def drop_missing_rows(self):
        before = len(self.df)
        self.df = self.df.dropna()
        print(f"Removed {before - len(self.df)} rows with missing values.")

    def drop_missing_columns(self):
        before = len(self.df.columns)
        self.df = self.df.dropna(axis=1)
        print(f"Removed {before - len(self.df.columns)} columns with missing values.")

    def duplicate_report(self):
        count = self.df.duplicated().sum()
        print(f"Duplicate rows found: {count}")

    def count_duplicates(self):
        return self.df.duplicated().sum()

    def remove_duplicates(self):
        before = len(self.df)
        self.df = self.df.drop_duplicates()
        print(f"Removed {before - len(self.df)} duplicate rows.")

    def rename_column(self, old_name, new_name):
        self.df = self.df.rename(columns={old_name: new_name})
        print(f"Column '{old_name}' renamed to '{new_name}'.")

    def drop_column(self, col_name):
        self.df = self.df.drop(columns=[col_name])
        print(f"Column '{col_name}' dropped.")

    def add_column(self, col_name, default_value=None):
        self.df[col_name] = default_value
        print(f"Column '{col_name}' added.")

    def select_columns(self, columns):
        self.df = self.df[columns]
        print(f"Selected columns: {columns}")

    def filter_rows(self, condition):
        before = len(self.df)
        self.df = self.df.query(condition)
        print(f"Filtered rows. Remaining: {len(self.df)} (removed {before - len(self.df)})")

    def sort_rows(self, column, ascending=True):
        self.df = self.df.sort_values(by=column, ascending=ascending)
        print(f"Dataset sorted by '{column}'.")

    def sample_rows(self, n=5):
        return self.df.sample(n)
