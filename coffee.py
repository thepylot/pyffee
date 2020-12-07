class CoffeeShop:
    
    menu = {
        'latte':5,
        'americano':10.99,
        'espresso':7,
        'capuccino':12.70,
        'coffee with milk':8
    }

    def __init__(self):
        self.total = 0
        self.items = []

    def add(self, item):
        """
        MENU
        =======================
        latte: 5$,
        americano: 10.99$,
        espresso: 7$,
        capuccino: 12.70$,
        coffee with milk: 8$
        =======================
        """
        self.items.append(item)
        self.total += self.menu[item]

    def print_bill(self, tax, service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total
        total = self.total + tax + service

        for item in self.items:
            print(f'{item:20} ${self.menu[item]}')
        print(f'Tax: {round(tax, 2)}$')
        print(f'Service: {round(service, 2)}$')
        print(f'Total: {round(total, 2)}$')

coffee = CoffeeShop()
print(coffee.add.__doc__)

while True:
    try:
        new_item = input('Enter which coffee do you want: ')
        coffee.add(new_item)
        more = input('Anything else? (y/n): ')
        if more == 'y':
            continue
        else:
            coffee.print_bill(10, 10)
            break
    except KeyError:
        print('-- Please enter valid item --')
        continue
        