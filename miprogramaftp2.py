import ftplib
import subprocess
ftp = ftplib.FTP("")
ftp.login("", "")
ftp.cwd("public_html/")
ftp.retrlines("LIST")
value = input("Archivo para descargar y comparar:\n")
ftp.cwd("../")
ftp.retrbinary(f'RETR public_html/{value}', open(f'{value}', 'wb').write)
subprocess.call(["C:\\Program Files\\Sublime Text\\sublime_text.exe", f'{value}'])
archivo = open(f'{value}', 'rb')

ftp = ftplib.FTP("")
ftp.login("", "")
ftp.cwd("public_html/")
ftp.retrlines("LIST")
ftp.cwd("../")
ftp.storbinary(f'STOR public_html/{value}', archivo)
