from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.account_devices import AccountDevices
from .apis.account_requests import AccountRequests
from .apis.account_service_controller import AccountServiceController
from .apis.account_subscriptions import AccountSubscriptions
from .apis.accounts import Accounts
from .apis.anomaly_settings import AnomalySettings
from .apis.anomaly_triggers import AnomalyTriggers
from .apis.anomaly_triggers_v2 import AnomalyTriggersV2
from .apis.billing import Billing
from .apis.campaigns_v2 import CampaignsV2
from .apis.campaigns_v3 import CampaignsV3
from .apis.client_logging import ClientLogging
from .apis.cloud_connector_devices import CloudConnectorDevices
from .apis.cloud_connector_subscriptions import CloudConnectorSubscriptions
from .apis.configuration_files import ConfigurationFiles
from .apis.connectivity_callbacks import ConnectivityCallbacks
from .apis.create_price_plan_triggers import CreatePricePlanTriggers
from .apis.device_actions import DeviceActions
from .apis.device_credential_management import DeviceCredentialManagement
from .apis.device_diagnostics import DeviceDiagnostics
from .apis.device_groups import DeviceGroups
from .apis.device_location_callbacks import DeviceLocationCallbacks
from .apis.device_management import DeviceManagement
from .apis.device_monitoring import DeviceMonitoring
from .apis.device_profile_management import DeviceProfileManagement
from .apis.device_reports import DeviceReports
from .apis.device_role_controller import DeviceRoleController
from .apis.device_service_management import DeviceServiceManagement
from .apis.device_sms_messaging import DeviceSmsMessaging
from .apis.devices_location_subscriptions import DevicesLocationSubscriptions
from .apis.devices_locations import DevicesLocations
from .apis.diagnostics_callbacks import DiagnosticsCallbacks
from .apis.diagnostics_factory_reset import DiagnosticsFactoryReset
from .apis.diagnostics_history import DiagnosticsHistory
from .apis.diagnostics_observations import DiagnosticsObservations
from .apis.diagnostics_settings import DiagnosticsSettings
from .apis.diagnostics_subscriptions import DiagnosticsSubscriptions
from .apis.e_uicc_device_profile_management import EUiccDeviceProfileManagement
from .apis.etxapp_configuration import EtxappConfiguration
from .apis.etxregistration import Etxregistration
from .apis.exclusions import Exclusions
from .apis.firmware_v1 import FirmwareV1
from .apis.firmware_v3 import FirmwareV3
from .apis.gbi_device_actions5 import GbiDeviceActions5
from .apis.global_reporting import GlobalReporting
from .apis.hpl_device_management import HplDeviceManagement
from .apis.hyper_precise_location_callbacks import HyperPreciseLocationCallbacks
from .apis.intelligence_service_controller import IntelligenceServiceController
from .apis.managing_e_sim_profiles import ManagingESimProfiles
from .apis.map_message_controller import MapMessageController
from .apis.promotion_period_information import PromotionPeriodInformation
from .apis.pwn import Pwn
from .apis.retrieve_rate_plan_list import RetrieveRatePlanList
from .apis.retrieve_the_triggers import RetrieveTheTriggers
from .apis.sensor_insights_device_profile import SensorInsightsDeviceProfile
from .apis.sensor_insights_devices import SensorInsightsDevices
from .apis.sensor_insights_gateways import SensorInsightsGateways
from .apis.sensor_insights_health_score import SensorInsightsHealthScore
from .apis.sensor_insights_notification_groups import SensorInsightsNotificationGroups
from .apis.sensor_insights_rules import SensorInsightsRules
from .apis.sensor_insights_sensors import SensorInsightsSensors
from .apis.sensor_insights_smart_alert_metrics import SensorInsightsSmartAlertMetrics
from .apis.sensor_insights_smart_alerts import SensorInsightsSmartAlerts
from .apis.sensor_insights_users import SensorInsightsUsers
from .apis.server_logging import ServerLogging
from .apis.service_plans import ServicePlans
from .apis.session_management import SessionManagement
from .apis.sim_actions import SimActions
from .apis.sim_secure_for_io_t_licenses import SimSecureForIoTLicenses
from .apis.sms import Sms
from .apis.software_management_callbacks_v1 import SoftwareManagementCallbacksV1
from .apis.software_management_callbacks_v2 import SoftwareManagementCallbacksV2
from .apis.software_management_callbacks_v3 import SoftwareManagementCallbacksV3
from .apis.software_management_licenses_v1 import SoftwareManagementLicensesV1
from .apis.software_management_licenses_v2 import SoftwareManagementLicensesV2
from .apis.software_management_licenses_v3 import SoftwareManagementLicensesV3
from .apis.software_management_reports_v1 import SoftwareManagementReportsV1
from .apis.software_management_reports_v2 import SoftwareManagementReportsV2
from .apis.software_management_reports_v3 import SoftwareManagementReportsV3
from .apis.software_management_subscriptions_v1 import SoftwareManagementSubscriptionsV1
from .apis.software_management_subscriptions_v2 import SoftwareManagementSubscriptionsV2
from .apis.software_management_subscriptions_v3 import SoftwareManagementSubscriptionsV3
from .apis.targets import Targets
from .apis.thing_space_quality_of_service_api_actions import ThingSpaceQualityOfServiceApiActions
from .apis.update_price_plan_triggers import UpdatePricePlanTriggers
from .apis.update_triggers import UpdateTriggers
from .apis.usage_trigger_management import UsageTriggerManagement
from .apis.wireless_network_performance import WirelessNetworkPerformance
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseVerizonClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    ClientCredentials,
    ClientCredentialsOrDict,
    ClientCredentialsTokenSource,
    HttpClient,
    HttpxClient,
    OAuth2Scheme,
    RawClient,
    TokenSource,
    client_secret_basic,
    no_auth,
    param,
)
from .server.environment import Environment
from .server.server_config import ServerConfigOrDict


class VerizonClient(BaseVerizonClient[RawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        timeout: float = DEFAULT_TIMEOUT,
        server_config: ServerConfigOrDict | None = None,
        custom_http_client: HttpClient | None = None,
        thingspace_oauth: ClientCredentialsOrDict | None = None,
        thingspace_oauth_token_source: TokenSource[ClientCredentials] | None = None,
        vz_m2_m_token: str | None = None,
        session_token: str | None = None,
        thingspace_oauth1: ClientCredentialsOrDict | None = None,
        thingspace_oauth1_token_source: TokenSource[ClientCredentials] | None = None,
    ) -> None:
        super().__init__(environment=environment, timeout=timeout, server_config=server_config)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout),
            global_headers=[
                param[str]("User-Agent", "VerizonClient/v1.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "v1.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(
            thingspace_oauth=(
                OAuth2Scheme(
                    credentials=ClientCredentials.coerce(thingspace_oauth),
                    source=(
                        thingspace_oauth_token_source
                        if thingspace_oauth_token_source is not None
                        else ClientCredentialsTokenSource(
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
                OAuth2Scheme(
                    credentials=ClientCredentials.coerce(thingspace_oauth1),
                    source=(
                        thingspace_oauth1_token_source
                        if thingspace_oauth1_token_source is not None
                        else ClientCredentialsTokenSource(
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
    def gbi_device_actions5(self) -> GbiDeviceActions5:
        return GbiDeviceActions5(self._raw_client, self._server, self._auth)

    @cached_property
    def account_devices(self) -> AccountDevices:
        return AccountDevices(self._raw_client, self._server, self._auth)

    @cached_property
    def account_requests(self) -> AccountRequests:
        return AccountRequests(self._raw_client, self._server, self._auth)

    @cached_property
    def account_service_controller(self) -> AccountServiceController:
        return AccountServiceController(self._raw_client, self._server, self._auth)

    @cached_property
    def account_subscriptions(self) -> AccountSubscriptions:
        return AccountSubscriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def accounts(self) -> Accounts:
        return Accounts(self._raw_client, self._server, self._auth)

    @cached_property
    def anomaly_settings(self) -> AnomalySettings:
        return AnomalySettings(self._raw_client, self._server, self._auth)

    @cached_property
    def anomaly_triggers(self) -> AnomalyTriggers:
        return AnomalyTriggers(self._raw_client, self._server, self._auth)

    @cached_property
    def anomaly_triggers_v2(self) -> AnomalyTriggersV2:
        return AnomalyTriggersV2(self._raw_client, self._server, self._auth)

    @cached_property
    def billing(self) -> Billing:
        return Billing(self._raw_client, self._server, self._auth)

    @cached_property
    def campaigns_v2(self) -> CampaignsV2:
        return CampaignsV2(self._raw_client, self._server, self._auth)

    @cached_property
    def campaigns_v3(self) -> CampaignsV3:
        return CampaignsV3(self._raw_client, self._server, self._auth)

    @cached_property
    def client_logging(self) -> ClientLogging:
        return ClientLogging(self._raw_client, self._server, self._auth)

    @cached_property
    def cloud_connector_devices(self) -> CloudConnectorDevices:
        return CloudConnectorDevices(self._raw_client, self._server, self._auth)

    @cached_property
    def cloud_connector_subscriptions(self) -> CloudConnectorSubscriptions:
        return CloudConnectorSubscriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def configuration_files(self) -> ConfigurationFiles:
        return ConfigurationFiles(self._raw_client, self._server, self._auth)

    @cached_property
    def connectivity_callbacks(self) -> ConnectivityCallbacks:
        return ConnectivityCallbacks(self._raw_client, self._server, self._auth)

    @cached_property
    def create_price_plan_triggers(self) -> CreatePricePlanTriggers:
        return CreatePricePlanTriggers(self._raw_client, self._server, self._auth)

    @cached_property
    def device_actions(self) -> DeviceActions:
        return DeviceActions(self._raw_client, self._server, self._auth)

    @cached_property
    def device_credential_management(self) -> DeviceCredentialManagement:
        return DeviceCredentialManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def device_diagnostics(self) -> DeviceDiagnostics:
        return DeviceDiagnostics(self._raw_client, self._server, self._auth)

    @cached_property
    def device_groups(self) -> DeviceGroups:
        return DeviceGroups(self._raw_client, self._server, self._auth)

    @cached_property
    def device_location_callbacks(self) -> DeviceLocationCallbacks:
        return DeviceLocationCallbacks(self._raw_client, self._server, self._auth)

    @cached_property
    def device_management(self) -> DeviceManagement:
        return DeviceManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def device_monitoring(self) -> DeviceMonitoring:
        return DeviceMonitoring(self._raw_client, self._server, self._auth)

    @cached_property
    def device_profile_management(self) -> DeviceProfileManagement:
        return DeviceProfileManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def device_reports(self) -> DeviceReports:
        return DeviceReports(self._raw_client, self._server, self._auth)

    @cached_property
    def device_sms_messaging(self) -> DeviceSmsMessaging:
        return DeviceSmsMessaging(self._raw_client, self._server, self._auth)

    @cached_property
    def device_service_management(self) -> DeviceServiceManagement:
        return DeviceServiceManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def devices_location_subscriptions(self) -> DevicesLocationSubscriptions:
        return DevicesLocationSubscriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def devices_locations(self) -> DevicesLocations:
        return DevicesLocations(self._raw_client, self._server, self._auth)

    @cached_property
    def diagnostics_callbacks(self) -> DiagnosticsCallbacks:
        return DiagnosticsCallbacks(self._raw_client, self._server, self._auth)

    @cached_property
    def diagnostics_factory_reset(self) -> DiagnosticsFactoryReset:
        return DiagnosticsFactoryReset(self._raw_client, self._server, self._auth)

    @cached_property
    def diagnostics_history(self) -> DiagnosticsHistory:
        return DiagnosticsHistory(self._raw_client, self._server, self._auth)

    @cached_property
    def diagnostics_observations(self) -> DiagnosticsObservations:
        return DiagnosticsObservations(self._raw_client, self._server, self._auth)

    @cached_property
    def diagnostics_settings(self) -> DiagnosticsSettings:
        return DiagnosticsSettings(self._raw_client, self._server, self._auth)

    @cached_property
    def diagnostics_subscriptions(self) -> DiagnosticsSubscriptions:
        return DiagnosticsSubscriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def etxapp_configuration(self) -> EtxappConfiguration:
        return EtxappConfiguration(self._raw_client, self._server, self._auth)

    @cached_property
    def etxregistration(self) -> Etxregistration:
        return Etxregistration(self._raw_client, self._server, self._auth)

    @cached_property
    def exclusions(self) -> Exclusions:
        return Exclusions(self._raw_client, self._server, self._auth)

    @cached_property
    def firmware_v1(self) -> FirmwareV1:
        return FirmwareV1(self._raw_client, self._server, self._auth)

    @cached_property
    def firmware_v3(self) -> FirmwareV3:
        return FirmwareV3(self._raw_client, self._server, self._auth)

    @cached_property
    def global_reporting(self) -> GlobalReporting:
        return GlobalReporting(self._raw_client, self._server, self._auth)

    @cached_property
    def hpl_device_management(self) -> HplDeviceManagement:
        return HplDeviceManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def hyper_precise_location_callbacks(self) -> HyperPreciseLocationCallbacks:
        return HyperPreciseLocationCallbacks(self._raw_client, self._server, self._auth)

    @cached_property
    def intelligence_service_controller(self) -> IntelligenceServiceController:
        return IntelligenceServiceController(self._raw_client, self._server, self._auth)

    @cached_property
    def managing_e_sim_profiles(self) -> ManagingESimProfiles:
        return ManagingESimProfiles(self._raw_client, self._server, self._auth)

    @cached_property
    def pwn(self) -> Pwn:
        return Pwn(self._raw_client, self._server, self._auth)

    @cached_property
    def promotion_period_information(self) -> PromotionPeriodInformation:
        return PromotionPeriodInformation(self._raw_client, self._server, self._auth)

    @cached_property
    def retrieve_rate_plan_list(self) -> RetrieveRatePlanList:
        return RetrieveRatePlanList(self._raw_client, self._server, self._auth)

    @cached_property
    def retrieve_the_triggers(self) -> RetrieveTheTriggers:
        return RetrieveTheTriggers(self._raw_client, self._server, self._auth)

    @cached_property
    def sim_actions(self) -> SimActions:
        return SimActions(self._raw_client, self._server, self._auth)

    @cached_property
    def sim_secure_for_io_t_licenses(self) -> SimSecureForIoTLicenses:
        return SimSecureForIoTLicenses(self._raw_client, self._server, self._auth)

    @cached_property
    def sms(self) -> Sms:
        return Sms(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_device_profile(self) -> SensorInsightsDeviceProfile:
        return SensorInsightsDeviceProfile(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_devices(self) -> SensorInsightsDevices:
        return SensorInsightsDevices(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_gateways(self) -> SensorInsightsGateways:
        return SensorInsightsGateways(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_health_score(self) -> SensorInsightsHealthScore:
        return SensorInsightsHealthScore(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_notification_groups(self) -> SensorInsightsNotificationGroups:
        return SensorInsightsNotificationGroups(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_rules(self) -> SensorInsightsRules:
        return SensorInsightsRules(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_sensors(self) -> SensorInsightsSensors:
        return SensorInsightsSensors(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_smart_alert_metrics(self) -> SensorInsightsSmartAlertMetrics:
        return SensorInsightsSmartAlertMetrics(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_smart_alerts(self) -> SensorInsightsSmartAlerts:
        return SensorInsightsSmartAlerts(self._raw_client, self._server, self._auth)

    @cached_property
    def sensor_insights_users(self) -> SensorInsightsUsers:
        return SensorInsightsUsers(self._raw_client, self._server, self._auth)

    @cached_property
    def server_logging(self) -> ServerLogging:
        return ServerLogging(self._raw_client, self._server, self._auth)

    @cached_property
    def service_plans(self) -> ServicePlans:
        return ServicePlans(self._raw_client, self._server, self._auth)

    @cached_property
    def session_management(self) -> SessionManagement:
        return SessionManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_callbacks_v1(self) -> SoftwareManagementCallbacksV1:
        return SoftwareManagementCallbacksV1(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_callbacks_v2(self) -> SoftwareManagementCallbacksV2:
        return SoftwareManagementCallbacksV2(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_callbacks_v3(self) -> SoftwareManagementCallbacksV3:
        return SoftwareManagementCallbacksV3(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_licenses_v1(self) -> SoftwareManagementLicensesV1:
        return SoftwareManagementLicensesV1(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_licenses_v2(self) -> SoftwareManagementLicensesV2:
        return SoftwareManagementLicensesV2(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_licenses_v3(self) -> SoftwareManagementLicensesV3:
        return SoftwareManagementLicensesV3(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_reports_v1(self) -> SoftwareManagementReportsV1:
        return SoftwareManagementReportsV1(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_reports_v2(self) -> SoftwareManagementReportsV2:
        return SoftwareManagementReportsV2(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_reports_v3(self) -> SoftwareManagementReportsV3:
        return SoftwareManagementReportsV3(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_subscriptions_v1(self) -> SoftwareManagementSubscriptionsV1:
        return SoftwareManagementSubscriptionsV1(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_subscriptions_v2(self) -> SoftwareManagementSubscriptionsV2:
        return SoftwareManagementSubscriptionsV2(self._raw_client, self._server, self._auth)

    @cached_property
    def software_management_subscriptions_v3(self) -> SoftwareManagementSubscriptionsV3:
        return SoftwareManagementSubscriptionsV3(self._raw_client, self._server, self._auth)

    @cached_property
    def targets(self) -> Targets:
        return Targets(self._raw_client, self._server, self._auth)

    @cached_property
    def thing_space_quality_of_service_api_actions(self) -> ThingSpaceQualityOfServiceApiActions:
        return ThingSpaceQualityOfServiceApiActions(self._raw_client, self._server, self._auth)

    @cached_property
    def update_price_plan_triggers(self) -> UpdatePricePlanTriggers:
        return UpdatePricePlanTriggers(self._raw_client, self._server, self._auth)

    @cached_property
    def update_triggers(self) -> UpdateTriggers:
        return UpdateTriggers(self._raw_client, self._server, self._auth)

    @cached_property
    def usage_trigger_management(self) -> UsageTriggerManagement:
        return UsageTriggerManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def wireless_network_performance(self) -> WirelessNetworkPerformance:
        return WirelessNetworkPerformance(self._raw_client, self._server, self._auth)

    @cached_property
    def device_role_controller(self) -> DeviceRoleController:
        return DeviceRoleController(self._raw_client, self._server, self._auth)

    @cached_property
    def e_uicc_device_profile_management(self) -> EUiccDeviceProfileManagement:
        return EUiccDeviceProfileManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def map_message_controller(self) -> MapMessageController:
        return MapMessageController(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = VerizonClient
