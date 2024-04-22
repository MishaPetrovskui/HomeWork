import random

def generate_expression():
    operator = '+'
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    return f"{num1} {operator} {num2}"

def calculate(num1, operator, num2):
    return num1 + num2

def main():
    print("Добро пожаловать в математическую игру!")
    print("Введите результат выражения. Для выхода из игры введите 'q'.")
    score = 0
    while True:
        expression = generate_expression()
        num1, _, num2 = expression.split()
        correct_answer = calculate(int(num1), None, int(num2))
        user_input = input(f"Решите выражение {expression}: ")
        if user_input.lower() == 'q':
            break
        user_answer = user_input.strip()
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if user_answer == correct_answer:
                print("Правильно!")
                score += 1
            else:
                print("Неправильно. Правильный ответ:", correct_answer)
        else:
            print("Некорректный ввод. Попробуйте еще раз.")
    print("Ваш счет:", score)
    
main()
