# Password Strength Checker

A modern Python-based password security application that evaluates password strength, identifies common and weak password patterns, provides security recommendations, and generates strong passwords.

---

## Project Overview

The Password Strength Checker is a desktop application built with Python and Tkinter. It provides users with an interactive interface for evaluating password security based on multiple criteria.

The application analyzes passwords using character composition, length, common-password detection, and repeated-character detection. It also provides a password generator for creating stronger credentials.

---

## Features

| Feature                     | Description                                                  |
| --------------------------- | ------------------------------------------------------------ |
| Password Strength Detection | Evaluates the overall strength of a password                 |
| Security Score              | Provides a score based on password characteristics           |
| Common Password Detection   | Identifies frequently used passwords                         |
| Character Analysis          | Checks uppercase, lowercase, numbers, and special characters |
| Password Generator          | Generates strong random passwords                            |
| Show / Hide Password        | Allows users to safely view or hide their password           |
| Clear Password              | Quickly removes the current password                         |
| Security Suggestions        | Provides recommendations for improving password strength     |
| Maximized Interface         | Application opens in a full-size window                      |
| Neon UI                     | Modern cybersecurity-inspired graphical interface            |

---

## Password Strength Analysis

The application evaluates passwords using several security factors:

* Password length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters
* Common password patterns
* Repeated characters

The resulting score is used to classify the password as:

**Very Weak → Weak → Medium → Strong → Very Strong**

---

## Technologies Used

| Technology          | Purpose                           |
| ------------------- | --------------------------------- |
| Python              | Core application development      |
| Tkinter             | Graphical user interface          |
| Regular Expressions | Password pattern validation       |
| Random              | Secure random password generation |
| String              | Character set generation          |

---

## Application Interface

### Main Interface

Add a screenshot of your application here.

```text
![Password Strength Checker](screenshots/main-interface.png)
```

### Password Analysis

Add a screenshot showing a password being analyzed.

```text
![Password Analysis](screenshots/password-analysis.png)
```

### Strong Password Generation

Add a screenshot showing the generated password feature.

```text
![Password Generator](screenshots/password-generator.png)
```

---

## How to Run

### Prerequisites

Make sure Python 3 is installed on your system.

### Clone the Repository

```bash
git clone https://github.com/Sara-png-ops/password-strength-checker.git
```

### Open the Project

```bash
cd password-strength-checker
```

### Run the Application

```bash
python password_checker.py
```

The application will launch in a maximized window.

---

## Project Structure

```text
password-strength-checker/
│
├── password_checker.py
├── README.md
└── screenshots/
    ├── main-interface.png
    ├── password-analysis.png
    └── password-generator.png
```

---

## Security Concepts Demonstrated

This project demonstrates practical concepts related to password security, including:

* Password complexity
* Weak password identification
* Common-password detection
* Character diversity
* Random password generation
* Input validation
* Basic security recommendations

---

## Future Improvements

Possible future enhancements include:

* Password entropy calculation
* More extensive common-password databases
* Password history analysis
* Dark and light interface themes
* Exporting password analysis reports
* Additional password security rules
* Improved accessibility
* Packaging the application as a standalone executable

---

## Learning Outcomes

Through this project, I gained practical experience with:

* Python GUI development
* Tkinter widgets and layouts
* Event-driven programming
* Regular expressions
* Input validation
* Random data generation
* User interface design
* Git and GitHub project management

---

## Author

**Sara Subhan**

B.Tech Computer Science & Engineering

---

## License

This project is created for educational and portfolio purposes.


## 👩‍💻 Author

**Sara Subhan**

Built with Python 🐍 and Tkinter.

