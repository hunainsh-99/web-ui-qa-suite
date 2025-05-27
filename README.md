![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

# Web UI QA Suite

## Setup

1. Clone the repo  
   `git clone https://github.com/hunainsh-99/web-ui-qa-suite && cd web-ui-qa-suite`

2. Create a virtual environment  
   `python3 -m venv venv`

3. Activate the environment  
   `source venv/bin/activate`

4. Install dependencies  
   ```
   pip install --upgrade pip
   pip install -r requirements.txt
   pip install flask webdriver-manager locust
   ```

## Running tests

- Run UI + API tests  
  `unset BASE_URL && pytest`

- Run Locust load test  
  ```
  python3 -m performance.server
  locust -f performance/locustfile.py --host http://127.0.0.1:8000 --headless -u 20 -r 5 --run-time 30s
  ```

## Reports

After a test run, open:  
`reports/report.html`

## Project Structure

```
web-ui-qa-suite/
├── pages/         # HTML and page objects
├── tests/         # pytest tests
├── performance/   # server + locust
├── reports/       # generated test reports
├── .github/       # CI config
├── README.md
├── requirements.txt
└── pytest.ini
```

## License

MIT