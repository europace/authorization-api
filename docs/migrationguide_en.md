# OAuth2 migration guide

Everything you need to switch to OAuth2-based authorization.

## Introduction
Security is one of the most important non-functional requirements of a platform like Europace which handles consumers' financial data. We take this responsibility very seriously. At the same time we believe that a  Europace API implementation can be achieved easily and quickly.

That is why we are moving away from the previous authentication method and introducing OAuth2 as the standard protocol for Europace. This protocol is widespread - almost every software developer has worked with it at some point. Because of this development effort for the implementation is minimised.

We are thereby increasing security by making it  easier to create and renew API credentials and making access to Europace APIs simpler.

With OAuth2 we will also enable real single sign-on in the future by integrating our own identity provider. In addition, after consultation with Europace partners, developers can integrate their applications into our platform more easily for everyone without knowing a username and password.

We are convinced that the introduction of OAuth2 is a crucial building block for us and our partners in order to drive the digitization of mortgage lending forward.

## Timelines for migration?
All current APIs (as of July 2020) will support the old authentication method based on API keys until the end of July 2021.

Authentication by username / password for APIs will be switched off at the end of October 2020. If you use this procedure, you have to switch to OAuth2 as soon as possible to ensure the functionality of your application!

# How to use OAuth2?
All Europace APIs are restricted, Which means to use our APIs you must login (authenticate) to Europace.

The following steps must be followed:
- Initially you have to register your client. As a result you will receive the `Client_ID` and the` Client-Secret` for the client
- To log in to Europace, call https://api.europace.de/auth/token with the `Client_ID` and the` Client_Secret` as Basic-Auth in order to receive an `Access_Token`.
- With the `Access_Token` as a bearer token you can make requests to the Europace APIs.
Request header variable: `Authorization: Bearer [Access_Token]`

Most HTTP clients already support OAuth2, you only have to store `Client_ID`, `Client_Secret` and the address of the authorization server in the config.

## How do I register a client?

Please contact <a href="mailto:helpdesk@europace2.de?subject=Register API-client&body=Hello,%0D%0Apls%20register%20a%20new%20API-Client%20for%20me.%0D%0A%0D%0APartnerID:%0D%0AClient-Name:%0D%0AClient-Description:%0D%0Atechnical%20contact-email-adress:%0D%0Ashort%20description%20of%20the%20Usecase:%0D%0Arequired%20scopes:%0D%0A%0D%0AThank%20you">helpdesk@europace.de</a> with the following data:
- EP2 partner id
- Client name
- Client description
- Contact email address for operational queries
- Brief description of the use case for your client
- required scopes

After a short review with the owner (Europace partner), we will register your client and provide you with the client ID and the client secret in your personal link list in Europace.

![Linksammlung.png](https://raw.githubusercontent.com/europace/authorization-api/master/docs/img/Linksammlung.png "Linkammlung")

Please note you agree to the [Europace API Terms of Use](https://docs.api.europace.de/nutzungsbedingungen/) by using the APIs.

## How do I get an access token?
To log into Europace, call `https://api.europace.de/auth/token` with the` Client_ID` and the `Client_Secret` as Basic-Auth to get an Access_Token.

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
Up till now, various authentication methods have been available to you. In this section we will show you the best way to switch to OAuth2 depending on the use case thereby benefitting from the simplification and standardization of the OAuth2 authentication process.

## API key
It is very likely that you also used this method for your implementation.

often used with these APIs:
- Vorgaenge-API
- Antraege-API
- Reporting-API

This method will be supported until the end of July 2021.

Legacy example:
```` cURL
curl --location --request POST 'https://api.europace.de/login' \
--header 'Content-Type: application / x-www-form-urlencoded' \
--data-urlencode 'username = [PartnerID] \
--data-urlencode 'password = [API key]'
````

New example: \
see “How do I get an access token?”

## API key (impersonation)
The impersonated API key procedure is used when you want to act as a specific user but don't want to request an individual API key for everyone in your organization. It is sufficient to have an organization's API key which acts as a master key and with which users in the organization can be logged in.

often used with these APIs:
- Silent Sign On
- Angebote-API
- Unterlagen-API

This method will be supported until the end of July 2021.

Legacy Example:
``` cURL
curl --location --request POST 'https://www.europace2.de/partnermanagement/login.api' \
--header 'x-partnerid: [PartnerID to be registered]' \
--header 'x-apikey: [Super API-Key]'
```

where `x-partnerid` is the partner ID of the user to be logged in and `x-apikey` is the master API key. The `x-apikey` Partner must be located   above the `x-partnerid` in the partner-management hierarchy, otherwise the necessary access rights are missing.

New example:
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
Subject | the partner ID of the user to be logged in |
Actor | the partner ID of the registered client |
Note | The actor partner ID must be located  above subject in the partner-management hierarchy, otherwise the necessary access rights are missing. |
Scope | must contain 'impersonieren' (Note: If a scope is specified, all required rights must be specified, i.e. impersonating scope alone does not make sense.) |

> ⚠️ **Note** \
For the use case of Silent Sign On, we will soon be offering Single Sign On via OpenID-Connect, with which you can connect your own user database to Europace as an Identity Provider. We will no longer support the current **Silent** Sign On procedure.

## Username / Password (Cookie)
This method is mostly used if you have integrated the Europace login dialog or your own login dialog on your website / intranet.

Legacy example:
``` cURL
curl --location --request POST 'https://www.europace2.de/partnermanagement/login.do' \
--header 'Content-Type: application / x-www-form-urlencoded' \
--data-urlencode 'username = [Username]' \
--data-urlencode 'password = [Password]'
```

You don't have to do anything here.

> ⚠️ **Note** \
The JWT that is stored in the cookie can no longer be used for API calls in the future. If you have this use case, switch to OAuth **by the end of October 2020.**

## Silent Sign On
In order to enable the seamless integration of Europace in an intranet or CRM system, Europace offers Silent Sign On, i.e. A system can register known Europace users using an API key (master key) and then redirect to the Europace interface. This eliminates the step of logging in for the user.

This method will be supported until the end of July 2021.

Legacy example: \
Registration of the user with PartnerID and master API Key: \
see previous example API key (impregnation), then call it with JWT in the browser:
``` html
https://www.europace2.de/partnermanagement/login?redirectTo=/uebersicht&authentication=[JWT]
```

New example: \
We are currently working on an OpenID Connect solution with which our own user database (Identity Service Provider) can be integrated as an authentication method. This is how Silent Sign On becomes real Single Sign On (SSO).

We will make this procedure available by the end of 2020 at the latest.

# Frequently Asked Questions (FAQ)
#### When does OAuth client approval take place?
Client approval is currently automatic with client registration. There is currently no client approval flow at Europace.

# Support
If you have problems, questions which have not been answered, or special use cases that are not listed, please contact us
helpdesk@europace2.de
