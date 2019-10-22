# Authorization API
*Aktuelle Version: 0.1*

Diese Dokumenation beschreibt den OAuth2 Flow um sich an der Europace Plattform zu autorisieren. Am Token-Enpoint kannst Du einen Token-Request ausführen um ein Access-Token zu erhalten.

⚠️ *ACHTUNG* Diese API befindet sich gerade in der Entwicklung.

# Was ist OAuth2?
OAuth 2.0 is an authorization protocol that gives an API client limited access to user data on a web server. GitHub, Google, and Facebook APIs notably use it. OAuth relies on authentication scenarios called flows, which allow the resource owner (user) to share the protected content from the resource server without sharing their credentials. For that purpose, an OAuth 2.0 server issues access tokens that the client applications can use to access protected resources on behalf of the resource owner. For more information about OAuth 2.0, see oauth.net and RFC 6749.


### Authorization-Flows

#### Client-Credentials Flow

Der Client-Credentials Flow ist der einfachste Flow. Es werden die Client-Credentials direkt gegen ein
[Access-Token](Access-Token.md#access-token) eingetauscht. Die API folgt
[OAuth 2.0 Client Credentials Grant][RFC6749#4.4]. Client-Id und Client-Secret müssen per [HTTP Basic Auth]
übergeben werden.

Client Credentials werden im Partnermanagement angelegt (TODO).

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
  [Client-Approval](Client-Approval.md#client-approval) durch den Akteur eingeschränkt.
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

#### Refresh-Token Flow
TODO

#### Authorization-Code Flow
TODO

[JWT]: https://tools.ietf.org/html/rfc7519
[ASCII]: http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-006.pdf
[UTF-8]: https://tools.ietf.org/html/rfc3629
[URI]: https://tools.ietf.org/html/rfc3986
[Unix-Timestamp]: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap04.html#tag_04_16
[RFC6749#4]: https://tools.ietf.org/html/rfc6749#section-4
[RFC6749#4.4]: https://tools.ietf.org/html/rfc6749#section-4.4
[HTTP Basic Auth]: https://tools.ietf.org/html/rfc7617#section-2
