import os
import sqlalchemy as sq

from sqlalchemy.orm import sessionmaker


basedir = os.path.abspath(os.path.dirname(__file__))
SQLITE_URI = 'sqlite:///' + os.path.join(basedir, 'contacts.db')

engine = sq.create_engine(SQLITE_URI)
session = sessionmaker(bind=engine)()
