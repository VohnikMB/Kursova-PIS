def object_nameDef(object_name):
    file_name = f"Data/tips/{object_name}.txt"
    file_content = ""
    try:

        with open(file_name, 'r', encoding='utf-8') as file:
            file_content = file.read()
        return file_content

    except Exception as e:
        print(f"Помилка при зчитуванні файлу: {e}")
        import traceback
        traceback.print_exc()
        return ""