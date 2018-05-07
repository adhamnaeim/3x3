import Siga
import TicTacToe as Tic
import RocketCollider as Rocket

# this is simple file for testing purposes, real mainframe won't be anything like this.

while True:
	Siga.runGame()
	if bool(input('>>> ')) == True:
		break