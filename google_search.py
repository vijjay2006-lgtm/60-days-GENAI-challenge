from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        )
        page = context.new_page()

        page.goto("https://www.google.com")

        # Wait for input box
        page.wait_for_selector("textarea[name='q']")

        # Type slowly like a human
        page.fill("textarea[name='q']", "")
        page.type("textarea[name='q']", "Best Python automation examples", delay=120)

        page.keyboard.press("Enter")
        page.wait_for_timeout(2500)

        # Scroll slowly (human behavior)
        for _ in range(3):
            page.mouse.wheel(0, 200)
            time.sleep(1)

        page.screenshot(path="google_search_result_safe.png")
        print("✅ Screenshot saved as: google_search_result_safe.png")

        browser.close()

if __name__ == "__main__":
    run()
