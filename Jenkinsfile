pipeline {
    agent any
    stages {
        stage('Checkout GitOps repo') {
            steps {
                checkout scm
            }
        }
        stage('Build image producer') {
            steps {
                dir('./producer-run/') {
                    script {
                        docker.build('producer:latest')
                        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                            docker.push("${env.BUILD_NUMBER}")
                        }
                    }
                }
            }
        }
        stage('Build image producer service') {
            steps {
                dir('./producer_service-run/') {
                    script {
                        docker.build('producer-service:latest')
                        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                            docker.push("${env.BUILD_NUMBER}")
                        }
                    }
                }
            }
        }
    }
}