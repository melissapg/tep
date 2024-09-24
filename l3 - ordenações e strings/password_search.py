import sys
from collections import defaultdict

def processar_linha(linha):
    # Divide a linha em tamanho do password e o texto
    partes = linha.split()
    N = int(partes[0])
    texto = partes[1]

    # Dicionário para contar a frequência das substrings
    contagem = defaultdict(int)
    
    # Verifica todas as substrings de tamanho N
    for i in range(len(texto) - N + 1):
        substring = texto[i:i + N]
        contagem[substring] += 1
    
    # Encontra a substring com a maior frequência
    max_frequencia = 0
    password = None
    for substring, freq in contagem.items():
        if freq > max_frequencia:
            max_frequencia = freq
            password = substring
    
    return password

def main():
    input = sys.stdin.read()
    linhas = input.strip().split('\n')
    
    for linha in linhas:
        if linha.strip():  # Ignora linhas em branco
            print(processar_linha(linha))

if __name__ == "__main__":
    main()