import random
from pymongo import MongoClient
from bson import ObjectId
from faker import Faker
from datetime import datetime, timedelta

# Configuración inicial
fake = Faker()
client = MongoClient('mongodb://localhost:27017/')
db = client['gymbroDB']


# Generar 30 usuarios aleatorios
users = []
for _ in range(30):
    experience = random.choice(['beginner', 'intermediate', 'advanced'])
    age = random.randint(18, 65)
    sex = random.choice(["M","F"])  # M: Masculino, F: Femenino, 
    height = round(random.uniform(150, 200), 1)
    weight = round(random.uniform(50, 120), 1)
    
    # Generar disponibilidad aleatoria
    days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    availability = []
    for day in random.sample(days, random.randint(2, 5)):
        hour = f"{random.randint(6, 10):02d}:00-{random.randint(16, 22):02d}:00"
        availability.append(f"{day} {hour}")
    
    user = {
        "_id": ObjectId(),
        "username": fake.user_name(),
        "height": height,
        "weight": weight,
        "experience": experience,
        "age": age,
        "sex": sex,
        "availability": availability,
        "description": fake.sentence()
    }
    users.append(user)

# Insertar usuarios
db.users.insert_many(users)
print("Insertados 30 usuarios")

# Generar 10 spots aleatorios
spots = []
spot_types = ['gym', 'park', 'outdoors', 'studio', 'community center', 'private space'] 
for _ in range(10):
    creator = random.choice(users)['_id']
    
    spot = {
        "_id": ObjectId(),
        "user_id": creator,
        "name": fake.company(),
        "location": fake.address(),
        "schedule": f"{random.choice(['Lunes-Viernes', 'Lunes-Sábado', 'Todos los días'])}, {random.randint(6, 8):02d}:00-{random.randint(20, 23):02d}:00",
        "type": random.choice(spot_types),
        "description": fake.sentence()
    }
    spots.append(spot)

# Insertar spots
db.spots.insert_many(spots)
print("Insertados 10 spots")

# Generar 5 trainings aleatorios
trainings = []
training_types = ['cardio', 'strength', 'yoga']
for _ in range(5):
    organizer = random.choice(users)['_id']
    spot = random.choice(spots)
    
    # Generar fecha aleatoria en los próximos 30 días
    date = datetime.now() + timedelta(days=random.randint(1, 30))
    time = f"{random.randint(6, 20):02d}:00"
    datetime_str = date.strftime('%Y-%m-%d') + ' ' + time
    
    training = {
        "_id": ObjectId(),
        "user_id": organizer,
        "spot_id": spot['_id'],
        "type": random.choice(training_types),
        "level": random.choice(['beginner', 'intermediate', 'advanced']),
        "datetime": datetime_str,
        "description": fake.sentence()
    }
    trainings.append(training)

# Insertar trainings
db.training.insert_many(trainings)
print("Insertados 5 trainings")

print("Generación de datos completada!")

