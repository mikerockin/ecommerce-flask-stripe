pipeline {
    agent any
    environment {
        DOCKER_HUB_REPO = "mikerockin1988/ecommerce-flask-stripe" 
        DOCKER_CREDENTIALS_ID = "dockerhub-credentials"
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/mikerockin/ecommerce-flask-stripe.git', branch: 'master'
            }
        }
        stage('Build and Push Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build("${DOCKER_HUB_REPO}:beta")
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS_ID) {
                        dockerImage.push("beta")
                    }
                }
            }
        }
    }
}
