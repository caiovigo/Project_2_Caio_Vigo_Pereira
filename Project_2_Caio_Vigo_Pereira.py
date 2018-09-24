# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 19:27:48 2018

@author: Caio Laptop
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

my_data_Shakespeare=pd.read_csv('C:/Users/Caio Laptop/OneDrive - The University of Kansas/Documents/PhD/11. Courses/19. EECS 731 - Introduction to Data Science/Homework/Section 4 - HW/Shakespeare_data.csv')

#Taking a look in my data
my_data_Shakespeare.head()
my_data_Shakespeare.shape
my_data_Shakespeare.index
my_data_Shakespeare.columns
my_data_Shakespeare.info()
my_data_Shakespeare.count()

#Want to know how many Play we have
my_data_Shakespeare["Play"].value_counts()

#Want to know how many Player we have
my_data_Shakespeare["Player"].value_counts()

#Creating new variables
counts_player=my_data_Shakespeare["Player"].value_counts()
counts_player[counts_player > 1000]
Player_top1000=my_data_Shakespeare[my_data_Shakespeare['Player'].isin(counts_player[counts_player > 1000].index)]

counts_play=my_data_Shakespeare["Play"].value_counts()
counts_play[counts_play > 3500]
Play_top3500=my_data_Shakespeare[my_data_Shakespeare['Play'].isin(counts_play[counts_play > 3500].index)]

my_data_Shakespeare_new=my_data_Shakespeare[my_data_Shakespeare['Play'].isin(counts_play[counts_play > 3500].index)]
my_data_Shakespeare_new=my_data_Shakespeare_new[my_data_Shakespeare_new['Player'].isin(counts_player[counts_player > 1000].index)]


sns.countplot(x="Player", data=my_data_Shakespeare, palette="Greens_d")
sns.countplot(x="Play", data=my_data_Shakespeare, palette="Greens_d")

sns.pairplot(my_data_Shakespeare_new.drop("Play", axis=1), hue="Player", size=3)

#Pearson Correlation
colormap = plt.cm.RdBu
plt.figure(figsize=(14,12))
plt.title('Pearson Correlation of Features', y=1.05, size=15)
sns.heatmap(my_data_Shakespeare.astype(float).corr(),linewidths=0.1,vmax=1.0, 
            square=True, cmap=colormap, linecolor='white', annot=True)


rf.model<- randomForest(player~play., 
                        data = my_data_Shakespeare, 
                        importance=TRUE,
                        keep.forest=TRUE)
> rf.predict <- predict(rf.model, test.data)
> confusionMatrix(test.data$income, rf.predict) # 88%
