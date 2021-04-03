from tda import auth, client
import json
from auth import config

try:
    c = auth.client_from_token_file(config.token_path, config.api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome() as driver:
        browser = webdriver.Chrome()

        c = auth.client_from_login_flow(
            driver, config.api_key, config.redirect_uri, config.token_path)

            
print(c.get_quote("SPDR").json())