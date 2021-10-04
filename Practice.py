#285 Programming HW1
stock_symbol = input("Enter your stock_symbol ")
Allotment = input("Enter no. of shares alloted ")
Final_Share_Price = input("Enter Final Share price in dollars ")
Proceeds = int(Allotment) * float(Final_Share_Price)
print('Proceeds is $' + str(Proceeds))
Sell_Commission = input("Enter your Sell Commission ")
Buy_Commision = input("Enter your Buy Commission ")
Commision = int(Sell_Commission) + int(Buy_Commision)
Initial_Share_Price = input(" Enter intial share price in dollars ")
Total_Shares_Purchase = int (Allotment)* int(Initial_Share_Price)

Total_Spent = int(Commision) + int(Total_Shares_Purchase)
Capital_Gain = int(Proceeds) - int(Total_Spent)
Tax_Capital_Gain = input("enter the tax rate ")
Tax =  int(Capital_Gain) * float (int(Tax_Capital_Gain)/100)
Cost = int(Total_Spent) + float(Tax)
print("Tax is $" +str(Tax))
print("Cost is $"+ str(Cost))
Net_Profit = float(Proceeds) - float(Cost)
print("Net_Profit is $"+ str(Net_Profit))
Return_on_investement =  float(float(Net_Profit)/int(Cost)*100)
print("Return on investments is " + str(Return_on_investement) +"%")
Break_even_price =float (int(Commision) / int(Allotment)) + int(Initial_Share_Price)
print("Break even price is $" + str(Break_even_price))








