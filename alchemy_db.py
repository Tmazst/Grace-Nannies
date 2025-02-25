
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine("mysql+mysqlconnector://root:tmazst41@localhost/Users_db",echo=True)

    # "mysql+mysqlconnector://<username>:<password>@<host>/<dbname>",
    #                    echo=True,
    #                    USERNAME="Tmaz",
    #                    password="Tmazst*@1111Aynwher_isto3",
    #                    host='DESKTOP-M6JL9UJ:3306',
    #                    dbname='Users_db'
    #                    )
# engine = create_engine("sqlite:///users_db.db",echo=True)

Base = declarative_base()

