# Capabilities

In order to offer a unified form of communication, the MarketPlace has defined a list
of typical functionalities, which we call _capabilities_, that a user might expect and an application can choose to support.
Each capability will have a name and a definition of the expected parameters and errors it can generate.

A capability is associated with an operation ID (capability and operation ID should match) and a specification of a _unique_ REST-API endpoint + HTTP method.
For instance, there can only be one capability under the `/dataset` path for the `get` method.

Capabilities are case sensitive.

## Capability types

Different types of capabilities are clustered into groups based on their purpose.
Thus, we can define applications as:

1. **Data source:** Applications for online data repositories which store generic data that can be used in different use cases. Examples of such data repositories are databases within [Materials Cloud](https://www.materialscloud.org/) and [NOMAD](https://nomad-lab.eu/).
1. **Data sink:** Applications that offer persistent data storage services.
1. **Transformation:** Applications that manipulate data. A simulation tool that generates data is an example of such an application.
1. **Front page:** Applications that have a web page.
1. **System:** Capabilities related to operability of applications.

The MarketPlace will be able to automatically infer the type of the application to the users, while recognizing the functionalities that are supported by it.
This allows the MarketPlace to use the applications in workflows that require apps with specific capabilities.
However, the capabilities are not enforced, and an application may choose to implement a mixed subset of capabilities.

Since the API is uniform, it is easy for the user to switch one application with another in case it is favourable.

## List of supported capabilities

These are the currently supported capabilities:

| Type           | Method | Capability                  | Description                                      |
| -------------- | :----: | --------------------------- | ------------------------------------------------ |
| FrontPage      |  GET   | frontend                    | Goes to login page of the application            |
| FrontPage      |  GET   | formPage                    | Goes to form page of the application             |
| System         |  GET   | heartbeat                   | To check if an application is alive              |
| System         |  GET   | globalSearch                | Search for strings                               |
| DataSource     |  GET   | getCollection               | Fetches list of datasets                         |
| DataSource     |  GET   | getCudsCollection           | Fetches list of cuds datasets                    |
| DataSource     |  GET   | getDataset                  | Fetches a particular Dataset                     |
| DataSource     |  GET   | getCudsDataset              | Fetches a particular Cuds Dataset                |
| DataSource     |  GET   | getMetadata                 | Fetch information about certain sets of data     |
| DataSource     |  GET   | queryDataset                | Execute search query on datasets                 |
| DataSource     |  POST  | postQueryDataset            | Execute search query on datasets                 |
| DataSource     |  POST  | exportDatasetWithAttributes | Export data with attribute values of datasets    |
| DataSource     |  GET   | getDatasetAttributes        | List attributes included in specified dataset    |
| DataSource     |  GET   | queryCollection             | Query a collection                               |
| DataSource     |  POST  | postQueryCollection         | Query a collection(Post for GraphQL)             |
| DataSink       |  POST  | createDataset               | Store a dataset                                  |
| DataSink       |  POST  | createCudsDataset           | Store cuds dataset                               |
| DataSink       |  POST  | createCollection            | create a collection(used for workflows)          |
| DataSink       |  POST  | createDatasetFromURI        | Store a dataset by fetching the data from a URI  |
| DataSink       |  PUT   | updateDataset               | Edit a dataset                                   |
| DataSink       |  PUT   | updateCudsDataset           | Edit a cuds dataset                              |
| DataSink       |  PUT   | updateDatasetFromURI        | Update a dataset by fetching the data from a URI |
| DataSink       | DELETE | deleteDataset               | Delete a dataset                                 |
| DataSink       | DELETE | deleteCudsDataset           | Delete a CUDS dataset                            |
| Transformation |  POST  | newTransformation           | Initialize a Transformation                      |
| Transformation |  POST  | startTransformation         | Start execution of a Transformation              |
| Transformation |  POST  | stopTransformation          | Stop the execution of a Transformation           |
| Transformation |  GET   | getTransformationStatus     | Get the status of a Transformation               |
| Transformation | DELETE | deleteTransformation        | Delete a transformation                          |
| Transformation |  GET   | getTransformationList       | Get the list of Transformation instances         |
