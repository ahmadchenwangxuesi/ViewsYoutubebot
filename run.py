#python2.7
#Coded by paceusa
from bs4 import BeautifulSoup
import requests, os

h = '\033[32m'
m = '\033[31m'
p = '\033[0m'

os.system('clear')
print "  _________   _______________    ____\n  /_  __/   | / ____/ ____/   |  / __ \  Code: PACEUSA \n   / / / /| |/ / __/ / __/ /| | / /_/ / https://github.com/ahmadchenwangxuesi\n  / / / ___ / /_/ / /_/ / ___ |/ _, _/ \n /_/ /_/  |_\____/\____/_/  |_/_/ |_|"
print('['+h+'+'+p+'] Usage: https://www.youtube.com/watch?v=C9XNMY_bnZE')
print('['+h+'?'+p+'] Code: C9XNMY_bnZE\n')
pilih = raw_input('[?] Code: ')
link = requests.get('https://youtu.be/'+ pilih)
data = link.text
soup = BeautifulSoup(data, 'html.parser')
judul = soup.find('title').text
des = soup.find('meta', {'name':'description'})
gun = soup.find('meta', {'name':'keywords'})
print '['+h+'~'+p+'] Judul Video:',judul
print '['+h+'~'+p+'] Descr Video:',des['content']
print '['+h+'~'+p+'] Tag Video:',gun['content']
