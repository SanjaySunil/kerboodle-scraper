<!-- Header -->
<br/><br/>
<h1 align="center">kerboodle-scraper</h1>
  <p align="center">
    Scrape any kerboodle textbook and convert into a PDF
    <br />
    <br />
    <a href="{report_bug}">Report Bug</a>
    ·
    <a href="{request_feature}">Request Feature</a>
  </p>
</h1>
<br/><br/>

<!-- Description -->
## What's kerboodle-scraper?

[kerboodle-scraper]() allows you to scrape any kerboodle textbook from kerboodle.com and combine each of its pages into one PDF file.
<br />



<!-- Installation -->
## Install/Requirements
1. Clone the repository
2. Install project requirements

```py
$ pip install Pillow
$ pip install wget
``` 
<!-- Usage -->
## Usage

When running the program, you will be asked to obtain a kerboodle textbook ID. This ID can be obtained from the following steps.

1. Login to your kerboodle account
2. Open the textbook you would like to scrape
3. Open Inspect Element (F12 or right click, then Inspect Element)
4. Filter out HTML containing the string 'img' (CTRL-F)
5. An image element should be located, and the `src` attribute contains the image file location.
6. Copy the image `src`
7. Format the image `src` where the book ID is the following

`//assets-runtime-production-oxed-oup.avallain.net/ebooks/{book_id}/images/1.jpg`

8. Copy the `book_id`
9. Run the program, and paste `book_id`

```py
python main.py
```

<!-- License -->
## License

Copyright © 2022 Sanjay Sunil (sanjaysunil@protonmail.com)

Distributed under the {license} License. See `LICENSE` for more information.