from BeautifulSoup import BeautifulSoup

f = open ('test.html', 'r')
data = f.read()
f.close()

soup = BeautifulSoup (data)
print (soup.prettify())
