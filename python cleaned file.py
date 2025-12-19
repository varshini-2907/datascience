import pandas as pd

df = pd.read_csv(r"E:\VD\Internship\varshini\NewCompanyDetails.csv")

df = df.drop_duplicates()
df = df.dropna()

df['revenue'] = df['revenue'].replace(r'[^0-9]', '', regex=True).astype(int)

df['total_workers'] = df['workers'] + df['previous_workers']

df.to_csv("newcleaneddetails.csv")

print("new file created")
