import locale
import uuid

import arrow
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from anymail.message import attach_inline_image_file

import myresources_profil
from functions.facades import get_date_and_time_by_id
from myresources.models import *
from myresources.serializer import NotificationSerializer
from myresources_profil.constants import URL_VALIDATE_CREATE

import datetime

from myresources_profil.models import Profile


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
    code = begin_url + "-" + uuid.uuid4().hex[:6].upper()
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


def create_notification(id_event, id_receiver, id_emetter, id_cat, message):
    tab_notify = {'id_event': id_event, 'id_reveiver': id_receiver, 'id_emetter': id_emetter, 'id_cat': id_cat,
                  'message': message}

    notify = Notifications()
    notify.id_event = Schedule.objects.get(pk=id_event)
    notify.id_receiver = User.objects.get(pk=id_receiver)
    notify.id_emetter = User.objects.get(pk=id_emetter)
    notify.id_cat = CategorieNotifications.objects.get(pk=id_cat)
    notify.message = message
    notify.save()


def verify_for_notification(request):
    type_schedule = TypeSchedule.objects.get(type=request['id_type'])
    user = User.objects.get(pk=request['id_user'])

    # si c'est une reservation creer par admin ou prof
    print("okey il est admin")
    print(request)

    if (request['type_reservation'] == RESERVATION) & user.is_teacher:

        print("mixxx admin admin")

        # on va notifier tous les admin

        all_admin = User.objects.filter(is_admin=True)

        print("c'est une resevation")
        print(all_admin)

        for admin in all_admin:
            # recherchons le cours concerné

            course = Course.objects.get(pk=request['id_course'])

            # recuperons les date starts et debut puis formtons en

            date = get_date_and_time_by_id(request['pk'])

            message = """ le professeur  %s a ajouté une réservation 
            pour le cours %s(%s)  qui serra le %s de %s 
            au %s a %s""" % (user.email, course.code_course, course.name,
                             date['date_start'], date['date_start_time'], date['date_end'],
                             date['date_end_time'])

            create_notification(id_event=request['pk'], id_receiver=admin.pk, id_emetter=user.id, id_cat=COURS,
                                message=message)
            return  # on sort un fois pour qu'il ne prenne pas le deuxieme if

    # si l'admin a créé un cours on notifie le prof
    if type_schedule.type == COURS:

        if user.is_admin:
            teacher = User.objects.get(pk=request['id_teacher'])

            message = "L'adminnistrateur " + user.email + "  vous a ajouté au cours  "
            course = Course.objects.get(pk=request['id_course'])

            date = get_date_and_time_by_id(request['pk'])


            message = """L'administrateur   %s a ajouté une réservation 
                        pour le cours %s(%s)  qui serra le %s de %s 
                        au %s a %s""" % (user.email, course.code_course, course.name,
                                         date['date_start'], date['date_start_time'], date['date_end'],
                                         date['date_end_time'])

            create_notification(id_event=request['pk'], id_receiver=teacher.pk, id_emetter=user.id, id_cat=COURS,
                                message=message)


def send_mail_notifications():
    msg = EmailMultiAlternatives(
        subject="ACTIVER SON COMPTE",
        body="Cliquer ici pour activer  votre compte",
        from_email="MyResources <myresources@gmail.com>",
        to=["New User  ", "theprogrammer.manager@example.com"],
        reply_to=["theprogrammer <theprogrammer@example.com>"])

    # Include an inline image in the html:

    html = """  <h3>VOICI VOTRE LIEN <a href="{url_activate}">activate</a>
                                  your account</h3>""".format(url_activate="dsfd")
    msg.attach_alternative(html, "text/html")

    # Optional Anymail extensions:
    msg.metadata = {"": "8675309", "experiment_variation": 1}
    msg.tags = ["activation", "onboarding"]
    msg.track_clicks = True
    msg.send()
