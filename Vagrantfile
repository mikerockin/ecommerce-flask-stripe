# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|

  config.vm.box = "centos-docker"
  config.vm.box_url = "file:///home/mikhaik/Os_images/CentOS-Stream-Vagrant-9-20250310.0.x86_64.vagrant-virtualbox.box"


  config.vm.define "doc" do |doc|
    doc.vm.hostname = "manager"
    doc.vm.network "private_network", ip: "192.168.56.10"

    # Ограничение ресурсов
    doc.vm.provider "virtualbox" do |vb|
      vb.memory = 1024
      vb.cpus = 1
    end

    doc.vm.provision "shell", inline: <<-SHELL
      sudo dnf -y install dnf-plugins-core
      sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
      sudo dnf -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
      sudo docker run hello-world
      sudo systemctl enable --now docker
      sudo groupadd docker
      sudo usermod -aG docker vagrant
      newgrp docker
      sudo systemctl enable docker.service
      sudo systemctl enable containerd.service
      sudo  dnf  -y  install  git
      sudo su vagrant
      git clone https://github.com/mikerockin/ecommerce-flask-stripe.git
      docker pull postgres:17.4-alpine 
      docker pull prom/prometheus 
      docker pull prom/node-exporter  
      docker pull prom/alertmanager 
      docker swarm init --advertise-addr 192.168.56.10
      docker info
      docker node ls
    SHELL
  end


  config.vm.define "work1" do |work1|
    work1.vm.hostname = "worker1"
    work1.vm.network "private_network", ip: "192.168.56.11"

    # Ограничение ресурсов
    work1.vm.provider "virtualbox" do |vb|
      vb.memory = 1024
      vb.cpus = 1
    end

    work1.vm.provision "shell", inline: <<-SHELL
      sudo dnf -y install dnf-plugins-core
      sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
      sudo dnf -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
      sudo docker run hello-world
      sudo systemctl enable --now docker
      sudo groupadd docker
      sudo usermod -aG docker vagrant
      newgrp docker
      sudo systemctl enable docker.service
      sudo systemctl enable containerd.service
      sudo  dnf  -y  install  git
      docker pull adminer
      docker pull mikerockin1988/ecommerce-flask-stripe-appseed-app:1.0
      docker pull nginx 
      docker pull prom/node-exporter
      docker pull prometheuscommunity/postgres-exporter
      docker pull grafana/grafana-oss 
    SHELL
  end


  config.vm.define "work2" do |work2|
    work2.vm.hostname = "worker2"
    work2.vm.network "private_network", ip: "192.168.56.12"

    # Ограничение ресурсов
    work2.vm.provider "virtualbox" do |vb|
      vb.memory = 1024
      vb.cpus = 1
    end

    work2.vm.provision "shell", inline: <<-SHELL
      sudo dnf -y install dnf-plugins-core
      sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
      sudo dnf -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
      sudo docker run hello-world
      sudo systemctl enable --now docker
      sudo groupadd docker
      sudo usermod -aG docker vagrant
      newgrp docker
      sudo systemctl enable docker.service
      sudo systemctl enable containerd.service
      sudo  dnf  -y  install  git
      docker pull adminer
      docker pull mikerockin1988/ecommerce-flask-stripe-appseed-app:1.0
      docker pull nginx 
      docker pull prom/node-exporter
      docker pull prometheuscommunity/postgres-exporter
      docker pull grafana/grafana-oss 
    SHELL
  end
end

