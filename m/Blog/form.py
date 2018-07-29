from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired



class NameForm(FlaskForm):
    username=StringField('What is on your mind',validators=[DataRequired()])
    submit=SubmitField('Post')
