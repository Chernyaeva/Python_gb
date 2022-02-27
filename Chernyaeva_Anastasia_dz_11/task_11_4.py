class Warehouse:

    def _move_item_decorator(func):
        '''
        checks if provided quantity of items is positive number
        would have been easier to make just regular function, but here we want to show off
        '''

        def wrapper(*args, **kwargs):
            if len(args) > 2:
                if type(args[2]) is not int or args[2] < 1:
                    raise TypeError('Number of items must be positive integer')
            return func(*args, **kwargs)

        return wrapper

    def __init__(self):
        self.inventory = {}

    @_move_item_decorator
    def receive_item(self, item, quantity=1):
        item_key = f'{item.maker} {item.model}'
        if item_key not in self.inventory:
            self.inventory[item_key] = quantity
        else:
            self.inventory[item_key] += quantity

    @_move_item_decorator
    def ship_item(self, item, quantity=1):
        item_key = f'{item.maker} {item.model}'
        if item_key not in self.inventory:
            raise ValueError(f'{item_key} not found in warehouse')
        if self.inventory[item_key] < quantity:
            raise ValueError(f'Not enough {item_key} in warehouse to ship')
        if self.inventory[item_key] > quantity:
            self.inventory[item_key] -= quantity
        else:
            del self.inventory[item_key]

    def __str__(self):
        inv_string = '\n'
        inv_string = inv_string.join([f'{key} : {val}' for key, val in self.inventory.items()])
        return inv_string

    def __add__(self, other):
        self.receive_item(other, 1)

    def __sub__(self, other):
        self.ship_item(other, 1)


class Device:
    def __init__(self, maker, model):
        self.maker = maker
        self.model = model

    def __str__(self):
        return f'{self.maker} {self.model}'


class Printer(Device):
    def __init__(self, maker, model, is_color=False, is_laser=False):
        super().__init__(maker, model)
        self.is_color = is_color
        self.is_laser = is_laser


class Scaner(Device):
    def __init__(self, maker, model, is_color=False, is_mobile=False):
        super().__init__(maker, model)
        self.is_color = is_color
        self.is_mobile = is_mobile


class Copier(Device):
    def __init__(self, maker, model, is_color=False, is_laser=False, is_pointless=True):
        super().__init__(maker, model)
        self.is_color = is_color
        self.is_laser = is_laser
        self.is_pointless = is_pointless


store = Warehouse()
a = Printer('HP', 'Laser Jet 2000')
b = Scaner('Ricoh', 'Ultrascan 3000')
c = Copier('Xerox', 'Supercopy 4000', is_laser=True)
print(a)
print(b)
print(c, c.is_color, c.is_laser)

store.receive_item(a, 100)
store.receive_item(b)
store + a
store.receive_item(b)
store.ship_item(a, 50)
store.receive_item(c)
store - c
print(store)
# store.ship_item(c,-1)
# store.ship_item(c)
