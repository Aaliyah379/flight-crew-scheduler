import pandas as pd
import random

# Загружаем данные
schedule_df = pd.read_csv('/content/List.csv.csv')
crew_df = pd.read_csv('/content/Pilots.csv.csv')

# Преобразуем запятые в числах в точки
crew_df['Flying hours /month'] = (
    crew_df['Flying hours /month']
    .astype(str)
    .str.replace(',', '.')
    .astype(float)
    .fillna(0)
)
crew_df['Maximum hour /month'] = (
    crew_df['Maximum hour /month']
    .astype(str)
    .str.replace(',', '.')
    .astype(float)
    .fillna(0)
)
schedule_df['Flying time (hours)'] = (
    schedule_df['Flying time (hours)']
    .astype(str)
    .str.replace(',', '.')
    .astype(float)
)

# Проверяем корректность названия колонки
if 'Qulification' in crew_df.columns:
    qual_col = 'Qulification'
elif 'Qualification' in crew_df.columns:
    qual_col = 'Qualification'
else:
    raise KeyError("В файле нет колонки 'Qulification' или 'Qualification'!")

# Фильтруем экипаж по квалификации
captains = crew_df[crew_df[qual_col] == 'Captain'].copy()
first_officers = crew_df[crew_df[qual_col] == 'First officer'].copy()
cabin_crew = crew_df[crew_df[qual_col] == 'Cabin crew'].copy()

def assign_crew_to_flight(row):
    assigned_crew = []  # Создаем список для экипажа
    
    # Выбираем капитана
    available_captains = captains[
        (captains['Flying hours /month'] + row['Flying time (hours)']) <= captains['Maximum hour /month']
    ]
    if not available_captains.empty:
        selected_captain = available_captains.sample(1)
        assigned_crew.append(selected_captain.iloc[0]['Name'])
    
    # Выбираем первого офицера
    available_first_officers = first_officers[
        (first_officers['Flying hours /month'] + row['Flying time (hours)']) <= first_officers['Maximum hour /month']
    ]
    if not available_first_officers.empty:
        selected_first_officer = available_first_officers.sample(1)
        assigned_crew.append(selected_first_officer.iloc[0]['Name'])
    
    # Назначаем бортпроводников
    available_cabin_crew = cabin_crew[
        (cabin_crew['Flying hours /month'] + row['Flying time (hours)']) <= cabin_crew['Maximum hour /month']
    ]

    num_cabin_crew = int(row['Cabin crew'])

    if len(available_cabin_crew) >= num_cabin_crew:
        selected_cabin_crew = available_cabin_crew.sample(num_cabin_crew)
    else:
        selected_cabin_crew = available_cabin_crew  # Берем всех, кто остался
        print(f"⚠️ ВНИМАНИЕ! Для рейса {row['Flight']} не хватает бортпроводников! "
              f"Требуется {num_cabin_crew}, но доступно только {len(available_cabin_crew)}.")

    assigned_crew += selected_cabin_crew['Name'].tolist()

    # Проверяем и выводим сообщение
    print(f"Рейс {row['Flight']}: Требуется {row['Cabin crew']} бортпроводников, Назначено {len(assigned_crew) - 2}")

    return ', '.join(assigned_crew) if assigned_crew else 'Не удалось назначить экипаж'

# Применяем функцию к каждому рейсу
schedule_df['Assigned crew'] = schedule_df.apply(assign_crew_to_flight, axis=1)

# Сохраняем результат
output_file = '/content/Schedule_with_Crew.csv'
schedule_df.to_csv(output_file, index=False)

print(f'Готово, любимая! Файл сохранен: {output_file} 💖')
