import pandas as pd;
#df = pd.read_csv("emps.csv")
# print(df)
# print("========================================================================================")
df1 = pd.read_csv("students.csv")
# print(df1.isnull())
# print("==============================df1.dropna()================================================")
# print(df1)
# print(df1.dropna())
# print("=============================df1.dropna(inplace=True)====================================")
print(df1)
print("====")
print(df1.dropna(inplace=True))
print(df1)
print("========================================================================================");

