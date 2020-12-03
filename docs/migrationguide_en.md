# OAuth2 migration guide

Everything you need to get on Switch to OAuth2.

## Introduction
Security is one of the most important non-functional requirements of a platform like Europace that uses consumer financial data. We take this responsibility very seriously. And at the same time we believe that a technical connection to Europace technology can be achieved easily and quickly.

That is why we are doing away with the previously proprietary authentication procedures and introducing OAuth2 as the standard technology for Europace. This method is widespread - almost every software developer has worked with it at some point. Because of this familiarity and simplicity, the development effort for the connection is reduced and the developers' nerves are spared.

We are thereby increasing security by making it even easier to renew API keys and making access to Europace technology even more traceable.

In addition, with OAuth2 we will enable real single sign-on in the future by integrating our own identity provider. In addition, after consultation with Europace partners, tool manufacturers can integrate their applications into self-service even more easily for everyone without knowing a username and password.

We are convinced that the introduction of OAuth2 at Europace is a crucial basic building block for our partners and us in order to advance the digitization of mortgage lending.

## Timelines for migration?
All current APIs (as of July 2020) will support the old authentication method based on API key until the end of July 2021.

The authentication by username / password at the APIs will be switched off until the end of October 2020. If you use this procedure, you have to switch to OAuth2 as soon as possible to ensure the functionality of your integration!

# How to use OAuth2?
All Europace APIs are restricted, that means, to use our APIs you must login (authenticate) to Europace.

The following steps must be followed:
- You have to register your client in Europace once, as a result you will receive the `Client_ID` and the` Client-Secret` for the client
- To log in to Europace, call up https://api.europace.de/auth/token with the `Client_ID` and the` Client_Secret` as Basic-Auth in order to receive an `Access_Token`.
- With the `Access_Token` as a bearer token you can make requests to the Europace APIs.
Request header variable: `Authorization: Bearer [Access_Token]`

Most HTTP clients already support OAuth2, you only have to store `Client_ID`, `Client_Secret` and the address of the authorization server in the config.

## How do I get a client registered?

<a href = "mailto: helpdesk@europace2.de? subject = Registration API-Client & body = Hello,% 0D% 0Abitte% 20registered% 20a% 20API-Client% 20for% 20me.% 0D% 0A% 0D% 0APartnerID:% 0D % 0AClient name:% 0D% 0AClient description:% 0D% 0Atechnical% 20Contact email address:% 0D% 0Ashort% 20Description% 20des% 20Use case:% 0D% 0Arequired% 20Scopes:% 0D% 0A% 0D% 0AVielen% 20Thanks "> for client registration </a>


Please contact <a href = "mailto: helpdesk@europace2.de? Subject = Registration API-Client & body = Hello,% 0D% 0Abitte% 20registered% 20a% 20API-Client% 20for% 20me.% 0D% 0A% 0D% 0APartnerID:% 0D% 0AClient name:% 0D% 0AClient description:% 0D% 0Atechnical% 20Contact email address:% 0D% 0Ashort% 20Description% 20des% 20Use case:% 0D% 0Required% 20Scopes:% 0D% 0A% 0D% 0AVielen% 20Tank "> helpdesk@europace.de </a> with the following data:
- EP2 partner id
- Client name
- Client description:
- Contact email address for operational queries
- Brief description of the use case (goal)
- required scopes

After a short check with the owner (Europace partner), we will register your client immediately and provide you with the client ID and the client secret in your personal link list in Europace.

! [Linksammlung.png] (https://raw.githubusercontent.com/europace/authorization-api/Migrationsguide/docs/img/Linksammlung.png "Linkammlung")

Please note you automatically agree to the [Europace API Terms of Use] (https://docs.api.europace.de/nutzungsbedingungen/) by using the APIs.

## How do I get an access token?
To log into Europace, call up `https://api.europace.de/auth/token` with the` Client_ID` and the `Client_Secret` as Basic-Auth to get an Access_Token.

Request:
```` cURL
curl --location --request POST 'https://api.europace.de/auth/token' \
--user '[Client_ID]: [Client_Secret]' \
--header 'Content-Type: application / x-www-form-urlencoded' \
--data-urlencode 'grant_type = client_credentials'
````

Response:
```` json
{"access_token": [Access_Token],
   "scope": [available scopes],
   "token_type": "Bearer",
   "expires_in": 3600}
````

In this case, an access token is created in the name and on behalf of the partner with whom the client is registered. Other use cases are covered in “Old World - New World”.

## How do I call an API with Access-Token?
With the Access_Token as a bearer token, you can make requests to the Europace APIs.
Request header variable: `Authorization: Bearer [Access_Token]`

Using the example of the Vorgaenge API in curl:
```` cURL
curl --location --request GET 'https://api.europace2.de/v2/vorgaenge' \
--header 'Content-Type: application / json' \
--header 'Authorization: Bearer [Access_Token]
````

# Old world - new world
So far, various authentication methods have been available to you. In this section we will show you the best way to switch to OAuth2 in the various use cases and thus benefit from the simplification and standardization of the OAuth2 authentication process.

## API key
API keys are used to access interfaces so that you do not have to save and use user passwords. It is very likely that you also used this method for your connection.

often used with these APIs:
- Vorgaenge-API
- Antraege-API
- Reporting-API

This method will be supported until the end of July 2021.

Example so far:
```` cURL
curl --location --request POST 'https://api.europace.de/login' \
--header 'Content-Type: application / x-www-form-urlencoded' \
--data-urlencode 'username = [PartnerID] \
--data-urlencode 'password = [API key]'
````

Example new: \
see “How do I get an access token?”

## API key (impersonation)
The impersonated API key procedure is used when the API needs the specific user and you don't want to request an API key for everyone. It is sufficient to have an organization's API key that acts as a general key and with which users to which the organization has access can be logged in.

often used with these APIs:
- Silent Sign On
- Angebote-API
- Unterlagen-API

This method will be supported until the end of July 2021.

Example so far:
``` cURL
curl --location --request POST 'https://www.europace2.de/partnermanagement/login.api' \
--header 'x-partnerid: [PartnerID to be registered]' \
--header 'x-apikey: [Super API-Key]'
```

with `x-partnerid` of the user to be logged on and `x-apikey` of the partner (with extensive access rights (master key)). The `x-apikey` must be located in the partner management structure above the` x-partnerid`, otherwise the necessary access rights are missing.

Example new:
``` cURL
curl --location --request POST 'https://api.europace.de/auth/token' \
--user '[ClientID]: [ClientSecret]' \
--header 'Content-Type: application / x-www-form-urlencoded' \
--data-urlencode 'grant_type = client_credentials' \
--data-urlencode 'scope=impersonieren baufinanzierung:echtgeschaeft baufinanzierung:vorgang:lesen baufinanzierung:ereignis:lesen baufinanzierung:antrag:lesen' \
--data-urlencode 'subject = [PartnerID to be registered]' \
--data-urlencode 'actor = [registered partnerID]'
```

 Parameters | description
--- | ---
Subject | the partner ID of the user to be logged on |
Actor | the partner ID of the registered client |
Note | The actor partner ID must be arranged in the partner management structure above the subject partner ID, otherwise the necessary access rights are missing. |
Scope | must contain impersonating (Note: If a scope is specified, all required rights must be specified, i.e. impersonating alone does not make sense.) |

> ⚠️ **Note** \
For the use case of Silent Sign On, we will soon be offering Single Sign On via OpenID-Connect, with which you can connect your own user database to Europace as an Identity Service Provider. We will no longer support the Silent Sign On procedure.

## Username / Password (Cookie)
This method is mostly used if you have integrated the Europace login mask or your own login mask on your website / intranet.

Example so far:
``` cURL
curl --location --request POST 'https://www.europace2.de/partnermanagement/login.do' \
--header 'Content-Type: application / x-www-form-urlencoded' \
--data-urlencode 'username = [Username]' \
--data-urlencode 'password = [Password]'
```

You don't have to do anything here.

> ⚠️ **Note** \
The JWT that is stored in the cookie can no longer be used for API calls in the future. If you have this use case, switch to OAuth **by the end of October 2020.**

## Username / Password (Token)
This method is often used by tool providers because new users can be connected in self-service. The user only needs a username and password and no technical information that may have to be obtained first.

often used with these APIs:
- Silent Sign On
- Vorgaenge-API
- Angebote-API
- Unterlagen-API

This method will only be supported until the end of October 2020. \
**Please change urgently !!!**

Example so far:
``` cURL
curl --location --request POST 'https://api.europace.de/login' \
--header 'Content-Type: application / x-www-form-urlencoded' \
--data-urlencode 'username = [Username]' \
--data-urlencode 'password = [Password]'
```

Example new: \
see “Example new” in “API key (impregnation)” \
or OAuth2 flow with client approval (not available yet)

> ⚠️ **Note** \
Since the username and password are often illegally cached in tools, **this method will no longer be available from the end of October 2020**. The JWT from this method can no longer be used for API calls in the future. It is urgent to switch to OAuth.

## Silent Sign On
In order to enable the seamless integration of Europace in the intranet or CRM system, Europace offers the option of Silent Sign On, i.e. A system can register known Europace users using an API key (master key) and display the Europace interface. This eliminates the step of logging in for the user.

This method will be supported until the end of July 2021.

Example so far: \
Registration of the user with PartnerID and Super API Key: \
see previous example API key (impregnation), then call it with JWT in the browser:
``` html
https://www.europace2.de/partnermanagement/login?redirectTo=/uebersicht&authentication=[JWT]
```

Example new: \
We are currently working on an OpenID Connect solution with which our own user database (Identity Service Provider) can be integrated as an authentication method. This is how Silent Sign On becomes real Single Sign On (SSO).

We will make this procedure available by the end of 2020 at the latest.

# Frequently Asked Questions (FAQ)
#### When does the client approval take place?
Client approval is currently automatic with client registration. So there is currently no client approval flow at Europace.

# Support
If you have problems, questions have not been answered, or special use cases are not listed, please contact us
helpdesk@europace2.de
