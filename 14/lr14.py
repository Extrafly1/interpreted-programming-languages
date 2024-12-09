import xml.etree.ElementTree as ET
from collections import defaultdict

def parse_osm(file_path):
    parking_count = defaultdict(int)

    tree = ET.parse(file_path)
    root = tree.getroot()

    ns = {'osm': 'http://www.openstreetmap.org/osm/0.6'}

    for element in root.findall(".//node") + root.findall(".//way"):
        tags = {tag.get('k'): tag.get('v') for tag in element.findall(".//tag")}
        if tags.get('amenity') == 'parking':
            parking_type = tags.get('parking', 'unknown')  # Тип парковки, если он указан
            parking_count[parking_type] += 1

    return dict(parking_count)

file_path = '11 - 2.osm'

results = parse_osm(file_path)

print("Количество парковок каждого типа:")
for parking_type, count in results.items():
    print(f"{parking_type}: {count}")
