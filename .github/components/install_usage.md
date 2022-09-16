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
6. Copy the image `src'
7. Format the image `src` where the book ID is the following

`//assets-runtime-production-oxed-oup.avallain.net/ebooks/{book_id}/images/1.jpg`

8. Copy `book_id` and paste into the kerboodle textbook ID prompt in the program