"""
Проект FitLife - MVP версия 1.0

Данный проект реализует MVP проекта FitLife
Программа запрашивает у клиента имя, возраст, вес рост
Вычисляет bmi, рекомендуемую норму воды
Затем вежливо приветсвует пользователя и выдает рекомендации
"""

WATER_PER_KG = 30
ML_IN_LITRE = 1000


def get_input_untill_numeric(message: str) -> str:
    """
    Функция для ввода пользователем числа (если ввод не число, просит ввести число еще раз)

        Параметры:
            message (str): сообщение пользователю

        Возвращаемое значение:
            input_variable (str): ввод пользователя
    """
    while True:
        try:
            input_variable = input(message)
            _ = float(input_variable)
            return input_variable
        except ValueError:
            print("Ответ должен быть числом, попробуйте еще раз")


user_name = input("Добрый день! Как Вас зовут?\n").title()
user_age = int(get_input_untill_numeric("Сколько вам полных лет?\n"))

user_weight = float(input("Какой у Вас вес (в кг)?\n").replace(",", "."))
user_height = float(
    input("Какой у Вас рост (в метрах, например 1.75)?\n").replace(",", ".")
)

bmi = user_weight / (user_height**2)
water_needed = (user_weight * WATER_PER_KG) / ML_IN_LITRE

print(f"\nОтчет для пользователя: {user_name} ({user_age} г.)")
print(f"Ваш Индекс Массы Тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_needed:.3f} л. в день", end="\n\n")
print("Расчет окончен. Будьте здоровы!")
