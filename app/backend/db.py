from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Создаём движок
engine = create_engine("sqlite:///taskmanager.db", echo=True)
# Создаём сессию связи с БД
SessionLocal = sessionmaker(bind=engine)


# Класс будущей БД, будет объединять таблицу БД и классы создающие таблицы
class Base(DeclarativeBase):
    pass


