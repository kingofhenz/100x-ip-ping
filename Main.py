import os

adress = raw_input("ip adress is: ")
hostname = adress
response = os.system("ping -c 1 " + hostname)


if response == 0:
  print (hostname + " is up!")
else:
  print (hostname + " is down!")
