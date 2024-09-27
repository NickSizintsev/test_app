from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
import sqlite3
# import yaml
from app.models import UserBase, UserPredict, UserPredictError
from app.exception_handlers import custom_exception_handler
from app.ml_model import predict
from app.constants import ROOT_DIR, DB_NAME, TABLE_NAME
from app.db_created_script import create_database
#
# with open("app/config.yml", "r") as file:
#     config = yaml.safe_load(file)
#
create_database()

app = FastAPI()

app.add_exception_handler(RequestValidationError, custom_exception_handler)

# TODO: как бы назвал эндпоинт?
# Вообще изначально думал идти через Path-параметры и "/get_predict/{user_id}",
# чтобы сразу можно было по id в пути навигироваться,
# но потом пошел через пайдемик и там немного криво получается, что-то типа "/get_predict/{user_id.user_id}"
@app.post("/get_predict")
# TODO: обработка RequestBody
async def root(user_id: UserBase) -> UserPredict | UserPredictError:
    conn = sqlite3.connect(ROOT_DIR + "/" + DB_NAME)
    cursor = conn.cursor()
    try:
        features_list = cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE user_id = {user_id.user_id}")
        features_list = list(*features_list.fetchall())[1:]
        predict_result = list(predict(features_list))
        conn.close()

        # TODO: Привести к необходимому формату и структуре JSON
        return {"status": "success", "data": predict_result}
    except:
        return {"status": "error", "message": "ID not in table"}