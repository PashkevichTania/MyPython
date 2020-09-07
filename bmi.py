def bmi():
    from colorama import init
    init()
    from colorama import Fore, Back, Style

    m = int(input('enter your weight '))
    h1 = int(input('enter your height in santimetres '))
    h2 = h1/100
    bmi = m/(h2*h2)

    bmi = float('{:.1f}'.format(bmi))
    print('your bmi is = ', bmi )

    if bmi <= 15 :
        print( Fore.MAGENTA)
        print('Very severely underweight')
    if 15 < bmi <= 16 :
        print( Fore.BLUE)
        print('Severely underweight')
    if 16 < bmi <= 18.5 :
        print( Fore.CYAN)
        print('Underweight')
    if 18.5 < bmi <= 25 :
        print( Fore.GREEN)
        print('Normal')
    if 25 < bmi <= 30 :
        print( Fore.YELLOW)
        print('Overweight')
    if 30 < bmi <= 35 :
        print( Fore.RED)
        print('Obese Class I (Moderately obese)')
    if 35 < bmi <= 40 :
        print( Fore.RED)
        print('Obese Class II (Severely obese)')
    if 40 < bmi :
        print( Fore.RED)
        print('Obese Class III and more (Very obese)')
    print( Fore.RESET)

while True:
    x = (input('enter bmi or exit '))
    if x == 'bmi' :
        bmi()
    elif x == 'exit' :
        break
    else :
        print('error')
print('finishing')
