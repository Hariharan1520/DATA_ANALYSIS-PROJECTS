# Importing necessary libraries
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the dataset
df = pd.read_csv('Iris.csv')

# Displaying the first few rows of the dataset
print(df.head())  

# Checking the shape of the dataset (rows, columns)
df.shape

# Getting information about the dataset (data types, non-null counts)
df.info()

# Descriptive statistics for numerical columns
df.describe()

# Checking for missing values in the dataset
df.isnull().sum()

# Dropping duplicate rows based on the "Species" column
# This keeps only one instance of each species
data = df.drop_duplicates(subset="Species",) 
print(data)

# Counting the occurrences of each species
df.value_counts("Species")

# Visualizing the distribution of species using a count plot
sns.countplot(x="Species", data=df)
plt.show()

# Scatter plot for Sepal Length vs Sepal Width, colored by species
sns.scatterplot(x="SepalLengthCm", y="SepalWidthCm", hue="Species", data=df)
# Positioning the legend outside the plot
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()

# Scatter plot for Petal Length vs Petal Width, colored by species
sns.scatterplot(x='PetalLengthCm', y='PetalWidthCm', hue='Species', data=df)
# Positioning the legend outside the plot
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()

# Pair plot for visualizing pairwise relationships between features, excluding the "Id" column
sns.pairplot(df.drop(['Id'], axis=1), hue='Species', height=2)

# Creating subplots for histograms of all numerical features
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# Histogram for Sepal Length
axes[0, 0].set_title("Sepal Length")
axes[0, 0].hist(df['SepalLengthCm'], bins=7)

# Histogram for Sepal Width
axes[0, 1].set_title("Sepal Width")
axes[0, 1].hist(df['SepalWidthCm'], bins=5)

# Histogram for Petal Length
axes[1, 0].set_title("Petal Length")
axes[1, 0].hist(df['PetalLengthCm'], bins=6)

# Histogram for Petal Width
axes[1, 1].set_title("Petal Width")
axes[1, 1].hist(df['PetalWidthCm'], bins=6)

# Adding space between subplots for better visibility
plt.tight_layout()

# Distribution plots for numerical features using FacetGrid
# Note: sns.distplot is deprecated, replaced with sns.histplot or sns.kdeplot
plot = sns.FacetGrid(df, hue="Species")
plot.map(sns.histplot, "SepalLengthCm").add_legend()

plot = sns.FacetGrid(df, hue="Species")
plot.map(sns.histplot, "SepalWidthCm").add_legend()

plot = sns.FacetGrid(df, hue="Species")
plot.map(sns.histplot, "PetalLengthCm").add_legend()

plot = sns.FacetGrid(df, hue="Species")
plot.map(sns.histplot, "PetalWidthCm").add_legend()

# Displaying all FacetGrid plots
plt.show()

# Calculating the correlation matrix for numerical columns
data.select_dtypes(include=['number']).corr(method='pearson')

# Heatmap for correlation matrix, excluding the "Id" column
sns.heatmap(df.select_dtypes(include=['number']).corr(method='pearson').drop( 
['Id'], axis=1).drop(['Id'], axis=0), 
            annot=True) 

plt.show()

# Function for creating box plots
def graph(y):
    sns.boxplot(x="Species", y=y, data=df)

# Creating subplots for box plots of all numerical features
plt.figure(figsize=(10, 10))

plt.subplot(221)
graph('SepalLengthCm')

plt.subplot(222)
graph('SepalWidthCm')

plt.subplot(223)
graph('PetalLengthCm')

plt.subplot(224)
graph('PetalWidthCm')

# Displaying the box plots
plt.show()

# Simple box plot for Sepal Width
sns.boxplot(x='SepalWidthCm', data=df)
