from bs4 import BeautifulSoup
import urllib2
import csv

response = urllib2.urlopen("https://www.volleyball.bayern/index.php?id=1144&wid=8051&mode=spielplan")
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

f = csv.writer(open("volleyball.csv", "w"))
f.writerow(["Team 1", "Team 2", "Sets Team 1", "Sets Team 2", "Ort", "Uhrzeit", "Datum"])


#print soup.tbody
datum = ''
soup = soup.find_all("table")[2]
trs = soup.find_all('tr')

for tr in trs:
    tds = tr.find_all("td")
    try:
        if tds[0].has_attr('class'):
            team1 = str(tds[2].get_text().encode("utf-8"))
            team2 = str(tds[3].get_text().encode("utf-8"))
            ort = str(tds[2].get_text().encode("utf-8"))
            uhrzeit = str(tds[0].get_text())
            datum = datum
            sets = str(tds[4].a.get_text().encode("utf-8"))
            if int(sets[0]):
                set1 = sets[0]
                set2 = sets[2]
            f.writerow([team1, team2, set1, set2, ort, uhrzeit, datum])
        else:
            datum = str(tds[0].get_text())
    except:
        print "bad string"
        continue