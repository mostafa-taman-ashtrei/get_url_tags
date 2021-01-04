from bs4 import BeautifulSoup
import requests

class URLTAGS:
    def __init__(self):
        url = str(input('Enter a url: '))
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.text, 'html.parser')
    
    def get_title(self):
        head = self.soup.head.find('title')
        title = head.text if head else None
        return title

    def get_desc(self):
        meta_desc = self.soup.find('meta', attrs={'name': 'description'})
        main_desc = meta_desc.get('content') if meta_desc else None

        meta_og =  self.soup.find('meta', property='og:description')
        og_desc = meta_og.get('content') if meta_og else None

        return main_desc or og_desc or None

    def get_key_words(self):
        meta = self.soup.find('meta', attrs={'name': 'keywords'})
        kw = meta.get('content') if meta else None
        return kw

    def get_image(self):
        meta_og =  self.soup.find('meta', property='og:image')
        img = meta_og.get('content') if meta_og else None
        return img
    
    def get_tags(self):
        return {
            'title': self.get_title(),
            'desc': self.get_desc(),
            'keywords': self.get_key_words(),
            'image': self.get_image()
        }

u = URLTAGS()
print(u.get_tags())