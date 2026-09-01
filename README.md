# BMI Calculator

A simple command-line Body Mass Index (BMI) calculator written in Python. It takes a user's weight and height, calculates their BMI and then classifies the result into a standard weight category.

---

## Features

- Calculates BMI from weight (kg) and height (m)
- Classifies BMI into standard categories
- Validates input and re-prompts on invalid entries (non-numeric, zero or negative values)
- No external dependencies, uses only the Python standard library.

---

## BMI Formula

```
BMI = Weight (kg) / Height (m) ** 2
```

---

## BMI Categories

| BMI Range     | Category      |
|---------------|---------------|
| Below 18.5    | Underweight   |
| 18.5 – 24.9   | Normal weight |
| 25.0 – 29.9   | Overweight    |
| 30.0 and above| Obesity       |

---

## Requirements

- Python 3.7 or higher.

---

## Installation / Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/AdarshZolekar/BMI-Calculator.git
   cd BMI-Calculator
   ```
2. No dependencies to install, the project only uses Python's standard library.

---

## How to Run

```bash
python bmi_calculator.py
```

---

## Example Usage

```
=== BMI Calculator ===

Enter your weight in kilograms: 70
Enter your height in meters: 1.75

Your BMI is: 22.86
Category: Normal weight
```

---

## Project Structure

```
BMI-Calculator/
│
├── README.md
├── bmi_calculator.py
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributions

Contributions are welcome!

- Open an issue for bugs or feature requests

- Submit a pull request for improvements.


<p align="center">
  <a href="#top">
    <img src="https://img.shields.io/badge/%E2%AC%86-Back%20to%20Top-blue?style=for-the-badge" alt="Back to Top"/>
  </a>
</p>


