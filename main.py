# +----------------------------------------------------------------------------+
# | CARDUI WORKS v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2025, CARDUI.COM (www.cardui.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.cardui.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: May 18nd, 2025
# | Last update..: May 21th, 2025
# | WhatIs.......: HashTest - Main
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# bcrypt 4.3.0: https://pypi.org/project/bcrypt/
# Hashing Passwords in Python with BCrypt: https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/

# ------------------------- Libraries -------------------------
import bcrypt

# ------------------------- Functions -------------------------
def hash_password_bcrypt(password, salt):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def verify_password_bcrypt(entered_password, stored_hash):
    return bcrypt.checkpw(entered_password.encode('utf-8'), stored_hash)

# ------------------------- Code -------------------------
# Dummy test log in
dummyUser = "admin@email.com"
dummyPassword = "aabb$12345678"

dummySalt = bcrypt.gensalt()
dummyPasswordHash = hash_password_bcrypt(dummyPassword, dummySalt)

# Dummy select to DB
db_passwords = {
    dummyUser: [dummyPasswordHash, dummySalt]
}

dummyEnteredPassword = "aabb$12345678j"
dummyEnteredPasswordHash = hash_password_bcrypt(dummyEnteredPassword, db_passwords[dummyUser][1])

print(verify_password_bcrypt(dummyEnteredPassword, dummyPasswordHash))