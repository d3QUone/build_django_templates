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


TARGET_FILES = [
	"base.html",
	"core__index.html",
	"core__question_page.html",
]