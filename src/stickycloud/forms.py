
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

class NoteForm( FlaskForm ):

    # TODO: Disallow name "new"

    title = StringField( 'Title' )
    content = TextAreaField( 'Content', label=None )
    