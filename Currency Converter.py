with open('Currency.txt.txt') as f:
	lines = f.readlines()

CurrencyDict = {}
for line in lines:
	parsed = line.split("\t")
	CurrencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter amount:\n"))
print("Enter the name of the Currency you want to convert this amount to? Available Options:\n")
[print(item) for item in CurrencyDict.keys()]
Currency = input("Please enter one of these values: \n")
print(f"{amount} INR is equal to {amount *float(CurrencyDict[Currency])} {Currency}")
