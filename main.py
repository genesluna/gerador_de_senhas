import argparse
from gerador_de_senha import gerar_senha


def main():
    # Configuração do parser de argumentos
    parser = argparse.ArgumentParser(description="Gerador de senhas seguras")
    parser.add_argument("--tamanho", type=int, default=12, help="Tamanho da senha")
    parser.add_argument("--especiais", action="store_true", help="Incluir caracteres especiais na senha")
    parser.add_argument("--maiusculas", action="store_true", help="Incluir letras maiúsculas na senha")
    parser.add_argument("--minusculas", action="store_true", help="Incluir letras minúsculas na senha")
    parser.add_argument("--numeros", action="store_true", help="Incluir números na senha")

    # Parse dos argumentos da linha de comando
    args = parser.parse_args()

    try:
        # Gera a senha com base nos critérios especificados
        senha = gerar_senha(args.tamanho, args.especiais, args.maiusculas, args.minusculas, args.numeros)

        resultado = f"Senha gerada: {senha}"

        # Exibe a senha gerada
        print("-" * len(resultado))
        print(resultado)
        print("-" * len(resultado))

    except ValueError as e:
        # Exibe mensagem de erro caso ocorra uma exceção durante a geração da senha
        print(f"Erro: {e}")


if __name__ == "__main__":
    # Chama a função principal quando o script é executado
    main()
