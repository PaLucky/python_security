import socket
import sys
import common_ports

def get_open_ports(target, port_range, verbose =False):
    open_ports = []
    ports= str(port_range[0]) + '-' + str(port_range[1])
    print(ports)    
    remoteServerIP = target
    if is_ip(target):
      print(target)      
    else:
      try:    
        remoteServerIP = socket.gethostbyname(target)
      except socket.gaierror:
        return "Error: Invalid hostname"
    try:
      for port in range(port_range[0],port_range[-1] +1):      
          sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          sock.settimeout(1)
          if sock.connect_ex((remoteServerIP, port)):
            print(port," the port is close")
          else:
              open_ports.append(port)
          sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()
    except socket.gaierror:
        return "Error: Invalid IP address"
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()
    if verbose:
      return verbose_format(open_ports, target , remoteServerIP)
    return(open_ports)

def is_ip(address):
    return address.replace('.', '').isnumeric()

def verbose_format(ports, url , ip):  
  if ip == url:
    try:
      url =socket.gethostbyaddr(ip)[0]
      result= f"Open ports for {url} ({ip})\nPORT     SERVICE"
    except:
      result= f"Open ports for {url}\nPORT     SERVICE"
  else:
    result= f"Open ports for {url} ({ip})\nPORT     SERVICE"
  print(ports)
  for p in ports:
    result +=  "\n" +str(p) + " " * (9 - len(str(p))) + common_ports.ports_and_services[p] 
  return result


