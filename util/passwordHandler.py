import bcrypt


def hash_password(plain_text_password):
    """
    It hashes password. By using bcrypt, the salt is saved into the hash itself
    :param plain_text_password: String
    :return: String
    """
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    """
    It verifies the given password compared to the saved one
    :param plain_text_password: String
    :param hashed_password: String
    :return: Boolean
    """
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)