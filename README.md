# datasetops

A Python toolkit for simplifying dataset preparation and preprocessing.

## Installation
```bash
pip install datasetops
```

## Usage
```python
from datasetops import DatasetOps

ds = DatasetOps("data.csv")

ds.summary()
ds.missing_report()
ds.remove_duplicates()
ds.normalize()
ds.encode_categorical()
ds.save_csv("clean_data.csv")
```

## Features

* **Loading:** `load_csv`, `load_excel`, `load_json`, `reload_dataset`
* **Inspection:** `summary`, `head`, `tail`, `shape`, `column_names`, `column_types`, `describe_stats`
* **Missing Values:** `missing_report`, `missing_percentage`, `fill_missing_mean`, `fill_missing_median`, `fill_missing_mode`, `fill_missing_value`, `drop_missing_rows`, `drop_missing_columns`
* **Duplicates:** `duplicate_report`, `count_duplicates`, `remove_duplicates`
* **Column Operations:** `rename_column`, `drop_column`, `add_column`, `select_columns`
* **Row Operations:** `filter_rows`, `sort_rows`, `sample_rows`
* **Transformation:** `normalize`, `standardize`, `log_transform`, `encode_categorical`, `one_hot_encode`
* **Analysis:** `data_quality_report`, `correlation_matrix`, `detect_outliers`, `column_unique_values`, `value_counts`, `group_by`, `aggregate_stats`, `top_values`
* **Visualization:** `plot_histogram`, `plot_boxplot`, `plot_scatter`, `plot_correlation_heatmap`
* **Export:** `save_csv`, `save_excel`, `export_report`
