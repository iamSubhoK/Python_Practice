income = [10, 30, 50]

def double_money(dollars):
    return dollars * 2

#using map function
#like - map(double_money, income)

new_income = list(map(double_money, income))
print(new_income)
