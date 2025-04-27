from faker import Faker
import random
import string

class RandomDataGenerator:
    def __init__(self):
        self.fake = Faker()

    def random_title(self, length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits + " ", k=length)).strip()

    def random_sentence(self, word_count=6):
        return self.fake.sentence(nb_words=word_count)