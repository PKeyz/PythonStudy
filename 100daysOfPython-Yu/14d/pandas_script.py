import pandas as pd

def transform_list_to_dict():
    df = pd.read_csv(filepath_or_buffer='./celebreties.csv')
    dict_of_list = df.to_dict(orient='records')
    return dict_of_list
celebreties = transform_list_to_dict()
print(celebreties)