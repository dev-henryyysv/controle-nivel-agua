# Nome: Henry Rodrigues
# Turma: (FAU - TO260015529D1)
# Atividade: Controle de Níveis de Água
# Descrição: Sistema que simula o monitoramento de um reservatório
# utilizando níveis com cores diferentes no terminal.
# Sistema de Monitoramento de Nível de Água
# Compatível com Pydroid 3

from colorama import Fore, Style, init
import time

# Inicializa colorama
init(autoreset=True)

# Lista de níveis (mensagem + cor)
niveis = [
    ("Muito baixo (CRÍTICO)", Fore.RED),
    ("Baixo", Fore.YELLOW),
    ("Médio", Fore.GREEN),
    ("Alto", Fore.CYAN),
    ("Muito alto (ALERTA)", Fore.BLUE)
]

# Função para exibir nível
def mostrar_nivel(nivel):
    if 1 <= nivel <= 5:
        mensagem, cor = niveis[nivel - 1]
        
        # Barra visual (pra ficar mais profissional)
        barra = "█" * nivel + "-" * (5 - nivel)
        
        print(cor + f"\nNível {nivel}: {mensagem}")
        print(cor + f"[{barra}]")
        print(Style.RESET_ALL)
    else:
        print("Nível inválido!")

# Simulação do sistema
def simular():
    print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")
    
    for nivel in range(1, 6):
        mostrar_nivel(nivel)
        time.sleep(1)  # pausa pra simular tempo real

    print("\nMonitoramento finalizado.")

# Executa o programa
simular()