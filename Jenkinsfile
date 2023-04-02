pipeline {
  agent {
    docker {
      image 'docker:20'
      args '--privileged --group-add=1000'
    }
  }
  environment {
    DOCKER_IMAGE_NAME = "calculator"
  }
  stages {
    stage('Build') {
      steps {
        script {
          docker.build DOCKER_IMAGE_NAME
        }
      }
    }
    stage('Test') {
      steps {
        script {
          docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            docker.image(DOCKER_IMAGE_NAME).push()
          }
        }
      }
    }
    stage('Deploy') {
      steps {
        script {
          sh "docker run -d --rm --name calculator -p 5000:5000 ${DOCKER_IMAGE_NAME}:latest"
        }
      }
    }
  }
}
