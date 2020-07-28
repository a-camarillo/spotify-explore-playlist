import json
import pandas as pd 

with open('features.json','r') as file:
    top_features = json.load(file)

df = pd.DataFrame.from_dict(top_features,orient='index')
df = df.reset_index()
df = df.rename(columns={'index':'name'})
df.to_csv('top_features.csv')
        

    


