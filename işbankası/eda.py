import pandas as pd

file_path = "/Users/selinaydin/PycharmProjects/işbankası/source_doc/fertility-rates_subnational_tur.csv"
df = pd.read_csv(file_path)


df_clean = df[['Location', 'Indicator', 'Value']].copy()
df_clean = df_clean.iloc[1:].reset_index(drop=True)


df_clean['Value'] = pd.to_numeric(df_clean['Value'], errors='coerce')


df_grouped = df_clean.groupby('Location')['Value'].mean().reset_index()


print(df_grouped)


df_grouped.to_csv("regional_fertility_rates.csv", index=False)
