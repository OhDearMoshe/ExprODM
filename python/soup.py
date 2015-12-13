from bs4 import BeautifulSoup
class SomeItem():
    def __init__(self, name, date, path):
        self.name = name
        self.date = date
        self.path = path

    def to_screen(self):
        print "Name: %s, Date: %s, Path: %s" % (self.name, self.date, self.path)

doc = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
 <head>
  <title>Index of /MyStuff</title></head>
 <body>
<div class="wrapper">
<!-- we open the `wrapper` element here, but close it in the `footer.html` file -->  <table id="indexlist">
   <tr class="indexhead"><th class="indexcolicon"><img src="/theme/icons/blank.png" alt="[ICO]" /></th><th class="indexcolname"><a href="?C=N;O=D">Name</a></th><th class="indexcollastmod"><a href="?C=M;O=A">Last modified</a></th><th class="indexcolsize"><a href="?C=S;O=A">Size</a></th></tr>
   <tr class="even"><td class="indexcolicon"><a href="/stuff/"><img src="/theme/icons/folder-home.png" alt="[PARENTDIR]" /></a></td><td class="indexcolname"><a href="/stuff/">Parent Directory</a></td><td class="indexcollastmod">&nbsp;</td><td class="indexcolsize">  - </td></tr>
   <tr class="odd"><td class="indexcolicon"><a href="stuff1.mkv"><img src="/theme/icons/video.png" alt="[TXT]" /></a></td><td class="indexcolname"><a href="stuff1.mkv">Stuff One</a></td><td class="indexcollastmod">2015-09-30 04:01  </td><td class="indexcolsize">925M</td></tr>
   <tr class="even"><td class="indexcolicon"><a href="stuff2.mkv"><img src="/theme/icons/video.png" alt="[TXT]" /></a></td><td class="indexcolname"><a href="stuff2.mkv">Stuff Two</a></td><td class="indexcollastmod">2015-10-07 07:01  </td><td class="indexcolsize">943M</td></tr>
   <tr class="odd"><td class="indexcolicon"><a href="stuff3.mkv"><img src="/theme/icons/video.png" alt="[TXT]" /></a></td><td class="indexcolname"><a href="stuff3.mkv">Stuff Three</a></td><td class="indexcollastmod">2015-10-14 04:00  </td><td class="indexcolsize">949M</td></tr>
   <tr class="even"><td class="indexcolicon"><a href="stuff4.mkv"><img src="/theme/icons/video.png" alt="[TXT]" /></a></td><td class="indexcolname"><a href="stuff4.mkv">Stuff Four</a></td><td class="indexcollastmod">2015-10-21 12:46  </td><td class="indexcolsize">858M</td></tr>
   <tr class="odd"><td class="indexcolicon"><a href="stuff5.mkv"><img src="/theme/icons/video.png" alt="[TXT]" /></a></td><td class="indexcolname"><a href="stuff5.mkv">Stuff Five</a></td><td class="indexcollastmod">2015-11-04 04:17  </td><td class="indexcolsize">884M</td></tr>
   <tr class="even"><td class="indexcolicon"><a href="stuff6.mkv"><img src="/theme/icons/video.png" alt="[TXT]" /></a></td><td class="indexcolname"><a href="stuff6.mkv">Stuff Six</a></td><td class="indexcollastmod">2015-11-11 04:09  </td><td class="indexcolsize">942M</td></tr>
   <tr class="odd"><td class="indexcolicon"><a href="stuff7.mkv"><img src="/theme/icons/video.png" alt="[TXT]" /></a></td><td class="indexcolname"><a href="stuff7.mkv">Stuff Seven</a></td><td class="indexcollastmod">2015-11-18 04:08  </td><td class="indexcolsize">953M</td></tr>
   <tr class="even"><td class="indexcolicon"><a href="stuff8.mp4"><img src="/theme/icons/video.png" alt="[VID]" /></a></td><td class="indexcolname"><a href="stuff8.mp4">Stuff eight</a></td><td class="indexcollastmod">2015-12-02 04:14  </td><td class="indexcolsize">256M</td></tr>
   <tr class="odd"><td class="indexcolicon"><a href="stuff9.mkv"><img src="/theme/icons/video.png" alt="[TXT]" /></a></td><td class="indexcolname"><a href="stuff9.mkv">Stuff Nine</a></td><td class="indexcollastmod">2015-12-08 16:05  </td><td class="indexcolsize">1.0G</td></tr>
</table>
</div><!--/.wrapper-->

<div class="footer">
</div><!--/.footer-->
</body></html>

"""
soup = BeautifulSoup(doc, 'html.parser')
tr = soup.find_all("tr")
#print tr
items = []
for line in tr:
    #print line
    td = line.find_all('td')
    #print "New Line:"
    iteration = 0
    date = None
    name = None
    url = None
    for t in td:
        #print t
        if iteration == 1:
            url = t.a['href']
            name = t.a.get_text()
        if iteration == 2:
            date = t.get_text().strip()
        iteration += 1
    print "Appending %s %s %s" % (url, name, date)
    items.append(SomeItem(name,date,url))

for item in items:
    item.to_screen()
