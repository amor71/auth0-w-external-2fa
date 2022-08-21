import toml
from twilio.rest import Client

secrets = toml.load(".creds.toml")


def test_twilio_auth():
    Client(secrets["twilio_account_sid"], secrets["twilio_auth_token"])

    return True


def test_twilio_email():
    client = Client(
        secrets["twilio_account_sid"], secrets["twilio_auth_token"]
    )

    verification = client.verify.v2.services(
        secrets["twilio_verify_service_id"]
    ).verifications.create(to="amichay.oren@gmail.com", channel="email")

    print(verification.sid)


def test_twilio_email_verify():
    client = Client(
        secrets["twilio_account_sid"], secrets["twilio_auth_token"]
    )

    print("Enter verification code: ")
    verification_code = input()

    verification_check = client.verify.v2.services(
        secrets["twilio_verify_service_id"]
    ).verification_checks.create(
        to="amichay.oren@gmail.com", code=verification_code
    )

    if verification_check.status != "approved":
        print(f"Verification failed w {verification_check.status}")
        return False

    return True
