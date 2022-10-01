import pandas as pd
import random

class LoadQuote(object):
    def __init__(self):
        self.dataset = pd.read_json('./quote.json')
        self.length = len(self.dataset)

    def get(self):
        random_id = random.randrange(0, self.length)

        message = self.dataset.iloc[random_id]["message"]
        author = self.dataset.iloc[random_id]["author"]

        return message, author


if __name__ == "__main__":
    quote_loader = LoadQuote()

    print(quote_loader.get())