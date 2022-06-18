import bcrypt

def hash_password(password):
    password = password.encode()  #.encode turns password into bytes
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt).decode() #.decode turns password into string

def validate_password(user_password, hashed_password):
    user_password = user_password.encode()
    hashed_password = hashed_password.encode()
    return bcrypt.checkpw(user_password, hashed_password)



if __name__ == '__main__':
    passw = hash_password("adewale")
    print(passw)
    print(validate_password("adewale", passw))