pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Create a virtual environment and install dependencies
               sh 'python3 -m venv venv'
                sh 'bash -c ". venv/bin/activate && pip install -r requirements.txt"'
                
            }
        }

        stage('Test') {
            steps {
                // Activate the virtual environment and run tests
               sh 'bash -c "source venv/bin/activate && pytest"'
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
}
