import datetime


class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        try:
            if len(name) == 0 or len(name) > 40:
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
            elif name not in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')
            else:
                self.__name_items.append(name)
                self.__number_items += 1

        except ValueError as e:
            print(f"{type(e).__name__}: {e}")

        except NameError as e:
            print(f"{type(e).__name__}: {e}")

    def delete_item_from_check(self, name):
        try:
            if name not in self.__name_items:
                raise NameError('Позиция отсутствует в чеке')
            else:
                self.__name_items.remove(name)
                self.__number_items -= 1

        except NameError as e:
            print(f"{type(e).__name__}: {e}")

    def check_amount(self):
        total = []
        for name_item in self.__name_items:
            try:
                total.append(self.__item_price[name_item])
            except KeyError:
                print(f"Позиция {name_item} отсутствует в товарном справочнике")

        if len(total) > 10:
            return sum(total) * 0.9
        else:
            return sum(total)

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        try:
            for name_item in self.__name_items:
                if name_item not in self.__tax_rate:
                    raise KeyError(f"Позиция {name_item} отсутствует в налоговом справочнике")
                elif name_item not in self.__item_price:
                    raise KeyError(f"Позиция {name_item} отсутствует в товарном справочнике")

                if self.__tax_rate[name_item] == 20:
                    twenty_percent_tax.append(name_item)
                    total.append(self.__item_price[name_item])

        except KeyError as e:
            print(f"{type(e).__name__}: {e}")

        return (sum(total) * 0.9) * 0.2 if len(twenty_percent_tax) > 10 else sum(total) * 0.2

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []

        try:
            for name_item in self.__name_items:
                if name_item not in self.__tax_rate:
                    raise KeyError(f"Позиция {name_item} отсутствует в налоговом справочнике")
                elif name_item not in self.__item_price:
                    raise KeyError(f"Позиция {name_item} отсутствует в товарном справочнике")

                if self.__tax_rate[name_item] == 10:
                    ten_percent_tax.append(name_item)
                    total.append(self.__item_price[name_item])

        except KeyError as e:
            print(f"{type(e).__name__}: {e}")

        return (sum(total) * 0.9) * 0.1 if len(ten_percent_tax) > 10 else sum(total) * 0.1

    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    def get_telephone_number(self, telephone_number):
        try:
            if not isinstance(telephone_number, int):
                raise ValueError('Необходимо ввести цифры')
            elif len(str(telephone_number)) > 10:
                raise ValueError('Необходимо ввести 10 цифр после "+7"')
            else:
                return f'+7{telephone_number}'
        except ValueError as e:
            print(f"{type(e).__name__}: {e}")

    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()

        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year]
        ]

        for interval in date:
            date_and_time.append(f'{interval[0]}: {interval[1](now)}')

        return date_and_time
#ну да, ну да
