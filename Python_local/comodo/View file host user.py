import os
print("Before clear host file")
with open('C:\Windows\System32\drivers\etc\hosts','r') as f:
	host_old = f.read()
print(host_old)