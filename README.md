# 🔐 Encryption Password Manager

<p align="center">

<img src="assets/Screenshot%202026-07-12%20154051.png" width="700">

</p>

<p align="center">
A secure desktop-based Password Manager built with <b>Python</b> and <b>MySQL</b> that encrypts sensitive credentials before storing them in the database.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?style=for-the-badge&logo=mysql)
![Encryption](https://img.shields.io/badge/Security-Encryption-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

</p>

---

# 📖 About The Project

Managing dozens of passwords manually is both inconvenient and insecure.

This project provides a secure password management system where users can safely store their website credentials in an encrypted format. Instead of saving passwords as plain text, every password is encrypted before being stored in the database, ensuring better security against unauthorized access.

The application follows a modular architecture, separating database operations, authentication, encryption, validation, and user interface into different Python modules for better maintainability.

---

# ✨ Features

- 🔐 User Registration & Login
- 👤 Separate vault for every user
- 🔒 Password Encryption before storage
- 🔑 Secure Authentication
- ➕ Add new credentials
- ✏️ Update existing passwords
- ❌ Delete stored credentials
- 📋 View all saved accounts
- 🔍 Search saved credentials
- 🗄️ MySQL database integration
- ⚙️ Environment variable support using `.env`
- 📂 Modular Python project structure

---

# 🛠 Tech Stack

| Technology               | Purpose               |
|--------------------------|-----------------------|
| Python                   | Backend Logic         |
| MySQL                    | Database              |
| mysql-connector-python   | Database Connectivity |
| python-dotenv            | Environment Variables |
| argon2-cffi              | Password Hashing      |
| Custom Encryption Module | Data Encryption       |

---

# 📁 Project Structure

```
Encryption-password-manager/
│
├── assets/
│   ├── screenshots
│
├── app.py
├── auth.py
├── config.py
├── database.py
├── encryption.py
├── models.py
├── ui.py
├── validation.py
├── main.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🔄 Project Workflow

```
============================         ============= FEATURES =============
|           User           |         >                                   <
|            │             |       /         SEARCH PASSWORDS             \
|            ▼             |      |                                        |
|      Login / Register    |       \         SAVE PASSWORDS               /
|            │             |        \                                    /
|            ▼             |         |       UPDATE PASSWORDS           |
|      Authentication      |         |                                  |
|            │             |         |       DELETE PASSWORDS           |
|            ▼             |        /                                    \
|        Dashboard         | ------<         ERROR MANAGEMENT             >
|            │             |        \                                    /
|            ▼             |         |       USER-FRIENDLY INTERFACE    |
|      MySQL Database      |         |                                  |
|            │             |         |       DELETE USER ACCOUNT        |
|            ▼             |        /                                    \
|    Retrieve & Decrypt    |       /         RESET MASTER PASSWORD        \
|            │             |      |                                        |
|            ▼             |       \         LOGOUT                       /
|      Display to User     |         >                                  <
============================         ====================================
```

---

# 🔒 Security Features

This project focuses on protecting user credentials through multiple security measures.

- Passwords are never stored in plain text.
- User passwords are securely encrypted before being inserted into the database.
- Database credentials are stored inside a `.env` file.
- Sensitive configuration files are ignored using `.gitignore`.
- Modular architecture keeps authentication, encryption, and database logic separated.

---

# 📸 Application Screenshots

## Login Page

<img src="assets/Screenshot%202026-07-12%20154051.png">

---

## Dashboard

<img src="assets\Screenshot 2026-07-12 154234.png">

---

## Password Management

<img src="assets\Screenshot 2026-07-12 155051.png">

> More screenshots are available inside the **assets** folder.

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/encryption-password-manager.git
```

---

## 2. Navigate into the project

```bash
cd encryption-password-manager
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file using `.env.example`

Example:

```env
DB_HOST = localhost
DB_USER = your_username
DB_PASSWORD = your_password
DB_NAME = password_vault

fill the required fields in the (.env.example) file and rename it to (.env)
```

---

## 5. Create the Database

Create your MySQL database with name 'password_vault'

The application will create the required tables if they do not already exist.

---

## 6. Run the application

```bash
python main.py
```

---

# 📦 Dependencies

```
argon2-cffi
mysql-connector-python
python-dotenv
```

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

# 🎯 Learning Outcomes

Through this project, I gained practical experience with:

- Writing modular Python applications
- Secure authentication systems
- Encryption and decryption
- MySQL database operations
- Environment variable management
- CRUD operations
- Project organization
- Git & GitHub workflow

---

# 🚀 Future Improvements

- GUI using CustomTkinter
- Password strength meter
- Password generator
- Two-Factor Authentication (2FA)
- Password categories
- Export/Import vault
- Cloud synchronization
- Dark mode interface
- Automatic backup
- Password breach detection

---

# 🤝 Contributing

Contributions, suggestions, and improvements are always welcome.

Feel free to fork the repository, create a new branch, and submit a pull request.

---

# 👨‍💻 Author

**Pushkar Chalukya**

Passionate about Python, Cybersecurity, AI tools, and solving real-world problems through software development.

If you found this project helpful, don't forget to ⭐ the repository!

---

## 📄 License

This project is intended for educational and learning purposes.

Feel free to use and modify it for personal projects.

---

<p align="center">
Made with ❤️ using Python
</p>
