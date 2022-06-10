# Authorization API

The Authorization API provides authentication to Europace for APIs. It is a mandatory requirement for using Europace APIs.


![advisors](https://img.shields.io/badge/-advisors-lightblue)
![loan providers](https://img.shields.io/badge/-loanProviders-lightblue)
![mortgage loans](https://img.shields.io/badge/-mortgageLoans-lightblue)
![consumer loans](https://img.shields.io/badge/-consumerLoans-lightblue)

[![authentication](https://img.shields.io/badge/Auth-OAuth2-green)](https://github.com/europace/authorization-api)

[![GitHub release](https://img.shields.io/github/v/release/europace/authorization-api)](https://github.com/europace/authorization-api/releases)
[![Pattern](https://img.shields.io/badge/Pattern-Tolerant%20Reader-yellowgreen)](https://martinfowler.com/bliki/TolerantReader.html)

## Documentation
[![YAML](https://img.shields.io/badge/OAS-HTML_Doc-lightblue)](https://europace.github.io/authorization-api/oas-doc.html)
[![YAML](https://img.shields.io/badge/OAS-YAML-lightgrey)](https://github.com/europace/authorization-api/blob/master/authorization.yaml)

**related articles** 
* [Migrationsguide](https://docs.api.europace.de/common/authentifizierung/oauth-migrationsguide_en).
* HowTo implement [auth-code-flow](https://docs.api.europace.de/common/authentifizierung/oauth-code-flow_en/)

## Usecases
- login user to use europace-apis with his identity

## Quickstart
To test our APIs and your use case as quickly as possible, we've put together a [Postman Collection](https://github.com/europace/api-schnellstart) for you.

## How to use OAuth2?

All Europace APIs are access restricted, i.e. in order to use them a login (authentication) to Europace has to be done first.

Follow these steps:
- you have to register your client once in Europace, whereupon you will receive the `Client_ID` and the `Client-Secret` for the client.
- To log in to Europace, call `https://api.europace.de/auth/token` with the `Client_ID` and the `Client_Secret` as Basic-Auth to get an `access_token`. Most HTTP clients already support OAuth2 and can be configured with these parameters.
- With the `access_token` as a bearer token you can make requests to the Europace APIs.
Request header variable: `Authorization: Bearer [access_token]`

## How to register your client?

<a href="mailto:helpdesk@europace2.de?subject=Registrierung API-Client&body=Hallo,%0D%0Abitte%20registriert%20einen%20API-Client%20für%20mich.%0D%0A%0D%0APartnerID:%0D%0AClient-Name:%0D%0AClient-Beschreibung:%0D%0Atechnische%20Kontakt-Email-Adresse:%0D%0Akurze%20Beschreibung%20des%20Anwendungsfalls:%0D%0Abenötigte%20Scopes:%0D%0A%0D%0AVielen%20Dank">apply client-registration</a>


Please contact <a href="mailto:helpdesk@europace2.de?subject=Registrierung API-Client&body=Hello,%0D%0Please%20register%20an%20API-Client%20for%20me. %0D%0A%0D%0APartnerID:%0D%0AClientName:%0D%0AClientDescription:%0D%0Atechnical%20contact email address:%0D%0Short%20description%20of%20the%20application:%0D%0Required%20Scopes:%0D%0A%0D%0AVever%20Thanks">helpdesk@europace2.de</a> with the following data:
- EP2 PartnerId
- Client name
- Client Description:
- Contact email address for operational queries
- Short description of the use case (goal)
- required scopes

After a short check with the owner (Europace partner) we will register your client immediately and provide you with the client ID and client secret in your personal link list in Europace.

![Linksammlung.png](https://docs.api.europace.de/Linksammlung.png "Linksammlung")

Please note that by using the APIs, you automatically agree to the [Europace API Terms of Use](https://docs.api.europace.de/nutzungsbedingungen/).

## How to get an access-token?
To log in to Europace, call `https://api.europace.de/auth/token` with the `Client_ID` and the `Client_Secret` as Basic-Auth to get an Access_Token.

Request:
```cURL
curl --location --request POST 'https://api.europace.de/auth/token' \
--user '[Client_ID]:[Client_Secret]' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=client_credentials'
```

Response:
```json
{  "access_token": [Access_Token],
   "scope": [verfügbare Scopes],
   "token_type": "Bearer",
   "expires_in": 3600   }
```

In this case, an access token is created in the name and on behalf of the partner to which the client is registered. Further use cases are discussed in "Old world - new world".

In addition to the grant type, the following request parameters are supported:

- ##### Grant-Type (`grant_type`)
  [OAuth2.0 Grant-Type][RFC6749#4], must be `client_credentials` for client credentials flow.
- ##### Scopes (`scope`).
  "` `"-separated list of scopes. If a subject is specified, `impersonate` must be included as a scope.
  Requested scopes are restricted according to the actor's permissions and the client's approval by the actor. It is possible to request restricted access by specifying specific scopes. A scope represents an authorization to perform actions on the platform. If no scopes are requested, the scope results from the scopes stored during client registration. The currently available scopes are maintained in an [Overview](https://github.com/europace/authorization-api/blob/master/docs/scopes.md).
- ##### Actor (`actor`)
  Partner id of the partner on whose behalf the client is acting, there must be a
  client-approval of the actor for the client. Currently the client-approval is granted automatically during registration for the actor and all subjects in the access area of the client.
- ##### Subject (`subject`)
  Partner id of the partner on whose behalf the client acts. The subject must be subordinate to the actor.

## How to call an API with access-token?
With the Access_Token as a Bearer token you can make requests to the Europace APIs.
Request header variable: `Authorization: Bearer [access_token]`

Using the example of the process API in curl:
```cURL
curl --location --request GET 'https://api.europace2.de/v2/vorgaenge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer [access_token]'
```

## How to authenticate different users with one client? (Impersonation)

The imperseded OAuth2 method is used when the API needs the specific user and you don't want to register a client for each user. It is enough to have one client for the organization that acts as a general key and can be used to log in users that the organization has access to.

```cURL
curl --location --request POST 'https://api.europace.de/auth/token' \
--user '[ClientID]:[ClientSecret]' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'scope=impersonieren baufinanzierung:echtgeschaeft baufinanzierung:vorgang:lesen baufinanzierung:ereignis:lesen baufinanzierung:antrag:lesen' \
--data-urlencode 'subject=[to be login PartnerID]' \
--data-urlencode 'actor=[registered PartnerID]'
```

Parameters | Description |
--------- | :--- |
Subject | the PartnerID of the user to be registered
Actor | the partnerID of the registered client<br/><br/>**Note**: The Actor partnerid must be placed above the Subject partnerid in the partner management structure, otherwise the necessary access rights are missing. There can be any number of scopes between the partnerids.
Scope | required scopes of the token<br/><br/>**Note**: The scope `impersonate` must always be included. All specified scopes must be enabled at the client.

## Terms of use
The APIs are made available under the following [Terms of Use](https://docs.api.europace.de/nutzungsbedingungen/).

## Support
If you have any questions or problems, you can contact devsupport@europace2.de.

[JWT]: https://tools.ietf.org/html/rfc7519
[ASCII]: http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-006.pdf
[UTF-8]: https://tools.ietf.org/html/rfc3629
[URI]: https://tools.ietf.org/html/rfc3986
[Unix-Timestamp]: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap04.html#tag_04_16
[RFC6749#4]: https://tools.ietf.org/html/rfc6749#section-4
[RFC6749#4.4]: https://tools.ietf.org/html/rfc6749#section-4.4
[HTTP Basic Auth]: https://tools.ietf.org/html/rfc7617#section-2
