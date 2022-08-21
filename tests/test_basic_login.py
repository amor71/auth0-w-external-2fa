import toml
from auth0.v3.authentication import GetToken


def test_login():
    secrets = toml.load(".creds.toml")
    token = GetToken(secrets["domain"])

    print(token)

    t = token.login(
        client_id=secrets["client_id"],
        client_secret=secrets["client_secret"],
        username=secrets["username"],
        password=secrets["password"],
        realm="Username-Password-Authentication",
        scope=None,
        audience=None,
    )

    print(t)

    return True
