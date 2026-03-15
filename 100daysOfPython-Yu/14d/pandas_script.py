import pandas as pd

def transform_list_to_dict():
    df = pd.read_csv(filepath_or_buffer='celebrities.csv')
    list_of_dicts = df.to_dict(orient='records')
    return list_of_dicts

# celebrities = transform_list_to_dict()
# print(celebrities[15])