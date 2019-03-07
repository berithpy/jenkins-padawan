node {
  checkout scm
  // Create a short commit-id to tag the images.
  sh "git rev-parse --short HEAD > commit-id"
  commitId = readFile('commit-id').trim()
  // Docer registry to tag the image and then push it.
  def dockerRegistry = "localhost:5001"
  def imageName = "${dockerRegistry}/flask-app:${commitId}"
  stage ('Build') {
    echo 'Building'
    sh "docker build . -t flask_app -t ${imageName} --no-cache"
  }

  stage('Deploy'){
    echo 'Deploying'
    sh  "docker run -d -p 5000:5000 ${imageName}"
  }

  stage('Test'){
    echo "Testing"
  }

  stage('Push'){
    echo 'Puhsing'
    sh "docker push " + imageName
  }

  stage('Clean'){
    echo 'Cleaning'
    sh 'docker stop \$(docker images flask_app -q | awk \'!a[$0]++\') || echo \'Container not running.\''
    sh 'docker rmi -f \$(docker images flask_app -q | awk \'!a[$0]++\') || echo \'Image not found.\''
  }
}
