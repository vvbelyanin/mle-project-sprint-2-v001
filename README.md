README.md

### Проект. Улучшение baseline-модели

**Оcновная задача**    
Усовершенствование базовой модели методами конструирования и отбора признаков, поиск оптимальных гиперпараметров модели в среде MLFlow.
Необходимо улучшить основную метрику проекта, документируя все эксперименты и объекты в MLflow. 

Подробный план проекта приведен в файле Jupyter Notebook /model_improvement/[mle-project-sprint-2-v003.ipynb](https://github.com/vvbelyanin/mle-project-sprint-2-v001/blob/main/model_improvement/mle-project-sprint-2-v003.ipynb)

**Краткий план проекта**    
- Этап 1. Разворачивание MLflow Tracking Server и MLflow Model Registry. Регистрация существующей модели    
    - Результаты:    
        - код для запуска MLflow-сервера (см. ниже) - скрипт [run_server.sh](https://github.com/vvbelyanin/mle-project-sprint-2-v001/blob/main/run_server.sh)
        - код для регистрации модели - скрипт /mlflow_server/[run_experiment.py](https://github.com/vvbelyanin/mle-project-sprint-2-v001/blob/main/mlflow_server/run_experiment.py)
        - залогированные данные, артефакты и модель: MLflow    
        - инструкция по поднятию MLflow-сервисов и регистрации модели в MLflow Tracking Server - см. ниже
- Этап 2. Проведение исследовательского анализа данных и логирование Jupyter Notebook с EDA в MLflow
    - Этот и дальнейшие этапы приведены в Jupyter Notebook []()
- Этап 3. Генерация признаков и обучение модели
- Этап 4. Отбор признаков и обучение новой версии модели
- Этап 5. Подбор гиперпараметров и обучение новой версии модели


**Инструкция по поднятию MLflow-сервисов и регистрации модели в MLflow Tracking Server:**    

В командной строке:    
```
# клонирование репозитория
git clone https://github.com/vvbelyanin/mle-project-sprint-2-v001    

# обновление установленных пакетов
sudo apt-get update    

# установка пакета виртуального окружения Python
sudo apt-get install python3.10-venv    

# создание виртуальной среды
python3.10 -m venv .venv_sprint_2    

# активирование окружения 
source .venv_sprint_2/bin/activate    

# фиксация конкретных версий пакетов
pip install -r requirements.txt    

# в текущей папке должен быть файл .env со следующими кредами
DB_DESTINATION_HOST=<...>
DB_DESTINATION_PORT=<...>
DB_DESTINATION_NAME=<...>
DB_DESTINATION_USER=<...>
DB_DESTINATION_PASSWORD=<...>
S3_BUCKET_NAME=<...>
AWS_ACCESS_KEY_ID=<...>
AWS_SECRET_ACCESS_KEY=<...>
MLFLOW_S3_ENDPOINT_URL=<...>
TRACKING_SERVER_CONN=http://127.0.0.1:5000

# загрузка переменных окружения из файла .env
export $(cat .env | xargs)    

# запуск сервера MLFlow
sh run_server.sh

# запуск кода загрузки данных и логирования в MLFlow
cd mlflow_server
python3 run_experiment.py
``` 
    
Параметры:    
    
S3 Bucket name: `s3-student-mle-20240325-4062b25c06`    
MLFlow experiment name:  `Спринт 3/9: 2 спринт → Тема 5/5: Проект`    
MLFlow run name: `ETL`    
TRACKING_SERVER_CONN=http://127.0.0.1:5000
