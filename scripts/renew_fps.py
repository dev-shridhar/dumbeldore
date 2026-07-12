#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

SERVER_URL = os.getenv("FPS_SERVER_URL", "https://panel.fps.ms/server/8cec563e")


def renew_server() -> bool:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=chrome_options)
    try:
        print(f"[INFO] Opening: {SERVER_URL}")
        driver.get(SERVER_URL)
        time.sleep(5)

        add_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Add 24 hours')]")
            )
        )
        print("[INFO] Found renewal button, clicking...")
        add_button.click()
        time.sleep(10)
        print("[SUCCESS] Server renewed!")
        return True
    except Exception as e:
        print(f"[ERROR] {e}")
        return False
    finally:
        driver.quit()


if __name__ == "__main__":
    success = renew_server()
    sys.exit(0 if success else 1)
