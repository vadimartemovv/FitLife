# Проект FitLife - MVP версия 1.0


def get_input_untill_numeric(message: str) -> float:
    """
    Функция для проверки ввода пользователя
    Просим пользователя ввести число (возраст, вес, тд)
    Если введено не число, выдаем что нужно число
    и просим еще раз ввести число
    """
    while True:
        try:
            input_variable = input(message)
            _ = float(input_variable)
            return input_variable
        except ValueError:
            print("Ответ должен быть числом, попробуйте еще раз")


# 1. Знакомство
user_name = input("Добрый день! Как Вас зовут?\n")
user_age = int(get_input_untill_numeric("Сколько вам полных лет?\n"))

# 2. Сбор данных
user_weight = float(get_input_untill_numeric("Какой у Вас вес (в кг)?\n"))
user_height = float(
    get_input_untill_numeric("Какой у Вас рост (в метрах, например 1.75)?\n")
)

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# Расчёт индекса массы тела
bmi = user_weight / (user_height**2)

# Подсчет воды: вес * 30 мл с конвертацией в литры
WATER_PER_KG = 30
water_needed = user_weight * WATER_PER_KG // 1000

# 4. Вывод красивого результата
print(f"\nОтчет для пользователя: {user_name} ({user_age} г.)")
print(f"Ваш Индекс Массы Тела: {bmi:.2f}")
print(f"Рекомендуемая норма воды: {water_needed:.2f} л. в день", end="\n\n")
print("Расчет окончен. Будьте здоровы!")
