# **Automation of Scheduling on Prenotami**  

This script automates the login process and checks for appointment availability on the **Prenotami** website, updating a **Google Sheets** spreadsheet with the retrieved information.  

## **Features**  
- ✅ Logs into the **Prenotami** website.  
- ✅ Checks the availability of services, such as **"First Passport Appointment"**.  
- ✅ Updates a **Google Sheets** spreadsheet with the availability status.  
- ✅ Performs multiple automatic attempts in case of failures or unavailability.  

## **Prerequisites**  

### **Python 3.8+**  

Required libraries (install with pip):  
- `seleniumbase`  
- `gspread`  
- `oauth2client`  
- `python-dotenv`  

## **Browser Management**  

The script uses **seleniumbase**, which **automatically manages** the browser (**Chrome**) and **ChromeDriver**.  
No manual installation or configuration of **ChromeDriver** is needed.  

## **Credentials for Google Sheets**  

- A **JSON** file with credentials from a **Google Cloud** service account.  
- Environment variables configured to access credentials and the spreadsheet.  

## **Setup**  

### **1. Creating the .env file**  
Create a `.env` file in the root of the project with the following variables:  

#### `.env`:  
```ini
GCHAVE=path/to/credentials.json
SPREADSHEET_ID=spreadsheet-id
MAIL=user-email
PASSWORD=user-password
```

2. Setting up Google Cloud
Enable the Google Sheets and Google Drive APIs in Google Cloud Console.
Create a service account and download the JSON file with credentials.
Share your Google Sheets spreadsheet with the service account email.viço.

3. Installing Dependencies
Install the required libraries with the following command:
```
pip install seleniumbase gspread oauth2client python-dotenv
```

## How to Use

Ensure the .env file is correctly configured.
Run the script with:
```
python login.py
```

## Script Structure

### Main Functions

#### realizar_tentativa()
* Logs into the Prenotami website.
* Checks for service availability.
* Updates a Google Sheets spreadsheet with the obtained status.

#### chamar_tentativa()
* Manages the number of automatic attempts in case of failures or unavailability.
* Retry mechanism - The script performs multiple attempts until it succeeds or reaches the configured limit.

## Notes
* ✅ Seleniumbase automatically manages the browser (Chrome) and ChromeDriver.
* ✅ No need to manually install or configure ChromeDriver.
* ✅ The script runs in headless mode (without displaying the browser).
* ✅ Include delays between attempts to avoid being blocked by the website.
* ✅ Ensure the Prenotami website is accessible at the time of execution.

🚀 This automation simplifies appointment scheduling and tracking for Prenotami!
