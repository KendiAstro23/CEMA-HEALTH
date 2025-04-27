CEMA Health — Fullstack Health Program Management App

A fullstack web application for managing health programs and client appointments, built with:

Backend: Django + Django REST Framework (MySQL/SQLite depending on deployment)

Frontend: React.js (with normal CSS styling)

Deployment: Render (backend) + Vercel (frontend)

PURPOSE OF THIS PROJECT
The project enables users to:

View a list of health programs

Book appointments for programs

View client profiles

Add new health programs (admin feature)

Built with an emphasis on smooth backend-frontend interaction, responsive UI, and deployment readiness.

TECHNOLOGIES USED

LAYER  STACK
Frontend	React.js, React Router DOM, Axios, CSS
Backend	Django, Django REST Framework
Database	MySQL (or SQLite fallback), and PostGres for Render
Hosting	Render (backend), Vercel (frontend)

PROJECT STRUCTURE
bash
Copy
Edit
CEMA-Health/
├── chbackend/      # Django project (APIs, models, views)
├── chfrontend/     # React app (pages, components, routing)
├── README.md       # (this file)

SETUP INSTRUCTIONS

BACKEND SETUP (Django)
Clone the repo

bash
Copy
Edit
git clone into repository
cd CEMA-Health/chbackend

CREATING VIRTUAL ENVIRONMENT AND INSTALLING REQUIREMENTS

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
pip install -r requirements.txt
Setup the database

Local testing → use MySQL or SQLite (by editing settings.py).

For Render → initially set up SQLite if no remote MySQL yet.

MICRATIONS

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate

Run BACKEND LOCALLY

bash
Copy
Edit
python manage.py runserver
Frontend Setup (React)

NAVIGATE TO FRONTEND

bash
Copy
Edit
cd ../chfrontend
Install dependencies

bash
Copy
Edit
npm install
Run FRONTEND LOCALLY

bash
Copy
Edit
npm start
The React app will run at http://localhost:3000.

COMMUNICATION BETWEEN BACKEND AND FRONTEND
Frontend Axios requests point to the deployed backend URL like:

ERROR HANDLING

Issue	Handling
Axios failed requests	.catch blocks log errors and show fallback messages
Pexels API fallback	Removed (switched to using a single default background image)
Django Database Connection Failure	Switched from local MySQL to SQLite for Render
CORS issues	Solved via corsheaders Django package


UI/UX HIGHLIGHTS

Mobile Responsive: Displays 2 cards per row on smaller screens.

Card Design: Default background image for all program cards.

Simple clean navigation using React Router.

Smooth form submissions with success messages and field clearing after adding new programs.

DEPLOYMENT PROCESS
BACKEND DEPLOYMENT (Render)
Create a Web Service on Render

Connect repo → choose Django project

Set PYTHON_VERSION, DJANGO_SETTINGS_MODULE, and PORT in Environment

Install Render build packages (mysqlclient if needed)

Switch database from localhost to SQLite or remote MySQL

FRONTEND DEPLOYMENT (Vercel)
Push React app separately to GitHub

Import project into Vercel

Set REACT_APP_API_URL if using .env for backend links

Deploy automatically

LESSONS LEARNED
The importance of handling CORS policies between domains

Dealing with backend errors like OperationalError on cloud hosting

Building dynamic frontend components that gracefully fallback if backend data is unavailable

Deploying fullstack apps smoothly across different platforms (Render + Vercel combo)



AUTHOR
Name: Dorcas Kendi

GitHub: KendiAstro23

FINAL NOTES
This project showcases how to build a full production-ready fullstack application
with React frontend, Django backend, smooth API communication, and cloud deployment