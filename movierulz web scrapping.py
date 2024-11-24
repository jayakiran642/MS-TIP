import requests
from bs4 import BeautifulSoup
import pandas as pd

movies, movie, year, quality, lang, link = [], [], [], [], [], []

for page in range(1, 222):  # Pages 1 to 10
    url = f'https://www.5movierulz.io/movies/page/{page}'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve page {page}")
        break

    soup = BeautifulSoup(response.content, 'html.parser')

    movie_section = soup.find(class_="clearfix row-fluid")
    if not movie_section:
        print(f"No data on page {page}")
        break

    # Extract links
    for a_tag in movie_section.find_all('a', href=True):
        link.append(a_tag['href'])

    # Extract movie details
    titles = movie_section.find_all(class_='boxed film')
    for title_tag in titles:
        try:
            title = title_tag.text.strip()
            movie.append(title.split("(")[0].strip())
            year.append(title.split("(")[1][:4].strip())
            details = title.split(") ")[1]

            # Language
            if "Movie" in details:
                lang_start = 6
                lang_end = details.index("Movie")
                lang.append(details[lang_start:lang_end].strip())

            # Quality
            if details.startswith("H"):
                quality.append("720p/1080p/4K")
            elif details.startswith("B"):
                quality.append("720p/1080p")
            else:
                quality.append("360p/480p")
        except Exception as e:
            print(f"Skipping due to error: {e}")

# Ensure lists are of equal length
min_length = min(len(movie), len(year), len(quality), len(lang), len(link))
movie = movie[:min_length]
year = year[:min_length]
quality = quality[:min_length]
lang = lang[:min_length]
link = link[:min_length]

# Save to Excel
df = pd.DataFrame({
    "Movie Name": movie,
    "Year Of Release": year,
    "Resolution": quality,
    "Language": lang,
    "Link": link
})
df.to_excel("movierulz_with_link.xlsx", index=False)
print("movierulz_with_link_real.xlsx created successfully")
