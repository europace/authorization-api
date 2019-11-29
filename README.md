# Authorization API
*Aktuelle Version: 0.1* ⚠️ *ACHTUNG* Diese API befindet sich gerade in der Entwicklung.


## Grundlegendes
Um die Europace Plattform zu nutzen brauchst du einen registrierten Client. Die Registrierung muss von einem Admin im Partnermanagement durchgeführt werden.

Clients agieren im Namen von Nutzern oder Organisationen, die im Partnermanagement hinterlegt sind. Ein registrierter Client wird durch eine `Client ID` und einem `Client Secret` identifiziert: beide werden bei der Registrierung generiert.

## Vergleich zur Vergangenheit
In der Vergangenheit benötigte man eine `Partner ID` und einen `API Key` um die Europace APIs zu nutzen. Jeder Europace Nutzer hatte automatisch einen API Zugang und konnte die APIs nutzen, vorausgesetzt `Parnter ID`und `API Key` warum ihm bekannt. Damals erfolgte der API Zugriff immer *im Namen des Nutzers*. Dieses ist nun nicht mehr so: der API Zugriff erfolgt nun im Namen eines Clients. Es können beliebig viele Clients an einem Client registriert werden.


## OAuth2
Diese Dokumenation beschreibt den OAuth2 Flow um sich an der Europace Plattform zu autorisieren. Um eine API zu verwenden müssen folgende Schritte durchlaufen werden:
1. Den Client einmalig registrieren.
2. Mit der `Client ID` und dem `Client Secret` kannst du am Token-Endpoint einen einen Token-Request ausführen um ein Access-Token zu erhalten.
3. Mit dem Access-Token kannst du Requests an den Europace REST APIs durchführen.


Bei OAuth handelt es sich um ein offenes Sicherheitsprotokoll für die tokenbasierte Autorisierung und Authentifizierung im Internet. Der Prozess zum Erhalt eines Tokens nennt sich Flow. Für mehr Information zu OAuth 2.0 siehe [oauth.net](https://oauth.net).


### Authorization-Flows
Von den 4 Authorization-Flows die OAuth2 spezifiziert wird aktuell nur der *Client-Credentials Flow* unterstützt.

Der Client-Credentials Flow ist der einfachste Flow. Es werden die Client-Credentials direkt gegen ein
Access-Token eingetauscht. Die API folgt [OAuth 2.0 Client Credentials Grant][RFC6749#4.4]. Client-Id und Client-Secret müssen per [HTTP Basic Auth]
übergeben werden.


Im einfachsten Fall genügt der Grant-Type als Parameter:

```http
POST /access-token HTTP/1.1
Host: api.europace.de
Authorization: Basic VVNRNEtNWTRZSFZBWE1YRDo0SmpDS3hRNVV6SVFNZDNoU2tWMEpCYjA=
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
```

oder als cURL-Aufruf:

```bash
curl "https://api.europace.de/access-token" \
  -u USQ4KMY4YHVAXMXD:4JjCKxQ5UzIQMd3hSkV0JBb0 \
  -F grant_type=client_credentials
```

In diesem Fall wird ein Access-Token im Namen und im Auftrag des Partners erstellt an dem der Client
[registriert](Client-Registrierung.md#client-registrierung) ist. Werden keine Scopes angfragt ergibt sich der
Scope aus den bei der Client-Registrierung hinterlegten Scopes.

Neben zum Grant-Type werden folgende Request-Parameter unterstützt:

- ##### Grant-Type (`grant_type`)
  [OAuth2.0 Grant-Type][RFC6749#4], muss für den Client-Credentials-Flow `client_credentials` sein.

  - ##### Scopes (`scope`)
  "` `"-separierte Liste von Scopes. Wird ein Subject angegeben muss `impersonierung` als Scope enthalten sein.
  Angefragte Scopes werden entsprechend der Rechte des Akteurs und dem
  Client-Approval durch den Akteur eingeschränkt. Aktuell wird der Client-Approvall automatisch bei der Registrierung erteilt.
- ##### Akteur (`actor`)
  Partner-Id des Partners in dessen Auftrag der Client agiert, es muss ein
  [Client-Approval](Client-Approval.md#client-approval) des Akteurs für den Client vorliegen.
- ##### Subject (`subject`)
  Partner-Id des Partners in dessen Namen der Client agiert. Das Subject muss dem Akteur untergeordnet sein.

Beispiel Response:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "access_token":"[...opaque ASCII string...]",
    "token_type":"bearer",
    "expires_in":3600,
    "scope": "granted scopes"
}
```


[JWT]: https://tools.ietf.org/html/rfc7519
[ASCII]: http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-006.pdf
[UTF-8]: https://tools.ietf.org/html/rfc3629
[URI]: https://tools.ietf.org/html/rfc3986
[Unix-Timestamp]: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap04.html#tag_04_16
[RFC6749#4]: https://tools.ietf.org/html/rfc6749#section-4
[RFC6749#4.4]: https://tools.ietf.org/html/rfc6749#section-4.4
[HTTP Basic Auth]: https://tools.ietf.org/html/rfc7617#section-2
