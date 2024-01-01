import pandas as pd 
dataframe = pd.read_csv ('fichier.csv', sep=";")
print(dataframe.head(10))
print(dataframe.info())  
total_number_of_columns_shape =dataframe.shape[1]
print(dataframe.loc[2]) 

#dataframe = pd.DataFrame(['item_name'])
#counts = dataframe['item_name'].value_counts()
#best_seller = counts.idxmax 
#print('best seller is:',best_seller)
nombre_total_articles_commandes = dataframe['quantity'].sum()
