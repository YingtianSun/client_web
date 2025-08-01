import requests
from bs4 import BeautifulSoup

def extract_company_info(url):
    try:
        response = requests.get(url, timeout=10)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else "N/A"

        candidates = ['aboutus', 'about', 'company-info', 'about-section']
        about_text = ""
        for cls in candidates:
            section = soup.find('div', class_=cls)
            if section:
                about_text = section.get_text(strip=True)
                break

        if not about_text:
            paragraphs = soup.find_all('p')
            about_text = "\n".join([
                p.get_text(strip=True)
                for p in paragraphs if len(p.get_text(strip=True)) > 60
            ])

        return {
            "title": title,
            "about": about_text
        }

    except Exception as e:
        return {"error": str(e)}