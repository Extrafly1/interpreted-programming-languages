import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('fitness_club.db')
cursor = conn.cursor()

# Экспорт в XML
cursor.execute('SELECT * FROM Clients')
rows = cursor.fetchall()

root = ET.Element('Clients')
for row in rows:
    client = ET.SubElement(root, 'Client')
    ET.SubElement(client, 'ID').text = str(row[0])
    ET.SubElement(client, 'Name').text = row[1]
    ET.SubElement(client, 'Age').text = str(row[2])
    ET.SubElement(client, 'Gender').text = row[3]

tree = ET.ElementTree(root)
tree.write('clients.xml')

# Импорт из XML
tree = ET.parse('clients.xml')
root = tree.getroot()

for client in root:
    data = (
        client.find('ID').text,
        client.find('Name').text,
        client.find('Age').text,
        client.find('Gender').text
    )
    print(data)

conn.close()
