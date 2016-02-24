import os
import shutil
import sys
import glob
import pyodbc
from datetime import datetime

reload(sys)
sys.setdefaultencoding("utf-8")

print datetime.now()
odbcConnection = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.0.79;DATABASE=JBM1;UID=iareader;PWD=14r34d3r')
dbPointer = odbcConnection.cursor()  

dbPointer.execute("""SELECT TEXTO FROM DIG_PROCESSADA WHERE IDADV_PROCESSO IN (SELECT IDADV_PROCESSO FROM ADV_PROCESSOAVANCADO WHERE IDTERCEIROSXDIVISAO_FILIAL = 376)
AND DTPUBLICACAO >= '2015-05-01'""")

columns = [desc[0] for desc in dbPointer.description]
dados = list(dbPointer.fetchall())

arqForImpression= open('c:\ArqComDados.txt', 'w')
count = 0
for row in dados:
    count+=1
    print "Gravando "+str(count)+ " de "+str(len(dados))
    arqForImpression.write(row[0])
        
dbPointer.close()
odbcConnection.close()

print datetime.now()