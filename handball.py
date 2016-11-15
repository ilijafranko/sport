from bs4 import BeautifulSoup
import urllib2
import csv

response = urllib2.urlopen("http://bhv-handball.liga.nu/cgi-bin/WebObjects/nuLigaHBDE.woa/w"
                           "a/groupPage?displayTyp=gesamt&displayDetail=meetings&championship=BHV+2016%2F17&group=205409")
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

f = csv.writer(open("handball.csv", "w"))
f.writerow(["Team 1", "Team 2", "Tore Team 1", "Tore Team 2", "Ort", "Uhrzeit", "Datum"])


#print soup.tbody

soup = soup.find("table")
#print soup
trs = soup.find_all('tr')

for tr in trs:
        #print tr
    tds = tr.find_all("td")
        #print tds
    try:
        team1 = str(tds[5].get_text().encode("utf-8")).strip()
        team2 = str(tds[6].get_text().encode("utf-8")).strip()
        ort = str(tds[3].span['title'].encode("utf-8")).strip()
        uhrzeit = "".join(str(tds[2].get_text().encode("utf-8")).split())
        datum = str(tds[1].get_text().encode("utf-8")).strip()
        tore = str(tds[7].a.span.get_text().encode("utf-8")).split(':')
        tor1 = tore[0].strip()
        tor2 = tore[1].strip()
        f.writerow([team1, team2, tor1, tor2, ort, uhrzeit, datum])
    except:
        print "bad string"
        continue