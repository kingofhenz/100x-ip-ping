from ipaddress import ip_address
import os
import subprocess
import sys

while true:
  ip_address = input("Enter an IP address: ")
  response = os.system("ping -c 100 " + ip_address)
  if response == 0:
    print(ip_address, "is up!")
  else:
    print(ip_address, "is down!")
