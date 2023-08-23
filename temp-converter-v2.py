print('Fahrenheit to Celsius')

try:
    fah = float(input('Enter Fahrenheit: '))

    if fah > -459.67:
        initialC = fah - 32
        celsius = initialC * 5/9

        print('Celsius: ', celsius)
    
    else:
        print('Value must be greater than the absolute zero temperature.')

except:
    print('Input Invalid!')
