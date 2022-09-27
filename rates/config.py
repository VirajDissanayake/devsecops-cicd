import boto3

region="us-east-1"
ssm = boto3.client("ssm", region=region)
rds = boto3.client('rds', region=region)

def get_param(param):
    return ssm.get_parameter(
        Name=param,
        #WithDecryption=True
    )

ENDPOINT = get_param("host")
PORT = get_param("port")
USER = get_param("user")
NAME = get_param("name")

token = rds.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=region)

DB = {
    "name": NAME,
    "user": USER,
    "host": ENDPOINT,
    "token": token
}
