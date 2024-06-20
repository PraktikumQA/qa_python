import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

# Этот спринт очень тяжело шёл, у меня сейчас каша в голове, скорее всего много чего неправильно сделал.
    def test_init_books_genre_empty(self):
        collector1 = BooksCollector()
        # Проверяем, что словарь books_genre пуст
        assert collector1.books_genre == {}

    @pytest.mark.parametrize("name", [
        "Новая книга",
        "Фантастическая книга",
        "Книга 1",
        "Книга 2",
        "Книга 3"
    ])

    def test_add_new_book_in_books_genre(self, name):
        collector2 = BooksCollector()
        collector2.add_new_book(name)
        # Проверяем, что в словаре books_genre появилась добавленная книга
        assert name in collector2.get_books_genre()

    @pytest.mark.parametrize("name, genre", [
        ("Новая книга", "Фантастика"),
        ("Фантастическая книга", "Фантастика"),
        ("Книга 1", "Детективы"),
        ("Книга 2", "Ужасы"),
        ("Книга 3", "Детективы")
    ])
    def test_set_book_genre_correct(self, name, genre):
        collector3 = BooksCollector()
        collector3.add_new_book(name)
        collector3.set_book_genre(name, genre)
        # Проверяем, что установленный жанр книги соответствует ожидаемому жанру
        assert collector3.get_book_genre(name) == genre

    def test_get_books_genre_empty(self):
        collector6 = BooksCollector()

        actual_books_genre = collector6.get_books_genre()
        # Проверяем, что полученный словарь пустой
        assert actual_books_genre == {}

    def test_get_books_with_specific_genre_correct(self):
        collector = BooksCollector()

        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Детективы")

        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 2", "Ужасы")

        collector.add_new_book("Книга 3")
        collector.set_book_genre("Книга 3", "Детективы")
        # проверяем, что в списке есть только книги жанра "Детективы"
        detective_books = collector.get_books_with_specific_genre("Детективы")

        assert detective_books == ["Книга 1", "Книга 3"]

    def test_get_books_genre_correct(self):
        collector6 = BooksCollector()
        collector6.add_new_book("Гордость и предубеждение и зомби")
        collector6.set_book_genre("Гордость и предубеждение и зомби", "Фантастика")
        # Проверяем, что в словаре books_genre есть книга "Гордость и предубеждение и зомби" с жанром "Фантастика"
        assert collector6.get_books_genre() == {"Гордость и предубеждение и зомби": "Фантастика"}

    def test_get_books_for_children_correct(self):
        collector7 = BooksCollector()
        collector7.add_new_book("Книга 1")
        collector7.set_book_genre("Книга 1", "Фантастика")

        collector7.add_new_book("Книга 2")
        collector7.set_book_genre("Книга 2", "Ужасы")

        collector7.add_new_book("Книга 3")
        collector7.set_book_genre("Книга 3", "Детективы")

        collector7.add_new_book("Книга 4")
        collector7.set_book_genre("Книга 4", "Мультфильмы")

        collector7.add_new_book("Книга 5")
        collector7.set_book_genre("Книга 5", "Комедии")

        children_books = collector7.get_books_for_children()

        expected_children_books = ["Книга 1", "Книга 4", "Книга 5"]
        # Проверяем, что в списке книг для детей есть только книги у которых нет возрастного рейтинга
        assert children_books == expected_children_books

    def test_add_book_in_favorites_added(self):
        collector8 = BooksCollector()
        collector8.add_new_book("Любимая книга")
        collector8.add_book_in_favorites("Любимая книга")
        favorites_books = collector8.get_list_of_favorites_books()
        # Проверяем, что книга присутствует в списке избранных
        assert "Любимая книга" in favorites_books

    def test_delete_book_from_favorites_deleted(self): # позитивная проверка на удаление книги из списка любимых книг
        collector11 = BooksCollector()
        collector11.add_new_book("Любимая книга")
        collector11.add_book_in_favorites("Любимая книга")
        collector11.delete_book_from_favorites("Любимая книга")
        favorites_books = collector11.get_list_of_favorites_books()
        assert "Любимая книга" not in favorites_books

    def test_delete_book_from_favorites_empty(self): # удаляем книгу из пустого списка избранных книг
        collector9 = BooksCollector()
        collector9.delete_book_from_favorites("Любимая книга")
        favorites_books = collector9.get_list_of_favorites_books()
        # Проверяем, что книга не присутствует в списке избранных
        assert len(favorites_books) == 0

    def test_get_list_of_favorites_books_empty(self):
        collector10 = BooksCollector()
        favorites_books = collector10.get_list_of_favorites_books()
        # Проверяем, что список любимых книг пуст
        assert len(favorites_books) == 0