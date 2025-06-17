from playwright.sync_api import sync_playwright
import os

def fetch_chapter(url: str, out_txt: str, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    text_lines = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector('#mw-content-text')
        content = page.locator('#mw-content-text').inner_text()
        page.screenshot(path=os.path.join(out_dir, 'screenshot.png'), full_page=True)
        browser.close()
    with open(out_txt, 'w', encoding='utf-8') as f:
        f.write(content)
    return content

if __name__ == "__main__":
    c = fetch_chapter(
        "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1",
        "scrape/chapter1.txt",
        "scrape/screenshots"
    )
    print("Fetched length:", len(c))
