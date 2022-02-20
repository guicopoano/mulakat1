from excel_class import ExcelSorts as EXC
import pandas as pd


#if you enter the file path you can delete from here to next command line.
import os

current_directory = os.getcwd()  
file_path = current_directory+'\\mulakat1\\'+'TestCaseData.xlsx'
xls = pd.ExcelFile(file_path)

#you can delete the code above from here to the next command line and replace xls = pd.ExcelFile(r'Dummy\Dummy\mulakat\TestCaseData.xlsx' )
excel_to_df = EXC()
df = pd.read_excel(xls)
df = df.dropna()


print("Toplam değer = ", excel_to_df.sum_of_rows(df,32))
print(excel_to_df.sorted_rows(df,32))

print(excel_to_df.reverse_sort_rows(df,32))
