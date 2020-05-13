from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    
    first_name = StringField("First Name",
        validatots=[
            DataRequired(),
            Length(min=2, max=30)
            ]
    )

    last_name = StringField("Last Name",
        validatots=[
            DataRequired(),
            Length(min=3, max=30)
            ]
    )

    title = StringField("Title",
        validatots=[
            DataRequired(),
            Length(min=3, max=30)
            ]
    )

    Content = StringField("Content",
        validatots=[
            DataRequired(),
            Length(min=3, max=1000)
            ]
    )
    submit = SubmitField('Post!')
