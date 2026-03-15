import matplotlib.pyplot as plt
import seaborn as sns


class VisualizationMixin:

    def plot_histogram(self, column, bins=20):
        self.df[column].hist(bins=bins)
        plt.title(f"Histogram - {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()

    def plot_boxplot(self, column):
        sns.boxplot(y=self.df[column])
        plt.title(f"Boxplot - {column}")
        plt.tight_layout()
        plt.show()

    def plot_scatter(self, x_col, y_col):
        self.df.plot.scatter(x=x_col, y=y_col)
        plt.title(f"Scatter - {x_col} vs {y_col}")
        plt.tight_layout()
        plt.show()

    def plot_correlation_heatmap(self):
        corr = self.df.corr(numeric_only=True)
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.show()
