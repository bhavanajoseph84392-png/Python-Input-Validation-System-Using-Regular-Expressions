# Python-Input-Validation-System-Using-Regular-Expressions
# Python Input Validation System Using Regular Expressions

## 📌 Project Overview

The **Python Input Validation System** is a console-based application that validates mobile numbers, passwords, and Gmail address formats using Python's built-in `re` module.

The project uses regular expressions (Regex) to check whether user-provided inputs match predefined validation patterns. It demonstrates how Python can be used to validate common input fields in applications such as registration forms and login systems.

This project was developed using **Python IDLE** to practise regular expressions, object-oriented programming, and input validation.

## 🎯 Project Objectives

- Understand regular expressions in Python.
- Validate Indian mobile number formats.
- Check password complexity requirements.
- Validate the basic format of Gmail addresses.
- Apply object-oriented programming concepts.
- Improve input validation skills using Python.

## ✨ Features

- **Mobile Number Validation:** Checks whether a mobile number contains 10 digits and starts with a digit from 6 to 9.
- **Password Validation:** Checks for a minimum of eight characters, an uppercase letter, a lowercase letter, a digit, and a permitted special character.
- **Gmail Format Validation:** Checks whether an email address follows a basic Gmail address format.
- **Regular Expression Matching:** Uses `re.fullmatch()` to validate the complete input.
- **Object-Oriented Structure:** Organizes validation logic into a class with separate methods.
- **Interactive Input:** Accepts a mobile number, password, and email address from the user.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Development Environment:** Python IDLE
- **Module:** `re` (Regular Expressions)

The `re` module is part of Python's standard library, so no external package installation is required.

## 📚 Concepts Used

### 1. Regular Expressions

Regular expressions are patterns used to search for or validate text. In this project, they check whether the user's input follows specified rules.

### 2. `re.fullmatch()`

The `re.fullmatch()` function checks whether the entire input matches a given regular expression. It returns a match object when the pattern matches and `None` otherwise.

### 3. Classes and Objects

The `Validation` class stores the mobile number, password, and email address. An object of the class calls the corresponding validation methods.

### 4. Constructor (`__init__`)

The constructor initializes the object with the input values supplied by the user.

### 5. Conditional Statements

`if` and `else` statements determine whether each input matches its required pattern and display the appropriate result.

### 6. User Input

Python's `input()` function collects the mobile number, password, and email address from the user.

## 📂 Project Structure

```text
Python-Input-Validation/
│
├── input_validation.py
└── README.md
```

## ⚙️ Requirements

- Python 3.x
- Python IDLE or Visual Studio Code

No third-party libraries are required.

## 🚀 How to Run the Project

### Step 1: Open Python IDLE

Open Python IDLE on your computer.

### Step 2: Create a Python File

Create a new file named `input_validation.py`.

### Step 3: Add the Code

Paste the Python input validation code into the file and save it.

### Step 4: Run the Program

In Python IDLE, select **Run → Run Module** or press **F5**.

### Step 5: Enter the Inputs

Provide the requested mobile number, password, and email address. The program displays the validation result for each input.

## 🔄 Application Workflow

1. Import Python's `re` module.
2. Define the `Validation` class.
3. Initialize the mobile number, password, and email address.
4. Apply the mobile number regular expression.
5. Apply the password complexity regular expression.
6. Apply the Gmail format regular expression.
7. Display the result of each validation.
8. End the program after all checks are completed.

## 🔍 Validation Rules

| Input | Validation rule |
|---|---|
| Mobile number | Exactly 10 digits, starting with 6–9 |
| Password | At least 8 characters, with uppercase, lowercase, digit, and an allowed special character |
| Gmail address | Basic address format ending in `@gmail.com` |

These are basic application-level checks. They do not independently confirm that a mobile number is active, that a Gmail account exists, or that a password is secure against every type of attack.

## 💻 Example Output

```text
Enter mobile number: 9876543210
Enter password: Hello@123
Enter email: example@gmail.com

Valid Indian number
Valid Password
Valid Gmail format
```

The output above illustrates an example in which all three inputs match the validation patterns.

## 🔐 Limitations

- Mobile number validation checks the format only, not whether the number is active or belongs to a particular person.
- Password validation checks the specified character requirements but does not measure password strength comprehensively.
- Gmail validation checks a basic format only and does not verify whether the email account exists.
- The application runs in the console and does not include a graphical interface.
- The application does not store validated information in a database.

## 🔮 Future Enhancements

- Add more comprehensive email format validation.
- Improve mobile number validation using country-specific rules.
- Provide clearer error messages for each failed condition.
- Add repeated password entry and password confirmation.
- Integrate validation into a registration form using Flask.
- Store user records in MySQL or SQLite.
- Create automated test cases for valid and invalid inputs.
- Build a graphical interface using Tkinter.

## 📚 Learning Outcomes

Through this project, I practised:

- Using regular expressions to validate text.
- Working with Python's built-in `re` module.
- Applying `re.fullmatch()` for complete input validation.
- Creating classes, constructors, and methods.
- Using conditional statements to display validation results.
- Building a simple, interactive Python console application.


## 📄 Disclaimer

This project was developed for educational purposes to practise Python programming and regular expression-based input validation. It is a basic demonstration and is not a complete authentication or security system.
