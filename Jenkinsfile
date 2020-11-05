pipeline {
    agent any
    triggers {
        pollSCM ''
    }
    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main',
                credentialsId: '48ae0803-4de4-44bf-8aa9-23a301fbb1b8',
                url: 'https://github.com/adiha2033/experts-games.git'
            } 
        }
        stage('Docker Build Image') {
            steps {
                bat 'docker-compose build'
            }
        }
        stage('Docker Run Container') {
            steps {
                bat 'docker-compose up -d'
            }
        }
        stage('Run Test: e2e.py') {
            steps {
                dir('./tests') {
                    python3 e2e.py
                }
            }
        }
    }
    post {
      always {
         sh "docker-compose down || true"
      }
    }
}