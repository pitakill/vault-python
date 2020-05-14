import os

from lib.vault import Vault

addr = os.environ['VAULT_ADDR']
token = os.environ['VAULT_TOKEN']

vault = Vault(addr, token)

print(vault.get_status())

if vault.is_root():
    print('Please use a token without such a power, you are using a token with root capabilities')
