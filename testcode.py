import pandas as pd

df = pd.read_csv("./data/Boston.csv")
print(df.to_html())
