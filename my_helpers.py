import pandas as pd

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