### 🏥 HEALTH INFORMATION SYSTEM
A simple Flask-based web application that allows health workers to manage clients and health programs effectively. The system supports client registration, program creation, enrollment, profile viewing, and API exposure for integration with other systems.



## 📌 FEATURES
Create health programs (e.g. Mental health, Dental care etc)

Register new clients into the system

Enroll clients into one or more health programs

Search and list registered clients

View client profiles with enrolled programs

Expose client profiles via a simple JSON API

Clean responsive frontend with a fullscreen background image


Organized folder structure with separate templates, static (CSS & images), and database

Data stored locally using SQLite



## 🖥️ TECH STACK
Backend: Python 3.13, Flask 3.x

Frontend: HTML5, CSS3

Database: SQLite

Tools: pip, virtualenv (optional)


## 📂 PROJECT STRUCTURE
health_system/
│
├── app.py
├── database.db
│
├── /templates
│   ├── base.html
│   ├── index.html
│   ├── add_program.html
│   ├── register_client.html
│   ├── enroll_client.html
│   ├── search_client.html
│   └── client_profile.html
│
├── /static
│   ├── /css
│   │   └── style.css
│   └── /images
│      └── bg.jpg



## 🚀 HOW TO RUN
Clone the repo:
git clone <your-repo-link>
cd health_system

Install dependencies:
pip install flask

Run the application:
python app.py

Visit in your browser: http://127.0.0.1:5000



## 📖 API ENDPOINT EXAMPLE
GET /api/client/<client_id>
Returns client profile and enrolled programs in JSON.
{
  "client_name": "John Doe",
  "age": 30,
  "enrolled_programs": ["Malaria", "TB"]
}


👨‍💻 AUTHOR
Ombati Emmanuel Bosire
Bachelor of Information Technology | South Eastern Kenya University


## 🌟 ACKNOWLEDGEMENTS

- Background image from :https://unsplash.com
- Official Flask documentation: https://flask.palletsprojects.com/
- My personal determination and grit 💪🔥

## ## PROTOTYPE PRESENTATION VIDEO

Watch the prototype demo video here:
[View Prototype Video]
https://youtu.be/1jASmKp3lik