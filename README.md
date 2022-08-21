# auth0-w-external-2fa

Proof of Concept for integrating AUTH0 with an external 2FA.

**Auth0 Setup**

* Clone to use,
* Setup an [auth0](https:https://auth0.com/) account, create an application (you will need to know your domain, client_id and client_secret), and grant `password` permissions (via 'advanced' on the application setup page),
* Add & Verify a test username & password.

**Twilio Verify for email based 2FA**

* Create [Twilio Verify](https://console.twilio.com/us1/develop/verify/email) account,
* Follow setups to create email verification via [SendGrid](https://docs.sendgrid.com/for-developers/sending-email/api-getting-started). SendGrid is a Twilio company for email sending,
* Note that both services provide a `freemium` tier for development.
* In SendGrid - create a validated "sender", and a [template](https://www.twilio.com/docs/verify/email#find-template-id),
* In Twilio - create the Verify service, by email and add email integration to SendGrid.

**Configuration**

* create local file `.creds.toml` with the following format:

```python
    domain = ""

    # Auth0
    client_id = ""
    client_secret = ""
    
    password = ""
    username = ""

    # SendGrid
    sender = ""
    sendgrid_api_key = ""

    # Twilio
    twilio_account_sid = ""
    twilio_auth_token = ""
    twilio_verify_service_id = ""

```

**
