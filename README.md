# LinkHarvest
The Link Scraper Project is a web application built using Django, Bootstrap, and BeautifulSoup4. It allows users to provide a URL, and the application scrapes all the links from the specified page. The scraped links are then displayed for the user to review.

### Table of Contents
- Installation
-  Usage
- Features
- Technologies Used

### Installation

1 Clone the repository:

```bash
git clone https://github.com/rupesh180902/LinkScrapper.git
```

2 Navigate to the project directory:

```bash
cd LinkScrapper
```

3 Apply migrations:

```bash
python manage.py migrate
```

4 Run the development server:

```bash
python manage.py runserver
```

5 Visit http://localhost:8000/ in your web browser.

### Usage
1 Open the application in your web browser.
2 Enter the URL of the webpage you want to scrape in the provided input field.
3 Click the "Scrape Links" button.
4 The application will scrape the links from the provided URL, and the results will be displayed on the page.

### Features
- **URL Input**: Users can input the URL of the webpage they want to scrape links from.

- **Link Scraper**: The application uses BeautifulSoup4 to scrape links from the specified webpage.

- **Results Display**: The scraped links are displayed on the page for the user to review.

- **Download Option**: Users can download the scraped links for further analysis.

### Technologies Used
- Django
- Bootstrap
- BeautifulSoup4

