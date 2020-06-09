from myresources.models import ReservationEquipment, Equipment
from myresources.serializer import ReservationSerializer


def CreateSheduleWithIdEquipment(request):
    id_equip = request.data['id_equipment']

    instance = Equipment.objects.get(pk=id_equip)

    # on recupere  l'instance  pour diminuer le numbre d'equipement et sauvegarder
    if instance.number != 0:
        number_instance = instance.number
        instance.number -= 1
        instance.save()

        # verication si il es dans reservation table , sinon , on le modifie

        try:

            # ajout dans la table reservation l'equipement qu'on a emprunté
            instance_reservation = ReservationEquipment.objects.get(id_equipment=id_equip)
            datas = {'id_equipment': id_equip, 'number': (instance_reservation.number + 1)}

            serializer_reservation = ReservationSerializer(instance_reservation, data=datas)
            if serializer_reservation.is_valid(raise_exception=True):
                serializer_reservation.save()

        except ReservationEquipment.DoesNotExist:
            # s'il n'existe pas deja cette equipement dans la table reservation on le cree et on l'incremente de 1

            datas = {'id_equipment': id_equip, 'number': 1}

            serializer_reservation = ReservationSerializer(data=datas)
            if serializer_reservation.is_valid(raise_exception=True):
                serializer_reservation.save()



