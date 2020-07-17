# Scopes für OAuth Clients bei Europace

Mit Hilfe der Scopes kannst du genau angeben, welche Art von Zugriff du benötigst. Scopes beschränken den Zugriff mittels OAuth-Token. Sie gewähren keine zusätzlichen Berechtigungen über die Rechte des Nutzers hinaus.

## Verfügbare Scopes

Die nachfolgende Tabelle stellt eine Liste, der aktuell verfügbaren Scopes dar.

| Name | Beschreibung  |
| --- | ---  |
| ` partner:plakette:anlegen ` |   Darf neue Plaketten anlegen.  |
| ` partner:plakette:loeschen ` |   Darf Plaketten löschen  |
| ` partner:plakette:lesen ` |   Darf Partner-Daten lesen  |
| ` partner:plakette:schreiben ` |   Darf Partner-Daten schreiben  |
| ` partner:beziehungen:lesen ` |   Darf Beziehungen zwischen Partnern lesen Erlaubt es unter anderem UebernahmeRecht, Administrierbare und Uebernehmbare abzurufen  |
| ` partner:beziehungen:schreiben ` |   Darf Beziehungen zwischen Partnern schreiben Erlaubt es unter anderem UebernahmeRecht, Administrierbare und Uebernehmbare zu schreiben  |
| ` partner:rechte:lesen ` |   Darf Rechte eines Partners lesen  |
| ` partner:rechte:schreiben ` |   Darf Rechte eines Partners schreiben  |
| ` reporting:rohdaten:lesen ` |   Darf den Rohdaten-Report runterladen  |
| ` reporting:produktanbieterreport:lesen ` |   Darf den Produktanbieter-Report runterladen  |
| ` baufinanzierung:echtgeschaeft ` |   Baufinanzierung-Echtgeschäft bearbeiten  |
| ` baufinanzierung:vorgang:lesen ` |   Baufinanzierungsvorgänge lesen  |
| ` baufinanzierung:vorgang:schreiben ` |   Baufinanzierungsvorgänge schreiben  |
| ` baufinanzierung:angebot:ermitteln ` |   Baufinanzierungsangebote ermitteln  |
| ` baufinanzierung:ereignis:lesen ` |   Baufinanzierungsereignisse lesen  |
| ` baufinanzierung:antrag:lesen ` |   Baufinanzierungsanträge lesen  |
| ` baufinanzierung:antrag:schreiben ` |   Baufinanzierungsanträge schreiben  |
| ` baufinanzierung:produktkonfiguration:lesen ` |   Produktkonfiguration lesen  |
| ` baufinanzierung:produktkonfiguration:schreiben ` |   Produktkonfiguration schreiben  |
| ` baufinanzierung:produktkonfiguration:freigeben ` |   Produktkonfiguration freigeben  |
| ` baufinanzierung:produkt:lesen ` |   Produkt lesen  |
| ` baufinanzierung:produkt:schreiben ` |   Produkt schreiben  |
| ` baufinanzierung:produktanbieter:lesen ` |   Produktanbieter lesen  |
| ` baufinanzierung:produktanbieter:schreiben ` |   Produktanbieter schreiben  |
| ` privatkredit:angebot:ermitteln ` |   Kreditsmartangebote ermitteln  |
| ` privatkredit:antrag:schreiben ` |   Kreditsmartanträge schreiben  |
| ` privatkredit:vorgang:lesen ` |   Kreditsmartvorgänge lesen  |
| ` privatkredit:vorgang:schreiben ` |   Kreditsmartvorgänge schreiben  |
| ` impersonieren ` |   Darf Impersonieren Eine Aktion wird im Namen eines Partners ausgeführt wobei die Autorisierung des Clients durch einen übergeordneten Partner erfolgt.  |
| ` openid ` |   Benutzer-Login durchführen Der Client kann das Login des Benutzers auf der Plattform mittels OpenID Connect anfordern und die Identität des Benutzers abrufen.  |
| ` profile ` |   Benutzerprofil lesen Der Client kann zusätzlich zur Identität (Partner ID) Profildaten des eingeloggten Benutzers abrufen.  |
