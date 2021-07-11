string = str(input("\nНапишіть свій рядок: "))
answer = ""
numbers = []
maxInNumbers = 0
answerNumbers = []

flag = False
for letter in string:
    if letter.isdigit():
        if flag:
            numbers[len(numbers) - 1] += str(letter)
        else:
            numbers.append(letter)
        flag = True
    else:
        flag = False

numbers = [int(x) for x in numbers]

string = string.replace('0', '')
string = string.replace('1', '')
string = string.replace('2', '')
string = string.replace('3', '')
string = string.replace('4', '')
string = string.replace('5', '')
string = string.replace('6', '')
string = string.replace('7', '')
string = string.replace('8', '')
string = string.replace('9', '')

print("\nВилучені номери:", numbers)

dividedString = string.split(' ')

for word in dividedString:
    if word:
        word = str(word).upper()[0] + word[1:]
        word = word[:len(word) - 1] + str(word).upper()[len(word) - 1]
        answer += word + ' '

print("\nПереробленний рядок:", answer)

try: 
    maxInNumbers = max(numbers)
except:
    maxInNumbers = 0
print("\nМаксимальне число -", maxInNumbers)

for i in range(len(numbers)):
    if numbers[i] != maxInNumbers:
        answerNumbers.append(int(numbers[i]) ** i)
    else:
        answerNumbers.append(numbers[i])

print("\nМасив чисел пиднесенний до степеня: ", answerNumbers)
