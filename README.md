# README.md

### Проект. Улучшение baseline-модели

**Оcновная задача**    
Усовершенствование базовой модели методами конструирования и отбора признаков, поиск оптимальных гиперпараметров модели в среде MLFlow.
Необходимо улучшить основную метрику проекта, документируя все эксперименты и объекты в MLflow. 

Подробный план проекта приведен в файле Jupyter Notebook [model_improvement](https://github.com/vvbelyanin/mle-project-sprint-2-v001/blob/main/model_improvement)/[mle-project-sprint-2-v002.ipynb](https://github.com/vvbelyanin/mle-project-sprint-2-v001/blob/main/model_improvement/mle-project-sprint-2-v002.ipynb)

**План проекта**    
- Этап 1. Разворачивание MLflow Tracking Server и MLflow Model Registry. Регистрация существующей модели    
        - Код для запуска MLflow-сервисов    
        - код для регистрации модели    
        - залогированные параметры, метрики, окружение и артефакты, сохранённые в репозитории GitHub    
        - Сохранённая в MLflow Model Registry базовая модель    
        - Инструкция по поднятию MLflow-сервисов и регистрации модели в MLflow Tracking Server
- Этап 2. Проведение исследовательского анализа данных и логирование Jupyter Notebook с EDA в MLflow
    - Этот и дальнейшие этапы приведены в Jupyter Notebook []()
- Этап 3. Генерация признаков и обучение модели
- Этап 4. Отбор признаков и обучение новой версии модели
- Этап 5. Подбор гиперпараметров и обучение новой версии модели


**Installing:**    
    
```
# клонирование репозитория
git clone https://github.com/vvbelyanin/mle-project-sprint-2-v001    

# обновление установленных пакетов
sudo apt-get update    

# установка пакета виртуального окружения Python
sudo apt-get install python3.10-venv    

# создание виртуальной среды
python3.10 -m venv .venv_sprint_2    

# загрузка переменных окружения из файла .env
export $(cat .env | xargs)    

# активирование окружения 
source .venv_sprint_2/bin/activate    

# фиксация конкретных версий пакетов
pip install -r requirements.txt    

# запуск сервера MLFlow
sh run_server.sh
``` 
    
Info:    
    
Bucket name: `s3-student-mle-20240325-4062b25c06`    
Run name:  `Спринт 3/9: 2 спринт → Тема 5/5: Проект`    
Run id: `97e36a4c008244f594b8213adc656d15`