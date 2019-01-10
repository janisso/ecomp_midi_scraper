#copied code from https://realpython.com/python-web-scraping-practical-introduction/ for web text wrangling

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup as bs
import os

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def remove_colon(text):
    col_ind = text.find(':')    #find index of colon in the string
    name = text[col_ind+1:]     #remove 'Name:' from string
    while name[0]==' ':
        name = name[1:]
    return name

class competitor(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        
curr_path = os.path.dirname(os.path.abspath(__file__))
url = curr_path+"/pages/ecomp_2018.asp"

#print get(url)# as resp:
#    print resp.content
#
#f = open(url, 'r')
#s = f.read()

s = simple_get(url)
html = bs(s, 'html')

participants = {}

for i, p in enumerate(html.select('span')):
    print i, p.text
    '''if i % 2 == 0:
        name = remove_colon(str(p.text))
    else:
        if i == 9:
            nationality = 'P. R. China'
        else:
            nationality = remove_colon(str(p.text))
            
        print i,(name, nationality)'''
