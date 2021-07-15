# Scopes für OAuth Clients bei Europace

Mit Hilfe der Scopes kannst du genau angeben, welche Art von Zugriff du benötigst. Scopes beschränken den Zugriff mittels OAuth-Token. Sie gewähren keine zusätzlichen Berechtigungen über die Rechte des Nutzers hinaus.

## Verfügbare Scopes

Die nachfolgende Tabelle stellt eine Liste, der aktuell verfügbaren Scopes dar.

| Scope | Name | Beschreibung  |
|-------|------|---------------| 
| ` partner:plakette:anlegen ` |  Partner anlegen  |   Neue Organisationen oder Personen können erstellt werden.  |
| ` partner:plakette:lesen ` |  Partner lesen  |    |
| ` partner:plakette:schreiben ` |  Partner verändern  |    |
| ` partner:beziehungen:lesen ` |  Partner-Beziehungen lesen  |   Zugriffs- und Einstellungsrechte können abgerufen werden.  |
| ` partner:beziehungen:schreiben ` |  Partner-Beziehungen schreiben  |   Zugriffsrechte können vergeben werden.  |
| ` partner:rechte:lesen ` |  Partner-Rechte lesen  |    |
| ` partner:rechte:schreiben ` |  Partner-Rechte verändern  |    |
| ` partner:login:silent-sign-in ` |  Silent-Sign-In erlaubt  |   Ermöglicht das öffnen von Europace im Browser ohne Passwortabfrage.  |
| ` report:rohdaten:lesen ` |  Vertriebs-Rohdaten-Report abrufen  |    |
| ` report:produktanbieter:lesen ` |  Produktanbieter-Report abrufen  |    |
| ` baufinanzierung:echtgeschaeft ` |  BaufiSmart-Echtgeschäft bearbeiten  |    |
| ` baufinanzierung:vorgang:lesen ` |  BaufiSmart-Vorgänge lesen  |    |
| ` baufinanzierung:vorgang:schreiben ` |  BaufiSmart-Vorgänge anlegen  |    |
| ` baufinanzierung:angebot:ermitteln ` |  BaufiSmart-Angebote ermitteln  |    |
| ` baufinanzierung:angebot:loeschen ` |  gespeicherte BaufiSmart-Angebote löschen  |    |
| ` baufinanzierung:ereignis:lesen ` |  BaufiSmart-Ereignisse lesen  |    |
| ` baufinanzierung:antrag:lesen ` |  BaufiSmart-Anträge lesen  |    |
| ` baufinanzierung:antrag:schreiben ` |  BaufiSmart-Anträge verändern  |   Der Antragsstatus und der Sachbearbeiter können verändert sowie die Produktanbieter-Renferenz ergänzt werden.  |
| ` baufinanzierung:produktkonfiguration:lesen ` |  Produktkonfiguration lesen  |   für Product-Cockpit  |
| ` baufinanzierung:produktkonfiguration:schreiben ` |  Produktkonfiguration verändern  |   für Product-Cockpit  |
| ` baufinanzierung:produktkonfiguration:freigeben ` |  Produktkonfiguration freigeben  |   für Product-Cockpit  |
| ` baufinanzierung:produkt:lesen ` |  Produkt lesen  |   für Product-Cockpit  |
| ` baufinanzierung:produkt:schreiben ` |  Produkt verändern  |   für Product-Cockpit  |
| ` baufinanzierung:produktanbieter:lesen ` |  Produktanbieter lesen  |   für Product-Cockpit  |
| ` baufinanzierung:produktanbieter:schreiben ` |  Produktanbieter verändern  |   für Product-Cockpit  |
| ` privatkredit:angebot:ermitteln ` |  KreditSmart-Angebote ermitteln  |   Ratenkredit-Angebote und -Schaufensterkonditionen können ermittelt werden.  |
| ` privatkredit:antrag:schreiben ` |  KreditSmart-Anträge anlegen/verändern  |   Anträge anlegen (annehmen) oder verändern (z.B. Antragsstatus).  |
| ` privatkredit:vorgang:lesen ` |  KreditSmart-Vorgänge lesen  |    |
| ` privatkredit:vorgang:schreiben ` |  KreditSmart-Vorgänge anlegen/verändern  |   Vorgänge anlegen oder verändern.  |
| ` dokumente:dokument:lesen ` |  Dokumente herunterladen  |   Dokumente können aus einem Vorgang oder Antrag gelesen (heruntergeladen) werden  |
| ` dokumente:dokument:schreiben ` |  Dokumente hinzufügen  |   Dokumente können zu einem Vorgang oder Antrag hinzugefügt (hochgeladen) werden  |
| ` unterlagen:dokument:lesen ` |  Unterlagendokumente herunterladen  |   Hochgeladene Dokumente eines Vorgangs können heruntergeladen werden.  |
| ` unterlagen:dokument:schreiben ` |  Unterlagendokumente hinzufügen und kategorisieren  |   Dokumente zu einem Vorgang können hochladen, umbenannt, gelöscht und die Kategorisierung gestartet werden, damit die Dokumente in der Unterlagenakte zu Verfügung stehen.  |
| ` unterlagen:unterlage:lesen ` |  Unterlagen lesen  |   Kategorisierte Dokumente (Unterlagen) können abgerufen werden.  |
| ` unterlagen:unterlage:schreiben ` |  Unterlagen neu zuordnen  |   Die Kategorie und der Bezug der Unterlagen können geändert werden.  |
| ` unterlagen:unterlage:freigeben ` |  Unterlagen freigeben  |   Unterlagen für einen Antrag können freigeben werden.  |
| ` unterlagen:freigabe:lesen ` |  Freigegebene Unterlagen lesen  |   Freigegebene Unterlagen zu einem Antrag können abgerufen werden.  |
| ` unterlagen:freigabe:schreiben ` |  Freigegebene Unterlagen aktualisieren  |   Der Status einer freigegeben Unterlagen kann verändert werden, um aus Produktanbietersicht den Empfang der Unterlagen zu bestätigen.  |
| ` impersonieren ` |  Impersonieren  |   Aktionen können im Namen eines untergeordneten Partners ausgeführt werden.  |
| ` openid ` |  Benutzer-Identität überprüfen  |   Die Anmeldung bei Europace kann angefordert werden, um die Identität des Benutzers zu überprüfen.  |
| ` profile ` |  Benutzerprofil lesen  |   Profildaten (Vor- und Nachname, Benutzername, E-Mail und Avatar-Bild) des angemeldeten Benutzers können abgerufen werden.  |
