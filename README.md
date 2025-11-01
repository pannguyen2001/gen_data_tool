# Gennerate mock data for "Renew capstone project 2023"

## Description
This project is used to generate mock data for the "Renew capstone project 2023". The project uses pandas library for generating data, flask framework for serving the data and unittest and pytest for testing. Follow TDD principle for development.

## Features
- Generate mock data for the "Renew capstone project 2023"
- Serve the data using flask framework
- Test the data using unittest and pytest
- Use pandas library for generating data
- Use scrapy library for scraping data from the internet
- Use requests library for making http requests
- Use BeautifulSoup library for parsing html data

## Installation
To install the project, follow these steps:
1. Clone the repository:
```
git clone https://github.com/panpan2001/mock-data.git
```
2. Change to the project directory:
```
cd mock-data
```
## Folder structure
The project has the following folder structure:
```
mock-data/
├── app.py
├── data/
│   ├── customer.py
│   ├── customer_address.py
│   ├── customer_contact.py
│   ├── customer_payment.py
│   ├── customer_payment_method.py
│   ├── customer_payment_status.py
│   ├── customer_payment_type.py
│   ├── customer_payment_type_status.py
│   ├── customer_payment_type_status_history.py
│   └── customer_payment_type_status_history_status.py
├── requirements.txt
├── README.md
└── tests/
    ├── test_customer.py
    ├── test_customer_address.py
    ├── test_customer_contact.py
    ├── test_customer_payment.py
    ├── test_customer_payment_method.py
    ├── test_customer_payment_status.py
    ├── test_customer_payment_type.py
    ├── test_customer_payment_type_status.py
    ├── test_customer_payment_type_status_history.py
    └── test_customer_payment_type_status_history_status.py
```

## Usage
1. Install virtual environment:
```
python -m venv .venv
```
2. Activate the virtual environment:
```
source venv/bin/activate or .venv\Scripts\Activate.ps1
```
3. Install the required libraries:
```
pip install -r requirements.txt
```
2. Run the script:
```
python app.py
```

## Testing
To run the tests, use the following command:
```
python -m unittest discover
```

## Deployment
To deploy the application, use the following command:
```
python -m flask run
```

## License
This project is licensed under the MIT License - see the LICENSE file for details

## Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues.

## Acknowledgments
This project is based on the work of the following people:
- [Pham Anh Nhat](https://github.com/panpan2001)

## Contact
For any questions or comments, please contact [Pham Anh Nhat](https://github.com/panpan2001).

## Disclaimer
This project is for educational purposes only and should not be used for any other purpose.

## Notes
- The data is generated using pandas library and using unittest and pytest for testing.
- The data is generated for the "Renew capstone project 2023".
- The data is generated for the following tables:
  - `customer`
  - `customer_address`
  - `customer_contact`
  - `customer_payment`
  - `customer_payment_method`
  - `customer_payment_status`
  - `customer_payment_type`
  - `customer_payment_type_status`
  - `customer_payment_type_status_history`
  - `customer_payment_type_status_history_status`

## References
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [unittest documentation](https://docs.python.org/3/library/unittest.html)
- [pytest documentation](https://docs.pytest.org/en/stable/)
- [flask documentation](https://flask.palletsprojects.com/en/2.2.x/)
- [Python documentation](https://www.python.org/)
- [Scrapy documentation](https://scrapy.org/)
- [requests documentation](https://docs.python-requests.org/en/latest/)
- [BeautifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Selenium documentation](https://www.selenium.dev/documentation/en/)
- [Scrapy-Splash documentation](https://github.com/scrapy-plugins/scrapy-splash)
- [loguru documentation](https://loguru.readthedocs.io/en/stable/)
- [MIT License](https://opensource.org/licenses/MIT)
- [GitHub](https://github.com/)

## Authors
- [Pham Anh Nhat](https://github.com/panpan2001)

## Version
1.0.0

