BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """Класс, описывающий книгу.

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        # Пример:
        # >>> book = Book(id_=1, name='test_name_1', pages=200)
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id_={self.id}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books: list[Book] = None):
        """Класс, описывающий библиотеку.

        :param books: Список книг
        # Примеры:
        # >>> library_1 = Library()
        # >>> library_2 = Library(books=list_books)
        """
        self.books = [] if books is None else books

    def get_next_book_id(self):
        """Метод, возвращающий идентификатор для добавления новой книги в библиотеку."""
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, id_: int):
        """Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса."""
        for index, book in enumerate(self.books):
            if id_ == book.id:
                return index
            else:
                raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
