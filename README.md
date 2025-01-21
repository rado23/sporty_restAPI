# PoetryDB API Test Automation - README

## Overview
This project automates API testing for **PoetryDB**, verifying poem retrieval and error handling. The tests ensure the API returns correct responses for valid and invalid queries.

## Technologies Used
- **Python** (Test automation scripting)
- **PyTest** (Automated API testing)
- **Requests** (HTTP requests for API testing)
- **PyTest-HTML** (Generating test reports)

## Project Structure
```
poetrydb_tests/
│── tests/
│   ├── test_poetrydb.py        # API test cases for PoetryDB
│   ├── conftest.py             # PyTest fixtures (if needed)
│
│── reports/                    # Test reports (HTML, logs)
│
│── requirements.txt             # Python dependencies
│── pytest.ini                   # PyTest configuration
│── README.md                    # Documentation
```

## Test Cases
| **Test Case** | **Description** | **Expected Result** | **Validation Method** |
|--------------|----------------|--------------------|------------------|
| **Fetch Poem by Title** | Get a poem with title "Ozymandias" | Returns a poem with correct title & content | Check `status_code == 200`, `title`, and `lines` |
| **Fetch Poem by Invalid Author** | Request a poem from a non-existent author | API returns `404` or an empty list | Check `status_code == 404` or `response.json()` for error message |

## **Validation Methods Used & Why**
| **Validation Type** | **Purpose** | **Why Used?** |
|------------------|-----------|------------|
| **Status Code Validation** | Ensures API request success (`200 OK`) or proper error handling (`404 Not Found`) | Confirms expected response type (success or failure) |
| **JSON Response Validation** | Verifies correct structure (e.g., title, lines in PoetryDB) | Ensures API returns structured, correct data |
| **Empty List Validation** | Ensures no invalid data returned for non-existent queries | Prevents incorrect assumptions about API behavior |

## How to Run the Tests
### 1️⃣ Install Dependencies
Ensure you have **Python 3.9+** installed, then run:
```sh
pip install -r requirements.txt
```

### 2️⃣ Run API Tests
Execute the test suite with:
```sh
pytest -v --html=reports/test_report.html --self-contained-html
```

### 3️⃣ View Test Report
After execution, open the HTML test report:
```sh
open reports/test_report.html
```

## Contributors
- **Developer:** Rado Rozkowinski


