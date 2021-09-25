import random 
money_man = 1000
money_auto = 1000
rnd = 0
user_choise = ""

print ("Вы подошли к автвмату и сели за него. У вас есть 1000$ и вы можете удовоить эту сумму.")
user_choise = input ("нажмите 1 для игры, нажмите 2 для того чтобы уйти." )
if user_choise == "1":
	print("Вы не ушли из казино и начали играть. Ставка равна 1$. ") 
	while money_man > 1:
		print("Вы нажали на рычаг и колесо покрутилось.")
		rnd = random.randrange(1, 1000, 1 )
		if rnd == 777:
			money_man += 1
			print("Вы выигарли")
		else :
			print("Вы проиграли")
else:
	print("Вы ушли и не потратили денег." )