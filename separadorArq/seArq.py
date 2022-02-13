import os, time, tkinter, datetime, shutil
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

def sel_pastas():
    if "y" == input("Selecionar pastas? [y/n] ").lower():
        file = open('C:\Windows\config.json', 'w')
        pastaFonte = filedialog.askdirectory(parent=root, initialdir="/", title="Selecionar pasta Fonte")
        pastaImagemDia = filedialog.askdirectory(parent=root, initialdir="/", title="Selecionar pasta de IMAGEM DO DIA")
        pastaVideoDia = filedialog.askdirectory(parent=root, initialdir="/", title="Selecionar pasta de VÍDEO DO DIA")
        pastaImagemMes = filedialog.askdirectory(parent=root, initialdir="/", title="Selecionar pasta de IMAGEM DO MÊS")
        pastaVideoMes = filedialog.askdirectory(parent=root, initialdir="/", title="Selecionar pasta de VÍDEO DO MÊS")
        file.write(pastaFonte + '\n' + pastaImagemDia  + '\n' + pastaVideoDia + '\n' + pastaImagemMes  + '\n' + pastaVideoMes)
        file.close()
        return pastaFonte, pastaImagemDia, pastaVideoDia, pastaImagemMes, pastaVideoMes

def ler_jason():
    file = open('C:\Windows\config.json', 'r')
    pastaFonte = str(file.readline()[0])
    file = open('C:\Windows\config.json', 'r')
    pastaImagemDia = str(file.readline()[1])
    file = open('C:\Windows\config.json', 'r')
    pastaVideoDia = str(file.readline()[2])
    file = open('C:\Windows\config.json', 'r')
    pastaImagemMes = str(file.readline()[3])
    file = open('C:\Windows\config.json', 'r')
    pastaVideoMes = str(file.readline()[4])
    file.close()
    return pastaFonte, pastaImagemDia, pastaVideoDia, pastaImagemMes, pastaVideoMes

def deleta_arquivos(pasta, dias):
    arquivo = os.listdir(pasta)
    for arq in arquivo:
        arq = pasta + f"/{arq}"
        dCria = time.strftime('%Y-%m-%d', time.strptime(time.ctime(os.path.getctime(arq))))
        dPass = (datetime.date.today() - datetime.timedelta(days=dias)).strftime('%Y-%m-%d')
        if dCria < dPass:
            try:
                os.remove(arq)
            except:
                continue

def loop(m = False):
    pastaFonte, pastaImagemDia, pastaVideoDia, pastaImagemMes, pastaVideoMes = ler_jason()
    if m:
        while True:
            try:
                arquivo = os.listdir(pastaFonte)
                dPass = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
                for arq in arquivo:
                    arquivosImagemDia = os.listdir(pastaImagemDia)
                    arquivosVideoDia = os.listdir(pastaVideoDia)
                    if arq not in (arquivosImagemDia, arquivosVideoDia):
                        arq = pastaFonte + f"/{arq}"
                        dCria = time.strftime('%Y-%m-%d', time.strptime(time.ctime(os.path.getctime(arq))))
                        if dCria >= dPass and (arq[-3:].lower() == "jpg" or arq[-3:].lower() == "png" or arq[-4:].lower() == "jpeg"):
                            try:
                                shutil.copy(arq, pastaImagemDia)
                                shutil.copy(arq, pastaImagemMes)
                            except:
                                continue
                        if dCria >= dPass and (arq[-3:].lower() == "mp4" or arq[-3:].lower() == "wmv" or arq[-4:].lower() == "mpeg"):
                            try:
                                shutil.copy(arq, pastaVideoDia)
                                shutil.copy(arq, pastaVideoMes)
                            except:
                                continue
                deleta_arquivos(pastaImagemDia, 1)
                deleta_arquivos(pastaVideoDia, 1)
                time.sleep(5)
            except:
                continue

if __name__ == "__main__":
    sel_pastas()
    loop(int(input("Ativar/Desativar programa? [1/0] ")))
