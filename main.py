# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.hide_letter = '*'
		self.hang = 0
		
	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in self.word:
			i = 0
			for letter_aux in self.word:
				if letter == letter_aux:
					self.hide_letter[i] = letter
				i += 1
		else:
			self.hang += 1

	# Método para verificar se o jogo terminou
	def	hangman_over(self):
			if	self.hang	>	5:
				return	False
			elif	'*'	not	in	self.hide_letter:
						return	False
			else:
						return	True

	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if self.hang <= 5 and '*' not in self.hide_letter:
			return True
		else:
			return False

	# Método para não mostrar a letra no board
	def hide_word(self):
		self.hide_letter = ["*" for letter_aux in self.word]
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[self.hang])
		print('\n', self.hide_letter)

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
	with open("palavras.txt", "rt") as f:
		bank = f.readlines()
	return bank[random.randint(0,len(bank))].upper().strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())
	game.hide_word()

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while game.hangman_over():
		game.print_game_status()
		try_letter = input("Tente uma letra: ").strip().upper()
		game.guess(try_letter)

	game.print_game_status()

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print('\nParabéns! Você venceu!!')

	else:
		print('\nGame over! Você perdeu.')
		print('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()

