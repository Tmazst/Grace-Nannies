from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TextAreaField,BooleanField,DateField,RadioField
from wtforms.validators import DataRequired,Length,Email, EqualTo, ValidationError
from flask_login import current_user
from flask_wtf.file import FileField , FileAllowed



class Register(FlaskForm):

    name = StringField('name', validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=120)])
    confirm = PasswordField('confirm', validators=[DataRequired(),EqualTo('password'), Length(min=8, max=120)])
    role_choice = RadioField('Job seeker/Employer',choices=[(True,"Job Seeker"),(False,"Employer")])

    submit = SubmitField('Create Account!')


    def validate_email(self,email):
        from app import db, user,app

        # with db.init_app(app):
        user_email = user.query.filter_by(email = self.email.data).first()
        if user_email:
            raise ValidationError(f"This email is already registered in this platform")



class Login(FlaskForm):

    email = StringField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=64)])
    stay_signed = BooleanField("Stay Signed: ")
    use_2fa_auth = BooleanField("Use 2-Factor-Authentication?: ")
    submit = SubmitField('Login')


class Contact_Form(FlaskForm):

    name = StringField('name')
    email = StringField('email', validators=[DataRequired(),Email()])
    subject = StringField("subject")
    message = TextAreaField("Message",validators=[Length(min=8, max=2000)])
    submit = SubmitField("Send")

class Two_FactorAuth_Form(FlaskForm):
    use_2fa_auth_input = StringField("Paste 2FA Code Here: ")
    submit = SubmitField('Continue')


class Update_account_form(FlaskForm):

    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=40)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    image_pfl = FileField('Profile Image', validators=[FileAllowed(['jpg','png'])])
    contacts = StringField('Contact(s)', validators=[Length(min=8, max=120)])
    date_of_birth = DateField('Date of Birth:', format="%Y-%m-%d")
    school = StringField('High School', validators=[Length(min=8, max=120)])
    tertiary = StringField('Tertiary (Optional)',validators=[Length(min=0, max=120)])
    experience = TextAreaField('Work Experience (Optional)',validators=[Length(min=0, max=120)])
    skills = TextAreaField('About Yourself Hint: Why should companies hire you', validators=[Length(min=10, max=30)])
    hobbies = StringField('Interests (Optional)')
    address = StringField('Physical Address', validators=[DataRequired(), Length(min=8, max=120)])
    cv_file = FileField('Upload CV/Resume', validators=[FileAllowed(['pdf', 'docx'])])
    reference_1 = TextAreaField('Reference ',
                                validators=[DataRequired(), Length(min=8, max=200)])
    reference_2 = TextAreaField('Reference',
                                validators=[DataRequired(), Length(min=8, max=200)])

    def validate_email(self,email):
        from app import db, user
        if current_user.email != self.email.data:
            #Check if email exeists in database
            user_email = user.query.filter_by(email = self.email.data).first()
            if user_email:
                raise ValidationError(f"email, {email.value}, already taken by someone")


    update = SubmitField('Update')


class Reset(FlaskForm):

    old_password = PasswordField('old password', validators=[DataRequired(), Length(min=8, max=120)])
    new_password = PasswordField('new password', validators=[DataRequired(), Length(min=8, max=120)])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo('new_password'), Length(min=8, max=120)])

    reset = SubmitField('Reset')


class Reset_Request(FlaskForm):

    email = StringField('email', validators=[DataRequired(), Email()])

    reset = SubmitField('Submit')

    # def validate_email(self,email):
    #     user = user.query.filter_by