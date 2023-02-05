import doctest


class SocialNetwork:
    def __init__(self, friends: int, posts: int):
        """
            Создание и подготовка к работе объекта "Социальная сеть"
            :param friends: Количество друзей
            :param posts: Количество записей на странице
            Примеры:
            >>> social_net = SocialNetwork(500, 10)
            """
        self.friends = friends
        self.posts = posts

    @property
    def friends(self) -> int:
        """Возвращает количество друзей профиля социальной сети."""
        return self._friends

    @friends.setter
    def friends(self, friends: int) -> None:
        """Устанавливает количество друзей профиля социальной сети."""
        if not isinstance(friends, int):
            raise TypeError("Количество друзей должно быть типа int")
        if friends <= 0:
            raise ValueError("Количество друзей должно быть положительным числом")
        self._friends = friends

    @property
    def posts(self) -> int:
        """Возвращает количество записей на странице профиля социальной сети."""
        return self._posts

    @posts.setter
    def posts(self, posts: int) -> None:
        """Устанавливает количество записей на странице профиля социальной сети."""
        if not isinstance(posts, int):
            raise TypeError("Количество записей должно быть типа int")
        if posts <= 0:
            raise ValueError("Количество записей должно быть положительным числом")
        self._posts = posts

    def to_add_friends(self, number_of_new_friends: int) -> None:
        """
            Добавление новых друзей.
            :param number_of_new_friends: Количество добавляемых новых друзей
            Примеры:
            >>> social_net = SocialNetwork(500, 10)
            >>> social_net.to_add_friends(2)
            """
        if not isinstance(number_of_new_friends, int):
            raise TypeError("Количество друзей должно быть типа int")
        if number_of_new_friends < 0:
            raise ValueError("Количество друзей должно быть положительным числом")
        self.friends += number_of_new_friends

    def is_there_videos(self) -> bool:
        """
            Функция, которая проверяет, есть ли видеоролики на странице профиля социальной сети.
            :return: Есть ли видеоролики
            Примеры:
            >>> social_net = SocialNetwork(500, 10)
            >>> social_net.is_there_videos()
            """
        ...

    def __str__(self):
        return f'Количество друзей профиля социальной сети: {self.friends}.\n' \
               f'Количество записей на странице профиля социальной сети: {self.posts}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.friends!r}, {self.posts!r})'


class InstagramPage(SocialNetwork):
    def __init__(self, friends: int, posts: int, subscribers: int, stories: int):
        """
            Создание и подготовка к работе объекта "Профиль инстаграма"
            :param subscribers: Количество подписчиков
            :param stories: Количество историй на странице
            Примеры:
            >>> inst_page = InstagramPage(500, 10, 1000, 2)
            """
        super().__init__(friends, posts)
        self.subscribers = subscribers

        if not isinstance(stories, int):
            raise TypeError("Количество историй должно быть типа int")
        if stories <= 0:
            raise ValueError("Количество историй должно быть положительным числом")
        self.stories = stories

    @property
    def subscribers(self) -> int:
        """Возвращает количество подписчиков профиля инстаграма."""
        return self._subscribers

    @subscribers.setter
    def subscribers(self, subscribers: int) -> None:
        """Устанавливает количество подписчиков профиля инстаграма."""
        if not isinstance(subscribers, int):
            raise TypeError("Количество подписчиков должно быть типа int")
        if subscribers <= 0:
            raise ValueError("Количество подписчиков должно быть положительным числом")
        self._subscribers = subscribers

    def is_there_videos(self) -> bool:
        """
            Функция, которая проверяет, есть ли reels на странице профиля инстаграм.
            :return: Есть ли reels
            Примеры:
            >>> inst_page = InstagramPage(500, 10, 1000, 2)
            >>> inst_page.is_there_videos()
            """
        ...

    def __str__(self):
        return f'Количество друзей профиля инстаграм: {self.friends}.\n' \
               f'Количество записей на странице профиля социальной сети: {self.posts}.\n' \
               f'Количество подписчиков профиля инстаграм: {self.subscribers}.\n' \
               f'Количество историй на странице профиля социальной сети: {self.stories}.'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.friends!r}, {self.posts!r}, {self.subscribers!r}, {self.stories!r})'


if __name__ == "__main__":
    doctest.testmod()


