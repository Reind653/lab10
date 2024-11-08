pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
        PYTHONPATH = "${WORKSPACE}"  // Set root directory for imports
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    bat "C:\\Users\\ENVY\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m venv ${VIRTUAL_ENV}"
                    bat "${VIRTUAL_ENV}\\Scripts\\activate && pip install -r requirements.txt"
                }
            }
        }

        stage('Lint') {
            steps {
                script {
                    bat "${VIRTUAL_ENV}\\Scripts\\activate && flake8 app.py"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    bat "${VIRTUAL_ENV}\\Scripts\\activate && pytest"
                }
            }
        }

        stage('Coverage') {
            steps {
                script {
                    bat "${VIRTUAL_ENV}\\Scripts\\activate && coverage run -m pytest"
                    bat "${VIRTUAL_ENV}\\Scripts\\activate && coverage report"
                }
            }
        }

        stage('Security Scan') {
            steps {
                script {
                    bat "${VIRTUAL_ENV}\\Scripts\\activate && bandit -r app.py"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo "Deploying application..."
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
