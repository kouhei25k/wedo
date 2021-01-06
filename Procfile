web: daphne wedo.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker --settings=wedo.settings -v2