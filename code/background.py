import os
from urllib.request import urlopen
import urllib3
from bs4 import BeautifulSoup
import requests
import urllib.request


def background():
    """
    Huge thanks to user "suriyadeepan" on github and "ton1c"
    on Stackoverflow for this code. It took a few hours trying to get
    it all to work, but I'm super pround of this.
    https://gist.github.com/suriyadeepan/b940caf6cba552527613c1f93e26cc80
    https://stackoverflow.com/questions/18497840/beautifulsoup-how-to-open-images-and-download-them
    """


    end_string = 'not_a_picture'
    #try:
    try:
        url = 'https://apod.nasa.gov/apod/astropix.html'
        # get contents from url
        content = requests.get(url).content
        # get soup
        soup = BeautifulSoup(content,'lxml') # choose lxml parser
        # find the tag : <img ... >
        image_tags = soup.findAll('img')
        # print out image urls
        for image_tag in image_tags:
            end_string = str(image_tag.get('src'))
            

            
        
        urllib.request.urlretrieve("https://apod.nasa.gov/apod/" + end_string, "background_main.jpg")
    except:
        print("Sorry, either the internets out or NASA doesn't know what a picture is. Setting Background to default")    