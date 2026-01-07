# Day 3 – Input Validation Utility

## 📌 Overview
The Input Validation Utility is a command-line application developed using Python that validates common user inputs such as **email**, **password**, and **age**.  
The program ensures that user data follows predefined rules and provides clear, meaningful feedback when invalid input is detected.  
This project focuses on writing clean, readable code while handling user errors gracefully.

---

## 🎯 Problem Statement
Create a utility that validates user inputs such as email, password, and age, ensuring proper error handling and meaningful feedback for invalid data.

---

## 🚀 Features
- Email format validation using regular expressions
- Password strength evaluation (Weak / Medium / Strong)
- Secure password input masking
- Continuous re-prompting until valid input is entered
- Age validation with numeric and range checks
- Clear and user-friendly error messages
- Robust input handling without program crashes

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Libraries Used:**  
  - `re` (Regular Expressions)  
  - `getpass` (Secure password input)

---

## 📚 Concepts Covered
- Functions and modular programming
- String manipulation
- Regular expressions
- Input validation techniques
- Error handling and control flow
- User-friendly CLI design

---

=== Input Validation Utility ===

Enter your email: bhargavi@gmail.com
✅ Valid email

Enter your password:
❌ Password is too weak.
Please try again.

Enter your password:
✅ Password strength: Strong

Enter your age: 21
✅ Valid age

🎉 All inputs validated successfully!

---

## ▶️ How to Run the Project
1. Clone or download the repository
2. Navigate to the project directory
3. Run the following command:

```bash
python input_validator.py
