
#3. Data Pre-processing and cleaning
#a. Do the appropriate preprocessing of the data like identifying NULL or Missing Values if any, handling of outliers if present in the dataset, skewed data etc. Apply appropriate feature engineering techniques for them.

#Now First check should be any Null is present or not
data.isnull().sum()

data['Age'].unique()
data['Kyphosis'].unique()
data['Kyphosis'].value_counts()

for col in data:
     if(col=='Kyphosis'):
            data[col]= data[col].map({'absent':0,'present':1})

	    data['Kyphosis'].value_counts()


	    data1=data

import missingno
     
     missingno.matrix(data1,figsize=(12,8))

     data1.boxplot(column=['Number'])

     data1.boxplot(column=['Start'])
     data1.boxplot(by="Age")




     #b. Apply the feature transformation techniques like Standardization, Normalization, etc. You are free to apply the appropriate transformations depending upon the structure and the complexity of your dataset.

     #Normalization
          from sklearn.preprocessing import StandardScaler
          scaler = StandardScaler() 
          data_scaled = scaler.fit_transform(data)

          print(data_scaled.mean(axis=0))
          print(data_scaled.std(axis=0))

          Standardization
          from sklearn.preprocessing import MinMaxScaler
          scaler = MinMaxScaler() 
          data_scaled = scaler.fit_transform(data)


          print('means (Age, Number and Start): ', data_scaled.mean(axis=0))
          print('std (Age, Number and Start): ', data_scaled.std(axis=0))

