from flask import Flask, render_template, request, jsonify
import requests
import gspread
from datetime import datetime, timedelta
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__, template_folder='templates')


# authentication for google sheets service account
# before testing this you should provide at least 'view' access to your google sheets for your
# google service account
def google_sheets_auth():
    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    return client


# INSERT YOUR SHEET_ID HERE TO TEST
sheet_id = "17M8ccJrnESwo5hcQQinGkKZizzyL2zuUVx5-WhKwJJM"
sheet = google_sheets_auth().open_by_key(sheet_id).sheet1
sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}"


# Home page with form
@app.route('/')
def home():
    return render_template('update_rate.html')


@app.route('/update_rate', methods=['POST'])
def update_rate():
    # Collecting data from the form
    update_from = request.form.get('update_from', datetime.now().strftime('%Y-%m-%d'))
    update_to = request.form.get('update_to', datetime.now().strftime('%Y-%m-%d'))

    # Checking the format and changing it an appropriate for Bank API
    try:
        update_from_date = datetime.strptime(update_from, '%Y-%m-%d')
        update_to_date = datetime.strptime(update_to, '%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Invalid date format. Use yyyy-mm-dd."}), 400

    # Making sure that the sheet is empty
    sheet.clear()
    sheet.append_row(["Date", "Exchange Rate (USD)"])

    # Filling up the spreadsheet from update_from_date to update_to_date
    while update_from_date <= update_to_date:
        date_str = update_from_date.strftime("%Y%m%d")
        url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date={date_str}&json"
        response = requests.get(url)
        rates = response.json()
        if rates:
            rate_usd = rates[0].get("rate")
            sheet.append_row([update_from_date.strftime("%Y-%m-%d"), rate_usd])

        update_from_date += timedelta(days=1)

    # Rerouting the user to the update_success.html page
    return render_template('update_success.html', sheet_url=sheet_url)


# Making similar function to enable updating today's rate
@app.route('/update_today_rate', methods=['POST'])
def update_today_rate():
    today = datetime.now().strftime('%Y%m%d')
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date={today}&json"
    response = requests.get(url)
    rates = response.json()
    if rates:
        rate_usd = rates[0].get("rate")
        sheet.clear()
        sheet.append_row(["Date", "Exchange Rate (USD)"])
        sheet.append_row([datetime.now().strftime('%Y-%m-%d'), rate_usd])

    return render_template('update_success.html', sheet_url=sheet_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
