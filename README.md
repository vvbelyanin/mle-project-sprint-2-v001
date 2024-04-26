# mle-template-case-sprint2

Добро пожаловать в репозиторий-шаблон Практикума для проекта 2 спринта. Ваша цель — улучшить ключевые метрики модели для предсказания стоимости квартир Яндекс Недвижимости.

Полное описание проекта хранится в уроке «Проект. Улучшение baseline-модели» на учебной платформе.

Здесь укажите имя вашего бакета:

git clone https://github.com/vvbelyanin/mle-project-sprint-2-v001
sudo apt-get update
sudo apt-get install python3.10-venv
python3.10 -m venv .venv_sprint_2
export $(cat .env | xargs)
source .venv_sprint_2/bin/activate          # no alias created
pip install -r requirements.txt
cd mlflow_server
sh run_server.sh
pip install -U mlflow