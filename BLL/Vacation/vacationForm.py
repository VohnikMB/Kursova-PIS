import os
from datetime import datetime


def generate_leave_request(pib, position, typeVacation, start_date, end_date, reason):
    if typeVacation == 2:
        type_vacation = "відпустку за власний рахунок"
    else:
        type_vacation = "оплачувану відпустку"
    date = datetime.now().strftime("%d-%m-%Y")
    company = "Company Knot Group"
    company_address = "м. Львів, вул. В'язова, 34А"
    contact_number = "+380123456789"

    html_content = f"""
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Заява на відпустку</title>
        <style>
            body {{
                margin: 20px;
            }}
            .content {{
                margin: 10px;
            }}
            .first-line {{
                margin-left: 25px;
                margin: 20px;
            }}
        </style>
    </head>
    <body>

        <div class="content">
            <h4>{pib}</h4>
            <p>{position}</p>
            <p>{company}</p>
            <p>{company_address}</p>
            <p>{contact_number}</p>
            <p>{date}</p>
            <br>
            <h4>Гуцулі О.</h4>
            <p>HR менеджеру</p>
            <p>{company_address}</p>

            <h2 align="center">ЗАЯВА</h2>

            <p class="first-line">Звертаюсь до вас із проханням надати мені {type_vacation} на період з {start_date} по {end_date}. У зв'язку з {reason}. Готовий надати усі необхідні документи, у визначений компанією період.</p>
            <br>
            <p>З повагою,<br>
            {pib}</p>
        </div>
    </body>
    </html>
    """

    directory = "C:/Users/PC/Desktop/GIT/Kursova-PIS/Data/forms/"
    os.makedirs(directory, exist_ok=True)

    file_name = f"{date}_{pib}_заява_на_відпустку.html"
    file_path = os.path.join(directory, file_name)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)
        return True

