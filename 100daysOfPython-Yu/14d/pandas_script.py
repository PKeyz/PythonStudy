import pandas as pd
path = "celebreties.csv"
text_data = pd.read_csv(path, sep=",",usecols=["Username","Owner","Followers (Millions)","Profession/Activity","Country"])

result = text_data.to_dict(orient="records")
result.to_

#TODO 1: Save result to dict file for later iterations
print_to_dict_file = result


print(result)
