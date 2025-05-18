pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "yourdockerhubusername/flask-ci-app"
        DOCKER_CREDENTIALS_ID = "dockerhub-creds-id"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/brownc61/ci-cd-flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: "$DOCKER_CREDENTIALS_ID", url: '']) {
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }
    }
}
