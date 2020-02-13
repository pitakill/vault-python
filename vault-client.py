import hvac
import os

client = hvac.Client(
    url=os.environ['VAULT_ADDR'],
    token=os.environ['VAULT_TOKEN'],
)

if not client.is_authenticated():
    print("Can't communicate with Vault")
    exit()

status = client.sys.read_health_status(method='GET')
print(status)
