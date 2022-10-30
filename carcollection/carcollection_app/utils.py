from carcollection.carcollection_app.models import Profile


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None
