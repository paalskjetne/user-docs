# Update an application

Once an application has already been registered, it can be updated without having to change the client ID and client secret values.

## 1. Update the .yml file

The `version` field must be updated each time the application is updated.
The `client-id` provided in the initial registration should be included in the `x-oauth-client` section.

If any products remain unchanged, their `product-id` should be included in the `x-products` description.

## 2. Update the application on the MarketPlace

Upload the new version of the openAPI specification in the _Admin console_ of your application:

![Update the application](../_static/img/app_registration/update_app.png)

If the process was successful, you will be informed:

![Update output](../_static/img/app_registration/update_output.png)
