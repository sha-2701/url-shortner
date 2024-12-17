from urllib.parse import urlencode
from urllib.request import urlopen
import contextlib
import sys

def short_url(url): 
    request_url = 'http://tinyurl.com/api-create.php?' + urlencode({'url': url})     
    with contextlib.closing(urlopen(request_url)) as response:                       
        return response.read().decode('utf-8')                                       

def main():                                                                 
    if len(sys.argv) > 1:
        urls = sys.argv[1:]
    else:
        urls = [input("Enter a URL to shorten: ")]
    
    for url in map(short_url, urls):                    
        print("Shortened URL:", url)

if __name__ == '__main__': 
    main()
