# Authorization API

Die Authorization-API stellt die Authentifizierung bei Europace für APIs zur Verfügung. Sie ist eine zwingende Voraussetzung zur Verwendung von Europace APIs.


![Vertrieb](https://img.shields.io/badge/-Vertrieb-lightblue)
![Produktanbieter](https://img.shields.io/badge/-Produktanbieter-lightblue)
![Baufinanzierung](https://img.shields.io/badge/-Baufinanzierung-lightblue)
![Privatkredit](https://img.shields.io/badge/-Privatkredit-lightblue)

[![Authentication](https://img.shields.io/badge/Auth-OAuth2-green)](https://github.com/europace/authorization-api)

[![GitHub release](https://img.shields.io/github/v/release/europace/authorization-api)](https://github.com/europace/authorization-api/releases)
[![Pattern](https://img.shields.io/badge/Pattern-Tolerant%20Reader-yellowgreen)](https://martinfowler.com/bliki/TolerantReader.html)

## Dokumentation
[![YAML](https://img.shields.io/badge/OAS-HTML_Doc-lightblue)](https://europace.github.io/authorization-api/oas-doc.html)
[![YAML](https://img.shields.io/badge/OAS-YAML-lightgrey)](https://github.com/europace/authorization-api/blob/master/authorization.yaml)

**Migrationsguide** \
Als Unterstützung für den Wechsel von den bisherigen Authentifizierungsverfahre auf OAuth2 gibt es diesen [Migrationsguide](https://docs.api.europace.de/baufinanzierung/authentifizierung/oauth-migrationsguide) ([english version](https://docs.api.europace.de/baufinanzierung/authentifizierung/oauth-migrationsguide_en)).

## Anwendungsfälle
- Benutzer anmelden, um Europace-APIs zu verwenden

## Schnellstart
Damit du unsere APIs und deinen Anwendungsfall schnellstmöglich testen kannst, haben wir eine [Postman-Collection](https://github.com/europace/api-schnellstart) für dich zusammengestellt.

## Wie benutze ich OAuth2?

Alle Europace-APIs sind zugangsbeschränkt, d.h. um sie verwenden zu können muss zuvor eine Anmeldung (Authentifizierung) bei Europace erfolgen.

Dabei müssen folgende Schritte durchlaufen werden:
- Einmalig musst du deinen Client in Europace registrieren lassen, woraufhin du die `Client_ID` und das `Client-Secret` für den Client erhältst
- Für die Anmeldung an Europace rufst du `https://api.europace.de/auth/token` mit der `Client_ID` und dem `Client_Secret` als Basic-Auth auf, um einen `Access_Token` zu erhalten. Die meisten HTTP Clients unterstützen OAuth2 bereits und lassen sich mit diesen Parametern konfigurieren.
- Mit dem `Access_Token` als Bearer-Token kannst du Requests an den Europace APIs durchführen.
Request-Header-Variable:  `Authorization: Bearer [Access_Token]`

## Wie bekomme ich einen Client registriert?

<a href="mailto:helpdesk@europace2.de?subject=Registrierung API-Client&body=Hallo,%0D%0Abitte%20registriert%20einen%20API-Client%20für%20mich.%0D%0A%0D%0APartnerID:%0D%0AClient-Name:%0D%0AClient-Beschreibung:%0D%0Atechnische%20Kontakt-Email-Adresse:%0D%0Akurze%20Beschreibung%20des%20Anwendungsfalls:%0D%0Abenötigte%20Scopes:%0D%0A%0D%0AVielen%20Dank">zur Client-Registrierung</a>


Bitte wende dich an <a href="mailto:helpdesk@europace2.de?subject=Registrierung API-Client&body=Hallo,%0D%0Abitte%20registriert%20einen%20API-Client%20für%20mich.%0D%0A%0D%0APartnerID:%0D%0AClient-Name:%0D%0AClient-Beschreibung:%0D%0Atechnische%20Kontakt-Email-Adresse:%0D%0Akurze%20Beschreibung%20des%20Anwendungsfalls:%0D%0Abenötigte%20Scopes:%0D%0A%0D%0AVielen%20Dank">helpdesk@europace.de</a> mit folgenden Daten:
- EP2-PartnerId
- Client-Name
- Client-Beschreibung:
- Kontakt-Email-Adresse für betriebliche Rückfragen
- Kurze Beschreibung des Anwendungsfalls (Ziel)
- benötigte Scopes

Nach einer kurzen Prüfung beim Eigentümer (Europace Partner) registrieren wir dir deinen Client umgehend und stellen dir die Client-ID und das Client-Secret in deiner persönlichen Linkliste in Europace zur Verfügung.

![Linksammlung.png](https://raw.githubusercontent.com/europace/authorization-api/master/docs/img/Linksammlung.png "Linksammlung")

Bitte beachte, dass du dich mit der Benutzung der APIs automatisch mit den [Europace API-Nutzungsbedingungen](https://docs.api.europace.de/nutzungsbedingungen/) einverstanden erklärst.

## Wie bekomme ich einen Access-Token?
Für die Anmeldung an Europace rufst du `https://api.europace.de/auth/token` mit der `Client_ID` und dem `Client_Secret` als Basic-Auth auf, um einen Access_Token zu erhalten.

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

In diesem Fall wird ein Access-Token im Namen und im Auftrag des Partners erstellt an dem der Client registriert ist. Weitere Anwendungsfälle werden in “Alte Welt - neue Welt” behandelt.

Neben dem Grant-Type werden folgende Request-Parameter unterstützt:

- ##### Grant-Type (`grant_type`)
  [OAuth2.0 Grant-Type][RFC6749#4], muss für den Client-Credentials-Flow `client_credentials` sein.
- ##### Scopes (`scope`)
  "` `"-separierte Liste von Scopes. Wird ein Subject angegeben muss `impersonieren` als Scope enthalten sein.
  Angefragte Scopes werden entsprechend der Rechte des Akteurs und dem Client-Approval durch den Akteur eingeschränkt. Es ist möglich einen eingeschränkten Zugriff anzufragen, in dem man spezifische Scopes angibt. Ein Scope stellt eine Berechtigung zum Ausführen von Aktionen auf der Plattform dar. Werden keine Scopes angefragt ergibt sich der Scope aus den bei der Client-Registrierung hinterlegten Scopes. Die aktuell verfügbaren Scopes werden in einer [Übersicht](https://github.com/europace/authorization-api/blob/master/docs/scopes.md) gepflegt.
- ##### Akteur (`actor`)
  Partner-Id des Partners in dessen Auftrag der Client agiert, es muss ein
  Client-Approval des Akteurs für den Client vorliegen. Aktuell wird der Client-Approval automatisch bei der Registrierung für den Aktuer und alle Subjects im Zugriffsbereich des Clients erteilt .
- ##### Subject (`subject`)
  Partner-Id des Partners in dessen Namen der Client agiert. Das Subject muss dem Akteur untergeordnet sein.

## Wie rufe ich eine API mit Access-Token auf?
Mit dem Access_Token als Bearer-Token kannst du Requests an den Europace APIs durchführen.
Request-Header-Variable:  `Authorization: Bearer [Access_Token]`

Am Beispiel der Vorgaenge-API in curl:
```cURL
curl --location --request GET 'https://api.europace2.de/v2/vorgaenge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer [Access_Token]
```

## Wie authentifiziere ich verschiedene Benutzer mit einem Client? (Impersionieren)

Das impersionierte OAuth2-Verfahren wird dann verwendet, wenn die API den konkreten Benutzer benötigt und man nicht für jeden Benutzer einen Client registrieren möchte. Es reicht einen Client für die Organisation zu haben, der als Generalsschlüssel fungiert und mit dem Benutzer, auf die die Organisation Zugriff hat, angemeldet werden können.

```cURL
curl --location --request POST 'https://api.europace.de/auth/token' \
--user '[ClientID]:[ClientSecret]' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'scope=impersonieren baufinanzierung:echtgeschaeft baufinanzierung:vorgang:lesen baufinanzierung:ereignis:lesen baufinanzierung:antrag:lesen' \
--data-urlencode 'subject=[anzumeldende PartnerID]' \
--data-urlencode 'actor=[registrierte PartnerID]'
```


Parameter | Beschreibung |
--------- | :--- |
Subject   | die PartnerID des anzumeldenden Benutzers
Actor     | die PartnerID des registrierten Clients<br/><br/>**Hinweis**: Die Actor-Partnerid muss in der Partnermanagementstruktur über der Subject-Partnerid angeordnet sein, da sonst die notwendigen Zugriffsrechte fehlen. Es können beliebig viele Ebenen zwischen den Partnerids liegen.
Scope     | benötigten Scopes des Tokens<br/><br/>**Hinweis**: Der Scope `impersonieren` muss immer enthalten sein. Alle angegebenen Scopes müssen beim Client aktiviert sein.

## Nutzungsbedingungen
Die APIs werden unter folgenden [Nutzungsbedingungen](https://docs.api.europace.de/nutzungsbedingungen/) zur Verfügung gestellt.

## Support
Bei Fragen oder Problemen kannst du dich an devsupport@europace2.de wenden.

[JWT]: https://tools.ietf.org/html/rfc7519
[ASCII]: http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-006.pdf
[UTF-8]: https://tools.ietf.org/html/rfc3629
[URI]: https://tools.ietf.org/html/rfc3986
[Unix-Timestamp]: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap04.html#tag_04_16
[RFC6749#4]: https://tools.ietf.org/html/rfc6749#section-4
[RFC6749#4.4]: https://tools.ietf.org/html/rfc6749#section-4.4
[HTTP Basic Auth]: https://tools.ietf.org/html/rfc7617#section-2
