import sqlite3

# Создание БД
conn = sqlite3.connect('fitness_club.db')
cursor = conn.cursor()

# Создание таблиц
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clients (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Age INTEGER NOT NULL,
    Gender TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Memberships (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Type TEXT NOT NULL,
    Price REAL NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Trainers (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Specialization TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Visits (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ClientID INTEGER NOT NULL,
    TrainerID INTEGER NOT NULL,
    VisitDate TEXT NOT NULL,
    FOREIGN KEY(ClientID) REFERENCES Clients(ID),
    FOREIGN KEY(TrainerID) REFERENCES Trainers(ID)
);
''')

conn.commit()
conn.close()

conn = sqlite3.connect('fitness_club.db')
cursor = conn.cursor()

# Заполнение данных
cursor.executemany('INSERT INTO Clients (Name, Age, Gender) VALUES (?, ?, ?)', [
    ('Иван Иванов', 25, 'М'),
    ('Мария Смирнова', 30, 'Ж'),
    ('Петр Петров', 35, 'М'),
])

cursor.executemany('INSERT INTO Memberships (Type, Price) VALUES (?, ?)', [
    ('Месячный', 2000.0),
    ('Квартальный', 5000.0),
    ('Годовой', 15000.0),
])

cursor.executemany('INSERT INTO Trainers (Name, Specialization) VALUES (?, ?)', [
    ('Алексей', 'Кардиотренировки'),
    ('Анна', 'Силовые тренировки'),
    ('Елена', 'Йога'),
])

cursor.executemany('INSERT INTO Visits (ClientID, TrainerID, VisitDate) VALUES (?, ?, ?)', [
    (1, 1, '2024-11-15'),
    (2, 2, '2024-11-16'),
    (3, 3, '2024-11-17'),
])

conn.commit()
conn.close()
