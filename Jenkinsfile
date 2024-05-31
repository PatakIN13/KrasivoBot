pipeline {
    agent {
        label 'Build'
    }
    environment {
        version = '0.1.0'
    }
    stages {
        stage('Build Docker Image version') {
            steps {
                script {
                    dockerImage = docker.build("${REGISTRY}/${image}:${version}")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry("http://${REGISTRY}", "${registryCredential}") {
                        dockerImage.push()
                        dockerImage.push('latest')
                    }
                }
            }
        }
        stage('Cleanup') {
            steps {
                script {
                    sh "docker rmi ${REGISTRY}/${image}:${version}"
                    sh "docker rmi ${REGISTRY}/${image}:latest"
                    sh "docker system prune -a -f"
                }
            }
        }
    }
}
