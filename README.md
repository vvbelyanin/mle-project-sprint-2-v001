# RAEDME.md

Installing:    
    
git clone https://github.com/vvbelyanin/mle-project-sprint-2-v001    
sudo apt-get update    
sudo apt-get install python3.10-venv    
python3.10 -m venv .venv_sprint_2    
export $(cat .env | xargs)    
source .venv_sprint_2/bin/activate    
pip install -r requirements.txt    
cd mlflow_server    
sh run_server.sh    
pip install -U mlflow    
    
Info:    
    
Bucket name: `s3-student-mle-20240325-4062b25c06`    
Run name:  `Спринт 3/9: 2 спринт → Тема 5/5: Проект`    
Run id: `97e36a4c008244f594b8213adc656d15`