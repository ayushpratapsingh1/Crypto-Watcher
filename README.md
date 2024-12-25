# Cryptocurrency Data Scraping and Display Web Application

This web app scrapes live cryptocurrency data from Yahoo Finance and displays it on a user-friendly website. It includes real-time data such as price, market cap, volume, and 24-hour percentage change. The app also computes total market cap and Bitcoin dominance.

---

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [How It Works](#how-it-works)
- [Example Output](#example-output)
- [Running the Application](#running-the-application)
- [Deploying the Application](#deploying-the-application)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

---

## Features

- **Real-Time Data Scraping**: Scrapes live data from Yahoo Finance.
- **Dynamic Webpage**: Displays cryptocurrency data with real-time updates.
- **Calculated Metrics**: Shows total market cap and Bitcoin dominance.
- **Responsive Design**: Adjusts for mobile and desktop views.
- **Continuous Updates**: Data is updated every 10 minutes.

---

## Technologies Used

- **Python**: For web scraping and data processing.
  - Libraries: `requests`, `beautifulsoup4`, `pandas`
- **Flask**: Web framework for the backend.
- **HTML/CSS**: Frontend design.
- **Jinja2**: Templating engine for dynamic data rendering.
- **UptimeRobot**: Monitors app uptime.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ayushpratapsingh1/Crypto-Watcher.git
   cd <Crypto-Watcher>
2. Create a virtual environment:
   
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install dependencies:
   
   ```bash
   pip install -r requirements.txt

## Configuration
- Web Scraping: The Python script scrapes cryptocurrency data from Yahoo Finance and processes it.
- Flask Setup: Flask serves the scraped data on the webpage, updating every 10 minutes.
- Uptime Monitoring: Use UptimeRobot to monitor the app.

## How It Works
- Data Scraping: Uses requests and BeautifulSoup to scrape live data from Yahoo Finance.
- Backend: Flask renders the data dynamically using Jinja2 templates.
- Calculations: Total market cap and Bitcoin dominance are computed and displayed.

## Example Output
The webpage displays:
- Table of Cryptocurrency Data: Name, price, market cap, volume, and 24-hour change.
- Bitcoin Dominance: Displays Bitcoin's market dominance.
- Total Market Cap: Shows the total market capitalization.

## Running the Application
1. Activate your virtual environment:

   ```
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
2. Run the Flask app:
   ```
   python app.py
   
3. Open in your browser: [http://127.0.0.1:8080]

## Deploying the Application
- Replit: Upload files to Replit for easy deployment.
- Render: Follow the Render guide for deployment.

## Troubleshooting
- ZeroDivisionError: Ensure market cap values are not missing or zero.
- CSS Issues: Make sure CSS is properly linked in the HTML files.

## License
- This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
- Contributions are welcome! Fork the repository and submit a pull request for any improvements or bug fixes.

## Acknowledgements
- BeautifulSoup: For parsing HTML.
- Flask: Web framework for the app.
- UptimeRobot: For uptime monitoring.
