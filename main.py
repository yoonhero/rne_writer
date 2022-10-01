import time
from creator import MakeWords
from crawler import Crawler
from dataset import LoadQuote

creator = MakeWords()
crawler = Crawler()
dataset = LoadQuote()

while True:
    contents,author = dataset.get()

    generated = creator.create(contents)

    print(f"Generated: {generated}")

    crawler.write(author,generated)

    time.sleep(3)

