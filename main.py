snacks = [
    {'id': 1, 'name': 'Chips', 'price': 10, 'available': True},
    {'id': 2, 'name': 'Cookies', 'price': 15, 'available': True},
    {'id': 3, 'name': 'Candies', 'price': 5, 'available': False}
]

sales_record = {}

def display_menu():
    print('\nMenu:')
    print('1. Check inventory')
    print('2. Add a snack to the inventory')
    print('3. Remove a snack from the inventory')
    print('4. Update snack availability')
    print('5. Record a sale')
    print('6. Exit')

def check_inventory():
    print('\nCurrent Inventory:')
    for snack in snacks:
        availability = 'Available' if snack['available'] else 'Not available'
        print(f"ID: {snack['id']}, Name: {snack['name']}, Price: {snack['price']}, Availability: {availability}")

def add_snack():
    snack_id = int(input('Enter the snack ID: '))
    if any(snack['id'] == snack_id for snack in snacks):
        print('A snack with the same ID already exists.')
        return
    name = input('Enter the snack name: ')
    price = float(input('Enter the snack price: '))
    available = input('Is the snack available? (yes/no): ').lower() == 'yes'
    snacks.append({'id': snack_id, 'name': name, 'price': price, 'available': available})
    print(f'Snack with ID {snack_id} has been added to the inventory.')

def remove_snack():
    snack_id = int(input('Enter the snack ID: '))
    for snack in snacks:
        if snack['id'] == snack_id:
            snacks.remove(snack)
            print(f'Snack with ID {snack_id} has been removed from the inventory.')
            return
    print('No snack found with the given ID.')

def update_availability():
    snack_id = int(input('Enter the snack ID: '))
    for snack in snacks:
        if snack['id'] == snack_id:
            snack['available'] = not snack['available']
            availability = 'Available' if snack['available'] else 'Not available'
            print(f'Snack with ID {snack_id} is now {availability}.')
            return
    print('No snack found with the given ID.')

def record_sale():
    snack_id = int(input('Enter the snack ID: '))
    for snack in snacks:
        if snack['id'] == snack_id:
            if not snack['available']:
                print('This snack is currently unavailable.')
                return
            if snack_id in sales_record:
                sales_record[snack_id] += 1
            else:
                sales_record[snack_id] = 1
            print('Sale recorded.')
            return
    print('No snack found with the given ID.')

# Main program loop
while True:
    display_menu()
    choice = input('Enter your choice (1-6): ')
    
    if choice == '1':
        check_inventory()
    elif choice == '2':
        add_snack()
    elif choice == '3':
        remove_snack()
    elif choice == '4':
        update_availability()
    elif choice == '5':
        record_sale()
    elif choice == '6':
        break
    else:
        print('Invalid choice!')

print('Thank you for using the snack inventory management system.')
