# Python Unit Test Examples

## 📂 Directory Structure

```bash
pytest/
├── basic_assertions/
│   ├── test_assert_equal.py
│   ├── test_assert_false.py
│   ├── test_assert_not_equal.py
│   └── test_assert_true.py
│
├── comparison_assertions/
│   ├── test_assert_greater.py
│   ├── test_assert_greater_equal.py
│   ├── test_assert_less.py
│   └── test_assert_less_equal.py
│
├── floating_point_assertions/
│   ├── test_assert_almost_equal.py
│   └── test_assert_not_almost_equal.py
│
├── identity_assertions/
│   ├── test_assert_is.py
│   └── test_assert_is_not.py
│
├── membership_assertions/
│   ├── test_assert_in.py
│   └── test_assert_not_in.py
│
├── type_check_assertions/
│   ├── test_assert_is_instance.py
│   ├── test_assert_is_none.py
│   ├── test_assert_is_not_none.py
│   └── test_assert_not_is_instance.py
│
└── README.md
```

## 🧪 Test Categories

### 🔹 Basic Assertions
- **`assertEqual` / `assertNotEqual`** → Check value equality
- **`assertTrue` / `assertFalse`** → Validate boolean conditions

### 🔹 Comparison Assertions
- **`assertGreater` / `assertLess`** → Test relative magnitude
- **`assertGreaterEqual` / `assertLessEqual`** → Compare magnitude with equality

### 🔹 Floating Point Assertions
- **`assertAlmostEqual` / `assertNotAlmostEqual`** → Compare floating point values with tolerance

### 🔹 Identity Assertions
- **`assertIs` / `assertIsNot`** → Validate object identity

### 🔹 Membership Assertions
- **`assertIn` / `assertNotIn`** → Check if an item exists in a container

### 🔹 Type Check Assertions
- **`assertIsInstance` / `assertNotIsInstance`** → Verify object types
- **`assertIsNone` / `assertIsNotNone`** → Check for `None` values

## 🚀 Getting Started

### Prerequisites
- Python **3.6+**
- `pytest` (optional but recommended)

### Installation

```bash
pip install pytest
```

### Running Tests

Run all tests:
```bash
pytest
```

Run a specific test category:
```bash
pytest comparison_assertions/
```

Run an individual test file:
```bash
pytest basic_assertions/test_assert_equal.py
```

Run tests with verbose output:
```bash
pytest -v
```

## ✅ Best Practices

1. **Keep test files focused** → Each file should target one assertion type.
2. **Descriptive test names** → Name test methods clearly to indicate their purpose.
3. **Include both positive and negative cases** → Test expected and edge cases.
4. **Ensure test independence** → Avoid dependencies between tests.
5. **Use fixtures for setup/teardown** → Simplify repetitive test initialization.

## 🤝 Contribution

Contributions are welcome! Please ensure:
- Tests follow the existing structure.
- New tests include both positive and negative cases.
- Code adheres to `pylint` / `flake8` checks.
- Documentation is updated accordingly.

---

