# Pytest Testing Framework Project

This project demonstrates various testing implementations using the Pytest framework in Python. It covers unit tests, fixtures, parameterized tests, error handling, and test organization.

## 📂 Project Structure
```
pytest/
│
├── conftest.py                # Shared pytest fixtures
├── calculator.py              # Calculator module implementation
├── test_calculator.py         # Calculator module tests
├── test_reversal.py           # String reversal tests
├── test_reversal2.py          # String reversal with error handling tests
├── test_sample.py             # Basic pytest test example
├── test_area.py               # Area calculation tests
├── area.py                    # Area module implementation
├── test1.py                   # Test file 1 using fixtures
├── test2.py                   # Test file 2 using fixtures
├── gfg.py                     # Sample test file 1
├── gfg2.py                    # Sample test file 2
├── main.py                    # Parameterized test examples
├── README.md                  # Project documentation
└── requirements.txt           # Project dependencies
```

## 🛠 Prerequisites
- Python 3+
- pip package manager

## 🚀 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pytest-project.git
   cd pytest-project
   ```
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ✅ Running Tests
### Run all tests
```bash
pytest
```
### Run specific test file
```bash
pytest test_calculator.py
```
### Run tests with verbose output
```bash
pytest -v
```
### Run tests matching a pattern
```bash
pytest -k "test_addition" -v
```
### Run parameterized tests
```bash
pytest main.py -v
```
### Run tests with coverage report
```bash
pytest --cov=.
```

## 🔹 Key Features
- **Basic Test Structure** (`test_sample.py`): Simple pytest test cases
- **Fixtures** (`conftest.py`): Shared test setup & teardown
- **Parameterized Tests** (`main.py`): Multiple input testing
- **Exception Handling** (`test_reversal2.py`): Testing error cases
- **Class-based Test Organization** (`test_area.py`): Organized test classes
- **Shared Fixtures Usage** (`test1.py`, `test2.py`): Leveraging `conftest.py`

## 📌 Dependencies
- `pytest`
- `pytest-cov` (for test coverage reports)

## 🤝 Contributing
1. Fork the project
2. Create a feature branch (`git checkout -b feature/new_feature`)
3. Commit your changes (`git commit -m 'Add new_feature'`)
4. Push to the branch (`git push origin feature/new_feature`)
5. Open a Pull Request

---
This refined README provides clear instructions for setting up, running tests, and understanding the project structure, making it easy for others to contribute or use your pytest examples.

