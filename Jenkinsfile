pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/your/repo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t fastapi-app .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // stop old container if running
                    sh 'docker stop fastapi-container || true && docker rm fastapi-container || true'
                    
                    // run new container
                    sh 'docker run -d -p 8000:8000 --name fastapi-container fastapi-app'
                }
            }
        }
    }
}
