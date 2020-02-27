from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.fields.html5 import DateField
from wtforms import RadioField
from wtforms import FloatField
from wtforms import IntegerField


class PostForm(FlaskForm):
    username = StringField("username")
    postbox = StringField("postbox")
    image = StringField('image', default="")
    submit = SubmitField("Post")


class TicketForm(FlaskForm):
    name = StringField("name")
    toothnum = IntegerField("toothnum")
    date = DateField(id='datepick')
    money = FloatField('money')
    radio = RadioField('Label', choices=[('bills', 'Bills'), ('coins', 'Coins')])
    submit = SubmitField("create")
