import mysql.connector

def get_employee_info(username, password):
    try:

        db_connection = mysql.connector.connect(
            host="localhost",
            user="login",
            password="login",
            database="worker"
        )

        cursor = db_connection.cursor()

        sql_query = f"""
            SELECT workers.name, workers.position_code, workers.full_title_position
            FROM users
            JOIN workers ON users.id = workers.ID
            JOIN profession_table ON workers.position_code = profession_table.position_code
            WHERE users.username = '{username}' AND users.password = '{password}'
        """


        cursor.execute(sql_query)

        result = cursor.fetchone()
        cursor.close()
        db_connection.close()

        return result

    except Exception as e:
        print(f"Error: {e}")
        return None

