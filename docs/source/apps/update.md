# Update an application

```{warning}
Temporarily not supported.
```

Once an application has already been registered, it can be updated without having to change the client ID and client secret values.

## 1. Update the .yml file

The `version` field must be updated each time the application is updated.
The `client-id` provided in the initial registration should be included in the `x-oauth-client` section.

If any products remain unchanged, their `product-id` should be included in the `products` description

## 2. Update the application in MarketPlace

TODO: This process is being reviewed in the latest version and has not been finalised yet.

Please re-register any application that needs to be updated for now

<!--
### Fields that can be updated

-  ``version`` must be different from already registered application version
-  ``x-products`` can be deleted or modified
-  ``x-image`` field can be updated
-  New ``paths`` with new capabilities can be added
-  ``x-application-name`` field can be updated

### Fields that cannot be updated


-  ``x-application-id`` field should not be modified
-  ``x-external-hostname`` cannot be modified
-  ``servers`` field cannot be modified
-  Existing ``paths`` and capabilities cannot be modified or deleted

## 3. Have an administrator approve the updated application

An administrator needs to approve the application again for it to appear
on the Marketplace page .
-->
