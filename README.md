# Book Info Scraper

## Overview
Book Info Scraper is a web scraping project that extracts book information from online sources and stores the data in various formats, including XLSX, CSV, and JSON.

## Features
- Scrapes book details such as title, author, price, and rating
- Stores data in multiple formats:
  - **XLSX** (Excel file)
  - **CSV** (Comma-Separated Values)
  - **JSON** (JavaScript Object Notation)

## Requirements
Ensure you have the following dependencies installed:
```bash
pip install requests beautifulsoup4 pandas openpyxl
```

## Installation
1. Clone the repository:
```bash
git clone https://github.com/Anupamm01/Book-info-scrapper.git
```
2. Navigate to the project directory:
```bash
cd Book-info-scrapper
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the script to start scraping book data:
```bash
python main.py
```
After execution, the scraped data will be saved in `books.xlsx`, `books.csv`, and `books.json`.

## Output Files
- **books.xlsx**: Stores the book data in an Excel file.
- **books.csv**: Stores the book data in a structured CSV format.
- **books.json**: Stores the book data in JSON format.

## Contributing
Feel free to fork this repository, create a branch, and submit a pull request if you'd like to contribute improvements!


