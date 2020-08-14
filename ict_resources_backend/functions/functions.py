import uuid

from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from anymail.message import attach_inline_image_file

import myresources_profil
from myresources_profil.constants import URL_VALIDATE_CREATE

from datetime import datetime


def send_activate_account_mail(email_to, url):
    msg = EmailMultiAlternatives(
        subject="ACTIVER SON COMPTE",
        body="Cliquer ici pour activer  votre compte",
        from_email="MyResources <myresources@gmail.com>",
        to=["New User  " + email_to, "theprogrammer.manager@example.com"],
        reply_to=["theprogrammer <theprogrammer@example.com>"])

    # Include an inline image in the html:

    html = """  <h3>VOICI VOTRE LIEN <a href="{url_activate}">activate</a>
                              your account</h3>""".format(url_activate=url)
    msg.attach_alternative(html, "text/html")

    # Optional Anymail extensions:
    msg.metadata = {"": "8675309", "experiment_variation": 1}
    msg.tags = ["activation", "onboarding"]
    msg.track_clicks = True
    msg.send()


def generate_url(email, begin_url):
    code = begin_url+"-"+uuid.uuid4().hex[:6].upper()
    url = URL_VALIDATE_CREATE + code
    expiration_date = datetime.now()
    User = get_user_model()
    user = User.objects.get(email=email)
    from myresources_profil.models import CodeValidation
    req_gen = CodeValidation.objects.create(url_code=url, date_expiration=expiration_date,
                                            id_creator=user,
                                            is_valid=False)
    req_gen.save()

    return url
