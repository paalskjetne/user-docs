# AiiDAlab resident app registration

## AiiDAlab app register

Your need to having your app registred in AiiDAlab registry first.
Please check the [AiiDAlab App developer guide](https://aiidalab.readthedocs.io/en/latest/app_development/index.html) for how to create your AiiDAlab app and publish it so it can be installed from [MarketPlace AiiDAlab](https://materials-marketplace.aiidalab.net/).

## AiiDAlab register to MarketPlace

As regular App it is required to [create a knowledge item](./registration.md#create-a-knowledge-item) first for the AiiDAlab App.
AiiDAlab in MarketPlace provide the frontend to all its sub-application there is the Host AiiDAlab App host by us and users can register the sub-application as resident App of the Host AiiDAlab App.

You can use the OpenAPI specification from the example below:

```yaml
---
openapi: 3.0.0

info:
    title: AiiDAlab dummy App
    description: OpenAPI Specification of the MarketPlace AiiDAlab deployment
    version: 0.1.0
    x-application-name: AiiDAlab dummy App
    x-external-hostname: https://materials-marketplace.aiidalab.net
    x-image: <logo-image>
    x-contacts:
        - <your email>
    x-products:
        - name: AiiDAlab dummy app
          productId:
servers:
    - url: https://materials-marketplace.aiidalab.net

paths:

    /user-redirect/apps/apps/home/open_app.ipynb?app=<dummy>&redirect=user-redirect/apps/apps/<dummy>/<nb>.ipynb:
        get:
            description: dummy App
            operationId: frontend
            security:
                - bearerAuth: []
            responses:
                '200':
                    description: Success
                '404':
                    description: Page not found

components:
    securitySchemes:
        bearerAuth:
            type: http
            scheme: bearer
            bearerFormat: JWT
```

Replace the `dummy` with your app name, set the `<logo-image>`, `<your emal>` and the path to the startup notebook. 
Using this OpenAPI specification to register the App as the type resident app of the Host AiiDAlab App (ID: `37afd7dc-31b5-4f59-ad53-167f666c80eb`).
![AiiDAlab resident App register](../_static/img/app_registration/aiidalab-app-registration.png)

Once you have the AiiDAlab resident App registred and approved, you can continue with the [link application](./registration.md#link-application) and [test application](./registration.md#test-application).