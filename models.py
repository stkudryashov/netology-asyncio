import sqlalchemy as sq
from sqlalchemy.orm import declarative_base


class Contact(declarative_base()):
    contact_id = sq.Column(sq.Integer, primary_key=True)
    first_name = sq.Column(sq.String(64))
    last_name = sq.Column(sq.String(64))
    email = sq.Column(sq.String(64))
    address = sq.Column(sq.String(128))

    __tablename__ = 'contacts'
