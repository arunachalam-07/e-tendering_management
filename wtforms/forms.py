from flask_wtf import Form
from wtforms import TextField,SubmitField
from wtforms.fields.core import IntegerField
class contactForm(Form):
    name=TextField('sample value')
    submit = SubmitField("Send")
class PlaceBid(Form):
    address=TextField('Enter your address',)
    bid=IntegerField('PlaceBid')
    quotation=TextField('Enter your Quote')
    submit=SubmitField('Submit')