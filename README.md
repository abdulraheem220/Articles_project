# 📝 Articles Project

A simple yet functional Django-based web application that allows users to register, log in, write, and view articles. This project also includes session-based authentication, profile management, and a clean, user-friendly interface.

---

## 🚀 Features

- 🔐 User Authentication (Login / Register / Logout)
- 🧾 Article Creation and Display
- 🙍‍♂️ Profile Page with Update & Password Change
- 🛡️ CSRF Protection Enabled
- 🎨 Clean and Professional UI with Custom CSS Styling

---

---

## ⚙️ Tech Stack

- **Backend:** Django 5.x (Python 3.12+)
- **Frontend:** HTML5, CSS3
- **Database:** SQLite (default)

---

## 📂 Project Structure

articles_project/ ├── authh/ # Handles user login, registration, and profile ├── articleapp/ # Article creation and display logic ├── templates/ # HTML Templates ├── static/ # CSS and static files ├── db.sqlite3 # Database ├── manage.py


---

## 🛠️ How to Run the Project

1. **Clone the repository**
```bash
git clone https://github.com/your-username/articles_project.git
cd articles_project


2. **Create and activate virtual environment**

python -m venv myenv
myenv\Scripts\activate   # On Windows

3. **Install dependencies**

pip install -r requirements.txt

4.**Run migrations**

python manage.py migrate

5.**Run the server**

python manage.py runserver

You will See http://127.0.0.1:8000/
