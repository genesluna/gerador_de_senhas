import string
import random


def gerar_senha(tamanho, incluir_caracteres_especiais, incluir_maiusculas, incluir_minusculas, incluir_numeros):

    # Verifica se pelo menos uma opção está habilitada
    if not (incluir_caracteres_especiais or incluir_maiusculas or incluir_minusculas or incluir_numeros):
        raise ValueError(
            "Pelo menos uma opção (--especiais, --maiusculas, --minusculas, --numeros) deve ser habilitada."
        )

    caracteres = ""
    conjunto_caracteres = ""

    # Cria os caracteres base e o conjunto global de caracteres
    if incluir_maiusculas:
        caracteres += random.choice(string.ascii_uppercase)
        conjunto_caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += random.choice(string.ascii_lowercase)
        conjunto_caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += random.choice(string.digits)
        conjunto_caracteres += string.digits
    if incluir_caracteres_especiais:
        caracteres += random.choice(string.punctuation)
        conjunto_caracteres += string.punctuation

    tamanho_restante = tamanho - len(caracteres)

    # Garante que o tamanho seja suficiente para incluir pelo menos um caractere de cada conjunto
    if tamanho < len(caracteres):
        raise ValueError("O tamanho da senha não pode ser menor que o número de opções escolhidas.")

    # Gera os caracteres restantes
    caracteres_restantes = "".join(random.choice(conjunto_caracteres) for _ in range(tamanho_restante))

    # Junta os caracteres restantes com os caracteres base
    caracteres += caracteres_restantes

    # Embaralha os caracteres e cria a senha
    senha = "".join(random.sample(caracteres, len(caracteres)))

    return senha
