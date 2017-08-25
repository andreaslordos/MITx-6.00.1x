#balance=484
#annualInterestRate=0.2
#monthlyPaymentRate=0.04
for x in range(12):
    minpayment=monthlyPaymentRate*balance
    balance=balance-minpayment
    interest=balance*(annualInterestRate/12)
    balance=balance+interest

print("Remaining balance: "+str(round(balance,2)))
