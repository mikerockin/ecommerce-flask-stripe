# ` Flask Mini eCommerce Education App`

- [Flask mini eCommerce](https://github.com/app-generator/ecommerce-flask-stripe) sources (this repo)

  *A database (PostgreSQL) has been added that records the amount of visits to the product presentation page.
  
  *Adminer has been added for database administration.
  
  *Added node and database connection monitoring (Prometheus + Grafana)
  
  *Added alerting (alert manager for Prometheus) + Telegram

  *Added Vagrantfile for quick deployment in docker swarm
  

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

## Start in `Docker Swarm` ##
### *To run this, you need:
- Installed Vagrant + VirtualBox + Centos (image box for vbox)
- or Three Linux hosts which can communicate over a network, with Docker installed

:arrow_right: Create a swarm

1. Open a terminal and ssh into the machine where you want to run your manager node. This tutorial uses a machine named manager.

2. Run the following command to create a new swarm:
   
       $ docker swarm init --advertise-addr <MANAGER-IP>
                        
:arrow_right: Add nodes to the swarm

1. Open a terminal and ssh into the machine where you want to run a worker node.

2. Run the command produced by the docker swarm init output from the Create a swarm, a worker node joined to the existing swarm:
   
       $ docker swarm join \
       --token  SWMTKN-1-49nj1cmql0jkz5s954yi3oex3nedyz0fb0xx14ie39trti4wxv-8vxv8rssmk743ojnwacrr2e7c \
       192.168.99.100:2377

       This node joined a swarm as a worker.

:arrow_right: Checking Nodes: 

Make sure all three nodes in the cluster:

    $ docker node ls
    ID                            HOSTNAME   STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
    paodf4bfton66h0p4vdvbcbjv *   manager    Ready     Active         Leader           28.0.4
    bp7zp5b0c8wc1ac9us53hs3xz     worker1    Ready     Active                          28.0.4
    cu5ihpaesleiln1obuyxvqp9u     worker2    Ready     Active                          28.0.4


Assigning a label to db: Assign the label db=true to the manager (replace <manager-node-id> with the node ID from docker node ls):

    $ docker node update --label-add db=true <manager-node-id>
:arrow_right: Deployment:

    $ cd ecommerce-flask-stripe/
    
1. Create the stack with docker stack deploy:   

       $ docker stack deploy -c docker-compose.yml stackdemo
   
2. Check that it's running with docker stack services stackdemo:
    
       $  docker stack services stackdemo
       ID             NAME                          MODE         REPLICAS   IMAGE                                                   PORTS
       ay7k442h4kub   stackdemo_adminer             replicated   1/1        adminer:latest                                          *:8080->8080/tcp
       w3x0re9cqqqb   stackdemo_alertmanager        replicated   1/1        prom/alertmanager:latest                                *:9093->9093/tcp
       mqkksiirbexm   stackdemo_appseed-app         replicated   2/2        mikerockin1988/ecommerce-flask-stripe-appseed-app:1.0   
       ngv49xy5js5n   stackdemo_appseed_app         replicated   2/2        mikerockin1988/ecommerce-flask-stripe-appseed-app:1.0   
       9asc8tsaidpc   stackdemo_db                  replicated   1/1        postgres:17.4-alpine                                    
       fav9q6tmj7wm   stackdemo_grafana             replicated   1/1        grafana/grafana-oss:latest                              *:3000->3000/tcp
       d9vlh2zvc05h   stackdemo_nginx               replicated   1/1        nginx:latest                                            *:5085->5085/tcp
       ayb81nz5stvr   stackdemo_node_exporter       global       3/3        prom/node-exporter:latest                               *:9100->9100/tcp
       6t8suvsk8wc   stackdemo_postgres_exporter    replicated   1/1        prometheuscommunity/postgres-exporter:latest            *:9187->9187/tcp
       uuw3ddc77hss   stackdemo_prometheus          replicated   1/1        prom/prometheus:latest                                  *:9090->9090/tcp


3. Bring the stack down with docker stack rm

       $ docker stack rm stackdemo

###### Tested on CentOS Stream 9 with Vagrant ###### 
    https://kojihub.stream.centos.org/kojifiles/packages/CentOS-Stream-Vagrant/9/20250326.0/images/CentOS-Stream-Vagrant-9-20250326.0.x86_64.vagrant-virtualbox.box
