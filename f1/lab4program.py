import os
import pandas as pd

filex1=os.path.join("datasets","housing","housing.xlsx")
data=pd.read_excel(filex1)
print("EXCEL LOAD AND PRINT")
print(data)
print("**********************************************")
file_path = os.path.join("datasets","housing","housing.csv")
df = pd.read_csv(file_path)
print("CSV LOAD AND PRINT")
print(df)
print("about excel file")
print("Usinginfo() to print details about columns along with datatypes",data.info())
print("**********************************************")
print("Using describe() to print the summary of the dataframe",data.describe())
print("**********************************************")
print("using head() printing first 5 rows by default",data.head())
print("**********************************************")
print("using tail() printing first 5 rows by default",data.tail())
print("**********************************************")
print("using value_counts() to count categorical values of a column",data["ocean_proximity"].value_counts())
print("Excel info end")
print("**********************************************")

print("about csv file")
print("Usinginfo() to print details about columns along with datatypes",df.info())
print("**********************************************")
print("Using describe() to print the summary of the dataframe",df.describe())
print("**********************************************")
print("using head() printing first 5 rows by default",df.head(-3))
print("**********************************************")
print("using tail() printing first 5 rows by default",df.tail(-3))
print("**********************************************")
print("using value_counts() to count categorical values of a column",df["ocean_proximity"].value_counts())
print("Excel info end")

