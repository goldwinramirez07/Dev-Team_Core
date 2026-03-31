def calculate_user_profile(names, ages, saleries):
    """Process user data and return analysis"""

    total_ages = sum(ages)
    average_age = total_ages / len(names)

    processed_user_data = []
    user_processed_data = []
    user_net_salary = []
    user_status = []

    for index, age in enumerate(ages):
        try:
            name = names[index]
            salary = saleries[index]
        except IndexError as error:
            raise ValueError("names, ages, or saleries lists contain None values") from error

        tax = salary * 0.15
        net = salary - tax

        processed_user_data.append({"name": name, "age": age})
        user_processed_data.append(processed_user_data)
        user_net_salary.append(net)

        if average_age > 30:
            status = "Senior"
        elif average_age < 25:
            status = "Junior"
        else:
            status = "Mid"

        user_status.append({"net_salary": net, "status": status})
        processed_user_data = [] # Resetting the processed_user_data for next iteration

    return user_processed_data, average_age, tuple(user_status)