import pandas as pd

houses = pd.read_csv('ressources/all_data.csv', sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
houses.head()