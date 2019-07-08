# oidc_test_client
Django app working as an OpenID Connect client to quickly test OIDC providers



Installation:

1. Clone this repository

2. `pip install -r requirements.txt`

3. Initialize Django: `python manage.py migrate --noinput`

4. In `oidc_provider/settings.py`  set the appropriate values for the `client_id`, `client_secret` and the url of the OIDC provider, `OIDC_URL` . These values can also be set using environment variables.

5. Start the application giving the URI of the OIDC provider. Example:

   `python  manage.py runserver 9000`

   In the above example oidc_test_client will run on port `9000`  and will try to use an OIDC provider running on `http://localhost:8000/oidc_provider` to authenticate 





Note, if used to test [Kolibri](https://github.com/learningequality/kolibri) with the [OIDC provider plugin](https://github.com/learningequality/kolibri/tree/release-v0.12.x/kolibri/plugins/oidc_provider_plugin), the client must be created in the provider. These are the needed steps in Kolibri:

1.  Enable the `oidc_provider_plugin` plugin: `kolibri plugin kolibri.plugins.oidc_provider_plugin enable`
3. These commands must be executed to create and fill some info in the needed authentication tables:
`kolibri manage migrate`
`kolibri manage creatersakey`
4. For each client, we need to insert into the database some information. As an example, if we want this **oidc_test_client** app to be a client of the Kolibri provider:
`kolibri manage oidccreateclient  --name=test --clientid=test.app --redirect-uri=http://localhost:9000/oidc/callback`


