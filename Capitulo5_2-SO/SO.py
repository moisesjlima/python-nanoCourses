import platform
import getpass
from datetime import datetime

print("------ Olá", getpass.getuser(), '-------'
      "\n------Informações do Sistema Operacional------- ", datetime.now())

print("Distribuição.............:", platform.platform())
print("Nome.....................:", platform.system())
print("Versão...................:", platform.release())
print("Arquitetura..............:", platform.architecture())
print("Nome do Computador.......:", platform.node())
print("Tipo da Máquina..........:", platform.machine())
print("Processador...............", platform.processor())
print("Versão do Python.........:", platform.python_version())
