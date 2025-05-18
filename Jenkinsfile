pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask-ci-app"
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

        stage('Done') {
            steps {
                echo "Pipeline complete. Docker image built locally as $DOCKER_IMAGE"
            }
        }
    }
}
