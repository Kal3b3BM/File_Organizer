import os, time, tkinter, datetime, shutil
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

def sel_pastas():
    if "y" == input("Selecionar pastas? [y/n] ").lower():
        file = open(r'C:\Windows\config.json', 'w')
        pastaFonte = filedialog.askdirectory(parent=root, initialdir="/", title="Selecionar pasta Fonte")
        pastaImagemDia = filedialog.askdirectory(parent=root, initialdir="/", title="Selecionar pasta de IMAGEM DO DIA")
        pastaVideoDia = filedialog.askdirectory(parent=root, initialdir="/", title="Selecionar pasta de VÍDEO DO DIA")
        pastaImagemMes = filedialog.askdirectory(parent=root, initialdir="/", title="Selecionar pasta de IMAGEM DO MÊS")
        pastaVideoMes = filedialog.askdirectory(parent=root, initialdir="/", title="Selecionar pasta de VÍDEO DO MÊS")
        file.write(f'{pastaFonte}\n{pastaImagemDia}\n{pastaVideoDia}\n{pastaImagemMes}\n{pastaVideoMes}')
        file.close()
        return (pastaFonte, pastaImagemDia, pastaVideoDia, pastaImagemMes, pastaVideoMes)

def ler_jason():
    file = open(r'C:\Windows\config.json', 'r')
    pastaFonte = str(file.readline()[:-1])
    pastaImagemDia = str(file.readline()[:-1])
    pastaVideoDia = str(file.readline()[:-1])
    pastaImagemMes = str(file.readline()[:-1])
    pastaVideoMes = str(file.readline()[:])
    file.close()
    return (pastaFonte, pastaImagemDia, pastaVideoDia, pastaImagemMes, pastaVideoMes)

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
                        print(arq, dCria, dPass)
                        if dCria >= dPass and arq[-3:].lower() in ("jpg", "png", "jpeg"):
                            shutil.copy(arq, pastaImagemDia)
                            shutil.copy(arq, pastaImagemMes)
                        if dCria >= dPass and arq[-3:].lower() in ("mp4", "wmv", "mpeg", "mov"):
                            shutil.copy(arq, pastaVideoDia)
                            shutil.copy(arq, pastaVideoMes)
                deleta_arquivos(pastaImagemDia, 1)
                deleta_arquivos(pastaVideoDia, 1)
                deleta_arquivos(pastaImagemMes, 30)
                deleta_arquivos(pastaVideoMes, 30)
            except:
                pass
            finally:
                time.sleep(5)


if __name__ == "__main__":
    sel_pastas()
    loop(int(input("Ativar/Desativar programa? [1/0] ")))
