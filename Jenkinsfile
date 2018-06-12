node {
  checkout scm
  sh "git rev-parse --short HEAD > .git/commit-id"
  commitId = readFile('.git/commit-id').trim()
  def registry = "localhost:5001"
  def imageName = "${registry}/flask-app:${commitId}"
  stage ('Build') {
    echo 'Building'
    sh "docker build . -t flask_app -t ${imageName} --no-cache"
  }

  stage('Deploy'){
    echo 'Deploying'
    sh  "docker run -d -p 5000:5000 ${imageName}"
  }

  stage('Test'){
    echo 'Testing'
    sh  "python3 app/test_microservice.py"
  }

  stage('Push'){
    echo 'Puhsing'
    sh "docker push " + imageName
  }

  stage('Clean'){
    echo 'Cleaning'
    sh 'docker rmi -f \$(docker images flask_app -q | awk \'!a[$0]++\') || echo \'Image not found.\''
  }
}
