import requests
def main():
    cep = input("Digite o Cep para consulta: ")
    if len(cep) != 8:
        print("quantidade de digitos inválido")
        main()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    endereco = request.json()

    if 'erro' not in endereco:
        print(" ==> Cep Encontrado <==")
        print("-"*20)
        print('CEP: {}'.format(endereco['cep']))
        print('Rua: {}'.format(endereco['logradouro']))
        print('Bairro: {}'.format(endereco['bairro']))
        print('Cidade: {}'.format(endereco['localidade']))
        print('Estado: {}'.format(endereco['uf']))
    else:
        print("{}: Cep invalido".format(cep))
    opcao = int(input("deseja realizar uma nova consulta?\n1. Sim\n2. Sair\n"))

    if opcao == 1:
        main()
    else:
        print('saindo...')
if __name__ == "__main__":
    main()




