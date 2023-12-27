import sqlalchemy as sq
from sqlalchemy.orm import declarative_base

Base = declarative_base() # функция для создания таблиц (классов)

# Класс который регестирует своих наследников по которым создает таблицы
class Publisher(Base):    # Издатель-автор
    __tablename__ = "publisher"  # Создаём таблицу "course"
    __table_args__ = {'schema': 'book_stores'}
    id_publisher = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    name_publisher = sq.Column(sq.String(length=40), unique=True)

    def __str__(self):  # определяем что будет выводить обьект класса
        return f'Издатель {self.id_publisher}: {self.name_publisher}'

class Book(Base):
    __tablename__ = "book"    # Книги
    __table_args__ = {'schema': 'book_stores'}
    id_book = sq.Column(sq.Integer, primary_key=True, autoincrement=True)   # id
    title = sq.Column(sq.String(length=40), nullable=False)   #  Название
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("book_stores.publisher.id_publisher"), nullable=False)   #

    def __str__(self):  # определяем что будет выводить обьект класса
        return f'Книги {self.id_book} Название {self.title} {self.id_publisher}'

class Shop(Base):
    __tablename__ = "shop"  # Магазин
    __table_args__ = {'schema': 'book_stores'}
    id_shop = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    name_shop = sq.Column(sq.String(length=40), unique=True)

    def __str__(self):  # определяем что будет выводить обьект класса
        return f'Магазин {self.id_shop} Название {self.name_shop}'

class Stock(Base):
    __tablename__ = "stock"  # Остатки
    __table_args__ = {'schema': 'book_stores'}
    id_stock = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book_stores.book.id_book"), nullable=False)  # какой книги
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("book_stores.shop.id_shop"), nullable=False)  # в каком магазине
    count = sq.Column(sq.Integer, nullable=False)  # сколько штук

    def __str__(self):  # определяем что будет выводить обьект класса
        return f'Остатки {self.id_stock} id book {self.id_book} id_shop {self.id_shop} количество {self.count}'

class Sale(Base):
    __tablename__ = "sale"  # Реализация
    __table_args__ = {'schema': 'book_stores'}
    id_sale = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    price = sq.Column(sq.Numeric(precision=5, scale=2), nullable=False)
    data_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("book_stores.stock.id_stock"), primary_key=True)
    count = sq.Column(sq.Integer, nullable=False)

    def __str__(self):  # определяем что будет выводить обьект класса
        return f'Реализация №{self.id_sale} цена {self.priсe} дата {self.data_sale}, {self.id_stock}шт'



# Функция для создания таблиц
# указываем наш движок
def create_tables(engine):
    # метод drop_all() - удаляет таблицы созданные ранее
    Base.metadata.drop_all(engine)
    # метод create_all() - создает таблицы и связанные с ними таблицы
    # если таблица создана, ошибки не будет
    Base.metadata.create_all(engine)
