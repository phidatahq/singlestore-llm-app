import sqlalchemy
from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://admin:passkey@svc-3nb226d8-ee13-47f0-8ca4-2dc820773442-dml.aws-oregon-2.svc.singlestore.com:3306/dbTest')
conn = engine.connect()
conn.execute("DELETE FROM stock WHERE code = 'rtky'")
result = conn.execute("SELECT * FROM stock")
for row in result:
	print(row)
conn.close()
