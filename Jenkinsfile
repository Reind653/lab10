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
                    // Run coverage analysis and generate a report
                    bat "${VIRTUAL_ENV}\\Scripts\\activate && coverage run -m pytest"
                    bat "${VIRTUAL_ENV}\\Scripts\\activate && coverage report"
                    bat "${VIRTUAL_ENV}\\Scripts\\activate && coverage html"  // Generate HTML report
                }
                // Publish HTML coverage report if HTML Publisher plugin is installed
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, 
                             reportDir: 'htmlcov', reportFiles: 'index.html', reportName: 'Coverage Report'])
            }
        }

        stage('Security Scan') {
            steps {
                script {
                    // Run Bandit to check for security vulnerabilities in app.py
                    bat "${VIRTUAL_ENV}\\Scripts\\activate && bandit -r app.py"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo "Deploying application..."
                    // Add your actual deployment commands here
                    // Example: bat "your_deployment_script.bat" or any other deployment step
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
