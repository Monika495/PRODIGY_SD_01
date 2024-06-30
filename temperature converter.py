TEMPERATURE_SCALES = {
    'Celsius': 'C',
    'Fahrenheit': 'F',
    'Kelvin': 'K' }
def convert_temperature(value, inputt, output):
    if inputt == 'C':
        if output == 'F':
            return value * 1.8 + 32
        elif output == 'K':
            return value + 273.15
        else:
            return value
    elif inputt == 'F':
        if output == 'C':
            return (value - 32) / 1.8
        elif output == 'K':
            return (value + 459.67) * 5 / 9
        else:
            return value
    elif inputt == 'K':
        if output == 'C':
            return value - 273.15
        elif output == 'F':
            return value * 9 / 5 - 459.67
        else:
            return value
    else:
        return value
while True:
    print('Enter the input temperature value:')
    value = float(input())
    print('Enter the input temperature scale (C, F, or K):')
    inputt = input().upper()
    print('Enter the output temperature scale (C, F, or K):')
    output = input().upper() 
    result = convert_temperature(value, inputt, output)
    print(f'{value} {inputt} = {result} {output}')
    print('Enter q to quit, or enter to continue:')
    choice = input()
    if choice.lower() == 'q':
        break
