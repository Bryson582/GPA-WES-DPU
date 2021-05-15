from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired
class MailForm(FlaskForm):
    name = StringField('您的学号',validators=[DataRequired()])
    pwd = PasswordField('您的密码',validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('查询绩点')

