import xml.sax
import numpy as np
matrix = []
class xmlHandler( xml.sax.ContentHandler ):
    count = 0
    def __init__(self):
        self.station = ""
        self.carrier = ""
        self.date = ""

   # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "station":
            self.station = attributes["id"][6:]
        elif tag == "carrier":
            self.carrier = attributes["id"]
        elif tag == "date":
            self.date = attributes["value"][3:]
      
def parseXml(xmlString):
    Handler = xmlHandler()
    xml.sax.parseString(xmlString,Handler)
    print("Station: " + str(Handler.station))
    print("Carrier: " + str(Handler.carrier))
    print("Date:    " + Handler.date)
    with open('log.txt', 'a') as log:
        log.write("%s - STATION:%s - CARRIER:%s" %(Handler.date, Handler.station, Handler.carrier))
    return (Handler)
