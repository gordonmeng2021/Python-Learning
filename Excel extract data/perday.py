
import openpyxl
import os
import pandas as pd

os.getcwd()

file = 'Excel extract data/instagram_report.xlsx'
data =  pd.ExcelFile(file)
#print(data.sheet_names) # this print the name of the sheet

df = data.parse('Socialinsider | Analytics Tool')
df.info
df.head(10)

# *****-------read in the spreadsheet data

ps = openpyxl.load_workbook('Excel extract data/instagram_report.xlsx') # relative path
sheet = ps['Socialinsider | Analytics Tool'] # sheet name
checking = input("What do you want to check : ")
list =['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF']
print()
print("------",checking,"------")
print()
for row in range(2,sheet.max_row +1):
    result = sheet['A'+str(row)].value
    
    if result == checking:
        wanted_row = row +2
        
        for i in list:
            topic = sheet[i+str(wanted_row)].value
            number = sheet[i+str(wanted_row+1)].value
            print('Date :',topic,'---- Number :',number)
                
         