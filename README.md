# Flight Crew Scheduler ✈️  
#This project automatically assigns crew to flights based on their flight hours and availability.

📌 Functionality:
Assigning captains, first officers and flight attendants
Keeping track of flight limits
Identifying staff shortages
Export schedule with crew to CSV

What code did 
Loaded the data

Read two CSV files:
List.csv.csv - flight schedule
Pilots.csv.csv - crew list.
Converted the data

Corrected numbers (replaced commas with dots to process them correctly as floats).
Checked correctness of column names (Qulification vs Qualification) to avoid errors.
Categorized the crew

Captains
First officers
Cabin crew
Assigned crew to flights

Looked for available captains, officers and cabin crew.
Checked their available flight hours to make sure they didn't exceed the limits.
Selected randomly from available candidates.
Processed crew shortages

If there were not enough flight attendants, displayed a warning (⚠️ NOTE!).
Save the result

Created a new CSV file Schedule_with_Crew.csv with the assigned crew.
What is this useful for?
✅ Automation - the program assigns the crew itself, saving time.
✅ Overtime control - we make sure that no one is working overtime.
✅ Forecasting problems - we can see where we are short of people and correct the situation in advance.
✅ Optimizing the airline's operations - more efficient use of personnel.

Этот проект автоматически назначает экипаж на рейсы с учетом их налёта и доступности.  

## 📌 Функционал:  
- Назначение капитанов, первых офицеров и бортпроводников  
- Учет лимитов налёта  
- Выявление нехватки персонала  
- Экспорт расписания с экипажем в CSV
- 

## 🚀 Запуск:  

![image](https://github.com/user-attachments/assets/f4123b81-61fd-4f22-8f3c-7c7b6b266da0)

Что сделали?
Загрузили данные

Прочитали два CSV-файла:
List.csv.csv – расписание рейсов
Pilots.csv.csv – список экипажа
Преобразовали данные

Исправили числа (заменили запятые на точки, чтобы корректно обрабатывались как float).
Проверили правильность названий колонок (Qulification vs Qualification), чтобы избежать ошибок.
Разделили экипаж по категориям

Captains (капитаны)
First officers (вторые пилоты)
Cabin crew (бортпроводники)
Назначили экипаж на рейсы

Искали доступных капитанов, офицеров и бортпроводников.
Проверяли их доступные лётные часы, чтобы не превышать лимиты.
Выбирали случайным образом из доступных кандидатов.
Обработали случаи нехватки экипажа

Если не хватало бортпроводников, выводили предупреждение (⚠️ ВНИМАНИЕ!).
Сохранили результат

Создали новый CSV-файл Schedule_with_Crew.csv с назначенным экипажем.
Для чего это полезно?
✅ Автоматизация – программа сама распределяет экипаж, экономя время.
✅ Контроль переработок – следим, чтобы никто не перерабатывал сверх нормы.
✅ Прогнозирование проблем – видим, где не хватает людей, и можем заранее исправить ситуацию.
✅ Оптимизация работы авиакомпании – более эффективное использование персонала.
---------------------------------------------------------

