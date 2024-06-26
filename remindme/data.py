import time
import requests
from remindme import crypto
from remindme.console import console
from yaml import load
from yaml import Loader
from rich.spinner import Spinner

ENCRYPTED_DATA_URL = "https://raw.githubusercontent.com/aaronbruckner/remind_me/main/resources/data.enc"

def pull_latest_data(password: str) -> dict:
    spinner = Spinner("dots", "Downloading and decrypting love...")
    with console.status(spinner):
        time.sleep(1.5)
        encrypted_data = requests.get(ENCRYPTED_DATA_URL).content
        decrypted_data = crypto.decrypt(encrypted_data, password)
        return load(decrypted_data, Loader)