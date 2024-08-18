import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("rational-logic-314303-04951c662eb6.json", scope)

gc = gspread.authorize(credentials)

wks = gc.open("TUTORIAL").sheet1
print(wks.get_all_records())

wks.append_row(["First Column", "Second Column"]) #append a ROW

wks.delete_row(2) #deletes row of index 2

