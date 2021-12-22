import PLCXMLparser
import csv
def getWaitTime(xmlstring):
    wait = 0
    carrier = PLCXMLparser.parseXml(xmlstring)
    carrier.carrier = int(carrier.carrier)
    return(1)

def getWait(data):
    xml = PLCXMLparser.parseXml(data)
    stationId = int(xml.station)
    carrierId = int(xml.carrier)
    if stationId < 10:
        stationId = "Station#0" + str(stationId)
    else:
        stationId = "Station#" + str(stationId)
    carrierId = "Carrier#" + str(carrierId)
    y = None
    with open('procssing_times_table.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if y == None:
                for x in range(len(row)):
                    if row[x] == stationId:
                        y = x
            
            if row[0] == carrierId:
                with open('log.txt', 'a') as log:
                    log.write(" - Wait time:%s \n"%(row[y]))
                    print("Wait: %s\n"%(row[y]))
                return(row[y])
                


