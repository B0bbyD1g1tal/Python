# Deposit Calculator

amount = float(input())
deposit_term = int(input())
annual_interest_rate = float(input())

interest_per_month = amount * annual_interest_rate / 100 / 12
result = amount + deposit_term * interest_per_month

print(result)
