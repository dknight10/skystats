export OUTPUT_TYPE=file
export OUTPUT_LOCATION=/Users/chaknight/Projects/skytrak-stats/upload/test.csv

FLASK_APP=upload/api.py FLASK_ENV=development flask run
