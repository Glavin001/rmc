import os
IS_PROD = os.path.isdir('/home/rmc')

# NOTE: This relies on the fact that this file is one level above the repo root
RMC_ROOT = os.path.join(os.path.dirname(__file__), "..")

if IS_PROD:
    SHARED_DATA_DIR = '/home/rmc/data'
else:
    SHARED_DATA_DIR = os.path.join(RMC_ROOT, 'shared_data')

# define cross file constants here

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB_RMC = 'rmc'

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

if IS_PROD:
    RMC_HOST = "http://uwflow.com"
else:
    RMC_HOST = "http://localhost:5000"

TERMS_OFFERED_DATA_DIR = 'terms_offered'
UCALENDAR_COURSES_DATA_DIR = 'ucalendar_courses'
OPENDATA_COURSES_DATA_DIR = 'opendata_courses'
UWDATA_COURSES_DATA_DIR = 'uwdata_courses'
REVIEWS_DATA_DIR = 'reviews'
DEPARTMENTS_DATA_DIR = 'departments'
EXAMS_DATA_DIR = 'exam_schedules'
SECTIONS_DATA_DIR = 'opendata_sections'

RATINGS_CONFIDENCE = 0.95

# Demo accounts
# TODO(Sandy): Have multiple demo accounts?
DEMO_ACCOUNT_FBID = '100004384843130'

# A long token normally lasts for 60 days
FB_FORCE_TOKEN_EXPIRATION_DAYS = 57

SIFT_API_KEY = 'b1eb450bb0c5a2f1'
