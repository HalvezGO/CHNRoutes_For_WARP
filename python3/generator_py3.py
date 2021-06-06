import urllib.request as urllib2
import re
import math

def generateRules():
    results = fetch_ip_data()
    rfile = open('chnrouteup', 'w')
    r1file = open('chnroutedown', 'w')
    for ip, mask, mask2 in results:
        route_item = "ip -4 rule add to %s/%s priority 1\n" % (ip, mask2)
        route_item2 = "ip -4 rule delete to %s/%s priority 1\n" % (ip, mask2)
        rfile.write(route_item)
        r1file.write(route_item2)
    rfile.close()
    r1file.close()

    print("All done!")

def fetch_ip_data():
    # fetch data from apnic
    print("Fetching data from apnic.net, it might take a few minutes, please wait... ")
    url = r'https://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest'
    data = urllib2.urlopen(url).read().decode('utf-8')

    cnregex = re.compile(r'apnic\|cn\|ipv4\|[0-9\.]+\|[0-9]+\|[0-9]+\|a.*', re.IGNORECASE)
    cndata = cnregex.findall(data)

    results = []

    for item in cndata:
        unit_items = item.split('|')
        starting_ip = unit_items[3]
        num_ip = int(unit_items[4])

        imask = 0xffffffff ^ (num_ip - 1)
        # convert to string
        imask = hex(imask)[2:]
        mask = [0] * 4
        mask[0] = imask[0:2]
        mask[1] = imask[2:4]
        mask[2] = imask[4:6]
        mask[3] = imask[6:8]

        # convert str to int
        mask = [int(i, 16) for i in mask]
        mask = "%d.%d.%d.%d" % tuple(mask)

        # mask in *nix format
        mask2 = 32 - int(math.log(num_ip, 2))

        results.append((starting_ip, mask, mask2))
    print("results tuple is like the following output:")
    print(results[0])
    return results

print("Starting...")
generateRules()