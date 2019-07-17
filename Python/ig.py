import functions
import kms

# Create An Object Of IG Class In kms Library.
a = kms.IG()

#Get Address Of Taget
address = input("Enter Your Target Address : ")

#Removes http:// From Address and Check If Website Is Valid.
#It removes http:// Because kms Library Doesnt Support A URL With
#an http:// .
if address.find("http://"):
    #Replace http:// With Nothing! Means Removing!
    address = address.replace("http://","")

    #check If URL Is Valid.
    if not functions.check(address):
        print("Sorry! Target Not Found!")
        exit(0)

print("\n")

cmd = ""

while True:

    print("""\033[1;36;[1] -> A Records
    [2] -> As Lookup
    [3] -> DNS Lookup
    [4] -> Find DNS Server
    [5] -> Http Headers
    [6] -> Ip Location
    [7] -> Page Links
    [8] -> Ping
    [9] -> Reverse Ip Lookup
    [10] -> Reverse DNS
    [11] -> Subnet Calculator
    [12] -> TCP Port Scan
    [13] -> Traceroute
    [14] -> Whois
    [15] -> Zone Transfer
    
    [99] -> exit
    \033[1;37;""")

    #Get Input
    cmd = input(">> ")

    # Get { A Records } Of A Website
    if cmd == "1":
        a.a_records()

    # Get An { AS Lookup } Of A Website
    elif cmd == "2":
        a.as_lookup()

    # Get A { DNS Lookup Test } Of A Website
    elif cmd == "3":
        a.dns_lookup()

    # { Find Dns Servers } Of A Website
    elif cmd == "4":
        a.find_dns_servers()

    # Get A { HTTP Headers } Of A Website
    elif cmd == "5":
        a.http_headers()

    # Get A { Ip Location } Of A Website
    elif cmd == "6":
        a.ip_location()

    # Get All { Page Links } Of A Website
    elif cmd == "7":
        a.page_links()

    # Get A Common { Ping }
    elif cmd == "8":
        a.ping()

    # Get A { Reverse Ip Lookup } Of A Website
    elif cmd == "9":
        a.reverse_ip_lookup()

    # Get A { Reverse DNS Test } Of A Website
    elif cmd == "10":
        a.reverse_dns()

    # { Subnet Calculator }. Test It! Its Good!
    elif cmd == "11":
        a.subnet_calc()

    # Get A { TCP Port Scan Test } Of A Website. Its Nice One!
    elif cmd == "12":
        a.tcp_port_scan()

    # Get A { Traceroute } Of A Website
    elif cmd == "13":
        a.traceroute()

    # Get A { Whois Test } Of A Website
    elif cmd == "14":
        a.whois()

    # Get A { Zone Transfer Test } Of A Website
    elif cmd == "15":
        a.zone_transfer()

    # Exit If cmd Is 99{Exit}
    elif cmd == "99":
        break

    else:
        print("\033[1;31;You Entered Wrong Command!\033[1;37;")