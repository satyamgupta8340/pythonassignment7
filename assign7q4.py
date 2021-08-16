
#4. Data Preparation
#a. Do the final feature selection and extract them into Column X and the class label into Column into Y.
#b. Split the dataset into training and test sets.
x = data.iloc[:, 1:]
y = data.iloc[:, 0]
x
y
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2, random_state=42)
x_train.shape,x_test.shape



#Part B
#1. Model Building
#a. Perform Model Development using at least three models, separately. You are free to apply any Machine Learning Models on the dataset. Deep Learning Models are strictly not allowed.
#In this dataset i will use LinearRegression, LogisticRegression and K-Nearst Neighbor
#LinearRegression
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(x_train,y_train)
y_pred=reg.predict(x_test)
from sklearn import metrics 
mse=metrics.mean_squared_error(y_test,y_pred)
print("Mean_squared_error:",mse)
rmse=np.sqrt(mse)
print("Root_Mean_squared_Error:",rmse)



## LogisticRegression
x = data.iloc[:, 1:]
y = data.iloc[:, 0]
x
y
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2, random_state=42)
from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)
y_pred=log_reg.predict(x_test)
y_pred
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, classification_report
acc = accuracy_score(y_test, y_pred)
print("Accuracy_Score:", acc)
confusion_matrix(y_test, y_pred)

#K-Nearst Neighbor
x = data.iloc[:, 1:]
y = data.iloc[:, 0]

x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2, random_state=42)




#b. Train the model and print the training accuracy and loss values.

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score, confusion_matrix
k_range=list(range(3,10))
acc=[]
for i in k_range:
    knn=KNeighborsClassifier(n_neighbors=i).fit(x_train,y_train)
    y_pred=knn.predict(x_test)
    acc.append(metrics.accuracy_score(y_test,y_pred))
    acc


    #2.Performance Evaluation
#a. Print the confusion matrix. Provide appropriate analysis for the same.
    
    
    confusion_matrix(y_test, y_pred)

 #   b. Do the prediction for the test data and display the results for the inference.
      
      print("Report:", classification_report(y_test, y_pred))
