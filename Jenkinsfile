node {
    def backend
    def db
    def redditapi
    def webui
    def buildname = 'b' + env.BUILD_NUMBER

    stage('Get Code') {
        checkout scm
    }

    stage('Build Backend') {
        backend = docker.build("kristianwindsor/redditeye-backend", "./backend/")
    }

    stage('Build DB') {
        db = docker.build("kristianwindsor/redditeye-db", "./db/")
    }

    stage('Build RedditAPI') {
        redditapi = docker.build("kristianwindsor/redditeye-redditapi", "./redditapi/")
    }

    stage('Build WebUI') {
        webui = docker.build("kristianwindsor/redditeye-webui", "./webui/")
    }

    stage('Push Images') {
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            backend.push(buildname)
            backend.push("latest")
            db.push(buildname)
            db.push("latest")
            redditapi.push(buildname)
            redditapi.push("latest")
            webui.push(buildname)
            webui.push("latest")
        }
    }
    stage('Deploy') {
        sh """
            sed -i "s/kristianwindsor\\/redditeye-backend.*/kristianwindsor\\/redditeye-backend:$buildname/" deployment.yaml
            sed -i "s/kristianwindsor\\/redditeye-db.*/kristianwindsor\\/redditeye-db:$buildname/" deployment.yaml
            sed -i "s/kristianwindsor\\/redditeye-redditapi.*/kristianwindsor\\/redditeye-redditapi:$buildname/" deployment.yaml
            sed -i "s/kristianwindsor\\/redditeye-webui.*/kristianwindsor\\/redditeye-webui:$buildname/" deployment.yaml
            cat deployment.yaml
            kubectl apply -f deployment.yaml
        """
    }
}