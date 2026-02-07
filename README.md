# 🚀 Quiz Nova (AI)

Quiz Nova is a next-generation intelligent quiz platform powered by **Google's Gemini 2.5 Flash** architecture. It features **"Nova"**, a Self-Healing AI Assistant that generates dynamic questions, interacts with users, and ensures a seamless learning experience.

## 🌟 Features
* **🤖 AI-Powered Chatbot (Nova):** Built using the latest `gemini-2.5-flash` model for instant, accurate, and human-like responses.
* **🧠 Dynamic Quiz Generation:** AI creates unique questions based on user topics.
* **🛡️ Self-Healing Mechanism:** Automatically handles API errors and switches logic to ensure zero downtime.
* **🔐 Secure Authentication:** User registration, login, and secure session management.
* **📧 Email Integration:** Sends OTPs and welcome emails (SMTP Configured).

## 🛠️ Tech Stack
* **Backend:** Django (Python)
* **AI Engine:** Google Generative AI (Gemini 2.5 Flash)
* **Database:** SQLite (Dev) / MySQL (Prod)
* **Frontend:** HTML5, CSS3, JavaScript

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/nileshdash25/Quiz-Nova-AI-.git](https://github.com/nileshdash25/Quiz-Nova-AI-.git)
    cd Quiz-Nova-AI-
    ```

2.  **Create & Activate Virtual Environment:**
    ```bash
    python -m venv venv
    venv\Scripts\activate  # For Windows
    ```

3.  **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Start Server:**
    ```bash
    python manage.py runserver
    ```

---
*Built with ❤️ by Nilesh Dash*