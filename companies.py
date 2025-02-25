
from app import Company_Register_Form, db, engine



class Process_Company_Registration:

    company_register = Company_Register_Form()

    company_register.metadata.create_all(bind=engine)

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if company_register.validate_on_submit():


        if request.method == 'POST':
            # context


            # If the webpage has made a post e.g. form post
            with engine.connect():
                print('Create All..........................................')
                company_hashd_pwd = encry_pw.generate_password_hash(company_register.company_password.data).decode \
                    ('utf-8')
                # Base.metadata.create_all()
                # ....user has inherited the Base class
                # user.metadata.create_all(bind=engine)
                user1 = company_data(company_name=company_register.company_name.data, company_email=company_register.company_email.data, company_password=company_hashd_pwd ,company_contacts=company_register.company_contacts.data,
                                     company_address=company_register.company_address.data, web_link=company_register.website_li
                                     k.data,fb_link=company_register.facebook_lin
                                     k.data,
                                     twitter_link=company_register.twitter_link.data,youtube=company_register.youtube_link
                                     .data)

                # db.rollback()
                db.add(user1)
                db.commit()
                flash(f"Account Successfully Created for {company_register.company_name.data}", "success")

                return redirect(url_for('login'))

                # print(company_register.name.data,company_register.email.data)
    elif company_register.errors:
        flash(f"Account Creation Unsuccessful ", "error")
        print(company_register.errors)



    # from myproject.models import user
    return render_template("company_signup_form.html",company_register=company_register)