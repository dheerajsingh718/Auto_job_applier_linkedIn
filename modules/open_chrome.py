'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

Support me: https://github.com/sponsors/GodsScion

version:    26.01.20.5.08
'''

from modules.helpers import get_default_temp_profile, make_directories
from config.settings import run_in_background, stealth_mode, disable_extensions, safe_mode, file_name, failed_file_name, logs_folder_path, generated_resume_path
from config.questions import default_resume_path
import subprocess
import re
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
if stealth_mode:
    import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from modules.helpers import find_default_profile_directory, critical_error_log, print_lg
from selenium.common.exceptions import SessionNotCreatedException, NoSuchWindowException, WebDriverException

def get_installed_chrome_major_version() -> int | None:
    """
    Detect installed Chrome major version on macOS/Linux.
    Returns the major version integer or None if detection fails.
    """
    commands = [
        ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--version"],
        ["google-chrome", "--version"],
        ["google-chrome-stable", "--version"],
        ["chromium", "--version"],
        ["chromium-browser", "--version"],
    ]
    for cmd in commands:
        try:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True).strip()
            match = re.search(r"(\d+)\.", output)
            if match:
                return int(match.group(1))
        except Exception:
            continue
    return None

def get_session_temp_profile() -> str:
    '''
    Create an isolated Chrome user-data-dir for this run.
    Reusing a shared temp profile is a common cause of Chrome startup exits.
    '''
    return tempfile.mkdtemp(prefix="auto-job-apply-chrome-")


def build_chrome_options(options_cls, isRetry: bool = False):
    options = options_cls()
    if run_in_background:   options.add_argument("--headless")
    if disable_extensions:  options.add_argument("--disable-extensions")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-renderer-backgrounding")

    print_lg("IF YOU HAVE MORE THAN 10 TABS OPENED, PLEASE CLOSE OR BOOKMARK THEM! Or it's highly likely that application will just open browser and not do anything!")
    profile_dir = find_default_profile_directory()
    if isRetry:
        print_lg("Will login with a guest profile, browsing history will not be saved in the browser!")
        temp_profile = get_session_temp_profile()
        print_lg(f"Using isolated temporary Chrome profile: {temp_profile}")
        options.add_argument(f"--user-data-dir={temp_profile}")
    elif profile_dir and not safe_mode:
        options.add_argument(f"--user-data-dir={profile_dir}")
    else:
        print_lg("Logging in with a guest profile, Web history will not be saved!")
        temp_profile = get_session_temp_profile()
        print_lg(f"Using isolated temporary Chrome profile: {temp_profile}")
        options.add_argument(f"--user-data-dir={temp_profile}")
    return options


def create_standard_chrome_session(isRetry: bool = False):
    options = build_chrome_options(Options, isRetry)
    driver = webdriver.Chrome(options=options)
    return options, driver


def createChromeSession(isRetry: bool = False):
    make_directories([file_name,failed_file_name,logs_folder_path+"/screenshots",default_resume_path,generated_resume_path+"/temp"])
    # Set up WebDriver with Chrome Profile
    options = None
    if stealth_mode:
        options = build_chrome_options(uc.ChromeOptions, isRetry)
        print_lg("Downloading Chrome Driver... This may take some time. Undetected mode requires download every run!")
        try:
            detected_major = get_installed_chrome_major_version()
            if detected_major:
                print_lg(f"Detected local Chrome major version: {detected_major}")
                driver = uc.Chrome(options=options, version_main=detected_major)
            else:
                print_lg("Could not detect local Chrome version. Falling back to uc default version selection.")
                driver = uc.Chrome(options=options)
        except (SessionNotCreatedException, WebDriverException) as e:
            print_lg("Undetected Chrome startup failed. Falling back to regular Selenium Chrome.", e)
            options, driver = create_standard_chrome_session(isRetry)
    else:
        options, driver = create_standard_chrome_session(isRetry) #, service=Service(executable_path="C:\\Program Files\\Google\\Chrome\\chromedriver-win64\\chromedriver.exe"))
    try:
        driver.maximize_window()
    except (NoSuchWindowException, WebDriverException) as e:
        print_lg("Chrome window could not be maximized. Falling back to a fixed window size.", e)
        driver.set_window_size(1440, 900)
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)
    return options, driver, actions, wait

try:
    options, driver, actions, wait = None, None, None, None
    options, driver, actions, wait = createChromeSession()
except SessionNotCreatedException as e:
    critical_error_log("Failed to create Chrome Session, retrying with guest profile", e)
    options, driver, actions, wait = createChromeSession(True)
except Exception as e:
    msg = 'Seems like Google Chrome is out dated. Update browser and try again! \n\n\nIf issue persists, try Safe Mode. Set, safe_mode = True in config.py \n\nPlease check GitHub discussions/support for solutions https://github.com/GodsScion/Auto_job_applier_linkedIn \n                                   OR \nReach out in discord ( https://discord.gg/fFp7uUzWCY )'
    if isinstance(e,TimeoutError): msg = "Couldn't download Chrome-driver. Set stealth_mode = False in config!"
    print_lg(msg)
    critical_error_log("In Opening Chrome", e)
    from pyautogui import alert
    alert(msg, "Error in opening chrome")
    try: driver.quit()
    except NameError: exit()
    
