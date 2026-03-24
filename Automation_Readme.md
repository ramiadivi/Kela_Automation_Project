# KelaProject Automation Framework

## 📌 Overview
This project is an end-to-end automation testing framework built using **Python, Pytest, and Playwright**.

It covers the main flows of the system:
- Login
- Dashboard
- Tasks
- Events
- Urgent Events

# 🏗️ Framework & Design Choices

## ✅ Why Pytest
- Simple and powerful test runner
- Rich plugin ecosystem (parallel execution, reporting)
- Easy parametrization and fixtures

## ✅ Why Playwright
- Fast and reliable browser automation
- Built-in auto-waiting mechanism
- Modern locator strategies (`get_by_test_id`, `get_by_role`)

## ✅ Design Pattern: Page Object Model (POM)

### Why POM?
- Improves maintainability
- Reduces duplication
- Makes tests readable

separated UI logic from tests:

- **pages/** → UI interactions
- **tests/** → test scenarios
- **reports** → test reports

📁 Project Structure

KelaProject/
│
├── tests/
│   ├── test_login.py
│   ├── test_dashboard.py
│   ├── test_tasks.py
│   ├── test_urgent_events.py
│   ├── test_view_events.py
│   ├── utils
│	 ├── test_data/
│	    ├── empty_fields_login.csv
│	    ├── invalid_users.csv
│	    ├── valid_users.csv
│	    ├── valid_tasks.csv
│	    ├── valid_urgent_events.csv
│	    ├── valid_users.csv
│	    ├── view_events.csv
│   ├── reports/
│       ├── report.html
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
├── conftest.py
└── pytest.ini

# 📦 Installation

## 1. Clone the repository

git clone < https://github.com/ramiadivi/Kela_Automation_Project.git >

## 2. Install dependencies

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

## 3. Install Playwright browsers

playwright install chromium

# ▶️ Running Tests

## 🔹 Headless
SET headless=True in the "conftest.py" file or Run from terminal headless


## 🔹 Headed (UI mode)
SET headless=False in the "conftest.py" file or Run from terminal headed

## 🔹 Test Run
Single test run can be done from UI or terminal using test name e.g. pytest .\tests\test_dashboard.py
All tests run can be done from UI or terminal using pytest .\tests\

# 📊 Test Reports

## Option 1: Pytest default report
Shown in terminal after execution

## Option 2: report.html
Open report.html file in the reports folder

# ✅ Test Coverage

## 🔐 Login
- Valid login
- Invalid credentials
- Empty fields

## 📋 Tasks
- Add task
- Empty task validation
- Task visibility
- Delete task

## 📅 Events
- Add event
- View events
- Event persistence
- Delete event 

## ⚡ Urgent Events
- Add urgent event
- Visibility in event list
- Delete event 

# 🐞 Bugs Found

👉 See full details in `BUGS.md`

