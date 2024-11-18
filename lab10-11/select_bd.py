import sqlite3

conn = sqlite3.connect('fitness_club.db')
cursor = conn.cursor()

# 1. Сколько раз каждый клиент посетил клуб
cursor.execute('''
SELECT Clients.Name, COUNT(Visits.ID) AS VisitCount
FROM Clients
LEFT JOIN Visits ON Clients.ID = Visits.ClientID
GROUP BY Clients.Name;
''')
print(cursor.fetchall())

# 2. Суммарная стоимость всех абонементов
cursor.execute('''
SELECT SUM(Price) AS TotalRevenue FROM Memberships;
''')
print(cursor.fetchone())

# 3. Самый посещаемый тренер
cursor.execute('''
SELECT Trainers.Name, COUNT(Visits.ID) AS VisitCount
FROM Trainers
LEFT JOIN Visits ON Trainers.ID = Visits.TrainerID
GROUP BY Trainers.Name
ORDER BY VisitCount DESC
LIMIT 1;
''')
print(cursor.fetchone())

conn.close()
