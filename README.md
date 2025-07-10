# django-user-management
# django-user-management
 Django User Management System 

Welcome to the Django User Management System, a sleek web app built with Django 5.2.4 and Python 3.13.2!  Featuring a blue sticky navbar and fixed footer, this app offers user registration, real email verification, a welcoming dashboard, profile updates, and secure login/logout. Deployed on Render’s free tier, it’s perfect for learning Django with a modern Bootstrap 5 UI. Clone it and make it yours! 

Live at insert Render URL here. Dev.to article: [insert Dev.to URL here].

 Features




commit
User Registration : Sign up with username, email, and password.



Email Verification : Receive a verification link via email (console-based for testing).



Dashboard : Welcoming page for verified users.



Profile Update : Edit username, email, and bio.



Login/Logout : Secure authentication with a custom logout page.



UI : Blue sticky navbar (fixed-top), fixed footer, Bootstrap 5, and django-widget-tweaks.



Tests : Unit tests for models and views.



Deployment : Hosted on Render’s free tier.


Prerequisites





Python 3.13.2 



Git 



Virtualenv 



A free Render account 

Clone and Set Up





Clone the Repository:

git clone https://github.com/your-username/user_management.git
cd user_management



Create Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate



Install Dependencies:

pip install -r requirements.txt



Apply Migrations:

python manage.py migrate



Create Superuser:

python manage.py createsuperuser



Run Server:

python manage.py runserver

Access at http://localhost:8000.

 Email Verification





Register at http://localhost:8000/register/.



Check your terminal for the verification link (console backend).



Visit the link (e.g., http://localhost:8000/verify-email/<token>/), click “I’ve Clicked the Link,” and land on the dashboard.

 Running Tests

python manage.py test
