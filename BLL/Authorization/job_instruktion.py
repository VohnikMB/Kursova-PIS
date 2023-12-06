from PyQt5.QtWidgets import QMessageBox

def jobInstructions_box(work_SQL_inf):
    file_name = f"Data/jobInstructions/{work_SQL_inf}.txt"
    dialog = QMessageBox()
    try:
        file_content = "Помилка, зверніться до HR спеціаліста"
        with open(file_name, 'r', encoding='utf-8') as file:
            file_content = file.read()
        dialog.setText(file_content)
        dialog.setWindowTitle("Посадові інструкції")
        dialog.exec_()

    except Exception as e:
        print(f"Помилка при зчитуванні файлу: {e}")
        import traceback
        traceback.print_exc()
