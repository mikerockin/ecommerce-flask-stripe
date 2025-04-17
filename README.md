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

Visit `http://host:5085` in your browser. The app should be up & running.

Prometheus `http://host:9090`

Grafana `http://host:3000`

Adminer `http://host:8080`

Alert manager `http://host:9093`

3. Bring the stack down with docker stack rm

       $ docker stack rm stackdemo

###### Tested on CentOS Stream 9 with Vagrant ###### 
    https://kojihub.stream.centos.org/kojifiles/packages/CentOS-Stream-Vagrant/9/20250326.0/images/CentOS-Stream-Vagrant-9-20250326.0.x86_64.vagrant-virtualbox.box

   ## Start in `Kubernetes Cluster` ##
   Using Yandex Cloud
   ##### *Yandex provides grants for test use of the platform
   ### To run this, you need:
- Locally installed kubectl 
- Kubernetes Cluster on cloud platform with authorization on the host where kubectl is installed
- The config files are located in k8s folder
  
:arrow_right: 1. Connect and Check info about cluster    
      
    $ kubectl cluster-info

    Kubernetes control plane is running at https://51.250.45.219
    CoreDNS is running at https://51.250.45.219/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

    To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
    
:arrow_right: 2. Apply manifests

    $ cd k8s
    $ kubectl apply -f databases

    deployment.apps/adminer created
    service/adminer created
    statefulset.apps/postgres created
    service/postgres created
    
    $ kubectl apply -f app

    deployment.apps/appseed-app created
    service/appseed-app created

    
    $ kubectl apply -f nginx

    configmap/nginx-config created
    deployment.apps/nginx created
    service/nginx created
    
    $ kubectl apply -f monitoring

    configmap/alertmanager-config created
    deployment.apps/alertmanager created
    service/alertmanager created
    deployment.apps/grafana created 
    service/grafana created
    daemonset.apps/node-exporter created
    daemonset.apps/node-exporter unchanged
    service/node-exporter created  
    deployment.apps/postgres-exporter created
    service/postgres-exporter created
    configmap/prometheus-config created
    deployment.apps/prometheus created

:arrow_right: 3. Сheck all cluster resources.

    $ kubectl get all

    NAME                                    READY   STATUS    RESTARTS   AGE
    pod/adminer-6658bd5444-64pvv            1/1     Running   0          3m16s
    pod/adminer-6658bd5444-v9982            1/1     Running   0          3m16s
    pod/alertmanager-645d749cf8-bc5wn       1/1     Running   0          56s
    pod/alertmanager-645d749cf8-zntsr       1/1     Running   0          55s
    pod/appseed-app-7f6f97679c-hfwng        1/1     Running   0          109s  
    pod/appseed-app-7f6f97679c-m6zf2        1/1     Running   0          109s
    pod/grafana-787d8f6bff-jh97d            1/1     Running   0          55s
    pod/grafana-787d8f6bff-rj52d            1/1     Running   0          55s
    pod/nginx-5d5d5c5985-8jzqv              1/1     Running   0          89s
    pod/nginx-5d5d5c5985-wqd6r              1/1     Running   0          89s
    pod/node-exporter-26w7f                 1/1     Running   0          55s
    pod/node-exporter-2lntb                 1/1     Running   0          55s
    pod/node-exporter-7s7js                 1/1     Running   0          55s
    pod/node-exporter-kntsc                 1/1     Running   0          55s
    pod/node-exporter-m8xfd                 1/1     Running   0          55s
    pod/postgres-0                          1/1     Running   0          3m15s   
    pod/postgres-exporter-f8dcbf588-6jwnw   1/1     Running   0          54s
    pod/postgres-exporter-f8dcbf588-tpsm4   1/1     Running   0          54s
    pod/postgres-exporter-f8dcbf588-x992l   1/1     Running   0          54s
    pod/prometheus-54fbc4f9bf-lsttz         1/1     Running   0          54s

    NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP       PORT(S)          AGE
    service/adminer             LoadBalancer   10.96.198.60    <pending>         8080/TCP         3m16s
    service/alertmanager        ClusterIP      10.96.203.89    <none>            9093/TCP         55s
    service/appseed-app         ClusterIP      10.96.222.225   <none>            5005/TCP         109s
    service/grafana             LoadBalancer   10.96.179.195   158.160.171.47    3000:31391/TCP   55s
    service/kubernetes          ClusterIP      10.96.128.1     <none>            443/TCP          30m
    service/nginx               LoadBalancer   10.96.201.215   158.160.182.200   5085:31313/TCP   88s
    service/node-exporter       ClusterIP      10.96.223.21    <none>            9100/TCP         54s
    service/postgres            ClusterIP      10.96.207.13    <none>            5432/TCP         3m15s
    service/postgres-exporter   ClusterIP      10.96.132.86    <none>            9187/TCP         54s
    service/prometheus          LoadBalancer   10.96.187.12    <pending>         9090:31909/TCP   54s

    NAME                           DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
    daemonset.apps/node-exporter   5         5         5       5            5           <none>          55s

    NAME                                READY   UP-TO-DATE   AVAILABLE   AGE
    deployment.apps/adminer             2/2     2            2           3m16s
    deployment.apps/alertmanager        2/2     2            2           56s
    deployment.apps/appseed-app         2/2     2            2           110s
    deployment.apps/grafana             2/2     2            2           55s
    deployment.apps/nginx               2/2     2            2           89s
    deployment.apps/postgres-exporter   3/3     3            3           54s
    deployment.apps/prometheus          1/1     1            1           54s

    NAME                                          DESIRED   CURRENT   READY   AGE
    replicaset.apps/adminer-6658bd5444            2         2         2       3m16s
    replicaset.apps/alertmanager-645d749cf8       2         2         2       56s
    replicaset.apps/appseed-app-7f6f97679c        2         2         2       110s
    replicaset.apps/grafana-787d8f6bff            2         2         2       55s
    replicaset.apps/nginx-5d5d5c5985              2         2         2       89s
    replicaset.apps/postgres-exporter-f8dcbf588   3         3         3       54s
    replicaset.apps/prometheus-54fbc4f9bf         1         1         1       54s

    NAME                        READY   AGE
    statefulset.apps/postgres   1/1     3m16s
    
   Available on public IP:
   
    app - `http://158.160.182.200:5085`
    Grafana `http://158.160.171.47:3000`
    
   Not available on public IP:
   
   *Quota limit (LoadBalancer) by Yandex Cloud
   
    Adminer `http://host:8080`
    Alert manager `http://host:9093`
    Prometheus `http://host:9090`
    
    
    
   

