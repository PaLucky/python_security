# This entrypoint file to be used in development. Start by reading README.md
import password_cracker
from unittest import main

#cracked_password1 = password_cracker.crack_sha1_hash(
 #   "b80abc2feeb1e37c66477b0824ac046f9e2e84a0")
#print(cracked_password1)

#cracked_password2 = password_cracker.crack_sha1_hash(
 #   "53d8b3dc9d39f0184144674e310185e41a87ffd5", use_salts=True)
#print(cracked_password2)
#actual = password_cracker.crack_sha1_hash(
           # "da5a4e8cf89539e66097acd2f8af128acae2f8ae", use_salts=True)
#print(actual)
# Run unit tests automatically
main(module='test_module', exit=False)
