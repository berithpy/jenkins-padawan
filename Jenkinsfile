pipeline {
  environment{
        dockerRegistry = "localhost:5001"
        imageName = "${dockerRegistry}/flask-app:latest"
        deployContainerName = "flask_app"
        deployIp = "172.17.0.1"
      }
  agent any
    stages{
      stage ('Build') {
        steps{
          echo 'Building'
          sh "docker build . -t flask_app -t ${imageName} --no-cache"
        }
      }
      stage('Deploy'){
        steps{
          echo 'Deploying'
          sh  "docker run -d -p 5000:5000 --name ${deployContainerName} ${imageName}"
        }
      }
      stage('Test'){
        steps{
          echo "Testing"
          sh "curl ${deployIp}:5000"
        }
      }
      stage('Push'){
        steps{
          echo 'Puhsing'
          sh "docker push " + imageName
        }
      }
    }
    post{
      always{
        echo 'Cleaning'
        sh 'docker stop ${deployContainerName} || echo \'Container not running.\''
        sh 'docker rm ${deployContainerName} || echo \'Container not deployed.\''
      }
    }
  }

