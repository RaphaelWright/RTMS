 import hashlib



password ="hello"
salt = "*!%)#"
salt2 = "@))#"
salted =  salt2 + password + salt 
print(salted)
enc = hashlib.new()

enc.update(password.encode())

newPassword = enc.hexdigest()

print(f"old encryption: {enc.hexdigest()}")
print(f"encoded: {password.encode()}")

