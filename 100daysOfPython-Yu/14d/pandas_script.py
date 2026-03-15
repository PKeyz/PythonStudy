import pandas as pd

def transform_list_to_dict():
    df = pd.read_csv(filepath_or_buffer='celebrities.csv')
    dict_of_list = df.to_dict(orient='records')
    # print(dict_of_list)
    return dict_of_list

# celebrities = transform_list_to_dict()
# print(celebrities[15])