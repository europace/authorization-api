# Scopes für OAuth Clients bei Europace

Mit Hilfe der Scopes kannst du genau angeben, welche Art von Zugriff du benötigst. Scopes beschränken den Zugriff mittels OAuth-Token. Sie gewähren keine zusätzlichen Berechtigungen über die Rechte des Nutzers hinaus.

## Verfügbare Scopes

Die nachfolgende Tabelle stellt eine Liste, der aktuell verfügbaren Scopes dar.

| Name | Beschreibung  |
| --- | ---  |
| ` partner:plakette:anlegen ` |   Darf neue Plaketten anlegen.  |
| ` partner:plakette:lesen ` |   Darf Partner-Daten lesen  |
| ` partner:plakette:schreiben ` |   Darf Partner-Daten schreiben  |
| ` partner:beziehungen:lesen ` |   Darf Beziehungen zwischen Partnern lesen Erlaubt es unter anderem UebernahmeRecht, Administrierbare und Uebernehmbare abzurufen  |
| ` partner:rechte:lesen ` |   Darf Rechte eines Partners lesen  |
| ` partner:rechte:schreiben ` |   Darf Rechte eines Partners schreiben  |
| ` report:rohdaten:lesen ` |   Darf den Rohdaten-Report runterladen  |
| ` report:produktanbieter:lesen ` |   Darf den Produktanbieter-Report runterladen  |
| ` baufinanzierung:echtgeschaeft ` |   Baufinanzierung-Echtgeschäft bearbeiten  |
| ` baufinanzierung:vorgang:lesen ` |   Baufinanzierungsvorgänge lesen  |
| ` baufinanzierung:vorgang:schreiben ` |   Baufinanzierungsvorgänge schreiben  |
| ` baufinanzierung:angebot:ermitteln ` |   Baufinanzierungsangebote ermitteln  |
| ` baufinanzierung:angebot:loeschen ` |   Baufinanzierungsangebote loeschen  |
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
| ` privatkredit:angebot:ermitteln ` |   Kreditsmartangebote ermitteln Der Client kann Ratenkredit-Angebote und Schaufensterkonditionen ermitteln.  |
| ` privatkredit:antrag:schreiben ` |   Kreditsmartanträge schreiben Der Client kann den Antragsstatus verändern oder den aktuellen Status um Zusatzinformationen ergänzen.  |
| ` privatkredit:vorgang:lesen ` |   Kreditsmartvorgänge lesen Der Client kann KreditSmart-Vorgänge automatisiert auslesen.  |
| ` privatkredit:vorgang:schreiben ` |   Kreditsmartvorgänge schreiben Der Client kann KreditSmart-Vorgänge automatisiert anlegen.  |
| ` unterlagen:dokument:lesen ` |   Dokumente lesen Der Client kann hochgeladene Dokumente eines Vorgangs abrufen.  |
| ` unterlagen:dokument:schreiben ` |   Dokumente schreiben und kategorisieren Der Client kann Dokumente zu einem Vorgang hochladen, umbenennen, löschen und die Kategorisierung anstoßen, damit die Dokumente in der Unterlagenakte zu Verfügung stehen.  |
| ` unterlagen:unterlage:lesen ` |   Unterlagen lesen Der Client kann die kategorisierten Dokumente (Unterlagen) abrufen.  |
| ` unterlagen:unterlage:schreiben ` |   Unterlagen neu zuordnen Der Client kann die Kategorie und den Bezug der Unterlagen ändern.  |
| ` unterlagen:unterlage:freigeben ` |   Unterlagen freigeben Der Client kann Unterlagen für einen Antrag freigeben.  |
| ` unterlagen:freigabe:lesen ` |   Freigegebene Unterlagen lesen Der Client kann freigegebene Unterlagen zu einem Antrag abrufen  |
| ` unterlagen:freigabe:schreiben ` |   Freigegebene Unterlagen aktualisieren Der Client kann den Status einer freigegeben Unterlagen setzen, um aus Produktanbietersicht den Empfang der Unterlagen zu bestätigen.  |
| ` impersonieren ` |   Darf Impersonieren Eine Aktion wird im Namen eines Partners ausgeführt wobei die Autorisierung des Clients durch einen übergeordneten Partner erfolgt.  |
| ` openid ` |   Benutzer-Login durchführen Der Client kann das Login des Benutzers auf der Plattform mittels OpenID Connect anfordern und die Identität des Benutzers abrufen.  |
| ` profile ` |   Benutzerprofil lesen Der Client kann zusätzlich zur Identität (Partner ID) Profildaten des eingeloggten Benutzers abrufen.  |
