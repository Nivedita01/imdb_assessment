Steps to configure this project into your system.

1. Install Git if you don’t have in your system from the site:

  	    https://git-scm.com/download/win
	
2. Open Git Bash and clone this repository in a directory using the command

  	    git clone https://github.com/Nivedita01/imdb_assessment.git
	
3. Once the project is cloned, open the project location in windows command prompt.

4. Open terminal and activate virtual environment using the command

   	   .\venv\Scripts\activate

5. Install requirements.txt on this virtual environment using the command

	   pip install -r requirements.txt

6. Run test suite using the command

		a.	pytest Tests/test_CreateAccountPage.py
		b.	pytest Tests/test_UserHomePage.py
