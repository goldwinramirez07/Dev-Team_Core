def calculate_user_profile(names, ages, saleries):
    """Process user data and return analysis"""

    total_age = 0
    for idx in range(len(ages)):
        total_age += ages[idx]

    average_age = total_age / len(names)

    processed_data = []
    for idx, name in enumerate(names):
        salary = saleries[idx]
        tax = salary * 0.15
        net = salary - tax
        user_profile = {
            'name': name,
            'salary': salary,
            'tax': tax,
            'net': net
        }
        processed_data.append(user_profile)

    status = None  # Initialize the variable before using it in the conditional statement
    if average_age > 30:
        status = "Senior"
    elif average_age < 25:
        status = "Junior"
    else:
        status = "Mid"

    return [item for item in processed_data], average_age, status