billAmt = float(raw_input("Total bill amount: "))
serviceLevel = raw_input("Service level: ")
numPeople = int(raw_input("Split between how many: "))

if serviceLevel == "good":
	tip = .20
elif serviceLevel == "fair":
	tip = .15
elif serviceLevel == "poor":
	tip = .10

def calcTip(billAmt, serviceLevel):
	tipAmt = billAmt * tip
	total = billAmt + tipAmt
	perPerson = total/numPeople

	print "Tip amount: %.2f " % (tipAmt)
	print "Total amount: %.2f " % (total)
	print "Amount per person: %.2f " % (perPerson)

calcTip(billAmt, serviceLevel)
