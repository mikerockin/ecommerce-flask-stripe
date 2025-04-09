# ` Flask Mini eCommerce Education App`

- [Flask mini eCommerce](https://github.com/app-generator/ecommerce-flask-stripe) sources (this repo)

  *A database (PostgreSQL) has been added that records the amount of visits to the product presentation page.
  
  *Adminer has been added for database administration.
  
  *Added node and database connection monitoring (Prometheus + Grafana)
  
  *Added alerting (alert manager for Prometheus) + Telegram
  

## Start in `Docker`
  :arrow_right: **Step 1** - Download the code from the GH repository (using `GIT`) 
```bash
$ git clone https://github.com/app-generator/ecommerce-flask-stripe.git
$ cd ecommerce-flask-stripe
```

 :arrow_right: **Step 2** - Add STRIPE secrets in `Dockerfile`
```Dokerfile
# Stripe Secrets 
ENV STRIPE_SECRET_KEY      <YOUR_STRIPE_SECRET_KEY>
ENV STRIPE_PUBLISHABLE_KEY <YOUR_STRIPE_PUBLISHABLE_KEY>
```

:arrow_right: **Step 3** - Start the APP in `Docker`
```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

Prometheus `http://localhost:9090`

Grafana `http://localhost:3000`

Adminer `http://localhost:8080`

Alert manager `http://localhost:9093`
## Start in `Docker Swarm`

<br />

