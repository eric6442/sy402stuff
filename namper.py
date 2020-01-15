#/usr/bin/env python
#Definenly repurposing code from the usage documentation
import nmap #imports python nmap lmao
import sys
def main():
    sys.argv.pop(0)
    scanrange = sys.argv[0]
    print(scanrange)
    resultsDict = scanports(scanrange)

def scanports(range):
    portobj = nmap.PortScanner()
    portobj.scan(hosts=range, arguments='-O -sV') 
    for a in portobj.all_hosts():
        print('Host: %s ($s)' (host, portobj[host].hostname()))
        print(portobj.csv())
    print("# of Hosts: ", portobj.all_hosts().size)
    return(0)


if __name__=="__main__":
    main()
