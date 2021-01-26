# Python script to search data in CSV file matching regular expression.

import pandas as pd
from pandas.errors import EmptyDataError

regex = '^A34|B89|P10|C56|Z67.*'

try:
    # Read csv file
    file = pd.read_csv('input_file.csv')
    # If file has only a header do nothing.
    if len(file) == 0:
        print('No rows. nothing to search')
        file.to_csv('result_file.csv', index=False)
    else:
        # Drop all rows that does not match the regex
        final_file = file[file['post_code'].str.match(regex) == True]
        final_file.to_csv('result_file.csv', index=False)
        print('File searched to find rows matching regular expression. Result saved to result_file.csv.')

except EmptyDataError:
    result = pd.DataFrame(columns=['No result'])
    result.to_csv('result.csv', index=False)
    print('File is empty. nothing to search.')