import os
import socket
import psutil
import time
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

LOG_FILE = "log.txt"
PASSWORD = "1234"

# =========================
# LOG
# =========================
def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")


# =========================
# BANNER
# =========================
def banner():
    print(Fore.GREEN + "=" * 60)
    print(Fore.GREEN + "   NICOLAS PRO NETWORK TOOL")
    print(Fore.GREEN + "   Técnico em Informática")
    print(Fore.GREEN + "=" * 60)


# =========================
# LOGIN
# =========================
def login():
    for _ in range(3):
        senha = input("Senha: ")
        if senha == PASSWORD:
            return True
        else:
            print("Senha incorreta")
    return False


# =========================
# REDE
# =========================
def scan_port(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Desconhecido"

            print(Fore.GREEN + f"[ABERTA] {port} ({service})")
            log(f"Porta aberta {port} em {target}")
        sock.close()
    except:
        pass


def port_scan():
    target = input("IP alvo: ")
    start = int(input("Porta inicial: "))
    end = int(input("Porta final: "))

    print(Fore.YELLOW + "\nEscaneando...\n")

    for port in range(start, end + 1):
        scan_port(target, port)


def ping():
    host = input("Host: ")
    log(f"Ping em {host}")
    os.system(f"ping -c 4 {host}")


# =========================
# SISTEMA
# =========================
def monitor():
    try:
        while True:
            os.system("clear")
            banner()
            print(Fore.CYAN + "\n=== MONITOR ===\n")
            print(f"CPU: {psutil.cpu_percent()}%")
            print(f"RAM: {psutil.virtual_memory().percent}%")
            print(f"Processos: {len(psutil.pids())}")
            print(f"Hora: {datetime.now()}")
            time.sleep(2)
    except KeyboardInterrupt:
        pass


# =========================
# ARQUIVOS
# =========================
def listar():
    print("\nArquivos:\n")
    for f in os.listdir():
        print(f)


def criar():
    nome = input("Nome: ")
    open(nome, "w").close()
    log(f"Arquivo criado: {nome}")


def deletar():
    nome = input("Arquivo: ")
    if os.path.exists(nome):
        os.remove(nome)
        log(f"Arquivo deletado: {nome}")
    else:
        print("Não encontrado")


# =========================
# MENU
# =========================
def menu():
    while True:
        banner()
        print(Fore.YELLOW + """
1 - Scanner de Portas
2 - Ping
3 - Monitor Sistema
4 - Listar Arquivos
5 - Criar Arquivo
6 - Deletar Arquivo
7 - Ver Logs
0 - Sair
""")

        op = input("Escolha: ")

        if op == "1":
            port_scan()
        elif op == "2":
            ping()
        elif op == "3":
            monitor()
        elif op == "4":
            listar()
        elif op == "5":
            criar()
        elif op == "6":
            deletar()
        elif op == "7":
            with open(LOG_FILE) as f:
                print(f.read())
        elif op == "0":
            break

        input("\nENTER...")
        os.system("clear")


# =========================
# START
# =========================
if __name__ == "__main__":
    os.system("clear")

    if login():
        menu()
    else:
        print("Acesso negado")






















































































































































































































































