from intuitlib.client import AuthClient

# clockify api_key
clockify_api_key="NDE4OTNjYTAtZTY2Zi00OTc0LWI5OGYtNjI4MzFlYmZiYzJm"
clockify_bearer_token = {'x-api-key': clockify_api_key}

#QB0 Oauth2.0
qbo_auth_client = AuthClient(
    "ABuQA6gZNqgZU8T21D9ZvLSqMU8oydSKTImRdMvMZxm9sNCnrA",
    "h2uXIawyjNBlpA0TeF4QUiqfMxBWi1yPIVpP8Sd4",
    "https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl",
    "production",
)
'''
auth_client = AuthClient(
    client_id,
    client_secret,
    redirect_uri,
    environment,
)
'''