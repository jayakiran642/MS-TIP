# MS-TIP
# Movierulz Web Scraping

This project is a Python-based web scraping tool designed to extract movie information from the Movierulz website, including details like movie name, release year, resolution, language, and download links.

## Features

- **Multi-page scraping**: Automatically retrieves data from up to 221 pages of the website.
- **Movie details extraction**:
  - Movie name
  - Year of release
  - Resolution (e.g., 720p/1080p/4K)
  - Language
  - Download link
- **Error handling**: Skips invalid or incomplete entries with appropriate error logging.
- **Data export**: Saves the scraped data to an Excel file for further use.

## Prerequisites

Ensure you have the following installed:

- Python 3.7 or later
- Required libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
    
Install dependencies using:

```bash
pip install requests beautifulsoup4 pandas
```

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movierulz-web-scraping.git
   cd movierulz-web-scraping
   ```

2. Run the script:
   ```bash
   python movierulz_web_scraping.py
   ```

3. The script will:
   - Scrape movie details from Movierulz.
   - Save the data to an Excel file named `movierulz_with_link.xlsx` in the current directory.

## Output

The output Excel file contains the following columns:

- **Movie Name**: Title of the movie.
- **Year Of Release**: Release year.
- **Resolution**: Available resolutions (e.g., 720p/1080p).
- **Language**: Language of the movie.
- **Link**: Link to the movie's page on Movierulz.

## Notes

- The scraper adheres to ethical scraping practices. Use this tool responsibly.
- The script may stop early if:
  - A page fails to load.
  - No data is found on a particular page.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Disclaimer

This project is for educational purposes only. The use of this scraper is subject to the terms of use of the website being scraped.
