import pandas as pd
#Dataframe creation
data = {
    'rocket' : [
        'Falcon 1', 
        'Falcon 9', 
        'Falcon Heavy',
        ],
    'launches': [5, 100, 3],
    }
df = pd.DataFrame(data)
#Printing the dataframe
print(df)
#Select and print 'rocket' column
print(df['rocket'])
#Filtering for rockets with more than five launches
more_than_five_launches = df[df['launches'] > 5]
print(more_than_five_launches)
