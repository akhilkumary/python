import random

customer_list = ["Akhil", "Buddha", "Christ", "David", "Elijah", "Forrest", "Ganesh", "Hanuman"]

print(customer_list[random.randint(0, len(customer_list)) - 1])

print(random.choice(customer_list))