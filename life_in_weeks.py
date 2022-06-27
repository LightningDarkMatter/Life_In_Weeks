age = input("How old are you? ")
age = int(age)

remaining_life = 90 - age

days = remaining_life * 365
weeks = round(days / 7)
months = round(days / 30)


print(f"You have {days} days, {weeks} weeks and {months} months left in your life.")