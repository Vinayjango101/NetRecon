import nmap 
import threading

scanner = nmap.PortScanner()

def fast_scan(target):
    print("[+] Fast scan started~!")
    scanner.scan(
        hosts=target,
        arguments="-4 -Pn -T4 --top-ports 1000"
    )
    print("[+] Fast scan done~!")

def service_scan(target):
    print("[+] Service scan started~!")
    scanner.scan(
        hosts=target,
        arguments="-4 -Pn -sV -T4"
    )
    print("[+] Service scan done~!")

def print_results():
    for host in scanner.all_hosts():
        print("\nHOST:", host)
        for proto in scanner[host].all_protocols():
            for port in scanner[host][proto]:
                service = scanner[host][proto][port].get("name", "")
                print(f"{port}/{proto} -> {service}")


target = input("[+] TARGET: ").strip()

t1 = threading.Thread(target=fast_scan, args=(target,))
t2 = threading.Thread(target=service_scan, args=(target,))

t1.start()
t2.start()

t1.join()
t2.join()


print_results()
