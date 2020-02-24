#importing packages
import pandas as pd

df = pd.read_csv('/Users/aakarsh.rajagopalan/Personal documents/Python projects/DuplicateIdentification/Duplicate Identification Data set/CPO contract extract as on 2-24.csv')

print(type(df))

#showing the list of columns
print(df[:0])

#storing the ExternalId__c field in a list
df_list = df['ExternalId__c'].tolist()
print(type(df_list))

#getting the count of the records in the list
print(len(df_list))

#removing duplicates by converting to set
df_set = set(df_list)
print(type(df_set))

#calculating the number of duplicates:
print(abs(len(df_set) - len(df_list)))

#converting the set to the a list
df_no_dup = list(df_set)
print(len(df_no_dup))
print(type(df_no_dup))

#getting the list of non common elements
df_list_of_dup = []
for elems in df_list:
    if df_list.count(elems)>1:
        df_list_of_dup.append(elems)
    else:
        continue

print(len(set(df_list_of_dup)))

#outputing to a csv file
pd.DataFrame(df_list_of_dup).to_csv('/Users/aakarsh.rajagopalan/Personal documents/Python projects/DuplicateIdentification/Duplicate Identification Data set/Duplicate CPO contract records as on 2-24.csv')


