import os
import json
import random
from flask import Flask, request, jsonify
from flask_cors import CORS
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Background colors for avatars
COLORS = ['bg-brand-primary', 'bg-emerald-500', 'bg-amber-500', 'bg-rose-500', 'bg-blue-500', 'bg-indigo-500', 'bg-purple-500']

def get_google_sheet():
    creds_json_str = os.environ.get('GOOGLE_CREDENTIALS')
    sheet_id = os.environ.get('SPREADSHEET_ID')
    
    if not creds_json_str or not sheet_id:
        raise Exception("Missing GOOGLE_CREDENTIALS or SPREADSHEET_ID in environment variables.")

    creds_dict = json.loads(creds_json_str)
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    credentials = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    client = gspread.authorize(credentials)
    
    # Open the spreadsheet and get the first sheet
    sheet = client.open_by_key(sheet_id).sheet1
    return sheet

@app.route('/api/reviews', methods=['GET', 'POST'])
def reviews():
    try:
        sheet = get_google_sheet()
        
        if request.method == 'GET':
            # We expect the sheet to have headers: name, country, text, initials, color
            records = sheet.get_all_records()
            return jsonify(records), 200

        elif request.method == 'POST':
            data = request.json
            name = data.get('name', '').strip()
            country = data.get('country', '').strip()
            text = data.get('text', '').strip()

            if not name or not text:
                return jsonify({"error": "Name and Review Text are required"}), 400

            # Generate initials
            parts = name.split()
            initials = ''.join([p[0].upper() for p in parts[:2]]) if parts else 'A'
            
            # Pick a random color
            color = random.choice(COLORS)

            # Check if headers exist
            headers = sheet.row_values(1)
            if not headers:
                # Initialize headers if sheet is completely blank
                sheet.append_row(['name', 'country', 'text', 'initials', 'color'])
            
            # Append the new review
            sheet.append_row([name, country, text, initials, color])
            
            return jsonify({"message": "Review added successfully!"}), 201

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

# This handles Vercel's serverless requirement where the app object is imported
if __name__ == '__main__':
    app.run(port=5000, debug=True)
