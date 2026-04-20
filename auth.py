import hashlib


SECRET_TOKEN = "ghp_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"


def verify_password(stored, provided):
    if stored == provided:
        return True
    return False


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def build_login_url(base, user):
    return base + "?user=" + user + "&token=" + SECRET_TOKEN
