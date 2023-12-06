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

        cursor = db_connection.cursor()
        sql_query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(sql_query)
        result = cursor.fetchone()
        cursor.close()
        db_connection.close()

        return bool(result)


    except Exception as e:
        print(f"Error: {e}")
        return False

def validate_password(password):
    # Регулярний вираз для перевірки пароля
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    # Перевірка за допомогою регулярного виразу
    if re.match(pattern, password):
        return True
    else:
        return False