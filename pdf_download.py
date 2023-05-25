"""Webscraping: download pdf from CSEP 590B Explainable AI (Su-In Lee, et al.)

https://sites.google.com/cs.washington.edu/csep590b


"""
#%%
import os
import requests
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import ssl


#%%
url_is = 'https://sites.google.com/cs.washington.edu/csep590b'
#If there is no such folder, the script will create one automatically
folder_location = r'outputs/pdf_download/'
if not os.path.exists(folder_location):os.mkdir(folder_location)

context = ssl._create_unverified_context()

def get_pdf_v1(url_is, folder_location):
    response = urlopen(url_is, context=context)

    soup= BeautifulSoup(response, "html.parser")  
    for link in soup.find_all('a'):
        current_link = link.get('href')
        if current_link.endswith('pdf'):
            print(f'current pdf file: {current_link}')
            filename = os.path.join(folder_location,link['href'].split('/')[-1]) # the file name is the pdf name in the url
            with open(filename, 'wb') as f:
                f.write(requests.get(urljoin(url_is,link['href']), verify=False).content)
    return print('done')

get_pdf_v1(url_is,folder_location)
    


#%%
