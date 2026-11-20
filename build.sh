
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Optional first-deploy helpers.
if [ "$SEED_DEMO" = "1" ]; then
  python manage.py seed_demo
fi

if [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
  python manage.py createsuperuser --noinput || true
fi
