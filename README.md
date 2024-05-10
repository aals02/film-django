# COMP208: MovieMate
Group 8: Aaliyah Gangat, Alex Goddard, Putri Monica, Rafi’ah Nadeem, Samiya Ali, Xiaowei Zhang

Selecting movies for group viewing often leads to the common setback of someone having already seen the chosen film. Our system addresses this by offering a movie suggestion engine that integrates user preferences. Users create accounts, input relevant details, and add friends to form a network. To ensure data security, our system employs encryption algorithms and multiple password-protected databases. We will then perform multiple SQL queries to identify ‘matches’. Drawing inspiration from Tinder, our interface displays movies with their posters, a brief synopsis, and main cast members, users can then mark a movie as watched or ‘swipe’ to show their preference. These movies will be randomly generated using the TMDb API. When linked users indicate similar preferences, the system identifies and recommends these mutual choices. This streamlined approach aims to simplify movie selection among friends, ensuring a more cohesive and enjoyable viewing experience.

# Follow carefully to ensure the system is configured correctly.

Installation:

Python installation: As the ‘pip’ command is integral for our system’s use with Django, Python 3.4 or later needs to be used. The following link can be accessed in order to download Python for the first time: https://www.python.org/ .

Installing Django: Enter the following command within the terminal to install Django:‘pip install Django’ in the terminal. Use “pip --version” to ensure you have pip, if not then download from https://pypi.org/project/pip/ .

Running the code:

Clone the repository from github or download the source code.
Open your terminal or command prompt and navigate to the project directory where you want the source code to run from.
If you’re using github, obtain the code url from the green button called code and write the following command in terminal ‘git clone "(add url here)"’ 
To successfully clone the repository on your local machine, write ‘code film django’ in the terminal.
To ensure code is up to date, write ‘git pull’ in the terminal. If not up to date, insert ‘git fetch’ to get the updated code.
To check whether there have been no changes in the database, write ‘python manage.py makemigrations’. 
If there are any changes, write ‘python manage.py migrate’ to insert the changes.
To obtain the movies and their information from the TMDB API, after the migrations, write ‘python manage.py api_call 1 5’.
‘1 5’ refers to the number of pages accessed by API. If more movies are required for testing purposes the following command can be executed ‘python manage.py api_call 1 10’.
Once these steps are successfully completed, run the command ‘python manage.py runserver’.
Within the terminal you will receive a URL which will lead you to the website’s homepage.

#

*This product uses the TMDB API but is not endorsed or certified by TMDB.*


<img src="https://github.com/aals02/film-django/assets/54577192/75231f8f-92b8-447c-b08b-7338860f2a84" width="100" height="100">
