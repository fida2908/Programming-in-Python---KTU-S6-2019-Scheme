import pandas as pd

df = pd.DataFrame([[26,'Bhanu',45,48], [34,'Fida',46,48],[35,'Fizza',48,34],[36,'Gautham',49,44]], columns=['Roll no','Name','Maths','Python'])


print(df)

df = df.set_index('Roll no')

print(df)

print('Details of Fida: ')
print(df.loc[34])