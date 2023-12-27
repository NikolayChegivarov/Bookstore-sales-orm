import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale
from config import login, password, name_database

# DSN - Data Source Name (строка подключения к источнику)
# DSN = "драйвер подключения://логин:пароль@Название сервера:хост/Название базы данных"
DSN = f"postgresql://{login}:{password}@localhost:5432/{name_database}"
engine = sqlalchemy.create_engine(DSN)   # create_engine() - функция sqlalchemy для подключения к базе данных (движок)
# подключиться к схеме сразу (попробовать в сл раз)
# engine = create_engine(connection_string, echo=True, execution_options={"my_schema": {None: schema}})

create_tables(engine)  # импортируем из соседнего файла

# создаем сессию с помощью функции sessionmaker(сессия = движок) аналог курсора
# с помощью сессии получаеются и отправляются данные
# создаем класс который умеет создавать сессии
Session = sessionmaker(bind=engine)  # класс
session = Session()  # экземпляр класса - сессия
# в конце сессию нужно закрыть
# session.close()

# course2 = Course(name='Pythonnnnn') # создать строку в таблице Course
# session.add(course2)   # Добавить одну строку

pub1 = Publisher(name_publisher='СТИВЕН КИНГ')
pub2 = Publisher(name_publisher='Сэр Артур Игнатиус Конан Дойл')
pub3 = Publisher(name_publisher='Нора Сакавич')
pub4 = Publisher(name_publisher='Мосян Тунсю')
session.add_all([pub1, pub2, pub3, pub4])
session.commit()
# Добаляю список строк

Book1 = Book(title='Зеленая миля', id_publisher='1')
Book2 = Book(title='Побег из Шоушенка', id_publisher='1')
Book3 = Book(title='Шерлок Хомс', id_publisher='2')
Book4 = Book(title='Собака Баскервилей', id_publisher='2')
Book5 = Book(title='Лисья нора', id_publisher='3')
Book6 = Book(title='Свита короля', id_publisher='3')
Book7 = Book(title='Благословение небожителей', id_publisher='4')
Book8 = Book(title='Основатель темного пути', id_publisher='4')
session.add_all([Book1, Book2, Book3, Book4, Book5, Book6, Book7, Book8])
session.commit()
# Добаляю список строк

Sh1 = Shop(name_shop='Страницы снов')
Sh2 = Shop(name_shop='Тайная комната')
session.add_all([Sh1, Sh2])
session.commit()

St1 = Stock(id_book='1', id_shop='1',  count='13')
St2 = Stock(id_book='2', id_shop='1',  count='7')
St3 = Stock(id_book='3', id_shop='1',  count='5')
St4 = Stock(id_book='4', id_shop='1',  count='7')
St5 = Stock(id_book='5', id_shop='1',  count='12')
St6 = Stock(id_book='6', id_shop='1',  count='3')
St7 = Stock(id_book='7', id_shop='1',  count='9')
St8 = Stock(id_book='8', id_shop='1',  count='14')
St9 = Stock(id_book='1', id_shop='2',  count='6')
St10 = Stock(id_book='2', id_shop='2',  count='4')
St11 = Stock(id_book='3', id_shop='2',  count='5')
St12 = Stock(id_book='4', id_shop='2',  count='8')
St13 = Stock(id_book='5', id_shop='2',  count='12')
St14 = Stock(id_book='5', id_shop='2',  count='15')
St15 = Stock(id_book='7', id_shop='2',  count='2')
session.add_all([St1, St2, St3, St4, St5, St6, St7, St8, St9, St10, St11, St12, St13, St14, St15])
session.commit()

Sh1 = Sale(price='315.50', data_sale='01.12.2023', id_stock='1', count='2')
Sh2 = Sale(price='514.60', data_sale='02.12.2023', id_stock='2', count='1')
Sh3 = Sale(price='812.00', data_sale='03.12.2023', id_stock='3', count='2')
Sh4 = Sale(price='210.60', data_sale='05.12.2023', id_stock='4', count='1')
Sh5 = Sale(price='625.00', data_sale='06.12.2023', id_stock='5', count='2')
Sh6 = Sale(price='785.60', data_sale='06.12.2023', id_stock='6', count='1')
Sh7 = Sale(price='255.00', data_sale='07.12.2023', id_stock='7', count='2')
Sh8 = Sale(price='960.00', data_sale='08.12.2023', id_stock='8', count='1')
Sh9 = Sale(price='650.50', data_sale='09.12.2023', id_stock='9', count='2')
Sh10 = Sale(price='950.50', data_sale='09.12.2023', id_stock='10', count='2')
Sh11 = Sale(price='240.60', data_sale='10.12.2023', id_stock='11', count='1')
Sh12 = Sale(price='365.50', data_sale='11.12.2023', id_stock='12', count='2')
Sh13 = Sale(price='965.60', data_sale='13.12.2023', id_stock='13', count='1')
Sh14 = Sale(price='645.50', data_sale='14.12.2023', id_stock='14', count='2')
Sh15 = Sale(price='956.60', data_sale='15.12.2023', id_stock='15', count='1')
Sh16 = Sale(price='315.50', data_sale='16.12.2023', id_stock='1', count='2')
Sh17 = Sale(price='514.60', data_sale='16.12.2023', id_stock='2', count='1')
Sh18 = Sale(price='812.00', data_sale='20.12.2023', id_stock='3', count='2')
Sh19 = Sale(price='210.60', data_sale='21.12.2023', id_stock='4', count='1')
session.add_all([Sh1, Sh2, Sh3, Sh4, Sh5, Sh6, Sh7, Sh8, Sh9, Sh10, Sh11, Sh12, Sh13, Sh14, Sh15, Sh16, Sh17, Sh18, Sh19])



def get_publisher_sales(id_publisher):
   sales = session.query(Publisher, Book, Stock, Sale)\
       .join(Book, Publisher.id_publisher == Book.id_publisher) \
       .join(Stock, Book.id_book == Stock.id_book) \
       .join(Sale, Stock.id_stock == Sale.id_stock) \
       .filter(Publisher.id_publisher == id_publisher).all()
   return sales

id_publisher_ = input(f'введите id_publisher: ')
sales = get_publisher_sales(id_publisher_)
for sale in sales:
   print(f'Автор {sale.Publisher.name_publisher} проданная книга {sale.Book.title}  {sale.Sale.data_sale} цена {sale.Sale.price}')

session.commit()  # фиксируем изменения
# print(pub2)

session.close()
