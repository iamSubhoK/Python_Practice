def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100 - age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

subhos_data = [25, 10, 12]
debos_data = [24, 10, 0]

health_calculator(subhos_data[0], subhos_data[1], subhos_data[2])
health_calculator(debos_data[0], debos_data[1], debos_data[2])

health_calculator(*subhos_data) # takes the lists of subhos_data and the * unpacks the list to the arg and do the process