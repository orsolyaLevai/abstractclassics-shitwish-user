from repository import dataManager


@dataManager.connection_handler
def insertUser(cursor, firstname, lastname, email, password, address, phonenumber):
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

@dataManager.connection_handler
def getUserByEmail(cursor, email):
    cursor.execute("""
                        SELECT * FROM shitwishusers
                        where email = %(email)s
                    """, {'email': email})
    user = cursor.fetchone()
    return user

@dataManager.connection_handler
def getUserById(cursor, id):
    cursor.execute("""
                        SELECT * FROM shitwishusers
                        where id = %(id)s
                    """, {'id': id})
    user = cursor.fetchone()
    return user