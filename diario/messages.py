'''
cria mensagens aleatórias de motivação por criar uma memória
'''
from random import randint
def get_message() -> str:
    """
    cria mensagens aleatórias de motivação por criar uma memória
    """
    lista_mensagens = [
    # Focadas no presente e futuro:        
    "Abrace cada momento. Registre e reviva.",
    "Hoje, uma lembrança. Amanhã, um tesouro.",
    "Construa um álbum de memórias, um dia de cada vez.",
    "Momentos únicos merecem ser guardados.",
    "Que tal adicionar mais uma página à sua história?",
    "Registre os detalhes. A vida é feita deles.",
    "Cada memória é uma semente que florescerá.",

    # Focadas no passado e na nostalgia:
    "Reviver é reviver emoções. Registre mais.",
    "Suas memórias são um presente para o futuro.",
    "Um baú de lembranças, sempre à mão.",
    "Que tal voltar no tempo hoje?",
    "Cada memória é um pedacinho de você.",

    # Mensagens mais gerais e inspiradoras
    "A vida é uma jornada. Registre cada passo.",
    "Memórias são como estrelas, iluminando o nosso caminho.",
    "A gratidão é a melhor maneira de registrar os momentos.",
    "Crie um legado de memórias.",
    "A felicidade está nos detalhes. Registre-os.",
    ]
    # return lista_mensagens[16]
    return lista_mensagens[randint(0, len(lista_mensagens)-1)]

if __name__ == "__main__":
    print(get_message())