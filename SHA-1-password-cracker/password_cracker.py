import hashlib

def crack_sha1_hash(hash, use_salts= False):
    f = open('top-10000-passwords.txt', 'r')
    content = f.readlines()
    if use_salts:
      s = open('known-salts.txt' , 'r')
      salt_content = s.readlines()
      for passw in content:
        for salt in salt_content:
          toCheck = salt.rstrip("\n") + passw.rstrip("\n")          
          hashed = hashlib.sha1(bytes(toCheck, encoding="ascii")).hexdigest()          
          if hashed == hash:
            return passw.rstrip("\n")
          toCheck2 = passw.rstrip("\n") + salt.rstrip("\n")
          hashed = hashlib.sha1(bytes(toCheck2, encoding="ascii")).hexdigest()          
          if hashed == hash:
            return passw.rstrip("\n")
    else:
      for passw in content:
        passw= passw.rstrip("\n")
        if hashlib.sha1(bytes(passw, encoding="ascii")).hexdigest() == hash:
          return passw
    return "PASSWORD NOT IN DATABASE"