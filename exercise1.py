bill = input('How much is your total bill?:')
payment = input('How much is your payment?:')
change = float(bill) - float(payment)
print("Hi! Your change is:"+str(change))