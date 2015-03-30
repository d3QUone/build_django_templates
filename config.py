#
# Vladimir Kasatkin. April, 2015
#
# --- EXAMPLE ---
#
# Run the 'build.py' script after doing "python manage.py collectstatic" 
#


# Django's standart folder-style
SOURCE_DIRS = [
	"example/core/templates/core/",
	"example/user_profile/templates/user_profile/"
]

# results will be saved here
TARGET_DIR = "example/templates/" 


# all files that have [[[ "file_name.html" ]]] - include tag OR must be in target dir 
TARGET_FILES = [
	"base.html",
	"core__index.html",
	"core__question_page.html",
	"user_profile__base.html"
]



"""
Output in this example:

$ python build.py

Found "navbar.html"
Found "navbar.html"
File "example/templates/base.html" complete with 2 insertions
--------------------------------------------------------------------------------
File "example/templates/core__index.html" complete with 0 insertions
--------------------------------------------------------------------------------
File "example/templates/core__question_page.html" complete with 0 insertions
--------------------------------------------------------------------------------
Found "user_profile login.html"
Found "login form validation.js"
File "example/templates/user_profile__base.html" complete with 2 insertions
--------------------------------------------------------------------------------
"""
