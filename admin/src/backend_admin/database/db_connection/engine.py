import os
from sqlalchemy import create_engine, URL
from dotenv import load_dotenv
load_dotenv()

url = URL.create(
    drivername="postgresql+psycopg",
    username=os.environ["DB_USER"],
    password=os.environ["POSTGRES_PASSWORD"],
    host=os.environ["DB_HOST"],
    port=int(os.environ["DB_PORT"]),
    database=os.environ["DB_NAME"],
)

engine = create_engine(url, echo=True)