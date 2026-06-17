import os
import json
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

load_dotenv()

def populate_sheet():
    creds_json_str = os.environ.get('GOOGLE_CREDENTIALS')
    sheet_id = os.environ.get('SPREADSHEET_ID')
    
    creds_dict = json.loads(creds_json_str)
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    credentials = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    client = gspread.authorize(credentials)
    
    sheet = client.open_by_key(sheet_id).sheet1
    
    # Check if headers exist
    try:
        headers = sheet.row_values(1)
    except:
        headers = []

    if not headers:
        print("Sheet is empty. Adding headers and mock data...")
        # Add headers
        sheet.append_row(['name', 'country', 'text', 'initials', 'color'])
        
        # Add mock reviews
        sheet.append_row(["Sarah & Mike", "United Kingdom", "Traveling with Andy was the highlight of our trip. His knowledge of the local history and secret spots made our adventure truly exceptional.", "SM", "bg-brand-primary"])
        sheet.append_row(["James Doe", "Australia", "We saw 3 leopards in Yala thanks to Andy's eagle eyes! He arranged everything perfectly and we just had to sit back and enjoy.", "JD", "bg-emerald-500"])
        sheet.append_row(["Anna Lindström", "Sweden", "The train ride to Ella was magical. Andy took care of our tickets months in advance. Best guide we've ever had on any of our travels!", "AL", "bg-amber-500"])
        sheet.append_row(["Paul Thompson", "Canada", "Our family of 5 had an incredible time. Andy was so patient with the kids and customized everything to our pace. Highly recommended.", "PT", "bg-rose-500"])
        print("Done.")
    else:
        print(f"Sheet already has data. Headers: {headers}")
        records = sheet.get_all_records()
        print(f"Found {len(records)} records.")

if __name__ == '__main__':
    populate_sheet()
