# main.py

import pandas as pd
import random
import time
import threading 
from data_sender import send_data_to_web, start_flask_app

# Rastgele isim ve soyisim listeleri
first_names = ["Kadiralp", "Mehmet", "Ali", "Ayşe", "Fatma", "Emre", "Elif", "Can", "Merve", "Burak"]
last_names = ["Yılmaz", "Kaya", "Demir", "Çelik", "Şahin", "Arslan", "Polat", "Kurt", "Öztürk", "Acar","Türker"]

# Rastgele meslek listesi
professions = ["Engineer", "Doctor", "Teacher", "Nurse", "Lawyer", "Architect", "Dentist", "Pharmacist", "Accountant", "Developer"]

# Rastgele veri üretme fonksiyonu
def generate_random_data(num_rows):
    data = {
        "First Name": [random.choice(first_names) for _ in range(num_rows)],
        "Last Name": [random.choice(last_names) for _ in range(num_rows)],
        "Profession": [random.choice(professions) for _ in range(num_rows)]
    }
    return pd.DataFrame(data)

# Veriyi `send_data_to_web` fonksiyonuna göndermek için gerekli kolonlar
df_columns = ["First Name", "Last Name", "Profession"]

# Flask uygulamasını başlatma
flask_thread = threading.Thread(target=start_flask_app)
flask_thread.start()

# Rastgele 10 satırlık veri üretilmesi ve gönderilmesi
df = generate_random_data(10)
for index, row in df.iterrows():
    new_data = row.to_dict()
    send_data_to_web(new_data, df_columns)
    time.sleep(1)  # Her veri gönderimi arasında 1 saniye bekle

print(df)
