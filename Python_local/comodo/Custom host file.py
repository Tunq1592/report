import os
print("Before clear host file")
with open('C:\Windows\System32\drivers\etc\hosts','rt') as f:
	host_old = f.read()
print(host_old)

contents= ['www.facebook.com']
print('\n')
print(contents)
print('\n')

host_old = host_old.split('\n')
for content in contents:
	if '127.0.0.1 ' + content in host_old :
		host_old.remove('127.0.0.1 ' + content)	
	else:
		print('remove failed')
		
	if '127.0.0.1 www.' + content in host_old:
		host_old.remove('127.0.0.1 www.' + content)	
	else:
		print('remove failed')
with open('C:\Windows\System32\drivers\etc\hosts','w+') as f:
	f.write('\n'.join(host_old))
print("\n\n\n")	
print("After change hosst file")
with open('C:\Windows\System32\drivers\etc\hosts', 'rt') as f:
	print(f.read())
