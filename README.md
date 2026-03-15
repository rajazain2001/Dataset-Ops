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

- Load CSV, Excel, JSON datasets
- Dataset summary and inspection
- Missing value detection and filling
- Duplicate detection and removal
- Normalization and standardization
- Categorical encoding
- Correlation analysis
- Outlier detection
- Visualization (histogram, boxplot, scatter, heatmap)
- Export to CSV and Excel
