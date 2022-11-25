import pandas as pd

x = "London"
df = pd.read_csv(f"CSV_files/listings_{x}.csv")
df1 =df[["host_id","host_name"]].head(10)
print(df1.to_html())