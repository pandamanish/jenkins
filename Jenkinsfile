pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying application...'
                // AWS-specific deploy commands (described below)
            }
        }
    }

    post {
        success {
            mail to: 'pandamanish75@gmail.com',
                subject: "Jenkins Build Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Good news! Jenkins completed the build successfully for ${env.JOB_NAME} #${env.BUILD_NUMBER}."
        }
        failure {
            mail to: 'pandamanish75@gmail.com',
                subject: "Jenkins Build Failure: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Oops! Jenkins failed the build for ${env.JOB_NAME} #${env.BUILD_NUMBER}. Please check the logs for more details."
        }
    }
}
