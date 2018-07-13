from repository import data_manager


@data_manager.connection_handler
def insert_user(cursor, firstname, lastname, email, password, address, phonenumber):
    cursor.execute("""
                                        INSERT INTO shitwishusers (first_name, last_name, email, password, address, phone_number)
                                        VALUES (
                                            %(firstName)s,
                                            %(lastName)s,
                                            %(email)s,
                                            %(password)s,
                                            %(address)s,
                                            %(phoneNumber)s);
                                            """, {'firstName': firstname,
                                                  'lastName': lastname,
                                                  'email': email,
                                                  'password': password,
                                                  'address': address,
                                                  'phoneNumber': phonenumber})


@data_manager.connection_handler
def get_user_by_email(cursor, email):
    cursor.execute("""
                        SELECT * FROM shitwishusers
                        WHERE email = %(email)s
                    """, {'email': email})
    user = cursor.fetchone()
    return user


@data_manager.connection_handler
def get_user_by_id(cursor, id):
    cursor.execute("""
                        SELECT * FROM shitwishusers
                        WHERE id = %(id)s
                    """, {'id': id})
    user = cursor.fetchone()
    return user