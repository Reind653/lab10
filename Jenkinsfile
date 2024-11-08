pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    // Create a virtual environment if it doesn't exist and install dependencies
                    if (!fileExists("${env.WORKSPACE}\\${VIRTUAL_ENV}")) {
                        bat "C:\\Users\\ENVY\\AppData\\Local\\Programs\\Python\\Python312\\python.exe ${VIRTUAL_ENV}"
                    }
                    // Activate the virtual environment and install requirements
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
