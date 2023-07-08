import pandas as pd

df = pd.read_csv('dataset1_assign_1.csv')
print(df)

#Find the country who has won the most Asia Cup
most_wins = df['Winner'].value_counts().idxmax()

#Find the country who Host most Asia Cup tournaments
most_hosts = df['Host'].value_counts().idxmax()

#Find the country who has the runner-up in 1988, 2004, and 2016
runner_up_1988 = df.loc[df['Year'] == 1988, 'Runner up'].values[0]
runner_up_2004 = df.loc[df['Year'] == 2004, 'Runner up'].values[0]
runner_up_2016 = df.loc[df['Year'] == 2016, 'Runner up'].values[0]

#Find the different formats of Asia Cup
formats = df['Format'].unique()

#Clean the dataset if record is empty with 0 values or delete incomplete data row
df.fillna(0, inplace=True)
df.dropna(inplace=True)

#Find all the years of Asia Cup won by India
india_wins = df.loc[df['Winner'] == 'India', 'Year'].values

#Find the final match hosted by 'Bangladesh'
final_match_bangladesh = df.loc[df['Final Venue'].str.contains('Dhaka'), 'Year'].values[-1]

#Print the results
print("a. Country with the most Asia Cup wins:", most_wins)
print("b. Country that hosted the most Asia Cup tournaments:", most_hosts)
print("c. Runner-up countries in 1988, 2004, and 2016:", runner_up_1988, runner_up_2004, runner_up_2016)
print("d. Different formats of Asia Cup:", formats)
print("f. Years of Asia Cup won by India:", india_wins)
print("g. Final match hosted by Bangladesh:", final_match_bangladesh)
