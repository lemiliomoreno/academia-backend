import json

from utils.secrets_manager import SecretsManager

secret_client = SecretsManager()

# list_of_secrets = secret_client.list_secrets()

secret_created = secret_client.create_secret(name="database/prod", secret_string=json.dumps({"DATABASE_USER": "emilio_prod", "DATABASE_PASSWORD": "emilio123_prod"}))

# updated_secret = secret_client.update_secret(name="database/prod", secret_string=json.dumps({"DATABASE_USER": "emilio_prod", "DATABASE_PASSWORD": "emilio123_prod"}))

# deleted_secret = secret_client.delete_secret(name="database/prod")

print(secret_created)
