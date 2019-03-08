pipeline {
  environment{
        dockerRegistry = "localhost:5001"
        imageName = "${dockerRegistry}/flask-app:latest"
        deployContainerName = "flask_app"
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
          sh "curl (docker inspect -f '\{\{range .NetworkSettings.Networks\}\}\{\{.IPAddress\}\}\{\{end\}\}' jovial_euclid):5000"
        }
      }
      stage('Push'){
        steps{
          echo 'Puhsing'
          sh "docker push " + imageName
        }
      }
      stage('Clean'){
        steps{
          echo 'Cleaning'
          sh 'docker stop \$(docker images flask_app -q | awk \'!a[$0]++\') || echo \'Container not running.\''
          sh 'docker rmi -f \$(docker images flask_app -q | awk \'!a[$0]++\') || echo \'Image not found.\''
        }
      }

    }
  }

