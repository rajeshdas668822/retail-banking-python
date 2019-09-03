import sqlalchemy as sa

from sqlalchemy.orm import scoped_session, sessionmaker
from orm.orm_data_access.models import Base


class OrmHelper:
    engine = None
    conn_string = None
    session = None

    def db_init(self, conn_string):
        self.conn_string = conn_string
        self.engine = sa.create_engine(self.conn_string, echo=True)
        self.session = scoped_session(sessionmaker(bind=self.engine))
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.session
