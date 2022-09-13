"""
Name: kerboodle-scraper
Description: Scrape any kerboodle textbook into a PDF file
Author: Sanjay Sunil
"""
import wget
import os
from PIL import Image

textbook_id = input("Kerboodle Textbook ID: ")
start_page = int(input("First page (image) number: "))
end_page = int(input("Last page (image) number: "))
textbook_name = input("PDF file name: ")
os.system('mkdir tmp')

for i in range(start_page, end_page+1):
    wget.download(
        f'http://assets-runtime-production-oxed-oup.avallain.net/ebooks/{textbook_id}/images/{i}.jpg', out='tmp')

images = [Image.open(f"tmp/{page_number}.jpg").convert('RGB')
          for page_number in range(start_page, end_page+1)]
images[0].save(
    textbook_name + '.pdf', "PDF", resolution=100.0, save_all=True, append_images=images[1:]
)
os.system('rm -rf tmp')
