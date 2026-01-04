import nmap


def print_banner():
    print("""
     BANNER HERE
""")
    

def take_target_input():

    t = input("[+]ENTER IP/URL to scan eg-(192.168.0.x or test.com)-->  ").strip()
    return t


def basic_scan(t):
    scanner = nmap.PortScanner()
    scanner.scan(t)
    print(scanner.all_hosts())

    for host in scanner.all_hosts():
        print("HOST:", host)
        print("STATE:", scanner[host].state())

        for protocol in scanner[host].all_protocols():
            print("PROTOCOL:", protocol)

            ports = scanner[host][protocol].keys()
            for port in ports: 
                print("PORT:", port,
                      "STATE:", scanner[host][protocol][port]['state'])
            
    
print_banner()
t = take_target_input()
basic_scan(t)