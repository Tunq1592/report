import os

contents='''
www.bittorrent.com
www.utorrent.com
now.bt.co
www.vuze.com
openpirate.org
www.torrentdownloads.me
'''## here mention host file name to change

print('Before change \n')
with open('C:\Windows\System32\drivers\etc\hosts', 'r') as f:
    print(f.read())
	
with open('C:\Windows\System32\drivers\etc\hosts', 'r') as f:
    data = f.read()
for content in contents.split('\n'): # so sanh file host
    if content not in data:
        with open('C:\Windows\System32\drivers\etc\hosts', 'a') as f:
            f.write('127.0.0.1 ' + content + '\n')
print('After change \n')
with open('C:\Windows\System32\drivers\etc\hosts', 'r') as f:
    print(f.read())