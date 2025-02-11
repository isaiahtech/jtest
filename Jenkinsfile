pipeline {
    agent any

    stages {
        stage('Build and Push Docker Image') {
            steps {
                script {
                    def imageName = "your-dockerhub-username/my-flask-app" // Replace with your Docker Hub username and image name
                    sh "docker build -t ${imageName}:latest."
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                       sh "docker login -u ${USERNAME} -p ${PASSWORD} "
                       sh "docker push ${imageName}:latest"
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}
