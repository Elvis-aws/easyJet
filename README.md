# Selenium-Python
Selenium Python framework

**********************
Installing virtual env 
**********************
- pip install virtualenv
- virtualenv venv
- source venv/bin/activate
- deactivate


**********************
Install requirements.txt
**********************
- touch requirements.txt
- pip3 install -r requirements.txt
- pip3 freeze > requirements.txt


**********************
Generating allure-report locally
**********************
- install allure - https://docs.qameta.io/allure/#_installing_a_commandline
- generate report - pytest -v -s --alluredir="rootdirectory/reports""
- display report - allure serve rootdirectory/reports