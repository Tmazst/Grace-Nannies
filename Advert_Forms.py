from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TextAreaField,BooleanField,RadioField
from wtforms.validators import DataRequired,Length,Email, EqualTo, ValidationError,URL
from flask_login import current_user
from wtforms.fields import DateField, TelField
from flask_wtf.file import FileField , FileAllowed

from Forms import Register

class Job_Ads_Form(FlaskForm):

    job_title = StringField('Job Title:', validators=[DataRequired(), Length(min=2, max=120)])
    pay_type_bl = BooleanField('Pay Type:')
    other_pay_type = StringField('Other:')
    other_job_bl = BooleanField('Other Job Type:')
    other_job_type = StringField('Other:')
    about_company = TextAreaField('Brief About Company:')
    description = TextAreaField('Job Description or Tasks:', validators=[DataRequired(), Length(min=5, max=400)])
    category = StringField('Category:')
    work_duration_bl = BooleanField('')
    work_duration = StringField('Work/Project Duration (Start - End):')
    start_date = DateField('Project Starts:', format="%Y-%m-%d")
    end_date = DateField('Ends: (Tick To Include)', format="%Y-%m-%d")
    work_days_bl = BooleanField('')
    work_days = StringField('Working Days: (Tick To Include)')
    work_hours_bl = BooleanField('')
    work_hours = StringField('Work Hours: (Tick To Include)')
    responsibilities = TextAreaField('Key Roles & Responsibilities:')
    qualifications = TextAreaField('Requirements & Qualifications:', validators=[DataRequired(), Length(min=5, max=400)])
    age_range_bl = BooleanField('Age Range: (Tick To Include)')
    age_range = StringField('Age Range: ')
    benefits_bl = BooleanField('Benefits: (Tick To Include)')
    benefits = TextAreaField('Benefits: ')
    application_deadline = DateField('Application Deadline:',format="%Y-%m-%d")
    # application_details = TextAreaField('Application Details', validators=[DataRequired(), Length(min=2, max=20)])
    posted_by = StringField('Posted By:')

    publish = SubmitField("Publish")

class Freelance_Ads_Form(FlaskForm):

    service_title = StringField('Project Title:', validators=[DataRequired(), Length(min=2, max=120)])
    speciality = StringField('Expertise or Skill:')
    category = StringField('Category:')
    description = TextAreaField('Project Description:', validators=[DataRequired(), Length(min=5, max=400)])
    start_date = DateField('Project Starts:',format="%Y-%m-%d")
    end_date = DateField('Ends:',format="%Y-%m-%d")
    project_duration = StringField('Project Duration (Start - End):')
    working_days = StringField('Project Working Days:')
    project_prerequits = TextAreaField('Pre-requisites for Project:', validators=[DataRequired(), Length(min=5, max=500)])
    benefits_bl = BooleanField('Include Benefits?:')
    benefits = TextAreaField('Benefits: (Tick To Include)')
    application_deadline = DateField('Application Deadline:', format="%Y-%m-%d" )
    # application_details = TextAreaField('Application Details', validators=[DataRequired(), Length(min=2, max=20)])
    posted_by = StringField('Posted By:')

    publish = SubmitField("Publish")

class Company_Register_Form(FlaskForm):

    company_name = StringField('Company Name', validators=[DataRequired(), Length(min=2, max=120)])
    company_email = StringField('Email', validators=[DataRequired(), Email()])
    company_password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=64)])
    company_confirm = PasswordField('Confirm', validators=[DataRequired(), EqualTo('company_password'), Length(min=8, max=64)])
    company_contacts = TelField('Contact(s)', validators=[Length(min=8, max=64)])
    company_address = StringField('Physical Address', validators=[DataRequired(), Length(min=8, max=100)])
    company_logo = FileField('Company Logo', validators=[FileAllowed(['jpg', 'png'])])
    website_link = StringField('Company Website Link')
    facebook_link = StringField('Facebook Link')
    twitter_link = StringField('X Link(former Twitter)')
    youtube_link = StringField('Youtube Link')
    payment_options = RadioField("Choose Payment Plan",
                                 choices=[("pay_plan_1", "Pay Monthly"), ("pay_plan_4", "Pay Annually"),
                                          ("pay_plan_2", "Pay Per Advert"), ("pay_plan_3", "Free For Now")])

    submit = SubmitField('Create Account!')


class Company_UpdateAcc_Form(FlaskForm):

    company_name = StringField('Company Name', validators=[DataRequired(), Length(min=2, max=60)])
    company_email = StringField('Email', validators=[DataRequired(), Email()])
    company_logo = FileField('Company Logo', validators=[ FileAllowed(['jpg','png'])])
    company_contacts = StringField('Contact(s)', validators=[Length(min=8, max=64)])
    company_address = StringField('Physical Address', validators=[DataRequired(), Length(min=8, max=100)])
    website_link = StringField('Company Website Link')
    facebook_link = StringField('Facebook Link')
    twitter_link = StringField('Twitter Link')
    youtube_link = StringField('Youtube Link')
    payment_options = RadioField("Choose Payment Plan", choices=[("pay_plan_1", "Pay Monthly"),("pay_plan_4", "Pay Annually"),
                                                                 ("pay_plan_2", "Pay Per Advert"),("pay_plan_3", "Free For Now")])

    # Validate email before saving it in database
    def validate_email(self,company_email):
        from app import db, company_user
        if current_user.company_email != self.company_email.data:
            #Check if email exeists in database
            cmp_user_email = db.query(company_user).filter_by(company_email = self.company_name.data).first()
            cmp_name = db.query(company_user).filter_by(company_email=self.company_name.data).first()
            if cmp_user_email or cmp_name:
                raise ValidationError(f"email, {company_email.value}, already taken.")

    def validate_company_name(self, company_name):
        from app import db, company_user
        if current_user.comapny_name != self.company_name.data:
            # Check if email exists in database
            cmp_name = db.query(company_user).filter_by(comapny_name=self.company_name.data).first()
            if cmp_name:
                raise ValidationError(f"Company Name, {company_name.value} , already taken.")

    company_submit = SubmitField('Update')

class Company_Login(FlaskForm):
    company_email = StringField('Company email', validators=[DataRequired(),Email()])
    company_password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=64)])
    company_submit = SubmitField('Login')


class Reset(FlaskForm):
    old_password = PasswordField('old password', validators=[DataRequired(), Length(min=8, max=64)])
    new_password = PasswordField('new password', validators=[DataRequired(), Length(min=8, max=64)])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo('new_password'), Length(min=8, max=64)])

    reset = SubmitField('Reset')

class Reset_Request(FlaskForm):

    email = StringField('email', validators=[DataRequired(), Email()])

    reset = SubmitField('Submit')

class Work_Feedback(FlaskForm):
    comment = TextAreaField('Work Feedback:', validators=[DataRequired(), Length(min=10, max=1000)])
    submit = SubmitField('Submit')

class Approved_Form(FlaskForm):

    submit = SubmitField('Approve')

class Freelance_Section(FlaskForm):
    skills = StringField('Skill(s):', validators=[DataRequired(), Length(min=5, max=100)])
    experience = TextAreaField('Previous Work (Optional):', validators=[DataRequired(), Length(min=4, max=300)])
    what_do_you_do = TextAreaField('Explain your Work:', validators=[DataRequired(), Length(min=10, max=1000)])
    other_fl = StringField('Your Sell Tag (Optional):')
    portfolio_file = FileField('Upload Portfolio', validators=[FileAllowed(['pdf', 'docx'])])
    fb_link = StringField('Facebook Link (Optional):')
    pinterest_link = StringField('Pinterest Link (Optional):')
    linkedin_link = StringField('LinkedIn Link (Optional):')
    twitter_link = StringField('X Link (Optional):')
    youtube_link = StringField('Youtube Link (Optional):')
    instagram_link = StringField('Instagram Link (Optional):')
    submit = SubmitField('Submit')

class Job_Feedback_Form(FlaskForm):
    job_feedback = TextAreaField('Explain your Work:', validators=[DataRequired(), Length(min=10, max=1000)])

    submit = SubmitField('Submit')

class Testimonials(FlaskForm):

    name = StringField('Name:', validators=[DataRequired(), Length(min=2, max=120)])
    title = RadioField('Title:',('Mr.','Mr.'),('Ms.','Ms.'),('Other','Other'), validators=[DataRequired()])
    occupation_choices = RadioField('Please Choose:', ('Working', 'Working'),('Not Working Yet', 'Not Working Yet'), ('Own Boss', 'Own Boss'), ('Student', 'Student'),
                                    ('Graduate', 'Graduate'),('Other', 'Other'), validators=[DataRequired()])
    occupation = StringField('Occupation/Company/College/etc:(Optional)', validators=[DataRequired(), Length(min=2, max=120)])
    image = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png'])])
    pay_type_bl = BooleanField('Pay Type:')
    testimony = TextAreaField('Testimony/Comments:', validators=[DataRequired(), Length(min=5, max=400)])
    qualifications = TextAreaField('Requirements or Qualifications:', validators=[DataRequired(), Length(min=5, max=400)])
    age_range_bl = BooleanField('Age Range:')
    age_range = StringField('Age Range:')