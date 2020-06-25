#!/usr/bin/env python

import sys
import yaml
from optparse import OptionParser

def transformScopesToMarkDown(input):
    scopes = input["flows"]["clientCredentials"]["scopes"].copy()

    intro="""# Scopes für OAuth Clients bei Europace

Mithilfe von Scopes können Sie genau angeben, welche Art von Zugriff Sie benötigen. Scopes beschränken den Zugriff für OAuth-Token. Sie gewähren keine zusätzlichen Berechtigungen über das hinaus, was der Benutzer bereits hat.

## Verfügbare Scopes

Die nachfolgende Tabelle stellt eine Liste, der aktuell verfügbaren Scopes dar.

| Name | Beschreibung  |
| --- | ---  |"""

    print(intro)
    for scope in scopes:
        print('| `', scope, '` | ', scopes[scope].replace('##', '').replace('\n', ' ').replace('\r', '').rstrip(), ' |')

def printScopes(inputfile):
    with open(inputfile) as stream:
        europace_security = ''
        try:
            europace_security = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

        transformScopesToMarkDown(europace_security)

def main():
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input", metavar="FILE")

    (options, args) = parser.parse_args()
    inputfile = options.input

    printScopes(inputfile)

if __name__ == "__main__":
    main()
