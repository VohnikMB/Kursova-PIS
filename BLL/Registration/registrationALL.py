import mysql.connector
import re

def check_username_exists(username):
    db_config = {
        "host": "localhost",
        "user": "registration",
        "password": "registration",
        "database": "worker"
    }

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    try:
        query = "SELECT COUNT(*) FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        return result[0] > 0
    finally:
        cursor.close()
        connection.close()

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(pattern, password):
        return True
    else:
        return False

def maxID():
    db_config = {
        "host": "localhost",
        "user": "registration",
        "password": "registration",
        "database": "worker"
    }

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    try:
        query = "SELECT MAX(id) FROM users"
        cursor.execute(query)
        max_id = cursor.fetchone()[0]

        return max_id
    finally:
        cursor.close()
        connection.close()



def register_new_worker(username, password, position_code, name, full_title_position):
    # З'єднання з базою даних
    connection = mysql.connector.connect(
        host="localhost",
        user="registration",
        password="registration",
        database="worker"
    )

    cursor = connection.cursor()

    try:
        # Додаємо користувача до таблиці `users`
        user_query = "INSERT INTO users (id, username, password) VALUES (%s, %s, %s)"
        user_values = (maxID()+1, username, password)
        cursor.execute(user_query, user_values)
        connection.commit()
        # Отримуємо id нового користувача
        user_id = maxID()

        # Додаємо працівника до таблиці `workers`
        worker_query = "INSERT INTO workers (ID, position_code, name, full_title_position) VALUES (%s, %s, %s, %s)"
        worker_values = (user_id, position_code, name, full_title_position)
        cursor.execute(worker_query, worker_values)

        # Зберігаємо зміни
        connection.commit()

        print("Новий працівник зареєстрований успішно!")
        return True

    except Exception as e:
        print(f"Помилка: {e}")

    finally:
        # Закриття з'єднання з базою даних
        cursor.close()
        connection.close()

