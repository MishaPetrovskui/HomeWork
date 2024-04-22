import random
def generate_expression():
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if operator == '/':
        while num1 % num2 != 0:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
    expression = str(num1) + ' ' + operator + ' ' + str(num2)
    return expression
def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 // num2
def main():
    print("Добро пожаловать в математическую игру!")
    print("Введите результат выражения. Для выхода из игры введите 'q'.")
    score = 0
    while True:
        expression = generate_expression()
        num1, operator, num2 = expression.split()
        num1 = float(num1)
        num2 = float(num2)
        correct_answer = calculate(num1, operator, num2)
        user_input = input("Решите выражение {} = ".format(expression))
        if user_input.lower() == 'q':
            break
        try:
            user_answer = float(user_input)
            if user_answer == correct_answer:
                print("Правильно!")
                score += 1
            else:
                print("Неправильно. Правильный ответ:", correct_answer)
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")
    print("Ваш счет:", score)
main()
