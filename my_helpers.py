import pandas as pd
import numpy as np

def print_types(data, name=""):
    first_line = 'Data types' 
    if name:
        first_line += f' of {name}'
    print(f'{first_line}:')
    dict_names = {k.name: [col for col in data.columns if data[col].dtypes==k] for k in data.dtypes.value_counts().to_dict().keys()}
    for k, v in dict_names.items():
        print(f'  {k} ({len(v)}):')
        for i in range(len(v)//3 + 1):
            line = ', '.join(v[i*5:(i+1)*5]) 
            if len(line) > 0:
                print(f'    - {line}')

def transform_data(data):
    df = data.copy()
    df.drop(['id', 'customer_id','begin_date', 'end_date'], axis=1, inplace=True)
    df.dropna(subset=['total_charges'], inplace=True)
    df.fillna('Unknown', inplace=True)
    df.dropna(inplace=True)
    return df

def display_statistics(data, freq_values=True, decimals=4):
    
    def get_freq_values(data, decimals=4, freq_num=3):
        if data.dtype in ['float', 'int']:
            return data.round(decimals).value_counts().head(freq_num).to_dict()
        else:
            return data.value_counts().head(freq_num).to_dict()

    def lo_hi_count(data, col, low=True):
        if data[col].dtype not in [float, int,'datetime64[ns]']:
            return '---'
        Q1 = np.nanquantile(data[col], 0.25)
        Q3 = np.nanquantile(data[col], 0.75)
        if low:
            return data[data[col] <= (Q1 - 1.5 * (Q3 - Q1))][col].count()
        else:
            return data[data[col] >= (Q3 + 1.5 * (Q3 - Q1))][col].count()

    if freq_values:
        freq_name = 'freq_values'
        freq_num = 3
    else:
        freq_name = 'most_freq'
        freq_num = 1
    return pd.DataFrame(
        {'type': [data[x].dtypes for x in data.columns],
         'count' : [data[x].count() for x in data.columns],
         'NaNs' : [data[x].isna().sum() for x in data.columns],
         'zero_values': [data[x].eq(0).sum() for x in data.columns],
         'unique_values': [data[x].nunique() for x in data.columns],
         freq_name: [get_freq_values(data[x], decimals, freq_num) for x in data.columns],
         'min': [data[x].min() if data[x].dtype!=object else '---' for x in data.columns],
         'mean': [data[x].mean() if data[x].dtype!=object else '---' for x in data.columns],
         'max': [data[x].max() if data[x].dtype!=object else '---' for x in data.columns],
         'std': [data[x].std() if data[x].dtype!=object else '---' for x in data.columns],
         'lo_count': [lo_hi_count(data, x) for x in data.columns],
         'hi_count': [lo_hi_count(data, x, low=False) for x in data.columns],
        }, index = [x for x in data.columns])