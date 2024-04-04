# Personagem: classe mae
# heroi: classe filha
# vilao: classe filha

# class Personagem:
import random

class Personagem:
    # atributos
    def __init__(self, nome, vida, nivel):
        # atributos privados
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
        
    # métodos
    def get_nome(self):
        return self.__nome
    def get_vida(self):
        return self.__vida
    def get_nivel(self):
        return self.__nivel    
    def exibir_detalhes(self):
        return f'\nNome: {self.get_nome()}, \nVida: {self.get_vida()}, \nNível: {self.get_nivel()}'
    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0           
    
    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)
        print(f'{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano.')

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
        
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}, \nHabilidade: {self.get_habilidade()}'
    
    def atacar_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_ataque(dano)
        print(f'{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano.')
        
class Vilao(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
        
    def get_tipo(self):
        return self.__tipo
    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}, \nTipo: {self.get_tipo()}'

# classe Jogo   
class Jogo:
    # método construtor
    def __init__(self):
        self.heroi = None
        self.vilao = None
    # método
    def iniciar_jogo(self):
        nome_heroi = input('Digite o nome do herói: ')
        nome_vilao = input('Digite o nome do vilão: ')
        
        self.heroi = Heroi(nome=nome_heroi, vida=100, nivel=5, habilidade='Super força')  
        self.vilao = Vilao(nome=nome_vilao, vida=80, nivel=5, tipo='Inteligência')

        self.iniciar_batalha()
    # método
    def iniciar_batalha(self):
        print('Batalha iniciada...')        
        while self.heroi.get_vida() > 0 and self.vilao.get_vida() > 0:
            self.exibir_detalhes_personargens()
            self.realizar_ataque_heroi()
            if self.vilao.get_vida() > 0:
                self.vilao.atacar(self.heroi)
        self.exibir_resultado_batalha()        

    def exibir_detalhes_personargens(self):        
        print('\n Detalhes dos personagens:')
        print(self.heroi.exibir_detalhes())
        print(self.vilao.exibir_detalhes())

    def realizar_ataque_heroi(self):
        input('\nPressione Enter para atacar...')
        while True:
            escolha = input('Escolha: 1 - Ataque normal, 2 - Ataque especial: ')
            if escolha == '1':
                self.heroi.atacar(self.vilao)                
            elif escolha == '2':
                self.heroi.atacar_especial(self.vilao)                
            else:
                print('Escolha inválida. Por favor, escolha 1 para ataque normal ou 2 para ataque especial.')
    
    def exibir_resultado_batalha(self):          
        if self.heroi.get_vida() > 0:
            print('O herói venceu a batalha.')
        else:
            print('O vilão venceu a batalha.')            

# instanciando objetos
jogo = Jogo()
jogo.iniciar_jogo()

