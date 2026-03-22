import face_auth


def calculate_risk():

    authorized = face_auth.verify()

    if authorized:

        return 1

    else:

        return 10