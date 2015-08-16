
from requests import get
from bs4 import BeautifulSoup as BS
from os.path import exists
from multiprocessing import Pool

url = "https://www.projecteuler.net/problem=%d"


def get_info(i):
    soup = BS(get(url % i, verify=False).content)
    problem = soup.find(id="content")
    title = problem.h2.string
    content = problem.find(class_="problem_content").get_text()
    info = title + '\n' + content
    info = info.encode('u8')
    return info


def save(i):
    name = "%03d.py" % i
    # if exists(name):
    #     print name, "exist"
    #     return
    f = file(name, "w")
    info = get_info(i)
    f.write(
'''\
#-*- encoding: utf-8 -*-
"""
%s"""

from utils import *


#
''' % info)
    f.close()
    print name, "saved"


def save_all(i, j):
    p = Pool()
    p.map(save, range(i, j + 1))


if __name__ == '__main__':
    N = 10
    last = int(file('last.txt').read())
    save_all(last + 1, last + N)
    file('last.txt', 'w').write(str(last + N))

