import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загружаем данные
crew_df = pd.read_csv('/content/Pilots.csv.csv')

# Преобразуем запятые в точки (если есть)
crew_df['Flying hours /month'] = (
    crew_df['Flying hours /month']
    .astype(str)
    .str.replace(',', '.')
    .astype(float)
    .fillna(0)
)

# 1️⃣ Диаграмма загруженности экипажа
plt.figure(figsize=(12, 6))
sns.barplot(
    x=crew_df['Name'], 
    y=crew_df['Flying hours /month'], 
    hue=crew_df['Qualification'],  
    dodge=False, 
    palette="viridis"  # Улучшенная цветовая палитра
)
plt.xticks(rotation=90)
plt.xlabel('Имя')
plt.ylabel('Часы налета за месяц')
plt.title('Загруженность экипажа (часы налета)')
plt.legend(title="Должность")
plt.show()

# 2️⃣ Топ-5 самых загруженных сотрудников
top_5_crew = crew_df.nlargest(5, 'Flying hours /month')

plt.figure(figsize=(8, 5))
sns.barplot(
    x=top_5_crew['Flying hours /month'], 
    y=top_5_crew['Name'], 
    palette="Reds_r",
    hue=None  # 🔥 Исправляем предупреждение
)
plt.xlabel('Часы налета')
plt.ylabel('Имя')
plt.title('Топ-5 самых загруженных сотрудников')
plt.show()

# Вывод списка топ-5
print("🏅 Топ-5 самых загруженных сотрудников:")
print(top_5_crew[['Name', 'Qualification', 'Flying hours /month']])
