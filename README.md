# **Flask App + Power BI: Manager Performance Dashboard with Exchange Rate Updater**

This project showcases a **Flask-based web application** integrated with a **Power BI dashboard**. The app updates USD exchange rates from the National Bank of Ukraine API into a Google Sheet, which serves as a data source for the dashboard. The dashboard provides key metrics and KPIs, offering insights into manager performance based on call data and deal outcomes.

---

## **Project Overview**

You are provided with an 8-page Excel dataset containing the following information:

- **Managers' names** (4 individuals).
- **Call logs** (start and end times).
- **Pipeline descriptions**.
- **Types of closed and open deals**.
- **Profit amounts in UAH** for each day.

The task involves:
1. Converting profits from UAH to USD using exchange rates from the National Bank of Ukraine.
2. Building a Flask application for fetching and updating exchange rates in a **public Google Sheet**.
3. Creating a **Power BI dashboard** to visualize the most critical metrics and KPIs, such as total profit, call outcomes, and deal performance.

---

## **Live Demo**

### **Key Links**
- **Flask App for Updating Exchange Rates**:  
  [https://projectdeployer.pythonanywhere.com/](https://projectdeployer.pythonanywhere.com/)  

- **Google Sheet with Updated Exchange Rates**:  
  [Exchange Rates Google Sheet](https://docs.google.com/spreadsheets/d/10aKh9FfIQISIuOY2ogh6oRd6BjHSk10FOq8IOCyAE74/htmlview)

---

## **Dashboard Files**

For full access to the dashboard, download the files below:

- **Power BI Report (.pbix)**:  
  [Download PBIX File](https://github.com/MykhailoKononov/flask_app_for_power_bi/blob/main/Project_power_bi_%26_flask.pbix)  
  *(Requires Power BI Desktop to open)*

- **PDF Report**:  
  [Download PDF Report](https://github.com/MykhailoKononov/flask_app_for_power_bi/blob/main/Project_power_bi_%26_flask.pdf)  
  *(For those without Power BI)*
---

## **Features**

- **Update Exchange Rates**: Fetch USD exchange rates for a selected date range or for today.
- **Google Sheets Integration**: Automatically updates exchange rates in a connected Google Sheet.
- **Power BI Dashboard**: Visualizes manager performance metrics with real-time data from the Google Sheet.

---

## **Setup Instructions**

### **Prerequisites**
- **Python 3.x** with Flask and other dependencies.
- **Google Sheets API** credentials for integration.
- **Power BI Desktop** for viewing or modifying the report.

### **Installation**

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/exchange-rate-updater.git
    cd exchange-rate-updater
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Google Sheets API**:
    - Obtain `credentials.json` and place it in the root directory.
    - Update `sheet_id` in `app.py` with your Google Sheet ID.

4. **Run the Application**:
    ```bash
    python app.py
    ```

5. Access the app at [http://localhost:5555](http://localhost:5555).

---

## **How It Works**

1. Use the Flask app to fetch and update exchange rates in the Google Sheet.
2. The Power BI dashboard connects to the updated Google Sheet, providing real-time insights into manager performance.
3. Key metrics include:
   - Total and daily profits (converted to USD).
   - Call success rates.
   - Deal closure performance.

---

## **Files Overview**

- **`app.py`**: Flask application logic.
- **`requirements.txt`**: Dependencies.
- **`templates/`**: HTML views.
- **`report.pbix`**: Power BI dashboard file.
- **`report.pdf`**: Static dashboard report.

---

This project highlights your technical ability to integrate data pipelines, automate updates, and visualize business-critical insights effectively.

1. Visit the home page at `/` to choose a date range or click the button to update the rate for today.
2. After submission, the exchange rates will be updated in the Google Sheet, and you will be redirected to a success page with a link to the updated sheet.

---

This documentation provides a clear setup, feature overview, and usage instructions to help users get started quickly.
