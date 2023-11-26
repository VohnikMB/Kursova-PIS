import mysql.connector

def check_credentials(username, password):
    try:
        # З'єднання з базою даних
        db_connection = mysql.connector.connect(
            host="localhost",
            user="login",
            password="login",
            database="worker"
        )

        # Створення курсора
        cursor = db_connection.cursor()

        # SQL-запит для перевірки наявності користувача з введеними логіном та паролем
        sql_query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

        # Виконання запиту
        cursor.execute(sql_query)

        # Отримання результатів
        result = cursor.fetchone()

        # Закриття курсора та з'єднання
        cursor.close()
        db_connection.close()


        return bool(result)

    except Exception as e:
        print(f"Error: {e}")
        return False

# Приклад використання
# username_input = input("Введіть логін: ")
# password_input = input("Введіть пароль: ")
#
# if check_credentials(username_input, password_input):
#     print("Логін та пароль вірні.")
# else:
#     print("Логін або пароль невірні.")


def validate_password(password):
    # Регулярний вираз для перевірки пароля
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    # Перевірка за допомогою регулярного виразу
    if re.match(pattern, password):
        return True
    else:
        return False