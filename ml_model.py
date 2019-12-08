import keras
import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense,BatchNormalization

# Grab Labels and Features + One hot the genre

# df = pd.read_csv('tmp_encoded_data.csv')
# g1 =df['genre_1'].dropna().unique()
# g2 =df['genre_1'].dropna().unique()
# g3 =df['genre_1'].dropna().unique()
# g4 =df['genre_1'].dropna().unique()
# genres = np.unique(np.concatenate((g1,g2,g3,g4)))

# for g in genres:
# 	df[g] = 0
# for g in genres:
# 	df[g] = ((df['genre_1'].str.contains(g))| (df['genre_2'].str.contains(g))| (df['genre_3'].str.contains(g))| (df['genre_4'].str.contains(g))).astype(float)

# # df['profit'] = np.load(df['profit']-df['profit'].min())
# # df['profit'] = df['profit']/df['profit'].max()
# df['vote_average'] = df['vote_average']/10

# labels = df[['profit','vote_average']]
# input_features = df[['Action','Adventure','Animation','Comedy','Crime','Documentary','Drama','Family','Fantasy','History','Horror','Music','Mystery','Romance','Science Fiction','Thriller','War','Western','budget','runtimeMinutes','prod_company_1_vote_average','prod_company_2_vote_average','prod_company_3_vote_average','prod_company_4_vote_average','prod_company_5_vote_average','writer_1_vote_average','writer_2_vote_average','writer_3_vote_average','writer_4_vote_average','writer_5_vote_average','director_1_vote_average','director_2_vote_average','director_3_vote_average','cast_1_vote_average','cast_2_vote_average','cast_3_vote_average','cast_4_vote_average','cast_5_vote_average','cast_6_vote_average','cast_7_vote_average','cast_8_vote_average','cast_9_vote_average','cast_10_vote_average','others_1_vote_average','others_2_vote_average','others_3_vote_average','others_4_vote_average','others_5_vote_average','others_6_vote_average','others_7_vote_average','others_8_vote_average','others_9_vote_average','others_10_vote_average','prod_company_1_vote_count','prod_company_2_vote_count','prod_company_3_vote_count','prod_company_4_vote_count','prod_company_5_vote_count','writer_1_vote_count','writer_2_vote_count','writer_3_vote_count','writer_4_vote_count','writer_5_vote_count','director_1_vote_count','director_2_vote_count','director_3_vote_count','cast_1_vote_count','cast_2_vote_count','cast_3_vote_count','cast_4_vote_count','cast_5_vote_count','cast_6_vote_count','cast_7_vote_count','cast_8_vote_count','cast_9_vote_count','cast_10_vote_count','others_1_vote_count','others_2_vote_count','others_3_vote_count','others_4_vote_count','others_5_vote_count','others_6_vote_count','others_7_vote_count','others_8_vote_count','others_9_vote_count','others_10_vote_count','prod_company_1_profit','prod_company_2_profit','prod_company_3_profit','prod_company_4_profit','prod_company_5_profit','writer_1_profit','writer_2_profit','writer_3_profit','writer_4_profit','writer_5_profit','director_1_profit','director_2_profit','director_3_profit','cast_1_profit','cast_2_profit','cast_3_profit','cast_4_profit','cast_5_profit','cast_6_profit','cast_7_profit','cast_8_profit','cast_9_profit','cast_10_profit','others_1_profit','others_2_profit','others_3_profit','others_4_profit','others_5_profit','others_6_profit','others_7_profit','others_8_profit','others_9_profit','others_10_profit','prod_company_1_rev_budget_ratio','prod_company_2_rev_budget_ratio','prod_company_3_rev_budget_ratio','prod_company_4_rev_budget_ratio','prod_company_5_rev_budget_ratio','writer_1_rev_budget_ratio','writer_2_rev_budget_ratio','writer_3_rev_budget_ratio','writer_4_rev_budget_ratio','writer_5_rev_budget_ratio','director_1_rev_budget_ratio','director_2_rev_budget_ratio','director_3_rev_budget_ratio','cast_1_rev_budget_ratio','cast_2_rev_budget_ratio','cast_3_rev_budget_ratio','cast_4_rev_budget_ratio','cast_5_rev_budget_ratio','cast_6_rev_budget_ratio','cast_7_rev_budget_ratio','cast_8_rev_budget_ratio','cast_9_rev_budget_ratio','cast_10_rev_budget_ratio','others_1_rev_budget_ratio','others_2_rev_budget_ratio','others_3_rev_budget_ratio','others_4_rev_budget_ratio','others_5_rev_budget_ratio','others_6_rev_budget_ratio','others_7_rev_budget_ratio','others_8_rev_budget_ratio','others_9_rev_budget_ratio','others_10_rev_budget_ratio']]
# labels.to_csv('ml_data/labels.csv')
# input_features.to_csv('ml_data/input_features.csv')


''' 
Actual Training
'''

# Read Data, Drop index col
labels = np.loadtxt('ml_data/labels.csv',skiprows=1,delimiter=',')[:,2] 
input_features = np.loadtxt('ml_data/input_features.csv',skiprows=1,delimiter=',')[:,1:]

num_data = labels.shape[0]

shuffle_idx = np.random.choice(num_data,size=num_data)
labels = labels[shuffle_idx]
input_features = input_features[shuffle_idx]

train_labels = labels[:3000]
train_feat   = input_features[:3000]

test_labels = labels[3000:]
test_feat   = input_features[3000:]

print(train_labels.shape)
print(train_feat.shape)
print(test_labels.shape)
print(test_feat.shape)


model = Sequential()
model.add(Dense(256, input_dim=152, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(128, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(64, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


model.compile(loss='MSE', optimizer='adam', metrics=['MSE'])
model.summary()


model.fit(train_feat, train_labels,validation_data=(test_feat,test_labels), epochs=150, batch_size=32)









