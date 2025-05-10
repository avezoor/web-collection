import random
from flask import Flask, render_template
from config import (
    SECRET_KEY, DEBUG, THEME, HOST, PORT,
    GALLERY_IMAGES, PROFILE_IMAGES, get_random_image,
    GALLERY_DATA, HALL_OF_FAME_DATA, PEOPLE_DATA, ORG_STRUCTURE
)

# Create Flask app
app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['THEME'] = THEME
app.debug = DEBUG

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    # Buat daftar gallery items dengan mengambil data dari konfigurasi
    gallery_items = []
    for item in GALLERY_DATA:
        gallery_item = item.copy()  # Buat salinan item
        gallery_item['image'] = get_random_image(GALLERY_IMAGES)  # Tambahkan gambar acak
        gallery_items.append(gallery_item)
    
    # Acak urutan gallery items
    random.shuffle(gallery_items)
    
    return render_template('gallery.html', gallery_items=gallery_items)

@app.route('/hall-of-fame')
def hall_of_fame():
    # Buat daftar hall of fame items dengan mengambil data dari konfigurasi
    hall_of_fame_items = []
    for item in HALL_OF_FAME_DATA:
        hof_item = item.copy()  # Buat salinan item
        hof_item['image'] = get_random_image(PROFILE_IMAGES)  # Tambahkan gambar acak
        hall_of_fame_items.append(hof_item)
    
    # Acak urutan hall of fame items
    random.shuffle(hall_of_fame_items)
    
    return render_template('hall_of_fame.html', hall_of_fame_items=hall_of_fame_items)

@app.route('/people')
def people():
    # Buat daftar people items dengan mengambil data dari konfigurasi
    people_items = []
    for item in PEOPLE_DATA:
        people_item = item.copy()  # Buat salinan item
        people_item['image'] = get_random_image(PROFILE_IMAGES)  # Tambahkan gambar acak
        people_items.append(people_item)
    
    # Acak urutan people items
    random.shuffle(people_items)
    
    return render_template('people.html', people_items=people_items)

@app.route('/structure')
def structure():
    # Gunakan struktur organisasi dari konfigurasi
    return render_template('structure.html', org_structure=ORG_STRUCTURE)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
