# mlflow_server/run_exp.py
#
# загрузка модели, данных, артефактов и их логирование в MLFlow
#

# импорт библиотек
import mlflow
import yaml
import os
import joblib
import json
import pandas as pd
import requests
import warnings
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split

# вспомогательные функции

def get_engine():
    load_dotenv()
    return create_engine(f"postgresql://{os.getenv('DB_DESTINATION_USER')}:"
                        f"{os.getenv('DB_DESTINATION_PASSWORD')}@"
                        f"{os.getenv('DB_DESTINATION_HOST')}:"
                        f"{os.getenv('DB_DESTINATION_PORT')}/"
                        f"{os.getenv('DB_DESTINATION_NAME')}"
                        )

def load_df(table_name):
    return pd.read_sql(sql=f'SELECT * FROM {table_name}', con=get_engine())

def load_data(path, loader):
    with open(path, 'r') as file:
        return  loader(file)

def check_mlflow_server(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("MLFlow server is running.")
            return True
        else:
            print("MLFlow server returned a status:", response.status_code)
            return False
    except requests.exceptions.ConnectionError:
        print("Failed to connect to the MLFlow server.")
        return False

warnings.filterwarnings("ignore")

# задание таблицы Postgres с данными, имени модели, названия эксперимента, имени запуска
TABLE_NAME = "clean_flats"
REGISTRY_MODEL_NAME = 'model_sprint_2'
EXPERIMENT_NAME = 'Спринт 3/9: 2 спринт → Тема 5/5: Проект'
RUN_NAME = "1 этап: ETL"
RANDOM_STATE = 42
target = 'price'

os.chdir(r"/home/mle-user/mle-project/mle-mlflow/mle-project-sprint-2-v001/mlflow_server/")

# задание каталогов к параметрам, модели, метрикам
project_path = '.'
path_to_params = project_path + '/models/params.yaml'
path_to_model = project_path + '/models/fitted_model.pkl'
path_to_metrics = project_path + '/results/cv_res.json'

# загрузка параметров, модели, метрик, тестовой выборки
params = load_data(path_to_params, yaml.safe_load)
model = joblib.load(path_to_model)
metrics = load_data(path_to_metrics, json.load)
df = load_df(TABLE_NAME)
_, X_test, _, _ = train_test_split(df.drop(target, axis=1), df[target], random_state=RANDOM_STATE) 

# проверка статуса сервера MLFlow
if check_mlflow_server(os.getenv('TRACKING_SERVER_CONN')):
    mlflow.set_tracking_uri(os.getenv('TRACKING_SERVER_CONN'))

    # инициализация сигнатуры модели, артефактов для логирования
    prediction = model.predict(X_test)
    signature = mlflow.models.infer_signature(X_test, prediction)
    input_example = X_test[:10]
    pip_requirements = '../requirements.txt'

    # создание / проверка актуальности эксперимента
    experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
    if not experiment:
        experiment_id = mlflow.create_experiment(EXPERIMENT_NAME)
    else:
        experiment_id = experiment.experiment_id
    
    # логирование модели, метрик, параметров
    with mlflow.start_run(run_name=RUN_NAME, experiment_id=experiment_id) as run:
        run_id = run.info.run_id
        mlflow.sklearn.log_model(sk_model=model, 
            artifact_path='models', 
            registered_model_name=REGISTRY_MODEL_NAME, 
            signature=signature, 
            input_example = input_example, 
            await_registration_for=60, 
            pip_requirements=pip_requirements
            )
        mlflow.log_metrics(metrics)
        mlflow.log_params(params)

    # вывод параметров для подтверждения
    experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
    run = mlflow.get_run(run_id)

    print(f'Experiment "{experiment.name}" stage: {experiment.lifecycle_stage}')
    print(f'Run "{run.info.run_name}", id={run.info.run_id} status: {run.info.status}')