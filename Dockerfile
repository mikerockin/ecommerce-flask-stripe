FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Used by Stripe for callback URL
# for successful payment and cancelled
ENV SERVER_ADDRESS http://localhost:5085/

# Stripe Secrets
ENV STRIPE_SECRET_KEY=nib3iutb45t
ENV STRIPE_PUBLISHABLE_KEY=biubiybui5c

COPY requirements.txt .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY env.sample .env

COPY . .

# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
