# Register an agent application

```{warning}
Temporarily not supported.
```

An agent application is a MarketPlace application that employs the message broker technique, offered by the MarketPlace platform, to allow application providers to register their applications which are unreachable directly over the internet due to a protective firewall. The technique relies on a message broker, specifically [Apache Kafka](https://kafka.apache.org/), to enable communication via the MarketPlace.
An agent application makes use of the [remote-agent](https://gitlab.cc-asp.fraunhofer.de/MarketPlace/remoteagent) wrapper to establish communication to the message broker.

## Register the application

The fist step is to register the application with the steps shown in the [app registration section](registration.md).

## Getting the certificate for Agent

Select a string as key and replace `KAFKA_SSL_PASSWORD` in the below steps.

### 1. Creating a Keystore

```bash
keytool -keystore kafka.client.keystore.jks -alias client -validity 3650 -genkey -keyalg RSA -ext SAN=dns:${dns} -storepass ${KAFKA_SSL_PASSWORD}
```

w.r.t the deployment server please change your dns.
when prompted for first and last name you can provide the dns you supplied.
Populate the next few prompted questions, and use the same keystore password when prompted for - key password for <server>

### 2. Create a Certificate Signing Request (CSR)

```bash
keytool -keystore kafka.client.keystore.jks -alias client -certreq -file ca-request-client -storepass ${KAFKA_SSL_PASSWORD}
```

when prompted for the keystore password, you can reuse the `KAFKA_SSL_PASSWORD`.

## Send the CSR to the admin

Admin signs the CSR and returns `ca-signed-client`, and the certificate file `ca-cert`.

## Import CA and the CSR into the keystore

### 1. Import CA into the keystore

```bash
keytool -keystore kafka.client.keystore.jks -alias ca-cert -import -file ca-cert -storepass ${KAFKA_SSL_PASSWORD}
```

### 2. Import CSR into the keystore

```bash
keytool -keystore kafka.client.keystore.jks -alias client -import -file ca-signed-client -storepass ${KAFKA_SSL_PASSWORD}
```

And answer `yes` when asked if you trust this certificate.

## Extract the key file for remote-agent

```bash
keytool -v -importkeystore -srckeystore kafka.client.keystore.jks -srcalias client -destkeystore cert_and_key.p12 -deststoretype PKCS12
```

```bash
 openssl pkcs12 -in cert_and_key.p12 -nocerts -nodes -out key.pem
```

when prompted for the new, source, keystore passwords provide `KAFKA_SSL_PASSWORD`

## Set certificate file paths and password as environment variables

Set paths to the location of certificate `ca-cert` and CSR `ca-signed-client` obtained from MarketPlace admin, as `CA_CERT_PATH` and `CA_SIGNED_CERT_PATH` respectively.

The path to key.pem generated in the previous step must be set as `KEY_PATH` and the `KAFKA_SSL_PASSWORD` used in previous steps must also be set as an env variable.

The `application-id` received while registering the agent must be assigned to `APPLICATION_ID`.

## Set up the agent_config.yml

There is a sample `agent_config.yml` file in the remote-agent wrapper, this needs to be modified to suit your agent application.

Users should set the script to be executed by editing the agent_config.yml. Parameters required by your application will be available by fetching using `input.<parametername>`
In the agent_config.yml set the `outputFile` to the output file path, and your output parameter name registered with marketplace must be assigned to `outputParameterName` and datasink must be assigned to `input.<parametername>`. The script to be executed must be added under the run: script section.
All input fields required by the application can be fetched by replacing `<parametername>` with the corresponding file extension. For example, if your inputs are journal_file and header_file, you can fetch it using `input.journal_file` and `input.header_file` respectively.

## Build and run the remote-agent

Once the remote agent is run, it is now ready to communicate with the MarketPlace.
For more information check the [Readme](https://gitlab.cc-asp.fraunhofer.de/MarketPlace/remoteagent/-/blob/master/README.md).
