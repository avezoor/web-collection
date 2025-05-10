import os
import random
import logging

# Konfigurasi aplikasi
SECRET_KEY = os.environ.get("SESSION_SECRET", "memories-app-secret-key")
DEBUG = True
HOST = '0.0.0.0'
PORT = 5000

# Konfigurasi logging
logging.basicConfig(level=logging.DEBUG)

# Konfigurasi tema
THEME = {
    'dark_mode': True,
    'primary_color': '#0a192f',  
    'secondary_color': '#172a45', 
    'accent_color': '#64ffda',   
    'text_color': '#FFFFFF',
    'muted_text_color': '#8892b0'
}

# Konfigurasi pagination
ITEMS_PER_PAGE = 6

# Konfigurasi Gambar
GALLERY_IMAGES = [
    '/static/images/gallery1.svg',
    '/static/images/gallery2.svg',
    '/static/images/gallery3.svg',
    '/static/images/placeholder.svg',
    'https://source.unsplash.com/random/800x600/?landscape',
    'https://source.unsplash.com/random/800x600/?nature',
    'https://source.unsplash.com/random/800x600/?city',
    'https://source.unsplash.com/random/800x600/?travel'
]

PROFILE_IMAGES = [
    '/static/images/profile1.svg',
    '/static/images/profile2.svg',
    '/static/images/profile3.svg',
    'https://source.unsplash.com/random/300x300/?portrait,woman',
    'https://source.unsplash.com/random/300x300/?portrait,man'
]

# Fungsi untuk mengacak gambar
def get_random_image(image_list):
    return random.choice(image_list)

# Konfigurasi Gallery data
GALLERY_DATA = [
    {
        'id': 1,
        'title': 'Mountain Landscape',
        'description': 'Our annual team building retreat at mountain resort',
        'date': '2023-06-15'
    },
    {
        'id': 2,
        'title': 'City Nightscape',
        'description': 'Celebrating the successful launch of our new project',
        'date': '2023-03-22'
    },
    {
        'id': 3,
        'title': 'Beach Sunset',
        'description': 'Our office retreat at the beach resort',
        'date': '2023-01-10'
    },
    {
        'id': 4,
        'title': 'Summer Picnic',
        'description': 'Annual summer gathering at the lake',
        'date': '2022-07-30'
    },
    {
        'id': 5,
        'title': 'Workshop Session',
        'description': 'Learning new skills during our monthly workshop',
        'date': '2022-05-12'
    },
    {
        'id': 6,
        'title': 'Conference Attendance',
        'description': 'Our team at the annual industry conference',
        'date': '2022-02-28'
    }
]

# Konfigurasi Hall of Fame data
HALL_OF_FAME_DATA = [
    {
        'id': 1,
        'title': 'Sarah Johnson',
        'description': 'Winner of National Science Competition',
        'date': '2023-04-18'
    },
    {
        'id': 2,
        'title': 'Michael Chen',
        'description': 'Outstanding Achievement in Mathematics',
        'date': '2023-02-05'
    },
    {
        'id': 3,
        'title': 'Aisha Patel',
        'description': 'First Prize in Regional Coding Challenge',
        'date': '2022-11-30'
    },
    {
        'id': 4,
        'title': 'David Rodriguez',
        'description': 'Excellence in Leadership Award',
        'date': '2022-09-15'
    },
    {
        'id': 5,
        'title': 'Emma Wilson',
        'description': 'Innovation Award for New Product Design',
        'date': '2022-06-22'
    },
    {
        'id': 6,
        'title': 'James Lee',
        'description': 'Community Service Recognition',
        'date': '2022-03-10'
    }
]

# Konfigurasi People data
PEOPLE_DATA = [
    {
        'id': 1,
        'name': 'Alex Morgan',
        'id_number': 'ID-1234',
        'birthdate': '1990-05-15',
        'position': 'Mahasiswa S1 Informatika'
    },
    {
        'id': 2,
        'name': 'Jordan Smith',
        'id_number': 'ID-2345',
        'birthdate': '1985-11-22',
        'position': 'Mahasiswa S2 Sistem Informasi'
    },
    {
        'id': 3,
        'name': 'Casey Johnson',
        'id_number': 'ID-3456',
        'birthdate': '1992-08-07',
        'position': 'Mahasiswa S1 Teknik Komputer'
    },
    {
        'id': 4,
        'name': 'Taylor Williams',
        'id_number': 'ID-4567',
        'birthdate': '1988-03-30',
        'position': 'Mahasiswa S3 Ilmu Komputer'
    },
    {
        'id': 5,
        'name': 'Jamie Davis',
        'id_number': 'ID-5678',
        'birthdate': '1995-09-12',
        'position': 'Mahasiswa S1 Informatika'
    },
    {
        'id': 6,
        'name': 'Riley Brown',
        'id_number': 'ID-6789',
        'birthdate': '1993-01-25',
        'position': 'Mahasiswa S1 Sistem Informasi'
    },
    {
        'id': 7,
        'name': 'Avery Miller',
        'id_number': 'ID-7890',
        'birthdate': '1991-07-18',
        'position': 'Mahasiswa S2 Teknik Komputer'
    },
    {
        'id': 8,
        'name': 'Cameron Wilson',
        'id_number': 'ID-8901',
        'birthdate': '1987-12-05',
        'position': 'Mahasiswa S1 Ilmu Komputer'
    },
    {
        'id': 9,
        'name': 'Morgan Lee',
        'id_number': 'ID-9012',
        'birthdate': '1994-04-20',
        'position': 'Mahasiswa S1 Informatika'
    },
    {
        'id': 10,
        'name': 'Dakota Martin',
        'id_number': 'ID-0123',
        'birthdate': '1989-10-31',
        'position': 'Mahasiswa S2 Ilmu Komputer'
    }
]

# Konfigurasi Organization Structure
ORG_STRUCTURE = {
    'leader': {
        'title': 'Chairman',
        'name': 'Nevanda Nur Syahdanu',
        'image': '/static/structure/230601110030.jpg'
    },
    'vice_leader': {
        'title': 'Vice Chairman',
        'name': 'Renata Dwi Yasarah',
        'image': '/static/structure/230601110034.jpg'
    },
    'treasurer': [
        {
            'title': 'Treasurer 1',
            'name': 'Nur Afiiqotul Ula',
            'image': '/static/structure/230601110052.jpg'
        },
        {
            'title': 'Treasurer 2',
            'name': 'Mochammad Imron Rosyadi',
            'image': '/static/structure/230601110051.jpg'
        }
    ],
    'secretary': [
        {
            'title': 'Secretary 1',
            'name': 'Sa’adah Rohmatan Amalia',
            'image': '/static/structure/230601110068.jpg'
        },
        {
            'title': 'Secretary 2',
            'name': 'Muhammad Farhan Rofiqi',
            'image': '/static/structure/230601110030.jpg'
        }
    ],
    'media_team': [
        {
            'title': 'Media Team Member',
            'name': 'Najwa Latansa Arif',
            'image': '/static/structure/230601110025.jpg'
        },
        {
            'title': 'Media Team Member',
            'name': 'Izzar Suly Nashrudin',
            'image': '/static/structure/230601110010.jpg'
        },
        {
            'title': 'Media Team Member',
            'name': 'Akmal Putra Sobur',
            'image': '/static/structure/230601110075.jpg'
        }
    ],
    'developers': [
        {
            'title': 'Developer',
            'name': 'Izzar Suly Nashrudin',
            'image': '/static/structure/230601110010.jpg'
        }
    ]
}
