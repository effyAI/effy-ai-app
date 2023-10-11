def calculator(currentAge, retirementAge, corpusGoal, interestRate):
    print("Function called.")
    interestRate = interestRate/100
    monthlyinterestRate = interestRate / 12
    numberofMonths = (retirementAge - currentAge) * 12
    MonthlySIP = (corpusGoal * monthlyinterestRate) / ((1 + monthlyinterestRate) ** numberofMonths - 1)
    # Initialize a list to store closing balances for each year
    RoundMonthlySIP = round(MonthlySIP/1000) *1000
    closingBalances = []
    openingBalance = 0
    for year in range(currentAge, retirementAge + 1):
                # Calculate the annual contribution (12 times the monthly SIP)
        annualContribution = MonthlySIP * 12
                        # Calculate the interest earned for the year
        interestEarned = (openingBalance + annualContribution) * interestRate
                        # Calculate the closing balance for the year
        closingBalance = openingBalance + annualContribution + interestEarned
                        # Append the closing balance to the list
        closingBalances.append({
                "Age": year,
                "ClosingBalance": round(closingBalance)
            })
        # Update the opening balance for the next year
        openingBalance = closingBalance

    response_data={
        "monthly sip": RoundMonthlySIP,
        "closing balances": closingBalances
    }    

    return response_data