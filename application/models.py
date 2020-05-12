from application import db

<class Posts(db.model):
    id = db.Column(db.integer, primary_key=True)
    first_name = db.Comimn(db.String(30), nullable=False)
    last_name = db.Colimn(db.String(30), nullable=False)

    def __repr__(self):
        return ''.join([
            'user: ', self.first_name, ' ' , self.last_name
            ])
