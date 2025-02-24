import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загружаем обработанный файл
file_path = "/content/Schedule_with_Crew.csv"  # Убедись, что путь правильный
schedule_df = pd.read_csv(file_path)

# Преобразуем колонку 'Assigned crew' в строковый формат и считаем количество членов экипажа
schedule_df['Assigned crew'] = schedule_df['Assigned crew'].fillna('').astype(str)
schedule_df['Assigned crew count'] = schedule_df['Assigned crew'].apply(lambda x: x.count(',') + 1 if x else 0)

# Вычисляем нехватку экипажа
schedule_df['Crew Shortage'] = schedule_df['Cabin crew'] - schedule_df['Assigned crew count']
schedule_df['Crew Shortage'] = schedule_df['Crew Shortage'].apply(lambda x: max(x, 0))

# 📊 Визуализация 1: Количество членов экипажа на рейсах
plt.figure(figsize=(12, 6))
sns.barplot(x='Flight', y='Assigned crew count', data=schedule_df, color='blue', label='Назначено')
sns.barplot(x='Flight', y='Cabin crew', data=schedule_df, color='red', alpha=0.5, label='Требуется')
plt.xticks(rotation=45)
plt.legend()
plt.title("Сравнение требуемого и назначенного экипажа на рейсах")
plt.ylabel("Количество членов экипажа")
plt.show()

# 📊 Визуализация 2: Нехватка экипажа
plt.figure(figsize=(12, 6))
sns.barplot(x='Flight', y='Crew Shortage', data=schedule_df, color='orange')
plt.xticks(rotation=45)
plt.title("Нехватка экипажа по рейсам")
plt.ylabel("Число недостающих членов экипажа")
plt.show()
