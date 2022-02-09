import boto3


class SecretsManager:

    def __init__(self,):
        self.client = boto3.client("secretsmanager")

    def list_secrets(self,):
        return self.client.list_secrets()["SecretList"]

    def create_secret(self, name, secret_string):
        response = self.client.create_secret(Name=name, SecretString=secret_string)
        return response

    def update_secret(self, name, secret_string):
        response = self.client.update_secret(SecretId=name, SecretString=secret_string)
        return response

    def delete_secret(self, name):
        response = self.client.delete_secret(SecretId=name, ForceDeleteWithoutRecovery=True)
        return response
