import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = 'C:/Users/pgs66/Desktop/customer/'
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith('.xls')]

customer_price = pd.read_excel('C:/Users/pgs66/Desktop/customer/생필품상품별_동향[2017-01월-2017-12월]15-3시50분.xls')

for i in range(1, len(file_list_py)):
    data = pd.read_excel(path + file_list_py[i], usecols=[1,10,11,12,13,14,15,16,17,18,19,20,21])
    customer_price = pd.merge(customer_price,data, on='상품명')
    
customer_price = customer_price.reset_index(drop = True)
customer_price


customer_price_index = pd.DataFrame()

customer_price_index = customer_price.copy()

#time으로 더 쉽게 할수 있지 않을까,,?
customer_price_index.dropna(inplace=True)
customer_price_index = customer_price_index.sum()


for i in range(11,74):
    customer_price_index.iloc[i] = (customer_price_index.iloc[i]-customer_price_index.iloc[10]) / (customer_price_index.iloc[10]) * 100

customer_price_index = customer_price_index.drop('2019-05')
plt.plot(customer_price_index.iloc[11:73], marker='o')
plt.tick_params(pad=16, labelsize=14, top=True)
plt.xticks(rotation = 45)
plt.show()



customer_price_index.iloc[41]