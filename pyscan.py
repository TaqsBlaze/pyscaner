import socket
import datetime

banner = f"""
{"_"*40}
	PyScanner
	v 1.0
	by R3$3T
{"_"*40}
"""
print(banner)

class Logging:
	
	def __init__(self, data:str,log_name:str):
		self.data = data
		self.log_name = log_name
		self.log_mode = "a"
		
	def log(self):
		
		with open(self.log_name, self.log_mode) as logger:
			logger.write(self.data)
	
class Console:
		
		def log(stream:str):
			
			print(stream)
			
		def grab_server_banner(sock):
			
			sock.send(bytes('WhoAreYou\r\n'.encode('utf-8')))
			banner = sock.recv(2048)
			
			print(banner.decode('utf-8').strip('\r\s\n'))
		
def scan_ports(target, start_port, end_port):
    print(f"Scanning ports on {target}...\n")
    date_time = str(datetime.datetime.now()).split(".")[0]
    log_info =f"""
-----------------------------------------------------------------
    port scan for:  {target}
    
    date time: {date_time}
-----------------------------------------------------------------\n
    """
   
    log_info = Logging(log_info, f"{target}-port-scan.txt")
    log_info.log()
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            Console.log(f" * Checking port {port}...")
            sock.connect_ex((target, port))
            service = socket.getservbyport(port)
            
            Console.log(
            f" * Port:{port} Open Service:{service}")
            data = f"Port: {port} Status: Open Service: {service}\n"
            logger = Logging(data, f"{target}-port-scan.txt")
            logger.log()
            Console.grab_server_banner(sock)

        except socket.error:
            pass
        finally:
            sock.close()

# Replace 'example.com' with the target host or IP address
target_host = str(input(" * Enter taget:"))

# Define the range of ports to scan (e.g., 1 to 1024)
start_port = int(input(" * Enter start port:"))
end_port = int(input(" * Enter end port:"))

# Run the port scanner
scan_ports(target_host, start_port, end_port)