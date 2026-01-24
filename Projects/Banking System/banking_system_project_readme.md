# 🏦 Banking System (Python CLI Project)

A simple **command-line banking system** built with Python. This project allows users to create and manage bank accounts, perform deposits and withdrawals, and view transaction history. Account data is stored persistently using CSV files.

---

## ✨ Features

- ✅ Add new bank accounts
- 👀 View all bank accounts
- ❌ Remove bank accounts (password protected)
- 💰 Deposit and withdraw money (password protected)
- 📄 View last transaction (password protected)
- 🧠 Input validation with custom error handling
- 💾 Persistent storage using CSV files

---

## 🗂 Project Structure

```
.
├── main.py                 # Entry point & main menu
├── bankingfunctions.py     # Core banking logic (BankingSystem class)
├── errorhandlimg.py        # Input validation & error handling
├── bankinginformation.csv  # Stores account data (auto-generated)
└── README.md               # Project documentation
```

---

## 🚀 How to Run the Project

1. Make sure you have **Python 3.x** installed.
2. Place all files in the same directory.
3. Run the program:

```bash
python main.py
```

The menu will appear in the terminal and guide you through all available options.

---

## 🔐 Account Security

- Each account is protected by a password
- Sensitive actions (remove account, deposit/withdraw, view transactions) require authentication
- Users are limited to **3 password attempts**

---

## 🧾 Data Storage

- Account data is stored in `bankinginformation.csv`
- The system automatically loads existing accounts on startup
- Data fields include:
  - First Name
  - Last Name
  - Username
  - Email
  - Password
  - Account Balance
  - Last Transaction

---

## 🛠 Error Handling

Custom input validation functions ensure:

- Integers are valid (`int_errorhandling`)
- Floats are valid and rounded to 2 decimals (`float_errorhandling`)
- Strings are not empty (`str_errorhandling`)
- Emails follow a valid format (`email_errorhandling`)

This prevents crashes and improves user experience.

---

## 📌 Notes & Limitations

- Passwords are stored in **plain text** (for learning purposes only)
- Only the **last transaction** is stored per account
- Not intended for real-world banking use

---

## 🔮 Possible Improvements

- Encrypt or hash passwords
- Store full transaction history per account
- Add unique account IDs
- Improve username collision handling
- Replace CSV storage with a database (e.g. SQLite)
- Add unit tests

---

## 📚 Learning Outcomes

This project demonstrates:

- Object-Oriented Programming (OOP)
- File handling with CSV
- Input validation & error handling
- Menu-driven CLI applications
- Basic authentication logic

---

## 👤 Author

Created as a Python learning project to practice real-world application logic and data handling.

Happy coding! 🚀

