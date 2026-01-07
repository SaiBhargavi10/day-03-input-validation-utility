# 🕷️ Input Validation Utility (GUI Version)

A responsive **GUI-based input validation web application** built using **Python (Flask)**, **HTML**, and **CSS**.  
This project validates **email, password, and age** inputs with strong defensive programming and provides **Spider-Man–inspired animated feedback** for invalid inputs.

This project is an enhanced GUI version of a CLI-based input validator and is part of the **30 Days – 30 Projects** challenge (Day 3).

---

## 🚀 Features

- ✅ Email validation using regex  
- ✅ Password strength validation  
- ✅ Age validation (numeric & range-based)  
- ❌ Animated error feedback (shake + glow)  
- 🕷️ Spider-Man–style animations:
  - Web-shoot animation
  - Validation failed badge
  - Screen flash
- 🪟 Non-blocking **popup modal** for invalid input
- 🔄 Proper UI reset after closing popup (no stuck state)
- 📱 Responsive and clean UI design

---

## 🧠 Concepts Covered

- Defensive programming
- Server-side validation (Flask)
- Regular expressions (Regex)
- HTML form handling
- CSS animations & transitions
- UI/UX best practices
- State management for error handling

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML5, CSS3
- **Validation:** Server-side (Python)
- **Animations:** CSS + minimal JavaScript

> ❌ No database  
> ❌ No frontend frameworks  
> ❌ No external libraries  

---

## 📂 Project Structure

day-03-input-validation-utility/
│
├── input_validator.py
│
├── templates/
│ └── index.html
│
├── static/
│ ├── style.css
│ └── animations.js
│
└── README.md


## 📋 Validation Rules

### 📧 Email
- Cannot be empty
- Must follow valid email format

### 🔐 Password
- Minimum 8 characters
- At least one uppercase letter
- At least one number
- At least one special character

### 🎂 Age
- Must be numeric
- Allowed range: 18–60

---

## 🎮 User Experience Flow

| Action | Behavior |
|------|---------|
| Invalid submit | Animated popup shown |
| Popup OK click | Error state fully cleared |
| Form | Returns to normal editable state |
| Valid submit | Success message displayed |

---

## ▶️ How to Run the Project

1. Clone or download the repository
2. Open terminal in the project folder
3. Install Flask:
   ```bash
   pip install flask
Run the application:

bash
python input_validator.py
Open browser and visit:
http://127.0.0.1:5000/

📌 Credits
This project was originally forked from a CLI-based input validation utility and extended into a full GUI web application with enhanced UI, animations, and improved user experience.

📄 License
This project is open-source and intended for learning, practice, and portfolio use.