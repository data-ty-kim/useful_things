###################################
## TO MAKE DATAFRAME FROM ORACLE ##
###################################

# Module 불러오기
import pandas as pd
import oracledb
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
import sys
import time


# 시간 측정 시작하기
start = time.time()
print()
print('Searching into OracleDB')

# OracleDB Version 설정하고 client 실행하기
oracledb.version = "8.3.0"
sys.modules["cx_Oracle"] = oracledb
oracledb.init_oracle_client()

# Oracle에서 데이터 가져오기
try:
    engine = (
        sqlalchemy.create_engine(
        "oracle://ID:PASSWORD@0.0.0.0:0000/?service_name=SERVICE_NAME",
        arraysize = 5000
        )
    )
    oracle_sql = """ QUERY """;
    df = pd.read_sql(oracle_sql, engine)

except SQLAlchemyError as e:
    print(e)

# 시간 측정 종료하기
end = time.time()
print(f"Time elapsed {end - start:.5f} sec", '\n')
print()

# 불러온 dataframe의 기본정보 출력하기
print(df.info())
print(df.describe())
