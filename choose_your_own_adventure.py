name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input('You are on a dirt road, it has come to an end and you can go left or right. which way you want to go? ').lower()

if answer == 'left':
    answer = input('You come to a river, you can walk around it or swim accross> Type walk to walk and swim to swim accross: ').lower()
    if answer == 'swim':
        print('You swam accross and were eater by an alligator.')
    elif answer == 'walk':
        print('You walked for many miles, ran out of water and lost the game!')
    else:
        print('Not a valid option. You Lose!')
elif answer == 'right':
    answer = input('You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back) ').lower()
    if answer == 'back':
        print('You go back and lose!')
    elif answer == 'cross':
        answer = input('You crossed the bridge and meet a stranger do you talk to them (yes/no)').lower()
        if answer == 'yes':
            print('You talk to the stranger and they gave you gold. You win!')
        elif answer == 'no':
            print('You ignore the stranger and they are offened! You lose!')
        else:
           print('Not a valid option. You Lose!') 
    else:
        print('Not a valid option. You Lose!')
else:
    print('Not a valid option. You Lose!')

print('Thank you for trying!', name)
