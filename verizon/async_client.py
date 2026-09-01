from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.account_devices import AsyncAccountDevices
from .apis.account_requests import AsyncAccountRequests
from .apis.account_service_controller import AsyncAccountServiceController
from .apis.account_subscriptions import AsyncAccountSubscriptions
from .apis.accounts import AsyncAccounts
from .apis.anomaly_settings import AsyncAnomalySettings
from .apis.anomaly_triggers import AsyncAnomalyTriggers
from .apis.anomaly_triggers_v2 import AsyncAnomalyTriggersV2
from .apis.billing import AsyncBilling
from .apis.campaigns_v2 import AsyncCampaignsV2
from .apis.campaigns_v3 import AsyncCampaignsV3
from .apis.client_logging import AsyncClientLogging
from .apis.cloud_connector_devices import AsyncCloudConnectorDevices
from .apis.cloud_connector_subscriptions import AsyncCloudConnectorSubscriptions
from .apis.configuration_files import AsyncConfigurationFiles
from .apis.connectivity_callbacks import AsyncConnectivityCallbacks
from .apis.create_price_plan_triggers import AsyncCreatePricePlanTriggers
from .apis.device_actions import AsyncDeviceActions
from .apis.device_credential_management import AsyncDeviceCredentialManagement
from .apis.device_diagnostics import AsyncDeviceDiagnostics
from .apis.device_groups import AsyncDeviceGroups
from .apis.device_location_callbacks import AsyncDeviceLocationCallbacks
from .apis.device_management import AsyncDeviceManagement
from .apis.device_monitoring import AsyncDeviceMonitoring
from .apis.device_profile_management import AsyncDeviceProfileManagement
from .apis.device_reports import AsyncDeviceReports
from .apis.device_role_controller import AsyncDeviceRoleController
from .apis.device_service_management import AsyncDeviceServiceManagement
from .apis.device_sms_messaging import AsyncDeviceSmsMessaging
from .apis.devices_location_subscriptions import AsyncDevicesLocationSubscriptions
from .apis.devices_locations import AsyncDevicesLocations
from .apis.diagnostics_callbacks import AsyncDiagnosticsCallbacks
from .apis.diagnostics_factory_reset import AsyncDiagnosticsFactoryReset
from .apis.diagnostics_history import AsyncDiagnosticsHistory
from .apis.diagnostics_observations import AsyncDiagnosticsObservations
from .apis.diagnostics_settings import AsyncDiagnosticsSettings
from .apis.diagnostics_subscriptions import AsyncDiagnosticsSubscriptions
from .apis.e_uicc_device_profile_management import AsyncEUiccDeviceProfileManagement
from .apis.etxapp_configuration import AsyncEtxappConfiguration
from .apis.etxregistration import AsyncEtxregistration
from .apis.exclusions import AsyncExclusions
from .apis.firmware_v1 import AsyncFirmwareV1
from .apis.firmware_v3 import AsyncFirmwareV3
from .apis.gbi_device_actions5 import AsyncGbiDeviceActions5
from .apis.global_reporting import AsyncGlobalReporting
from .apis.hpl_device_management import AsyncHplDeviceManagement
from .apis.hyper_precise_location_callbacks import AsyncHyperPreciseLocationCallbacks
from .apis.intelligence_service_controller import AsyncIntelligenceServiceController
from .apis.managing_e_sim_profiles import AsyncManagingESimProfiles
from .apis.map_message_controller import AsyncMapMessageController
from .apis.promotion_period_information import AsyncPromotionPeriodInformation
from .apis.pwn import AsyncPwn
from .apis.retrieve_rate_plan_list import AsyncRetrieveRatePlanList
from .apis.retrieve_the_triggers import AsyncRetrieveTheTriggers
from .apis.sensor_insights_device_profile import AsyncSensorInsightsDeviceProfile
from .apis.sensor_insights_devices import AsyncSensorInsightsDevices
from .apis.sensor_insights_gateways import AsyncSensorInsightsGateways
from .apis.sensor_insights_health_score import AsyncSensorInsightsHealthScore
from .apis.sensor_insights_notification_groups import AsyncSensorInsightsNotificationGroups
from .apis.sensor_insights_rules import AsyncSensorInsightsRules
from .apis.sensor_insights_sensors import AsyncSensorInsightsSensors
from .apis.sensor_insights_smart_alert_metrics import AsyncSensorInsightsSmartAlertMetrics
from .apis.sensor_insights_smart_alerts import AsyncSensorInsightsSmartAlerts
from .apis.sensor_insights_users import AsyncSensorInsightsUsers
from .apis.server_logging import AsyncServerLogging
from .apis.service_plans import AsyncServicePlans
from .apis.session_management import AsyncSessionManagement
from .apis.sim_actions import AsyncSimActions
from .apis.sim_secure_for_io_t_licenses import AsyncSimSecureForIoTLicenses
from .apis.sms import AsyncSms
from .apis.software_management_callbacks_v1 import AsyncSoftwareManagementCallbacksV1
from .apis.software_management_callbacks_v2 import AsyncSoftwareManagementCallbacksV2
from .apis.software_management_callbacks_v3 import AsyncSoftwareManagementCallbacksV3
from .apis.software_management_licenses_v1 import AsyncSoftwareManagementLicensesV1
from .apis.software_management_licenses_v2 import AsyncSoftwareManagementLicensesV2
from .apis.software_management_licenses_v3 import AsyncSoftwareManagementLicensesV3
from .apis.software_management_reports_v1 import AsyncSoftwareManagementReportsV1
from .apis.software_management_reports_v2 import AsyncSoftwareManagementReportsV2
from .apis.software_management_reports_v3 import AsyncSoftwareManagementReportsV3
from .apis.software_management_subscriptions_v1 import AsyncSoftwareManagementSubscriptionsV1
from .apis.software_management_subscriptions_v2 import AsyncSoftwareManagementSubscriptionsV2
from .apis.software_management_subscriptions_v3 import AsyncSoftwareManagementSubscriptionsV3
from .apis.targets import AsyncTargets
from .apis.thing_space_quality_of_service_api_actions import AsyncThingSpaceQualityOfServiceApiActions
from .apis.update_price_plan_triggers import AsyncUpdatePricePlanTriggers
from .apis.update_triggers import AsyncUpdateTriggers
from .apis.usage_trigger_management import AsyncUsageTriggerManagement
from .apis.wireless_network_performance import AsyncWirelessNetworkPerformance
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseVerizonClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    AsyncClientCredentialsTokenSource,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncOAuth2Scheme,
    AsyncRawClient,
    AsyncTokenSource,
    ClientCredentials,
    ClientCredentialsOrDict,
    client_secret_basic,
    no_auth,
    param,
)
from .server.environment import Environment
from .server.server_config import ServerConfigOrDict


class AsyncVerizonClient(BaseVerizonClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        timeout: float = DEFAULT_TIMEOUT,
        server_config: ServerConfigOrDict | None = None,
        custom_async_http_client: AsyncHttpClient | None = None,
        thingspace_oauth: ClientCredentialsOrDict | None = None,
        thingspace_oauth_token_source: AsyncTokenSource[ClientCredentials] | None = None,
        vz_m2_m_token: str | None = None,
        session_token: str | None = None,
        thingspace_oauth1: ClientCredentialsOrDict | None = None,
        thingspace_oauth1_token_source: AsyncTokenSource[ClientCredentials] | None = None,
    ) -> None:
        super().__init__(environment=environment, timeout=timeout, server_config=server_config)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            global_headers=[
                param[str]("User-Agent", "VerizonClient/v1.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "v1.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            thingspace_oauth=(
                AsyncOAuth2Scheme(
                    credentials=ClientCredentials.coerce(thingspace_oauth),
                    source=(
                        thingspace_oauth_token_source
                        if thingspace_oauth_token_source is not None
                        else AsyncClientCredentialsTokenSource(
                            client=self._raw_client,
                            token_url=self._server.o_auth_server("/oauth2/token"),
                            placement=client_secret_basic,
                        )
                    ),
                )
                if thingspace_oauth is not None
                else no_auth
            ),
            vz_m2_m_token=ApiKeyHeaderScheme("VZ-M2M-Token", vz_m2_m_token) if vz_m2_m_token is not None else no_auth,
            session_token=ApiKeyHeaderScheme("SessionToken", session_token) if session_token is not None else no_auth,
            thingspace_oauth1=(
                AsyncOAuth2Scheme(
                    credentials=ClientCredentials.coerce(thingspace_oauth1),
                    source=(
                        thingspace_oauth1_token_source
                        if thingspace_oauth1_token_source is not None
                        else AsyncClientCredentialsTokenSource(
                            client=self._raw_client,
                            token_url=self._server.o_auth_server("/"),
                            placement=client_secret_basic,
                        )
                    ),
                )
                if thingspace_oauth1 is not None
                else no_auth
            ),
        )

    @cached_property
    def gbi_device_actions5(self) -> AsyncGbiDeviceActions5:
        return AsyncGbiDeviceActions5(self._raw_client, self._server, self._auth)

    @cached_property
    def account_devices(self) -> AsyncAccountDevices:
        return AsyncAccountDevices(self._raw_client, self._server, self._auth)

    @cached_property
    def account_requests(self) -> AsyncAccountRequests:
        return AsyncAccountRequests(self._raw_client, self._server, self._auth)

    @cached_property
    def account_service_controller(self) -> AsyncAccountServiceController:
        return AsyncAccountServiceController(self._raw_client, self._server, self._auth)

    @cached_property
    def account_subscriptions(self) -> AsyncAccountSubscriptions:
        return AsyncAccountSubscriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def accounts(self) -> AsyncAccounts:
        return AsyncAccounts(self._raw_client, self._server, self._auth)

    @cached_property
    def anomaly_settings(self) -> AsyncAnomalySettings:
        return AsyncAnomalySettings(self._raw_client, self._server, self._auth)

    @cached_property
    def anomaly_triggers(self) -> AsyncAnomalyTriggers:
        return AsyncAnomalyTriggers(self._raw_client, self._server, self._auth)

    @cached_property
    def anomaly_triggers_v2(self) -> AsyncAnomalyTriggersV2:
        return AsyncAnomalyTriggersV2(self._raw_client, self._server, self._auth)

    @cached_property
    def billing(self) -> AsyncBilling:
        return AsyncBilling(self._raw_client, self._server, self._auth)

    @cached_property
    def campaigns_v2(self) -> AsyncCampaignsV2:
        return AsyncCampaignsV2(self._raw_client, self._server, self._auth)

    @cached_property
    def campaigns_v3(self) -> AsyncCampaignsV3:
        return AsyncCampaignsV3(self._raw_client, self._server, self._auth)

    @cached_property
    def client_logging(self) -> AsyncClientLogging:
        return AsyncClientLogging(self._raw_client, self._server, self._auth)

    @cached_property
    def cloud_connector_devices(self) -> AsyncCloudConnectorDevices:
        return AsyncCloudConnectorDevices(self._raw_client, self._server, self._auth)

    @cached_property
    def cloud_connector_subscriptions(self) -> AsyncCloudConnectorSubscriptions:
        return AsyncCloudConnectorSubscriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def configuration_files(self) -> AsyncConfigurationFiles:
        return AsyncConfigurationFiles(self._raw_client, self._server, self._auth)

    @cached_property
    def connectivity_callbacks(self) -> AsyncConnectivityCallbacks:
        return AsyncConnectivityCallbacks(self._raw_client, self._server, self._auth)

    @cached_property
    def create_price_plan_triggers(self) -> AsyncCreatePricePlanTriggers:
        return AsyncCreatePricePlanTriggers(self._raw_client, self._server, self._auth)

    @cached_property
    def device_actions(self) -> AsyncDeviceActions:
        return AsyncDeviceActions(self._raw_client, self._server, self._auth)

    @cached_property
    def device_credential_management(self) -> AsyncDeviceCredentialManagement:
        return AsyncDeviceCredentialManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def device_diagnostics(self) -> AsyncDeviceDiagnostics:
        return AsyncDeviceDiagnostics(self._raw_client, self._server, self._auth)

    @cached_property
    def device_groups(self) -> AsyncDeviceGroups:
        return AsyncDeviceGroups(self._raw_client, self._server, self._auth)

    @cached_property
    def device_location_callbacks(self) -> AsyncDeviceLocationCallbacks:
        return AsyncDeviceLocationCallbacks(self._raw_client, self._server, self._auth)

    @cached_property
    def device_management(self) -> AsyncDeviceManagement:
        return AsyncDeviceManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def device_monitoring(self) -> AsyncDeviceMonitoring:
        return AsyncDeviceMonitoring(self._raw_client, self._server, self._auth)

    @cached_property
    def device_profile_management(self) -> AsyncDeviceProfileManagement:
        return AsyncDeviceProfileManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def device_reports(self) -> AsyncDeviceReports:
        return AsyncDeviceReports(self._raw_client, self._server, self._auth)

    @cached_property
    def device_sms_messaging(self) -> AsyncDeviceSmsMessaging:
        return AsyncDeviceSmsMessaging(self._raw_client, self._server, self._auth)

    @cached_property
    def device_service_management(self) -> AsyncDeviceServiceManagement:
        return AsyncDeviceServiceManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def devices_location_subscriptions(self) -> AsyncDevicesLocationSubscriptions:
        return AsyncDevicesLocationSubscriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def devices_locations(self) -> AsyncDevicesLocations:
        return AsyncDevicesLocations(self._raw_client, self._server, self._auth)

    @cached_property
    def diagnostics_callbacks(self) -> AsyncDiagnosticsCallbacks:
        return AsyncDiagnosticsCallbacks(self._raw_client, self._server, self._auth)

    @cached_property
    def diagnostics_factory_reset(self) -> AsyncDiagnosticsFactoryReset:
        return AsyncDiagnosticsFactoryReset(self._raw_client, self._server, self._auth)

    @cached_property
    def diagnostics_history(self) -> AsyncDiagnosticsHistory:
        return AsyncDiagnosticsHistory(self._raw_client, self._server, self._auth)

    @cached_property
    def diagnostics_observations(self) -> AsyncDiagnosticsObservations:
        return AsyncDiagnosticsObservations(self._raw_client, self._server, self._auth)

    @cached_property
    def diagnostics_settings(self) -> AsyncDiagnosticsSettings:
        return AsyncDiagnosticsSettings(self._raw_client, self._server, self._auth)

    @cached_property
    def diagnostics_subscriptions(self) -> AsyncDiagnosticsSubscriptions:
        return AsyncDiagnosticsSubscriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def etxapp_configuration(self) -> AsyncEtxappConfiguration:
        return AsyncEtxappConfiguration(self._raw_client, self._server, self._auth)

    @cached_property
    def etxregistration(self) -> AsyncEtxregistration:
        return AsyncEtxregistration(self._raw_client, self._server, self._auth)

    @cached_property
    def exclusions(self) -> AsyncExclusions:
        return AsyncExclusions(self._raw_client, self._server, self._auth)

    @cached_property
    def firmware_v1(self) -> AsyncFirmwareV1:
        return AsyncFirmwareV1(self._raw_client, self._server, self._auth)

    @cached_property
    def firmware_v3(self) -> AsyncFirmwareV3:
        return AsyncFirmwareV3(self._raw_client, self._server, self._auth)

    @cached_property
    def global_reporting(self) -> AsyncGlobalReporting:
        return AsyncGlobalReporting(self._raw_client, self._server, self._auth)

    @cached_property
    def hpl_device_management(self) -> AsyncHplDeviceManagement:
        return AsyncHplDeviceManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def hyper_precise_location_callbacks(self) -> AsyncHyperPreciseLocationCallbacks:
        return AsyncHyperPreciseLocationCallbacks(self._raw_client, self._server, self._auth)

    @cached_property
    def intelligence_service_controller(self) -> AsyncIntelligenceServiceController:
        return AsyncIntelligenceServiceController(self._raw_client, self._server, self._auth)

    @cached_property
    def managing_e_sim_profiles(self) -> AsyncManagingESimProfiles:
        return AsyncManagingESimProfiles(self._raw_client, self._server, self._auth)

    @cached_property
    def pwn(self) -> AsyncPwn:
        return AsyncPwn(self._raw_client, self._server, self._auth)

    @cached_property
    def promotion_period_information(self) -> AsyncPromotionPeriodInformation:
        return AsyncPromotionPeriodInformation(self._raw_client, self._server, self._auth)

    @cached_property
    def retrieve_rate_plan_list(self) -> AsyncRetrieveRatePlanList:
        return AsyncRetrieveRatePlanList(self._raw_client, self._server, self._auth)

    @cached_property
    def retrieve_the_triggers(self) -> AsyncRetrieveTheTriggers:
        return AsyncRetrieveTheTriggers(self._raw_client, self._server, self._auth)

    @cached_property
    def sim_actions(self) -> AsyncSimActions:
        return AsyncSimActions(self._raw_client, self._server, self._auth)

    @cached_property
    def sim_secure_for_io_t_licenses(self) -> AsyncSimSecureForIoTLicenses:
        return AsyncSimSecureForIoTLicenses(self._raw_client, self._server, self._auth)

    @cached_property
    def sms(self) -> AsyncSms:
        return AsyncSms(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_device_profile(self) -> AsyncSensorInsightsDeviceProfile:
        return AsyncSensorInsightsDeviceProfile(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_devices(self) -> AsyncSensorInsightsDevices:
        return AsyncSensorInsightsDevices(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_gateways(self) -> AsyncSensorInsightsGateways:
        return AsyncSensorInsightsGateways(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_health_score(self) -> AsyncSensorInsightsHealthScore:
        return AsyncSensorInsightsHealthScore(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_notification_groups(self) -> AsyncSensorInsightsNotificationGroups:
        return AsyncSensorInsightsNotificationGroups(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_rules(self) -> AsyncSensorInsightsRules:
        return AsyncSensorInsightsRules(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_sensors(self) -> AsyncSensorInsightsSensors:
        return AsyncSensorInsightsSensors(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_smart_alert_metrics(self) -> AsyncSensorInsightsSmartAlertMetrics:
        return AsyncSensorInsightsSmartAlertMetrics(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_smart_alerts(self) -> AsyncSensorInsightsSmartAlerts:
        return AsyncSensorInsightsSmartAlerts(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_users(self) -> AsyncSensorInsightsUsers:
        return AsyncSensorInsightsUsers(self._raw_client, self._server, self._auth)

    @cached_property
    def server_logging(self) -> AsyncServerLogging:
        return AsyncServerLogging(self._raw_client, self._server, self._auth)

    @cached_property
    def service_plans(self) -> AsyncServicePlans:
        return AsyncServicePlans(self._raw_client, self._server, self._auth)

    @cached_property
    def session_management(self) -> AsyncSessionManagement:
        return AsyncSessionManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_callbacks_v1(self) -> AsyncSoftwareManagementCallbacksV1:
        return AsyncSoftwareManagementCallbacksV1(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_callbacks_v2(self) -> AsyncSoftwareManagementCallbacksV2:
        return AsyncSoftwareManagementCallbacksV2(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_callbacks_v3(self) -> AsyncSoftwareManagementCallbacksV3:
        return AsyncSoftwareManagementCallbacksV3(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_licenses_v1(self) -> AsyncSoftwareManagementLicensesV1:
        return AsyncSoftwareManagementLicensesV1(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_licenses_v2(self) -> AsyncSoftwareManagementLicensesV2:
        return AsyncSoftwareManagementLicensesV2(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_licenses_v3(self) -> AsyncSoftwareManagementLicensesV3:
        return AsyncSoftwareManagementLicensesV3(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_reports_v1(self) -> AsyncSoftwareManagementReportsV1:
        return AsyncSoftwareManagementReportsV1(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_reports_v2(self) -> AsyncSoftwareManagementReportsV2:
        return AsyncSoftwareManagementReportsV2(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_reports_v3(self) -> AsyncSoftwareManagementReportsV3:
        return AsyncSoftwareManagementReportsV3(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_subscriptions_v1(self) -> AsyncSoftwareManagementSubscriptionsV1:
        return AsyncSoftwareManagementSubscriptionsV1(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_subscriptions_v2(self) -> AsyncSoftwareManagementSubscriptionsV2:
        return AsyncSoftwareManagementSubscriptionsV2(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_subscriptions_v3(self) -> AsyncSoftwareManagementSubscriptionsV3:
        return AsyncSoftwareManagementSubscriptionsV3(self._raw_client, self._server, self._auth)

    @cached_property
    def targets(self) -> AsyncTargets:
        return AsyncTargets(self._raw_client, self._server, self._auth)

    @cached_property
    def thing_space_quality_of_service_api_actions(self) -> AsyncThingSpaceQualityOfServiceApiActions:
        return AsyncThingSpaceQualityOfServiceApiActions(self._raw_client, self._server, self._auth)

    @cached_property
    def update_price_plan_triggers(self) -> AsyncUpdatePricePlanTriggers:
        return AsyncUpdatePricePlanTriggers(self._raw_client, self._server, self._auth)

    @cached_property
    def update_triggers(self) -> AsyncUpdateTriggers:
        return AsyncUpdateTriggers(self._raw_client, self._server, self._auth)

    @cached_property
    def usage_trigger_management(self) -> AsyncUsageTriggerManagement:
        return AsyncUsageTriggerManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def wireless_network_performance(self) -> AsyncWirelessNetworkPerformance:
        return AsyncWirelessNetworkPerformance(self._raw_client, self._server, self._auth)

    @cached_property
    def device_role_controller(self) -> AsyncDeviceRoleController:
        return AsyncDeviceRoleController(self._raw_client, self._server, self._auth)

    @cached_property
    def e_uicc_device_profile_management(self) -> AsyncEUiccDeviceProfileManagement:
        return AsyncEUiccDeviceProfileManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def map_message_controller(self) -> AsyncMapMessageController:
        return AsyncMapMessageController(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncVerizonClient
