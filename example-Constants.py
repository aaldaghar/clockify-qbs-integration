from intuitlib.client import AuthClient
from intuitlib.enums import Scopes

# clockify api_key
clockify_api_key="api-key"
clockify_bearer_token = {'x-api-key': clockify_api_key}

#QB0 Oauth2.0
#Instantiate client
qbo_auth_client = AuthClient(
    'client_id',
    'client_secret',
    'redirect_uri',
    'environment',
)
#Prepare scopes  
qbo_scopes = [
    Scopes.ACCOUNTING,
    ]
#Get authorization URL
qbo_auth_url = qbo_auth_client.get_authorization_url(qbo_scopes)
#Access TOKEN url 
qbo_access_token_url = '{0}/access_token'.format(qbo_auth_url)
# You have to fetch the code from the UI as there is no easy way to extract it using the intuitlib SDK. (you can try and build your own Auth using rauth library)
qbo_auth_code = "auth-code"
# real_id
qbo_realm_id = "realm-id"
#get authorization code
qbo_auth_client.get_bearer_token(qbo_auth_code, realm_id=qbo_realm_id)

