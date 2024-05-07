while True:
    try:
        x = int(input('Enter value for x: '))
        y = int(input('Enter value for y: '))
        break
    except ValueError:
        print('Invalid input. Please enter numeric values for x and y.')

# Rest of your code here...