from scrape.scraper import fetch_chapter
from versioning.db import save_version
from human_loop.ui import app
import os

def main():
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    txt = fetch_chapter(url, "scrape/chapter1.txt", "scrape/screenshots")
    print("Fetched!")
    os.makedirs("human_loop/data", exist_ok=True)
    #import subprocess; subprocess.run(["python","human_loop/ui.py"])
    import subprocess; subprocess.run(["python", "-m", "human_loop.ui"])
    final_path = "human_loop/data/final.txt"
    if not os.path.exists(final_path):
        raise FileNotFoundError("Final text file not created. Was the flow interrupted?")

    with open(final_path, encoding="utf-8") as f:
        final = f.read()

    vid = save_version("chapter1", final, {"source_url": url})
    print("✅ Saved version:", vid)
    # final = open("human_loop/data/final.txt").read()
    
    # vid = save_version("chapter1", final, {"source_url": url})
    # print("Saved version", vid)

if __name__=="__main__":
    main()
