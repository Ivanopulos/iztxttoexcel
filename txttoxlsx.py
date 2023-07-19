import os
import pandas as pd

# Путь к директории с txt-файлами
dir_path = 'C:\\Users\\.има.\\Desktop\\Новая папка'

# Инициализация списка для хранения данных
data = []

# Проходим по каждому файлу в указанной директории
for file_name in os.listdir(dir_path):
    # Проверяем, является ли файл txt-файлом
    if file_name.endswith('.txt'):
        # Открываем файл
        with open(os.path.join(dir_path, file_name), 'r', encoding='utf-8') as f:
            # Проходим по каждой строке файла
            for line in f:
                # Проверяем, является ли строка непустой
                if line.strip():
                    # Добавляем строку и имя файла в список данных
                    data.append([line.strip(), file_name])

# Создаем DataFrame из данных
df = pd.DataFrame(data, columns=['Text', 'File_Name'])

# Записываем данные в Excel
df.to_excel('output.xlsx', index=False)