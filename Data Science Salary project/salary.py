import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea 
data=pd.read_csv(ds_salaries.csv)
sea.set(style='whitegrid')

# Data Preparation
employment_counts=data['employment_type'].value_counts()
experience_counts=data['experience_level'].value_counts()

# Create subplots
fig,axes=plt.subplots(1,2,figsize=(14,6))

# Employment Type Pie Chart
axes[0].pie(employment_counts, labels=employment_counts.index, autopct='%1.1f%%', 
            startangle=140, colors=sea.color_palette("pastel"))
axes[0].set_title("Distribution of Employment Types")

# Experience Level Bar Chart
sea.barplot(x=experience_counts.index, y=experience_counts.values, ax=axes[1], palette="Blues_r")
axes[1].set_title("Frequency of Experience Levels")
axes[1].set_xlabel("Experience Level")
axes[1].set_ylabel("Count")

plt.tight_layout()
plt.show()
