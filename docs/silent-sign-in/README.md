# Silent-Sign-In API

Europace's Silent Sign-In API allows users to sign in through an OAuth client and invoke the Europace user interface in the browser.

---- 
![advisor](https://img.shields.io/badge/-advisor-lightblue)
![loanProvider](https://img.shields.io/badge/-loanProvider-lightblue)
![mortgageLoans](https://img.shields.io/badge/-mortgageLoans-lightblue)
![consumerLoans](https://img.shields.io/badge/-consumerLoans-lightblue)

[![Authentication](https://img.shields.io/badge/Auth-OAuth2-green)](https://docs.api.europace.de/baufinanzierung/authentifizierung/)
![Release](https://img.shields.io/badge/release-1.0-blue)

## Usecases

- Log in a user and display Europace seamlessly in an iFrame or new browser tab.

## Dokumentation
[![YAML](https://img.shields.io/badge/OAS-HTML_Doc-lightblue)](https://europace.github.io/authorization-api/ssi.html)
[![YAML](https://img.shields.io/badge/OAS-YAML-lightgrey)](https://github.com/europace/authorization-api/blob/master/docs/silent-sign-in/ssi-openapi.yaml)

Feedback and questions are welcome as [GitHub Issue](https://github.com/europace/authorization-api/issues/new).


## Steps of the Silent Sign-In
![seq-ssi](seq_ssi.png)

## Example: Log on user and open process

### Step 1 - Login user
The step is optional if a user access token already exists.

To use the API, the OAuth2 client requires the following scopes:
| Scope                                  | API-Usecase                                                      |
| -------------------------------------- | ---------------------------------------------------------------- |
| ` partner:login:silent-sign-in `       |   Silent sign-in allowed                                         |
| ` impersonieren `                      |   Log in other users as subject       

> The access token must be issued in the name of the user. 
Impersonation can be applied to create this as a client. See: [Authorization API Impersonate](https://docs.api.europace.de/common/authentifizierung/authorization-api/#wie-authentifiziere-ich-verschiedene-benutzer-mit-einem-client-impersionieren)

### Step 2 - Generate one-time password
For security reasons, a one-time password is used to access Europace via the browser.

Example-request:
``` http
POST /authorize/silent-sign-in?subject=[user-partner-id] HTTP/1.1
Host: www.europace2.de
Authorization: Bearer [user-access-token]
```

Example-resonse:
``` json
{
  "otp": "05448389A4014F49AFC896EB15B60A07AE8B"
}
```

### Step 3 - Open Europace in the browser
Europace can now be opened with the OTP. To display the process AB45C2 directly, the redirect_uri will be passed with `/vorgang/oeffne/[vorgangsnummer]`.

Example-request:
``` http
GET /authorize/silent-sign-in?subject=[user-partner-id]&redirect_uri=/vorgang/oeffne/AB45C2&otp=[otp] HTTP/1.1
Host: www.europace2.de
```

Example-response: \
Redirect with EP session to `https://www.europace2.de/[redirect_uri]`

List of Redirect_uris:
* `/uebersicht` (default)
* `/vorgangsmanagement`
* `/vorgang/oeffne/[vorgangsnummer]`
* `/antragsuebersicht` (for product providers only)
* `/partnermanagement` 
