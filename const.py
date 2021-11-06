import dotenv
import os

dotenv.load_dotenv()

CHROME_DRIVER = "C:\\Users\petar\python_projects\chromedriver.exe"
LIB_URL = "https://www.buecherhallen.de/entliehene-medien.html"
USER = os.environ.get("USER")
PASS = os.environ.get("PASS")
