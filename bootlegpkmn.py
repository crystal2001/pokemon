
import time
import random
print()
print('-' * 80)

print('A wild Jigglypuff appears')
time.sleep(0.2)
print('You only have one Pokèmon, Snorlax.')
time.sleep(1)
print('I choose you Snorlax!!!')
time.sleep(1)
print()
# Starting HP
snorlax_hp = 200
jiggly_hp = 125

print()

print('Starting HP')
time.sleep(0.2)
print('-Snorlax HP: ' + str(snorlax_hp))
time.sleep(0.2)
print('-Jigglypuff HP: ' + str(jiggly_hp))
time.sleep(0.2)
print()
time.sleep(0.2)
print()

while snorlax_hp > 0 and jiggly_hp > 0:

	print('Battle Options:')
	time.sleep(0.2)
	print('-[1] Sleep Heal')
	time.sleep(0.2)
	print('-[2] Tackle')
	time.sleep(0.2)
	print('-[3] Roundhouse Kick')
	time.sleep(0.2)
	print('-[4] Hyper Beam')
	time.sleep(0.2)
	print('-[5] Run')
	time.sleep(0.2)
	

	your_move = input('Choose a move using the corresponding number ')
	print()
	if your_move == '1':
		print('Snorlax uses Sleep Heal')
		snorlax_hp = snorlax_hp + 50
		print('Snorlax uses Sleep Heal, his HP increases to ' + str(snorlax_hp))
		time.sleep(0.2)

	elif your_move == '2':
		jiggly_hp = jiggly_hp - 10
		print('Snorlax uses tackele and deals 10 damage to JigglyPuff!')
		time.sleep(0.2)

	elif your_move == '3':
		jiggly_hp = jiggly_hp - 3
		print('Snorlax uses RoundHouse Kick and deals 3 damage to JigglyPuff!')
		time.sleep(0.2)

	elif your_move == '4':
		jiggly_hp = jiggly_hp - 40
		print('Snorlax uses HyperBeam and deals 40 damage to JigglyPuff!')
		time.sleep(0.2)

	elif your_move == '5':
		running = random.randint(1,2)
	elif running == 1:
		print('You were able to escape')
		break
	else:
		print('You could not escape!')
	
	print()

	# Jigglypuff
	enemy_move = random.randint(1,2)
	enemy_move = str(enemy_move)

	if enemy_move == '1':
		snorlax_hp = snorlax_hp - 30
		jiggly_hp = jiggly_hp + 30
		print('Jigglypuff uses Singing, dealing 30 damage and gaining 30 HP!')
		time.sleep(0.2)

	elif enemy_move == '2':
		snorlax_hp = snorlax_hp - 50
		print('Jigglypuff uses headbutt dealing 50 damage to Snorlax!')
		time.sleep(0.2)

	print()

	#Check for overkill and if so, set hp to 0
	if snorlax_hp < 0:
		snorlax_hp = 0

	if jiggly_hp < 0:
		jiggly_hp < 0

	print('Updated HP1')
	time.sleep(0.2)
	print('-Snorlax HP: ' + str(snorlax_hp))
	time.sleep(0.2)
	print('-Jigglypuff HP: ' + str(jiggly_hp))
	time.sleep(0.2)
	print()
	time.sleep(0.2)


if snorlax_hp == 0:
	print('Snorlax has faninted! The Jigglypuff Wins.')
elif jiggly_hp == 0:
	print('The Jigglypuff has faninted. Snorlax wins!')