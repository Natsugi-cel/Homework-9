print("Hello world")

#- домашній номер телефону (тільки цифри та довжина номера)
home_phone_numbers = ["123456", "1234", "1234567", "+12345"]

for number in home_phone_numbers:
    if re.match(r"^\d{6}$", number):
        print(f"Phone number {number} is correct")
    else:
        print(f"Phone number {number} is not correct")

#- Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
mobile_phone_numbers = ["+380123456789", "380123456789", "+3801234567892", "+3801234567", "++380123456789"]

for number in mobile_phone_numbers:
    if re.match(r"^\+?\d{12}$", number):
        print(f"Phone number {number} is correct")
    else:
        print(f"Phone number {number} is not correct")

# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
users = ["Vasya Vasya Vasya", "vasya vasya vasya", "vasya1 vasya vasya", "vasya_vasya vasya", "vasya vasya vasya vasya"]

for user in users:
    if re.match(r"^[A-ZА-ЯЁЇІҐЄ][a-zа-яёїієґ]{1,19}\s[A-ZА-ЯЁЇІҐЄ][a-zа-яёїієґ]{1,19}\s[A-ZА-ЯЁЇІҐЄ][a-zа-яёїієґ]{1,19}$", user):
        print(f"User {user} is correct")
    else:
        print(f"User {user} is not correct")
