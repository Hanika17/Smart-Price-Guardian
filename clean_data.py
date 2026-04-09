import pandas as pd

df = pd.read_csv("amazon.csv")

df = df.rename(columns={
    'actual_price': 'claimed_price',
    'discounted_price': 'current_price',
    'product_name': 'product'
})

df['claimed_price'] = df['claimed_price'].replace('[₹,]', '', regex=True).astype(float)
df['current_price'] = df['current_price'].replace('[₹,]', '', regex=True).astype(float)

df = df[['product', 'claimed_price', 'current_price']]

df = df.head(10)

df.to_csv("cleaned_data.csv", index=False)

print("Cleaned dataset ready!")