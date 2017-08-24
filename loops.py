i = 1

while i < 11:
	print i
	i += 1

coins = 0
print "You have %d coins." % (coins)
moreCoins = raw_input("Would you like another coin? ")
while coins >= 0:
	if moreCoins == 'yes':
		coins += 1
		print "You have %s coins." % (coins)
		moreCoins = raw_input("Would you like another coin? ")	
	else:			
		print "Bye."
		break
			

