import ftplib
import subprocess
ftp = ftplib.FTP("") #Host
ftp.login("", "") # Usuario, Contraseña
ftp.cwd("public_html/") # Directorio donde se va a conectar el script
ftp.retrlines("LIST")
value = input("Archivo para descargar:\n")
ftp.cwd("../")
ftp.retrbinary(f'RETR public_html/{value}', open(f'{value}', 'wb').write)
#subprocess.Popen('C:\\Python39\\python.exe miprogramaftp2.py & ')
# Cambia en la línea de abajo, donde se encuentra el ejecutable del editor que quieras utilizar
subprocess.call(["C:\\Program Files\\Sublime Text\\sublime_text.exe", f'{value}'])
archivo = open(f'{value}', 'rb')
ftp.quit()

# Esto es porque si tardas en realizar los cambios que haz hecho, pues se desconecta
ftp = ftplib.FTP("") #Host
ftp.login("", "") # Usuario, Contraseña
ftp.cwd("public_html/") # Directorio donde se va a conectar el script
ftp.retrlines("LIST")
ftp.cwd("../")
ftp.storbinary(f'STOR public_html/{value}', archivo)
subprocess.call(["DELETE", f'{value}'])
