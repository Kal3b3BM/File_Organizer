import os, time, tkinter, datetime, shutil
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

def selPastas():
    global pastaFonte, pastaImagem, pastaVideo
    if "y" == input("Selecionar pastas? [y/n] ").lower():
        file = open('C:\Windows\config.json', 'w')
        pastaFonte = filedialog.askdirectory(parent=root, initialdir="/", title="Selecionar pasta Fonte")
        pastaImagem = filedialog.askdirectory(parent=root, initialdir="/", title="Selecionar pasta de Imagem")
        pastaVideo = filedialog.askdirectory(parent=root, initialdir="/", title="Selecionar pasta de Video")
        file.write(pastaFonte + '\n' + pastaImagem  + '\n' + pastaVideo)
        file.close()

def lerJason():
    global pastaFonte, pastaImagem, pastaVideo
    file = open('C:\Windows\config.json', 'r')
    pastaFonte = str(file.readlines()[0][:-1])
    file = open('C:\Windows\config.json', 'r')
    pastaImagem = str(file.readlines()[1][:-1])
    file = open('C:\Windows\config.json', 'r')
    pastaVideo = str(file.readlines()[2])
    file.close()

def loop(inp = "d"):
    lerJason()
    if "a" == inp:
        while True:
            arquivo = os.listdir(pastaFonte)
            dPass = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
            for arq in arquivo:
                arqi = os.listdir(pastaImagem)
                arqv = os.listdir(pastaVideo)
                if arq not in arqi and arq not in arqv:
                    arq = pastaFonte + f"/{arq}"
                    dCria = time.strftime('%Y-%m-%d', time.strptime(time.ctime(os.path.getctime(arq))))
                    if dCria >= dPass and (arq[-3:].lower() == "jpg" or arq[-3:].lower() == "png" or arq[-4:].lower() == "jpeg"):
                        try:
                            shutil.copy(arq, pastaImagem)
                        except:
                            continue
                    if dCria >= dPass and (arq[-3:].lower() == "mp4" or arq[-3:].lower() == "wmv" or arq[-4:].lower() == "mpeg"):
                        try:
                            shutil.copy(arq, pastaVideo)
                        except:
                            continue
            arquivo = os.listdir(pastaImagem)
            for arq in arquivo:
                arq = pastaImagem + f"/{arq}"
                dCria = time.strftime('%Y-%m-%d', time.strptime(time.ctime(os.path.getctime(arq))))
                if dCria < dPass:
                    try:
                        os.remove(arq)
                    except:
                        continue
            arquivo = os.listdir(pastaVideo)
            for arq in arquivo:
                arq = pastaVideo + f"/{arq}"
                dCria = time.strftime('%Y-%m-%d', time.strptime(time.ctime(os.path.getctime(arq))))
                if dCria < dPass:
                    try:
                        os.remove(arq)
                    except:
                        continue
            time.sleep(5)

if __name__ == "__main__":
    selPastas()
    loop(input("Ativar/Desativar programa? [a/d] ").lower())
