pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Create a virtual environment and install dependencies
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                // Activate the virtual environment and run tests
                sh '''
                    source venv/bin/activate
                    pytest
                '''
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying application...'
                // AWS-specific deploy commands (e.g., using AWS CLI or scripts)
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
