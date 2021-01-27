#!/usr/bin/env python3
import pandas as pd
from pandas.errors import EmptyDataError

try:
    # Read csv files
    file1 = pd.read_csv('file1.csv')
    file2 = pd.read_csv('file2.csv')
    # Merge csv files
    merged_file = pd.merge(file1, file2, on='id')
    merged_file.set_index('id', inplace=True)
    # Write result to csv
    merged_file.to_csv('result.csv')
    print('Files merged')
except EmptyDataError:
    result = pd.DataFrame(columns=['No result'])
    result.to_csv('result.csv')
    print('Nothing to merge')
