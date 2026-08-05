
# Getting Started with Verizon

## Introduction

"The Connection Planner is a service that provides devices windows to connect to their backend APIs. The service validates device access permissions and processes valid devices asynchronously. For each batch, it retrieves device connectivity windows from the RAN KPI Data Application, and sends callbacks back to customers via UWS-Callback for both successful and failed device requests."

Best Practices for Callbacks: [https://thingspace.verizon.com/documentation/apis/connectivity-management/working-with-verizon/about-callback-services/best-practices.html](https://thingspace.verizon.com/documentation/apis/connectivity-management/working-with-verizon/about-callback-services/best-practices.html)

## Building

You must have Python `3.7+` installed on your system to install and run this SDK. This SDK package depends on other Python packages like pytest, etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK. To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&step=installDependencies)

## Installation

The following section explains how to use the verizon library in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&projectName=verizon&step=openProject1)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&projectName=verizon&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&projectName=verizon&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&projectName=verizon&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from verizon.verizon_client import VerizonClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&projectName=verizon&libraryName=verizon.verizon_client&className=VerizonClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&projectName=verizon&libraryName=verizon.verizon_client&className=VerizonClient&step=runProject)

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| environment | [`Environment`](README.md#environments) | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524, 408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT", "GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| thingspace_oauth_credentials | [`ThingspaceOauthCredentials`](doc/auth/oauth-2-client-credentials-grant.md) | The credential object for OAuth 2 Client Credentials Grant |
| vz_m2m_token_credentials | [`VZM2mTokenCredentials`](doc/auth/custom-header-signature.md) | The credential object for Custom Header Signature |
| session_token_credentials | [`SessionTokenCredentials`](doc/auth/custom-header-signature-1.md) | The credential object for Custom Header Signature |
| thingspace_oauth_1_credentials | [`ThingspaceOauth1Credentials`](doc/auth/oauth-2-client-credentials-grant-1.md) | The credential object for OAuth 2 Client Credentials Grant |

The API client can be initialized as follows:

### Code-Based Client Initialization

```python
from verizon.configuration import Environment
from verizon.http.auth.session_token import SessionTokenCredentials
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.thingspace_oauth_1 import ThingspaceOauth1Credentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.verizon_client import VerizonClient

client = VerizonClient(
    thingspace_oauth_credentials=ThingspaceOauthCredentials(
        oauth_client_id='OAuthClientId',
        oauth_client_secret='OAuthClientSecret'
    ),
    vz_m2m_token_credentials=VZM2mTokenCredentials(
        vz_m2m_token='VZ-M2M-Token'
    ),
    session_token_credentials=SessionTokenCredentials(
        session_token='SessionToken'
    ),
    thingspace_oauth_1_credentials=ThingspaceOauth1Credentials(
        oauth_client_id='OAuthClientId',
        oauth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.PRODUCTION
)
```

### Environment-Based Client Initialization

```python
from verizon.verizon_client import VerizonClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = VerizonClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](doc/environment-based-client-initialization.md) section for details.

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| PRODUCTION | **Default** |
| STAGING | - |
| DEV | - |
| QA | - |
| MOCK_SERVER_FOR_LIMITED_AVAILABILITY_SEE_QUICK_START | - |

## Authorization

This API uses the following authentication schemes.

* [`thingspace_oauth (OAuth 2 Client Credentials Grant)`](doc/auth/oauth-2-client-credentials-grant.md)
* [`VZ-M2M-Token (Custom Header Signature)`](doc/auth/custom-header-signature.md)
* [`sessionToken (Custom Header Signature)`](doc/auth/custom-header-signature-1.md)
* [`thingspace_oauth1 (OAuth 2 Client Credentials Grant)`](doc/auth/oauth-2-client-credentials-grant-1.md)

## List of APIs

* [Account Service Controller](doc/controllers/account-service-controller.md)
* [Intelligence Service Controller](doc/controllers/intelligence-service-controller.md)
* [Device Management](doc/controllers/device-management.md)
* [Device Groups](doc/controllers/device-groups.md)
* [Session Management](doc/controllers/session-management.md)
* [Connectivity Callbacks](doc/controllers/connectivity-callbacks.md)
* [Account Requests](doc/controllers/account-requests.md)
* [Service Plans](doc/controllers/service-plans.md)
* [Device Diagnostics](doc/controllers/device-diagnostics.md)
* [Device Monitoring](doc/controllers/device-monitoring.md)
* [Device Profile Management](doc/controllers/device-profile-management.md)
* [E UICC Device Profile Management](doc/controllers/e-uicc-device-profile-management.md)
* [Devices Locations](doc/controllers/devices-locations.md)
* [Devices Location Subscriptions](doc/controllers/devices-location-subscriptions.md)
* [Device Location Callbacks](doc/controllers/device-location-callbacks.md)
* [Usage Trigger Management](doc/controllers/usage-trigger-management.md)
* [Software Management Subscriptions V1](doc/controllers/software-management-subscriptions-v1.md)
* [Software Management Licenses V1](doc/controllers/software-management-licenses-v1.md)
* [Firmware V1](doc/controllers/firmware-v1.md)
* [Software Management Callbacks V1](doc/controllers/software-management-callbacks-v1.md)
* [Software Management Reports V1](doc/controllers/software-management-reports-v1.md)
* [Software Management Subscriptions V2](doc/controllers/software-management-subscriptions-v2.md)
* [Software Management Licenses V2](doc/controllers/software-management-licenses-v2.md)
* [Campaigns V2](doc/controllers/campaigns-v2.md)
* [Software Management Callbacks V2](doc/controllers/software-management-callbacks-v2.md)
* [Software Management Reports V2](doc/controllers/software-management-reports-v2.md)
* [Client Logging](doc/controllers/client-logging.md)
* [Server Logging](doc/controllers/server-logging.md)
* [Configuration Files](doc/controllers/configuration-files.md)
* [Software Management Subscriptions V3](doc/controllers/software-management-subscriptions-v3.md)
* [Software Management Licenses V3](doc/controllers/software-management-licenses-v3.md)
* [Campaigns V3](doc/controllers/campaigns-v3.md)
* [Software Management Reports V3](doc/controllers/software-management-reports-v3.md)
* [Firmware V3](doc/controllers/firmware-v3.md)
* [Account Devices](doc/controllers/account-devices.md)
* [Software Management Callbacks V3](doc/controllers/software-management-callbacks-v3.md)
* [SIM Securefor Io T Licenses](doc/controllers/sim-securefor-io-t-licenses.md)
* [Account Subscriptions](doc/controllers/account-subscriptions.md)
* [Diagnostics Subscriptions](doc/controllers/diagnostics-subscriptions.md)
* [Diagnostics Observations](doc/controllers/diagnostics-observations.md)
* [Diagnostics History](doc/controllers/diagnostics-history.md)
* [Diagnostics Settings](doc/controllers/diagnostics-settings.md)
* [Diagnostics Callbacks](doc/controllers/diagnostics-callbacks.md)
* [Diagnostics Factory Reset](doc/controllers/diagnostics-factory-reset.md)
* [Cloud Connector Subscriptions](doc/controllers/cloud-connector-subscriptions.md)
* [Cloud Connector Devices](doc/controllers/cloud-connector-devices.md)
* [HPL Device Management](doc/controllers/hpl-device-management.md)
* [Device Service Management](doc/controllers/device-service-management.md)
* [Device Reports](doc/controllers/device-reports.md)
* [Hyper Precise Location Callbacks](doc/controllers/hyper-precise-location-callbacks.md)
* [Device Credential Management](doc/controllers/device-credential-management.md)
* [Anomaly Settings](doc/controllers/anomaly-settings.md)
* [Anomaly Triggers](doc/controllers/anomaly-triggers.md)
* [Anomaly Triggers V2](doc/controllers/anomaly-triggers-v2.md)
* [Wireless Network Performance](doc/controllers/wireless-network-performance.md)
* [Managinge SIM Profiles](doc/controllers/managinge-sim-profiles.md)
* [Device SMS Messaging](doc/controllers/device-sms-messaging.md)
* [Device Actions](doc/controllers/device-actions.md)
* [Thing Space Qualityof Service API Actions](doc/controllers/thing-space-qualityof-service-api-actions.md)
* [Promotion Period Information](doc/controllers/promotion-period-information.md)
* [Retrievethe Triggers](doc/controllers/retrievethe-triggers.md)
* [Update Triggers](doc/controllers/update-triggers.md)
* [SIM Actions](doc/controllers/sim-actions.md)
* [Global Reporting](doc/controllers/global-reporting.md)
* [Retrieve Rate Plan List](doc/controllers/retrieve-rate-plan-list.md)
* [Create Price Plan Triggers](doc/controllers/create-price-plan-triggers.md)
* [Update Price Plan Triggers](doc/controllers/update-price-plan-triggers.md)
* [5G BI Device Actions](doc/controllers/5g-bi-device-actions.md)
* [Sensor Insights Sensors](doc/controllers/sensor-insights-sensors.md)
* [Sensor Insights Devices](doc/controllers/sensor-insights-devices.md)
* [Sensor Insights Gateways](doc/controllers/sensor-insights-gateways.md)
* [Sensor Insights Smart Alerts](doc/controllers/sensor-insights-smart-alerts.md)
* [Sensor Insights Rules](doc/controllers/sensor-insights-rules.md)
* [Sensor Insights Health Score](doc/controllers/sensor-insights-health-score.md)
* [Sensor Insights Notification Groups](doc/controllers/sensor-insights-notification-groups.md)
* [Sensor Insights Users](doc/controllers/sensor-insights-users.md)
* [Sensor Insights Device Profile](doc/controllers/sensor-insights-device-profile.md)
* [Sensor Insights Smart Alert Metrics](doc/controllers/sensor-insights-smart-alert-metrics.md)
* [Accounts](doc/controllers/accounts.md)
* [SMS](doc/controllers/sms.md)
* [Exclusions](doc/controllers/exclusions.md)
* [Billing](doc/controllers/billing.md)
* [Targets](doc/controllers/targets.md)
* [PWN](doc/controllers/pwn.md)
* [Device-Role-Controller](doc/controllers/device-role-controller.md)
* [ETX App Configuration](doc/controllers/etx-app-configuration.md)
* [ETX Registration](doc/controllers/etx-registration.md)
* [Map-Message-Controller](doc/controllers/map-message-controller.md)

## SDK Infrastructure

### Configuration

* [ProxySettings](doc/proxy-settings.md)
* [Environment-Based Client Initialization](doc/environment-based-client-initialization.md)

### HTTP

* [HttpResponse](doc/http-response.md)
* [HttpRequest](doc/http-request.md)

### Utilities

* [ApiResponse](doc/api-response.md)
* [ApiHelper](doc/api-helper.md)
* [HttpDateTime](doc/http-date-time.md)
* [RFC3339DateTime](doc/rfc3339-date-time.md)
* [UnixDateTime](doc/unix-date-time.md)

