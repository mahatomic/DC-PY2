import doctest


class Garland:
    def __init__(self, color: str, glow_mode: str):
        """
            Создание и подготовка к работе объекта "Гирлянда"
            :param color: Цвет гирлянды
            :param glow_mode: Режим свечения гирлянды
            Примеры:
            >>> garland = Garland('синий', 'непрерывный')
            """
        self.color = color
        self.glow_mode = glow_mode

    def turn_on_the_garland(self) -> None:
        """
            Включение гирлянды в сеть.
            Примеры:
            >>> garland = Garland('синий', 'непрерывный')
            >>> garland.turn_on_the_garland()
            """
        ...

    def set_the_glow_mode(self, another_glow_mode: str) -> None:
        """
            Изменение режима свечения гирлянды.
            :param another_glow_mode: Другой режим свечения гирлянды.
            Примеры:
            >>> garland = Garland('синий', 'непрерывный')
            >>> garland.set_the_glow_mode('мерцание')
            """
        ...


class CoffeeMachine:
    def __init__(self, volume_of_the_tank: int, current_volume_of_water: int):
        """
            Создание и подготовка к работе объекта "Кофеварка"
            :param volume_of_the_tank: Объем бака для воды
            :param current_volume_of_water: Текущее количество воды в баке
            Примеры:
            >>> coffee_machine = CoffeeMachine(500, 200)
            """
        if not isinstance(volume_of_the_tank, int):
            raise TypeError("Объем бака для воды должен быть типа int")
        if volume_of_the_tank <= 0:
            raise ValueError("Объем бака для воды должен быть положительным числом")
        self.volume_of_the_tank = volume_of_the_tank

        if not isinstance(current_volume_of_water, int):
            raise TypeError("Текущее количество воды в баке должно быть int")
        if current_volume_of_water < 0:
            raise ValueError("Текущее количество воды в баке не может быть отрицательным числом")
        self.current_volume_of_water = current_volume_of_water

    def add_water_to_the_tank(self, water: int) -> None:
        """
            Добавление воды в бак.
            :param water: Количество добавляемой жидкости
            :raise ValueError: Если количество добавляемой жидкости превышает свободное место в баке, то вызываем ошибку
            Примеры:
            >>> coffee_machine = CoffeeMachine(500, 200)
            >>> coffee_machine.add_water_to_the_tank(300)
            """
        if not isinstance(water, int):
            raise TypeError("Добавляемая жидкость должна быть типа int")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна быть положительным числом")
        ...

    def add_ground_coffee_to_filter(self, number_of_spoons: int) -> None:
        """
            Добавление молотого кофе на фильтр кофеварки.
            :param number_of_spoons: Добавляемое количество ложек молотого кофе
            Примеры:
            >>> coffee_machine = CoffeeMachine(500, 200)
            >>> coffee_machine.add_ground_coffee_to_filter(3)
            """
        if not isinstance(number_of_spoons, int):
            raise TypeError("Количество ложек молотого кофе должно быть типа int")
        if number_of_spoons < 0:
            raise ValueError("Количество ложек молотого кофе должно положительным числом")
        ...

    def brew_coffee(self) -> None:
        """
            Запуск кофеварки для приготовления кофе.
            Примеры:
            >>> coffee_machine = CoffeeMachine(500, 200)
            >>> coffee_machine.brew_coffee()
            """
        ...


class VkontaktePage:
    def __init__(self, friends: int, posts: int):
        """
            Создание и подготовка к работе объекта "Страница ВКонтакте"
            :param friends: Количество друзей
            :param posts: Количество записей на странице
            Примеры:
            >>> vkpage = VkontaktePage(500, 10)
            """
        self.friends = friends
        self.posts = posts

    def to_add_friends(self, number_of_new_friends: int) -> None:
        """
            Добавление новых друзей.
            :param number_of_new_friends: Количество добавляемых новых друзей
            Примеры:
            >>> vkpage = VkontaktePage(500, 10)
            >>> vkpage.to_add_friends(2)
            """
        if not isinstance(number_of_new_friends, int):
            raise TypeError("Количество друзей должно быть типа int")
        if number_of_new_friends < 0:
            raise ValueError("Количество друзей должно быть положительным числом")
        ...

    def is_there_photo(self) -> bool:
        """
            Функция, которая проверяет, есть ли фотография профиля у страницы ВКонтакте.
            :return: Есть ли фотография
            Примеры:
            >>> vkpage = VkontaktePage(500, 10)
            >>> vkpage.is_there_photo()
            """
        ...


if __name__ == "__main__":
    doctest.testmod()


