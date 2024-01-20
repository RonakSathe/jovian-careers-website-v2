from sqlalchemy import create_engine,text
import os

db_connection_string="mysql://root:root@127.0.0.1/himenincareers"
engine = create_engine(db_connection_string)



def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("Select * from jobs;"))
    columns = result.keys()
    results= result.fetchall()
    JOBS=[]
    for row in results:
       JOBS.append(dict(zip(columns,row)))
    return JOBS

def load_job_from_db(id):
   with engine.connect() as conn:
      
      result = conn.execute(text("select * from jobs where id= :id").bindparams(id=id))
      columns=result.keys()
      rows = result.all()
      JOBS =[]
      for row in rows:
        JOBS.append(dict(zip(columns,row)))
      if len(rows) == 0:
         return None
      else:
         print(JOBS)
         return JOBS