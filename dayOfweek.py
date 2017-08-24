"""day = int(raw_input("Enter a number between 0-6: "))

if day == 0:
	print "Sunday"
elif day == 1:
	print "Monday"
elif day == 2:
	print "Tuesday"
elif day == 3:
	print "Wednesday"
elif day == 4:
	print "Thursday"
elif day == 5:
	print "Friday"
elif day == 6:
	print "Saturday"""

day = int((raw_input("Enter a number between 0-6: ")))
sunday = 0
monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6

if day == saturday or day == sunday:
	print "Sleep in! Yay!"
else:
	print "Grrr! Get up and go to work."