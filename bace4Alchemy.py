from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создание базы данных и сессии
engine = create_engine('sqlite:///my_database.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Определение модели таблицы
class MyTable(Base):
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Создание таблицы
Base.metadata.create_all(engine)

# Заполнение таблицы
data = [
    {'name': 'John', 'age': 25},
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 35}
]

for item in data:
    record = MyTable(**item)
    session.add(record)

session.commit()