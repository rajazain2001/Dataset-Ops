class ExportMixin:

    def save_csv(self, filepath="clean_data.csv"):
        self.df.to_csv(filepath, index=False)
        print(f"Dataset saved as CSV: {filepath}")

    def save_excel(self, filepath="clean_data.xlsx"):
        self.df.to_excel(filepath, index=False)
        print(f"Dataset saved as Excel: {filepath}")

    def export_report(self, filepath="report.txt"):
        with open(filepath, "w") as f:
            f.write("DATA QUALITY REPORT\n")
            f.write("=" * 40 + "\n")
            f.write(f"Rows             : {self.df.shape[0]}\n")
            f.write(f"Columns          : {self.df.shape[1]}\n")
            f.write(f"Missing Values   : {self.df.isnull().sum().sum()}\n")
            f.write(f"Duplicate Rows   : {self.df.duplicated().sum()}\n")
            f.write("=" * 40 + "\n")
        print(f"Report exported: {filepath}")
