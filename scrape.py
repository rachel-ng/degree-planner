import sys
import urllib.request
import re
import unicodedata
from bs4 import BeautifulSoup

courses = dict()

# retrive html code from given url
def read_url(url):
    with urllib.request.urlopen(url) as fp:
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
    return mystr

# get all target links on a page
def get_pgs(dir_url):
    direc = read_url(dir_url)
    soup = BeautifulSoup(direc, 'html.parser')
    for tr in soup.find_all('a',target="_blank",href=re.compile("preview_course_nopop.php")):
        courses[unicodedata.normalize("NFKD", tr.string)] = tr.get("href")

for start_num in range(1, 26):
    print("pg ", start_num)
    #dir_url = "http://catalog.hunter.cuny.edu/content.php?catoid=39&catoid=39&navoid=11821&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D=" + str(start_num) + "#acalog_template_course_filter"
    dir_url = "http://catalog.hunter.cuny.edu/content.php?catoid=43&catoid=43&navoid=13946&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D=" + str(start_num) + "#acalog_template_course_filter"
    get_pgs(dir_url)

#print(courses)

s = ""

for i in courses: 
    s += i + "*" + courses[i] + "\n"

fin = open("data/courses.txt","w")
fin.write(s)
fin.close()

