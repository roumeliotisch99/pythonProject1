import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Final.csv")
cn = df.groupby('zip_code')
most_popular_item = cn.aggregate(np.sum).head(1)


cn2=df.groupby('store_name')
y = cn2.aggregate(np.sum)
sum1=(np.sum(y['sale_dollars']))
percentage_of_sales_per_store=(y['sale_dollars']/sum1)*100

b=np.array(df["bottles_sold"])
z=np.array(df['zip_code'])
for i in range(0,len(b)):
    plt.scatter( z[i],b[i])
plt.title('Bottles Sold')
plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")
plt.show()









