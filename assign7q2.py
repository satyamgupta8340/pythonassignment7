#2. Data Visualization and Exploration
#a. Print at least 5 rows for sanity check to identify all the features present in the dataset and if the target matches with them.


data.head()
data.info()
data.columns





# b. Print the description and shape of the dataset.

data.describe()
data.shape


#c. Provide appropriate visualization to get an insight about the dataset.
data['Kyphosis'].value_counts()




#Data Visualization

sns.set(rc={'figure.figsize':(25,8)})
g = sns.countplot(data["Age"], ax=None)
g.set_title("Age")



#count kyphosis
sns.set(rc={'figure.figsize':(5,4)})
l = len(data[data["Kyphosis"]=="present"])
g = sns.countplot([l,len(data)-l])
g.set_title("With Kyphosis")

g = sns.countplot(data["Number"])
g.set_title("Number")


g = sns.countplot(data["Start"])
g.set_title("Start")



# Exploratory data analysis

#Having kyphosis Age vs Number Lineplot Age in X axis
k = data[data["Kyphosis"]=="present"]
g = sns.lineplot(data=k, x="Age", y="Number")
g = sns.lineplot(data=k, x="Age", y="Start")


