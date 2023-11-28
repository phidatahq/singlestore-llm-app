import sqlalchemy
from sqlalchemy import create_engine, text

ss_db_url = "mysql+pymysql://admin:pass@svc-7fe9dml.aws-virginia-6.svc.singlestore.com:3306"

engine = create_engine(ss_db_url)
conn = engine.connect()
result = conn.execute(text("select now();"))
for row in result:
	print(row)
conn.close()
