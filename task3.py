#webpage title scraper

import requests as r
import re

def scraper(url, output):
    response = r.get(url)
    match = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
    
    if match:
        title = match.group(1).strip()
        with open(output, "a", encoding="utf-8") as file:
            file.write(title + "\n") 
        print(f"title saved: \"{title}\"")
    else:
        print("title not found :( ")

if __name__ == "__main__":
    url = input("enter a website url: ")
    scraper(url, "website_titles.txt")

