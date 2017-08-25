annualInterestRate=0.18
#annualInterestRate=float(input("Input the Annual Interest Rate: "))
monthlyInterestRate=annualInterestRate/12
balance=999999
#balance=float(input("Input the Initial Balance: "))
OpeningBalance=balance
PaidOff=False
ClosingBalance=1
interest=0
#Duration=int(input("Input the number of months that you would like to pay the debt off: "))
Duration=12
GuesstimateTotalInterest=(OpeningBalance*annualInterestRate*(Duration/12)/2)
GuesstimateFixedPayments=(OpeningBalance+GuesstimateTotalInterest)/Duration

while PaidOff==False:
    OpeningBalance=balance
    for x in range(1,Duration+1):
        interest=monthlyInterestRate*OpeningBalance
        ClosingBalance=OpeningBalance-GuesstimateFixedPayments+interest
        OpeningBalance=ClosingBalance
    #print("Fixed payment: "+str(GuesstimateFixedPayments))
    #print("Error: "+str(ClosingBalance))
    #print("-----------")
    if ClosingBalance>0.0000000000000001 or ClosingBalance<-0.0000000000000001:
        GuesstimateFixedPayments=GuesstimateFixedPayments+ClosingBalance/Duration
    else:
        PaidOff=True

GuesstimateFixedPayments=round(GuesstimateFixedPayments,2)
print("Lowest payment: "+str((GuesstimateFixedPayments)))
