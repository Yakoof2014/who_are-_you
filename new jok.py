print('привет сегодня ты узнаешь кто ты из смешариков\n')

points=0
question1="Вопрос 1 ты любишь играть на улице?"
question2='Вопрос 2 ты любишь тишину? '
question3='Вопрос 3 любишь ли ты музыку?'
question4='Вопрос 4 ты к птицам или к животным?'
question5='Вопрос 5 ты спокойный?'

print(question1)
print('1 да.2 нет.3 неочень.')
answer = int(input())
points += answer

print(question2)
print('1 да.2 нет.')
answer = int(input())
points += answer

print(question3)
print('1 да.2 нет .3 неочень.')
answer = int(input())
points += answer

print(question4)
print('1 к птицам .2 к животным.')
answer = int(input())
points += answer

print(question5)
print('1 да.2 нет.')
answer = int(input())
points += answer

if points <= 6:
    print("поздравляю ты совунья!!!!!!!!!")
elif points == 7:
    print("поздравляю ты лосяш!!!!!!")
elif points ==8:
    print("поздравляюсты ёжик!!!!!!")
elif points ==9:
    print("поздравляю ты крош!!!!!!!!!")
else :
    print("поздравляю ты копатыч!!!!!!!!")