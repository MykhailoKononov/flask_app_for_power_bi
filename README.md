# **Flask App for Power BI: Exchange Rate Updater**

This project is a **Flask-based web application** designed to update exchange rates in a Google Sheet. It fetches USD exchange rates from the National Bank of Ukraine API ([bank.gov.ua](https://bank.gov.ua)) for a specified date range or for the current day. The application is hosted and can be accessed through a simple web interface.

---

## **Features**

- **Update Exchange Rate for a Date Range**: Allows users to update the exchange rates between two specified dates.
- **Update Today's Exchange Rate**: Provides an option to update the exchange rate for the current date.
- **Google Sheets Integration**: The application updates a Google Sheet with the exchange rates.

---

## **Setup**

### **Prerequisites**
- **Python 3.x** installed on your machine.
- **Flask** and other dependencies, which can be installed using `pip`.
- **Google Sheets API** enabled and credentials configured. You can get your service account credentials [here](https://developers.google.com/sheets/api/guides/authorizing).
- **API Key for NBU Exchange Rates**: This project uses the National Bank of Ukraine’s API. Ensure you have access to it.

### **Installation**

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/exchange-rate-updater.git
    cd exchange-rate-updater
    ```

2. **Install the required Python libraries**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Google Sheets credentials**:
    - Create a `credentials.json` file for Google Sheets API and place it in the project root.
    - Replace `sheet_id` in `app.py` with your actual Google Sheets ID.

---

## **Running the Application**

To run the application locally, use:

```bash
python app.py
```

The app will run on [http://localhost:5555](http://localhost:5555).

---

## **How It Works**

- **User Input**: The app allows users to specify a date range or opt to update the exchange rate for today.
- **Data Fetching**: Once the exchange rates are updated, the app performs a request to the National Bank of Ukraine API to fetch exchange rates.
- **Google Sheets Update**: The rates are then written to the Google Sheet via the `gspread` library.

### **Google Sheets Format**

The data is written to a Google Sheet with the following columns:
1. **Date**
2. **Exchange Rate (USD)**

**Note**: Make sure to grant view or edit access to the sheet for the service account email from the `credentials.json` file.

---

## **Files and Directories**

- **app.py**: Contains Flask application logic.
- **requirements.txt**: Lists Python dependencies.
- **templates/**: Contains HTML files for rendering views.
    - **update_rate.html**: The form for selecting a date range or updating today's rate.
    - **update_success.html**: The success page after the exchange rate has been updated.
- **credentials.json**: Google Sheets API credentials file (*do not share this file publicly*).

---

## **Usage**

1. Visit the home page at `/` to choose a date range or click the button to update the rate for today.
2. After submission, the exchange rates will be updated in the Google Sheet, and you will be redirected to a success page with a link to the updated sheet.

---

This documentation provides a clear setup, feature overview, and usage instructions to help users get started quickly.
