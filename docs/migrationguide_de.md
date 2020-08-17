# OAuth Migrations-Guide

Alles was du brauchst, um auf
OAuth zu wechseln.

## Einleitung
Sicherheit ist einer der wichtigsten nicht-funktionalen Anforderungen an eine Plattform wie Europace, die Finanzdaten von Verbrauchern verwendet. Wir nehmen diese Verantwortung sehr ernst. Und gleichzeitig glauben wir daran, dass eine technische Anbindung an die Europace-Technologie leichtgewichtig und schnell passieren kann.

Deshalb räumen wir mit den bislang proprietären Authentifizierungsverfahren auf und führen OAuth2 als Standard-Technologie für Europace ein. Dieses Verfahren ist weit verbreitet - fast jeder Software-Entwickler hat damit schon einmal gearbeitet. Durch diese Bekanntheit und Einfachheit werden der Entwicklungsaufwand bei der Anbindung reduziert und die Nerven der Entwickler geschont.

Wir erhöhen damit die Sicherheit, indem API-Keys noch einfacher erneuert werden können und der Zugriff auf die Europace-Technologie noch nachvollziehbarer wird.

Außerdem ermöglichen wir mit OAuth2 zukünftig echtes Single Sign On über die Einbindung eigener Benutzerdatenbanken für das Anmeldeverfahren. Zudem können Toolhersteller ihre Anwendungen nach Rücksprache mit den Europace-Partnern noch einfacher für alle im Self-Service einbinden, ohne Benutzername und Passwort zu kennen.

Wir sind davon überzeugt, die Einführung von OAuth bei Europace ist ein entscheidender Basis-Baustein für unsere Partner und uns, um die  Digitalisierung der Baufinanzierung voranzutreiben.

## Bis wann muss die Migration erfolgen?
Alle aktuellen APIs (Stand Juli 2020) werden noch bis Ende Juli 2021 die alten Authentifizierungsverfahren auf Basis von API-Key unterstützen.

Die Authentifizierung durch Username/Password an den APIs wird bis Ende Oktober 2020 abgeschaltet. Wenn du dieses Verfahren einsetzt, musst du schnellstmöglich auf OAuth wechseln, um die Funktionsfähigkeit deiner Integration sicherzustellen!

## Wie benutze ich OAuth?
Alle Europace-APIs sind zugangsbeschränkt, d.h. um sie verwenden zu können muss zuvor eine Anmeldung (Authentifizierung) bei Europace erfolgen.

Dabei müssen folgende Schritte durchlaufen werden:
- Einmalig musst du deinen Client in Europace registrieren lassen woraufhin du die Client_ID und das Secret für den Client erhältst
- Für die Anmeldung an Europace rufst du https://api.europace.de/auth/token mit der `Client_ID` und dem `Client_Secret` als Basic-Auth auf, um einen `Access_Token` zu erhalten.
- Mit dem `Access_Token` als Bearer-Token kannst du Requests an den Europace APIs durchführen.
Request-Header-Variable:  `Authorization: Bearer [Access_Token]

Die meisten HTTP Clients unterstützen OAuth2 bereits, lediglich Client_ID, Client_Secret sowie die Adresse des Authorization Servers musst du in der Config hinterlegen.

#### Wie bekomme ich einen Client registriert?

<a href="mailto:helpdesk@europace2.de?subject=Registrierung API-Client&body=Hallo,%0D%0Abitte%20registriert%20einen%20API-Client%20für%20mich.%0D%0A%0D%0APartnerID:%0D%0AClient-Name:%0D%0AClient-Beschreibung:%0D%0Atechnische%20Kontakt-Email-Adresse:%0D%0Akurze%20Beschreibung%20des%20Anwendungsfalls:%0D%0Abenötigte%20Scopes:%0D%0A%0D%0AVielen%20Dank">zur Client-Registrierung</a>


Bitte wende dich an <a href="mailto:helpdesk@europace2.de?subject=Registrierung API-Client&body=Hallo,%0D%0Abitte%20registriert%20einen%20API-Client%20für%20mich.%0D%0A%0D%0APartnerID:%0D%0AClient-Name:%0D%0AClient-Beschreibung:%0D%0Atechnische%20Kontakt-Email-Adresse:%0D%0Akurze%20Beschreibung%20des%20Anwendungsfalls:%0D%0Abenötigte%20Scopes:%0D%0A%0D%0AVielen%20Dank">helpdesk@europace.de</a> mit folgenden Daten:
- EP2-PartnerId
- Client-Name
- Client-Beschreibung:
- Kontakt-Email-Adresse für betriebliche Rückfragen
- Kurze Beschreibung des Anwendungsfalls (Ziel)
- benötigte Scopes

Nach einer kurzen Prüfung beim Eigentümer (Europace Partner) registrieren wir dir deinen Client umgehend und stellen dir die Client-ID und das Client-Secret in deiner persönlichen Linkliste in Europace zur Verfügung.

Bitte beachte, dass du dich mit der Benutzung der APIs automatisch mit den [Europace API-Nutzungsbedingungen](https://developer.europace.de/terms/) einverstanden erklärst.

#### Wie bekomme ich einen Access-Token?
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

#### Wie rufe ich eine API mit Access-Token auf?
Mit dem Access_Token als Bearer-Token kannst du Requests an den Europace APIs durchführen.
Request-Header-Variable:  `Authorization: Bearer [Access_Token]`

Am Beispiel der Vorgaenge-API in curl:
```cURL
curl --location --request GET 'https://api.europace2.de/v2/vorgaenge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer [Access_Token]
```

## Alte Welt - neue Welt
Bislang standen dir verschiedene Authentifizierungsverfahren zur Verfügung. In diesem Abschnitt zeigen wir dir, wie du am Besten in den unterschiedlichen Anwendungsfällen auf OAuth wechselst und so von der Vereinfachung und Standardisierung des OAuth-Authentifizierungsverfahrens profitierst.

### API-Key
Damit du keine Passworte von Benutzern speichern und verwenden musst, werden für den Zugriff auf Schnittstellen API-Keys verwendet. Mit großer Wahrscheinlichkeit hast auch du diese Methode für deine Anbindung verwendet.

häufig genutzt bei diesen APIs:
- Vorgaenge-API
- Antraege-API
- Reporting-API

Dieses Verfahren wird noch bis Ende Juli 2021 unterstützt.

Beispiel bisher:
```cURL
curl --location --request POST 'https://api.europace.de/login' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'username=[PartnerID] \
--data-urlencode 'password=[API-Key]'
```

Beispiel neu: \
siehe “Wie bekomme ich einen Access-Token?”

### API-Key (Impersionieren)
Das impersionierte API-Key-Verfahren wird dann verwendet, wenn die API den konkreten Benutzer benötigt und man nicht für jeden einen API-Key anfordern möchte. Es reicht einen API-Key einer Organisation zu besitzen, der als Generalsschlüssel fungiert und mit dem Benutzer, auf die die Organisation Zugriff hat, angemeldet werden können.

häufig genutzt bei diesen APIs:
- Silent Sign On
- Angebote-API
- Unterlagen-API

Dieses Verfahren wird noch bis Ende Juli 2021 unterstützt.

Beispiel bisher:
```cURL
curl --location --request POST 'https://www.europace2.de/partnermanagement/login.api' \
--header 'x-partnerid: [anzumeldende PartnerID]' \
--header 'x-apikey: [Super API-Key]'
```

mit x-partnerid des anzumeldenden Benutzers und `x-apikey` des Partners (mit weitreichenden Zugriffsrechten (Generalschlüssel)). Der `x-apikey` muss in der Partnermanagement-Struktur über der `x-partnerid` angeordnet sein, da sonst die notwendigen Zugriffsrechte fehlen.

Beispiel neu:
```cURL
curl --location --request POST 'https://api.europace.de/auth/token' \
--user '[ClientID]:[ClientSecret]' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'scope=impersonieren baufinanzierung:echtgeschaeft baufinanzierung:vorgang:lesen baufinanzierung:ereignis:lesen baufinanzierung:antrag:lesen' \
--data-urlencode 'subject=[anzumeldende PartnerID]' \
--data-urlencode 'actor=[registrierte PartnerID]'
```

 Parameter | Beschreibung
--- | ---  
Subject |	die Partnerid des anzumeldenden Benutzers |
Actor 	|	die Partnerid des registrierten Clients |
Hinweis | die Actor-Partnerid muss in der Partnermanagementstruktur über der Subject-Partnerid angeordnet sein, da sonst die notwendigen Zugriffsrechte fehlen. |
Scope |	muss impersonieren enthalten (Hinweis: Wenn ein Scope angegeben wird, müssen alle erforderlichen Rechte angegeben werden, d.h. impersonieren allein macht keinen Sinn.) |

>⚠️ *Hinweis* \
Für den Anwendungsfalls des Silent Sign On werden wir demnächst das Single Sign On über OpenID-Connect anbieten, mit dem du deine eigene Benutzerdatenbank als Identity Service Provider an Europace anbinden kannst. Das Silent Sign On Verfahren werden wir nicht länger unterstützen.

### Username/Password (Cookie)
Diese Methode wird meistens verwendet, wenn du die angebotene Login-Maske von Europace oder eine eigene Loginmaske auf deiner Website/Intranet eingebunden hast.

Beispiel bisher:
```cURL
curl --location --request POST 'https://www.europace2.de/partnermanagement/login.do' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'username=[Username]' \
--data-urlencode 'password=[Password]'
```

Hier musst du erst einmal nichts tun.

>⚠️ **Hinweis** \
Das JWT, dass im Cookie gespeichert wird, kann zukünftig nicht mehr für API-Aufrufe verwendet werden. Wenn du diesen Anwendungsfall hast, dann wechsle **bis Ende Oktober 2020 auf OAuth.**

### Username/Password (Token)
Diese Methode wird häufig von Toolanbietern verwendet, weil die Anbindung neuer Benutzer im Self-Service erfolgen kann. Der Benutzer benötigt nur Username und Password und keine technischen Informationen, die ggf. erst besorgt werden müssen.

häufig genutzt bei diesen APIs:
- Silent Sign On
- Vorgaenge-API
- Angebote-API
- Unterlagen-API

Dieses Verfahren wird nur noch bis Ende Oktober 2020 unterstützt. \
**Bitte dringend wechseln!!!**

Beispiel bisher:
```cURL
curl --location --request POST 'https://api.europace.de/login' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'username=[Username]' \
--data-urlencode 'password=[Password]'
```

Beispiel neu: \
siehe “Beispiel neu” in “API-Key (Impersionieren)” \
oder OAuth-Flow mit Client-Approval

>⚠️ **Hinweis** \
Da hier Benutzername und Password oft in Tools unerlaubterweise zwischengespeichert werden, **wird diese Methode ab Ende Oktober 2020 nicht mehr zur Verfügung stehen**. Das JWT aus dieser Methode kann zukünftig nicht mehr für API-Aufrufe verwendet werden. Es ist dringend auf OAuth zu wechseln.

### Silent Sign On
Um die Einbindung von Europace in Intranet oder CRM-System nahtlos zu ermöglichen, bietet Europace die Möglichkeit des Silent Sign On, d.h. ein System kann ihm bekannte Europace-Benutzer mittels API-Key (Generalschlüssel) anmelden und die Oberfläche von Europace anzeigen. Damit entfällt der Schritt der Anmeldung für den Benutzer.

Dieses Verfahren wird noch bis Ende Juli 2021 unterstützt.

Beispiel bisher: \
Anmeldung des Benutzers mit PartnerID und Super-API-Key: \
siehe bisheriges Beispiel API-Key (Impersionieren), dann mit JWT im Browser aufrufen:
```html
https://www.europace2.de/partnermanagement/login?redirectTo=/uebersicht&authentication=[JWT]
```

Beispiel neu: \
Wir arbeiten gerade an einer OpenID Connect Lösung, mit der die eigene Benutzerdatenbank (Identity Service Provider) als Authentifizierungsverfahren eingebunden werden kann.  So wird aus Silent Sign On echtes Single Sign On (SSO).

Dieses Verfahren werden wir bis spätestens Ende 2020 zur Verfügung stellen.

# Frequently Asked Questions (FAQ)
#### Wann findet das Client-Approval statt?
Das Client-Approval ist aktuell automatisch mit Client-Registrierung erfolgt. Es gibt also aktuell kein Client-Approval-Flow bei Europace.

# Support
Wenn Probleme auftreten, Fragen nicht beantwortet wurden oder spezielle Anwendungsfälle nicht aufgeführt sind, wende dich gern an
helpdesk@europace2.de
