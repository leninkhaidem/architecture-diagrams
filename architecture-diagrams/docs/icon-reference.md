# Architecture Diagrams — Icon Reference

Complete catalog of all available icons in the Diagrams Python library.

**Total Icons:** 2634 across 17 providers

---

## Table of Contents

1. [Generic](#generic) (26 icons)
2. [Amazon Web Services (AWS)](#amazon-web-services-aws) (562 icons)
3. [Microsoft Azure](#microsoft-azure) (810 icons)
4. [Google Cloud Platform (GCP)](#google-cloud-platform-gcp) (144 icons)
5. [Kubernetes](#kubernetes) (69 icons)
6. [On-Premise](#on-premise) (211 icons)
7. [SaaS](#saas) (42 icons)
8. [Programming](#programming) (81 icons)
9. [Elastic Stack](#elastic-stack) (47 icons)
10. [Firebase](#firebase) (23 icons)
11. [DigitalOcean](#digitalocean) (25 icons)
12. [IBM Cloud](#ibm-cloud) (180 icons)
13. [Oracle Cloud Infrastructure (OCI)](#oracle-cloud-infrastructure-oci) (152 icons)
14. [OpenStack](#openstack) (54 icons)
15. [Outscale](#outscale) (12 icons)
16. [Alibaba Cloud](#alibaba-cloud) (131 icons)
17. [GIS (Geospatial)](#gis-geospatial) (65 icons)

---

## Generic

_General-purpose infrastructure icons for network devices, compute, databases, storage, OS, and more_ — **26 icons** across **9 categories**

### Blank (Layout)

**Import:** `from diagrams.generic.blank import ...`

| Class Name | Import Example |
|------------|---------------|
| `Blank` | `from diagrams.generic.blank import Blank` |

### Compute

**Import:** `from diagrams.generic.compute import ...`

| Class Name | Import Example |
|------------|---------------|
| `Rack` | `from diagrams.generic.compute import Rack` |

### Database

**Import:** `from diagrams.generic.database import ...`

| Class Name | Import Example |
|------------|---------------|
| `SQL` | `from diagrams.generic.database import SQL` |

### Device

**Import:** `from diagrams.generic.device import ...`

| Class Name | Import Example |
|------------|---------------|
| `Mobile` | `from diagrams.generic.device import Mobile` |
| `Tablet` | `from diagrams.generic.device import Tablet` |

### Network

**Import:** `from diagrams.generic.network import ...`

| Class Name | Import Example |
|------------|---------------|
| `Firewall` | `from diagrams.generic.network import Firewall` |
| `Router` | `from diagrams.generic.network import Router` |
| `Subnet` | `from diagrams.generic.network import Subnet` |
| `Switch` | `from diagrams.generic.network import Switch` |
| `VPN` | `from diagrams.generic.network import VPN` |

### Operating System

**Import:** `from diagrams.generic.os import ...`

| Class Name | Import Example |
|------------|---------------|
| `Android` | `from diagrams.generic.os import Android` |
| `Centos` | `from diagrams.generic.os import Centos` |
| `Debian` | `from diagrams.generic.os import Debian` |
| `IOS` | `from diagrams.generic.os import IOS` |
| `LinuxGeneral` | `from diagrams.generic.os import LinuxGeneral` |
| `Raspbian` | `from diagrams.generic.os import Raspbian` |
| `RedHat` | `from diagrams.generic.os import RedHat` |
| `Suse` | `from diagrams.generic.os import Suse` |
| `Ubuntu` | `from diagrams.generic.os import Ubuntu` |
| `Windows` | `from diagrams.generic.os import Windows` |

### Place

**Import:** `from diagrams.generic.place import ...`

| Class Name | Import Example |
|------------|---------------|
| `Datacenter` | `from diagrams.generic.place import Datacenter` |

### Storage

**Import:** `from diagrams.generic.storage import ...`

| Class Name | Import Example |
|------------|---------------|
| `Storage` | `from diagrams.generic.storage import Storage` |

### Virtualization

**Import:** `from diagrams.generic.virtualization import ...`

| Class Name | Import Example |
|------------|---------------|
| `Qemu` | `from diagrams.generic.virtualization import Qemu` |
| `Virtualbox` | `from diagrams.generic.virtualization import Virtualbox` |
| `Vmware` | `from diagrams.generic.virtualization import Vmware` |
| `XEN` | `from diagrams.generic.virtualization import XEN` |

---

## Amazon Web Services (AWS)

_Complete AWS service icon catalog_ — **562 icons** across **26 categories**

### Analytics

**Import:** `from diagrams.aws.analytics import ...`

| Class Name | Import Example |
|------------|---------------|
| `AmazonOpensearchService` | `from diagrams.aws.analytics import AmazonOpensearchService` |
| `Analytics` | `from diagrams.aws.analytics import Analytics` |
| `Athena` | `from diagrams.aws.analytics import Athena` |
| `Cloudsearch` | `from diagrams.aws.analytics import Cloudsearch` |
| `CloudsearchSearchDocuments` | `from diagrams.aws.analytics import CloudsearchSearchDocuments` |
| `DataLakeResource` | `from diagrams.aws.analytics import DataLakeResource` |
| `DataPipeline` | `from diagrams.aws.analytics import DataPipeline` |
| `EMR` | `from diagrams.aws.analytics import EMR` |
| `EMRCluster` | `from diagrams.aws.analytics import EMRCluster` |
| `EMREngine` | `from diagrams.aws.analytics import EMREngine` |
| `EMREngineMaprM3` | `from diagrams.aws.analytics import EMREngineMaprM3` |
| `EMREngineMaprM5` | `from diagrams.aws.analytics import EMREngineMaprM5` |
| `EMREngineMaprM7` | `from diagrams.aws.analytics import EMREngineMaprM7` |
| `EMRHdfsCluster` | `from diagrams.aws.analytics import EMRHdfsCluster` |
| `ES` | `from diagrams.aws.analytics import ES` |
| `ElasticsearchService` | `from diagrams.aws.analytics import ElasticsearchService` |
| `Glue` | `from diagrams.aws.analytics import Glue` |
| `GlueCrawlers` | `from diagrams.aws.analytics import GlueCrawlers` |
| `GlueDataCatalog` | `from diagrams.aws.analytics import GlueDataCatalog` |
| `Kinesis` | `from diagrams.aws.analytics import Kinesis` |
| `KinesisDataAnalytics` | `from diagrams.aws.analytics import KinesisDataAnalytics` |
| `KinesisDataFirehose` | `from diagrams.aws.analytics import KinesisDataFirehose` |
| `KinesisDataStreams` | `from diagrams.aws.analytics import KinesisDataStreams` |
| `KinesisVideoStreams` | `from diagrams.aws.analytics import KinesisVideoStreams` |
| `LakeFormation` | `from diagrams.aws.analytics import LakeFormation` |
| `ManagedStreamingForKafka` | `from diagrams.aws.analytics import ManagedStreamingForKafka` |
| `Quicksight` | `from diagrams.aws.analytics import Quicksight` |
| `Redshift` | `from diagrams.aws.analytics import Redshift` |
| `RedshiftDenseComputeNode` | `from diagrams.aws.analytics import RedshiftDenseComputeNode` |
| `RedshiftDenseStorageNode` | `from diagrams.aws.analytics import RedshiftDenseStorageNode` |

### AR/VR

**Import:** `from diagrams.aws.ar import ...`

| Class Name | Import Example |
|------------|---------------|
| `ArVr` | `from diagrams.aws.ar import ArVr` |
| `Sumerian` | `from diagrams.aws.ar import Sumerian` |

### Blockchain

**Import:** `from diagrams.aws.blockchain import ...`

| Class Name | Import Example |
|------------|---------------|
| `Blockchain` | `from diagrams.aws.blockchain import Blockchain` |
| `BlockchainResource` | `from diagrams.aws.blockchain import BlockchainResource` |
| `ManagedBlockchain` | `from diagrams.aws.blockchain import ManagedBlockchain` |
| `QLDB` | `from diagrams.aws.blockchain import QLDB` |
| `QuantumLedgerDatabaseQldb` | `from diagrams.aws.blockchain import QuantumLedgerDatabaseQldb` |

### Business

**Import:** `from diagrams.aws.business import ...`

| Class Name | Import Example |
|------------|---------------|
| `A4B` | `from diagrams.aws.business import A4B` |
| `AlexaForBusiness` | `from diagrams.aws.business import AlexaForBusiness` |
| `BusinessApplications` | `from diagrams.aws.business import BusinessApplications` |
| `Chime` | `from diagrams.aws.business import Chime` |
| `Workmail` | `from diagrams.aws.business import Workmail` |

### Compute

**Import:** `from diagrams.aws.compute import ...`

| Class Name | Import Example |
|------------|---------------|
| `AMI` | `from diagrams.aws.compute import AMI` |
| `AppRunner` | `from diagrams.aws.compute import AppRunner` |
| `ApplicationAutoScaling` | `from diagrams.aws.compute import ApplicationAutoScaling` |
| `AutoScaling` | `from diagrams.aws.compute import AutoScaling` |
| `Batch` | `from diagrams.aws.compute import Batch` |
| `Compute` | `from diagrams.aws.compute import Compute` |
| `ComputeOptimizer` | `from diagrams.aws.compute import ComputeOptimizer` |
| `EB` | `from diagrams.aws.compute import EB` |
| `EC2` | `from diagrams.aws.compute import EC2` |
| `EC2Ami` | `from diagrams.aws.compute import EC2Ami` |
| `EC2AutoScaling` | `from diagrams.aws.compute import EC2AutoScaling` |
| `EC2ContainerRegistry` | `from diagrams.aws.compute import EC2ContainerRegistry` |
| `EC2ContainerRegistryImage` | `from diagrams.aws.compute import EC2ContainerRegistryImage` |
| `EC2ContainerRegistryRegistry` | `from diagrams.aws.compute import EC2ContainerRegistryRegistry` |
| `EC2ElasticIpAddress` | `from diagrams.aws.compute import EC2ElasticIpAddress` |
| `EC2ImageBuilder` | `from diagrams.aws.compute import EC2ImageBuilder` |
| `EC2Instance` | `from diagrams.aws.compute import EC2Instance` |
| `EC2Instances` | `from diagrams.aws.compute import EC2Instances` |
| `EC2Rescue` | `from diagrams.aws.compute import EC2Rescue` |
| `EC2SpotInstance` | `from diagrams.aws.compute import EC2SpotInstance` |
| `ECR` | `from diagrams.aws.compute import ECR` |
| `ECS` | `from diagrams.aws.compute import ECS` |
| `EKS` | `from diagrams.aws.compute import EKS` |
| `ElasticBeanstalk` | `from diagrams.aws.compute import ElasticBeanstalk` |
| `ElasticBeanstalkApplication` | `from diagrams.aws.compute import ElasticBeanstalkApplication` |
| `ElasticBeanstalkDeployment` | `from diagrams.aws.compute import ElasticBeanstalkDeployment` |
| `ElasticContainerService` | `from diagrams.aws.compute import ElasticContainerService` |
| `ElasticContainerServiceContainer` | `from diagrams.aws.compute import ElasticContainerServiceContainer` |
| `ElasticContainerServiceService` | `from diagrams.aws.compute import ElasticContainerServiceService` |
| `ElasticContainerServiceServiceConnect` | `from diagrams.aws.compute import ElasticContainerServiceServiceConnect` |
| `ElasticContainerServiceTask` | `from diagrams.aws.compute import ElasticContainerServiceTask` |
| `ElasticKubernetesService` | `from diagrams.aws.compute import ElasticKubernetesService` |
| `Fargate` | `from diagrams.aws.compute import Fargate` |
| `Lambda` | `from diagrams.aws.compute import Lambda` |
| `LambdaFunction` | `from diagrams.aws.compute import LambdaFunction` |
| `Lightsail` | `from diagrams.aws.compute import Lightsail` |
| `LocalZones` | `from diagrams.aws.compute import LocalZones` |
| `Outposts` | `from diagrams.aws.compute import Outposts` |
| `SAR` | `from diagrams.aws.compute import SAR` |
| `ServerlessApplicationRepository` | `from diagrams.aws.compute import ServerlessApplicationRepository` |
| `ThinkboxDeadline` | `from diagrams.aws.compute import ThinkboxDeadline` |
| `ThinkboxDraft` | `from diagrams.aws.compute import ThinkboxDraft` |
| `ThinkboxFrost` | `from diagrams.aws.compute import ThinkboxFrost` |
| `ThinkboxKrakatoa` | `from diagrams.aws.compute import ThinkboxKrakatoa` |
| `ThinkboxSequoia` | `from diagrams.aws.compute import ThinkboxSequoia` |
| `ThinkboxStoke` | `from diagrams.aws.compute import ThinkboxStoke` |
| `ThinkboxXmesh` | `from diagrams.aws.compute import ThinkboxXmesh` |
| `VmwareCloudOnAWS` | `from diagrams.aws.compute import VmwareCloudOnAWS` |
| `Wavelength` | `from diagrams.aws.compute import Wavelength` |

### Cost Management

**Import:** `from diagrams.aws.cost import ...`

| Class Name | Import Example |
|------------|---------------|
| `Budgets` | `from diagrams.aws.cost import Budgets` |
| `CostAndUsageReport` | `from diagrams.aws.cost import CostAndUsageReport` |
| `CostExplorer` | `from diagrams.aws.cost import CostExplorer` |
| `CostManagement` | `from diagrams.aws.cost import CostManagement` |
| `ReservedInstanceReporting` | `from diagrams.aws.cost import ReservedInstanceReporting` |
| `SavingsPlans` | `from diagrams.aws.cost import SavingsPlans` |

### Database

**Import:** `from diagrams.aws.database import ...`

| Class Name | Import Example |
|------------|---------------|
| `Aurora` | `from diagrams.aws.database import Aurora` |
| `AuroraInstance` | `from diagrams.aws.database import AuroraInstance` |
| `DAX` | `from diagrams.aws.database import DAX` |
| `DB` | `from diagrams.aws.database import DB` |
| `DDB` | `from diagrams.aws.database import DDB` |
| `DMS` | `from diagrams.aws.database import DMS` |
| `Database` | `from diagrams.aws.database import Database` |
| `DatabaseMigrationService` | `from diagrams.aws.database import DatabaseMigrationService` |
| `DatabaseMigrationServiceDatabaseMigrationWorkflow` | `from diagrams.aws.database import DatabaseMigrationServiceDatabaseMigrationWorkflow` |
| `DocumentDB` | `from diagrams.aws.database import DocumentDB` |
| `DocumentdbMongodbCompatibility` | `from diagrams.aws.database import DocumentdbMongodbCompatibility` |
| `Dynamodb` | `from diagrams.aws.database import Dynamodb` |
| `DynamodbAttribute` | `from diagrams.aws.database import DynamodbAttribute` |
| `DynamodbAttributes` | `from diagrams.aws.database import DynamodbAttributes` |
| `DynamodbDax` | `from diagrams.aws.database import DynamodbDax` |
| `DynamodbGSI` | `from diagrams.aws.database import DynamodbGSI` |
| `DynamodbGlobalSecondaryIndex` | `from diagrams.aws.database import DynamodbGlobalSecondaryIndex` |
| `DynamodbItem` | `from diagrams.aws.database import DynamodbItem` |
| `DynamodbItems` | `from diagrams.aws.database import DynamodbItems` |
| `DynamodbStreams` | `from diagrams.aws.database import DynamodbStreams` |
| `DynamodbTable` | `from diagrams.aws.database import DynamodbTable` |
| `ElastiCache` | `from diagrams.aws.database import ElastiCache` |
| `Elasticache` | `from diagrams.aws.database import Elasticache` |
| `ElasticacheCacheNode` | `from diagrams.aws.database import ElasticacheCacheNode` |
| `ElasticacheForMemcached` | `from diagrams.aws.database import ElasticacheForMemcached` |
| `ElasticacheForRedis` | `from diagrams.aws.database import ElasticacheForRedis` |
| `KeyspacesManagedApacheCassandraService` | `from diagrams.aws.database import KeyspacesManagedApacheCassandraService` |
| `Neptune` | `from diagrams.aws.database import Neptune` |
| `QLDB` | `from diagrams.aws.database import QLDB` |
| `QuantumLedgerDatabaseQldb` | `from diagrams.aws.database import QuantumLedgerDatabaseQldb` |
| `RDS` | `from diagrams.aws.database import RDS` |
| `RDSInstance` | `from diagrams.aws.database import RDSInstance` |
| `RDSMariadbInstance` | `from diagrams.aws.database import RDSMariadbInstance` |
| `RDSMysqlInstance` | `from diagrams.aws.database import RDSMysqlInstance` |
| `RDSOnVmware` | `from diagrams.aws.database import RDSOnVmware` |
| `RDSOracleInstance` | `from diagrams.aws.database import RDSOracleInstance` |
| `RDSPostgresqlInstance` | `from diagrams.aws.database import RDSPostgresqlInstance` |
| `RDSSqlServerInstance` | `from diagrams.aws.database import RDSSqlServerInstance` |
| `Redshift` | `from diagrams.aws.database import Redshift` |
| `RedshiftDenseComputeNode` | `from diagrams.aws.database import RedshiftDenseComputeNode` |
| `RedshiftDenseStorageNode` | `from diagrams.aws.database import RedshiftDenseStorageNode` |
| `Timestream` | `from diagrams.aws.database import Timestream` |

### Developer Tools

**Import:** `from diagrams.aws.devtools import ...`

| Class Name | Import Example |
|------------|---------------|
| `CLI` | `from diagrams.aws.devtools import CLI` |
| `Cloud9` | `from diagrams.aws.devtools import Cloud9` |
| `Cloud9Resource` | `from diagrams.aws.devtools import Cloud9Resource` |
| `CloudDevelopmentKit` | `from diagrams.aws.devtools import CloudDevelopmentKit` |
| `Cloudshell` | `from diagrams.aws.devtools import Cloudshell` |
| `Codeartifact` | `from diagrams.aws.devtools import Codeartifact` |
| `Codebuild` | `from diagrams.aws.devtools import Codebuild` |
| `Codecommit` | `from diagrams.aws.devtools import Codecommit` |
| `Codedeploy` | `from diagrams.aws.devtools import Codedeploy` |
| `Codepipeline` | `from diagrams.aws.devtools import Codepipeline` |
| `Codestar` | `from diagrams.aws.devtools import Codestar` |
| `CommandLineInterface` | `from diagrams.aws.devtools import CommandLineInterface` |
| `DevTools` | `from diagrams.aws.devtools import DevTools` |
| `DeveloperTools` | `from diagrams.aws.devtools import DeveloperTools` |
| `ToolsAndSdks` | `from diagrams.aws.devtools import ToolsAndSdks` |
| `XRay` | `from diagrams.aws.devtools import XRay` |

### Enablement

**Import:** `from diagrams.aws.enablement import ...`

| Class Name | Import Example |
|------------|---------------|
| `CustomerEnablement` | `from diagrams.aws.enablement import CustomerEnablement` |
| `Iq` | `from diagrams.aws.enablement import Iq` |
| `ManagedServices` | `from diagrams.aws.enablement import ManagedServices` |
| `ProfessionalServices` | `from diagrams.aws.enablement import ProfessionalServices` |
| `Support` | `from diagrams.aws.enablement import Support` |

### End User

**Import:** `from diagrams.aws.enduser import ...`

| Class Name | Import Example |
|------------|---------------|
| `Appstream20` | `from diagrams.aws.enduser import Appstream20` |
| `DesktopAndAppStreaming` | `from diagrams.aws.enduser import DesktopAndAppStreaming` |
| `Workdocs` | `from diagrams.aws.enduser import Workdocs` |
| `Worklink` | `from diagrams.aws.enduser import Worklink` |
| `Workspaces` | `from diagrams.aws.enduser import Workspaces` |

### Engagement

**Import:** `from diagrams.aws.engagement import ...`

| Class Name | Import Example |
|------------|---------------|
| `Connect` | `from diagrams.aws.engagement import Connect` |
| `CustomerEngagement` | `from diagrams.aws.engagement import CustomerEngagement` |
| `Pinpoint` | `from diagrams.aws.engagement import Pinpoint` |
| `SES` | `from diagrams.aws.engagement import SES` |
| `SimpleEmailServiceSes` | `from diagrams.aws.engagement import SimpleEmailServiceSes` |
| `SimpleEmailServiceSesEmail` | `from diagrams.aws.engagement import SimpleEmailServiceSesEmail` |

### Game Tech

**Import:** `from diagrams.aws.game import ...`

| Class Name | Import Example |
|------------|---------------|
| `GameTech` | `from diagrams.aws.game import GameTech` |
| `Gamelift` | `from diagrams.aws.game import Gamelift` |

### General

**Import:** `from diagrams.aws.general import ...`

| Class Name | Import Example |
|------------|---------------|
| `Client` | `from diagrams.aws.general import Client` |
| `Disk` | `from diagrams.aws.general import Disk` |
| `Forums` | `from diagrams.aws.general import Forums` |
| `General` | `from diagrams.aws.general import General` |
| `GenericDatabase` | `from diagrams.aws.general import GenericDatabase` |
| `GenericFirewall` | `from diagrams.aws.general import GenericFirewall` |
| `GenericOfficeBuilding` | `from diagrams.aws.general import GenericOfficeBuilding` |
| `GenericSDK` | `from diagrams.aws.general import GenericSDK` |
| `GenericSamlToken` | `from diagrams.aws.general import GenericSamlToken` |
| `InternetAlt1` | `from diagrams.aws.general import InternetAlt1` |
| `InternetAlt2` | `from diagrams.aws.general import InternetAlt2` |
| `InternetGateway` | `from diagrams.aws.general import InternetGateway` |
| `Marketplace` | `from diagrams.aws.general import Marketplace` |
| `MobileClient` | `from diagrams.aws.general import MobileClient` |
| `Multimedia` | `from diagrams.aws.general import Multimedia` |
| `OfficeBuilding` | `from diagrams.aws.general import OfficeBuilding` |
| `SDK` | `from diagrams.aws.general import SDK` |
| `SamlToken` | `from diagrams.aws.general import SamlToken` |
| `SslPadlock` | `from diagrams.aws.general import SslPadlock` |
| `TapeStorage` | `from diagrams.aws.general import TapeStorage` |
| `Toolkit` | `from diagrams.aws.general import Toolkit` |
| `TraditionalServer` | `from diagrams.aws.general import TraditionalServer` |
| `User` | `from diagrams.aws.general import User` |
| `Users` | `from diagrams.aws.general import Users` |

### Integration

**Import:** `from diagrams.aws.integration import ...`

| Class Name | Import Example |
|------------|---------------|
| `ApplicationIntegration` | `from diagrams.aws.integration import ApplicationIntegration` |
| `Appsync` | `from diagrams.aws.integration import Appsync` |
| `ConsoleMobileApplication` | `from diagrams.aws.integration import ConsoleMobileApplication` |
| `EventResource` | `from diagrams.aws.integration import EventResource` |
| `Eventbridge` | `from diagrams.aws.integration import Eventbridge` |
| `EventbridgeCustomEventBusResource` | `from diagrams.aws.integration import EventbridgeCustomEventBusResource` |
| `EventbridgeDefaultEventBusResource` | `from diagrams.aws.integration import EventbridgeDefaultEventBusResource` |
| `EventbridgeEvent` | `from diagrams.aws.integration import EventbridgeEvent` |
| `EventbridgePipes` | `from diagrams.aws.integration import EventbridgePipes` |
| `EventbridgeRule` | `from diagrams.aws.integration import EventbridgeRule` |
| `EventbridgeSaasPartnerEventBusResource` | `from diagrams.aws.integration import EventbridgeSaasPartnerEventBusResource` |
| `EventbridgeScheduler` | `from diagrams.aws.integration import EventbridgeScheduler` |
| `EventbridgeSchema` | `from diagrams.aws.integration import EventbridgeSchema` |
| `ExpressWorkflows` | `from diagrams.aws.integration import ExpressWorkflows` |
| `MQ` | `from diagrams.aws.integration import MQ` |
| `SF` | `from diagrams.aws.integration import SF` |
| `SNS` | `from diagrams.aws.integration import SNS` |
| `SQS` | `from diagrams.aws.integration import SQS` |
| `SimpleNotificationServiceSns` | `from diagrams.aws.integration import SimpleNotificationServiceSns` |
| `SimpleNotificationServiceSnsEmailNotification` | `from diagrams.aws.integration import SimpleNotificationServiceSnsEmailNotification` |
| `SimpleNotificationServiceSnsHttpNotification` | `from diagrams.aws.integration import SimpleNotificationServiceSnsHttpNotification` |
| `SimpleNotificationServiceSnsTopic` | `from diagrams.aws.integration import SimpleNotificationServiceSnsTopic` |
| `SimpleQueueServiceSqs` | `from diagrams.aws.integration import SimpleQueueServiceSqs` |
| `SimpleQueueServiceSqsMessage` | `from diagrams.aws.integration import SimpleQueueServiceSqsMessage` |
| `SimpleQueueServiceSqsQueue` | `from diagrams.aws.integration import SimpleQueueServiceSqsQueue` |
| `StepFunctions` | `from diagrams.aws.integration import StepFunctions` |

### IoT

**Import:** `from diagrams.aws.iot import ...`

| Class Name | Import Example |
|------------|---------------|
| `FreeRTOS` | `from diagrams.aws.iot import FreeRTOS` |
| `Freertos` | `from diagrams.aws.iot import Freertos` |
| `InternetOfThings` | `from diagrams.aws.iot import InternetOfThings` |
| `Iot1Click` | `from diagrams.aws.iot import Iot1Click` |
| `IotAction` | `from diagrams.aws.iot import IotAction` |
| `IotActuator` | `from diagrams.aws.iot import IotActuator` |
| `IotAlexaEcho` | `from diagrams.aws.iot import IotAlexaEcho` |
| `IotAlexaEnabledDevice` | `from diagrams.aws.iot import IotAlexaEnabledDevice` |
| `IotAlexaSkill` | `from diagrams.aws.iot import IotAlexaSkill` |
| `IotAlexaVoiceService` | `from diagrams.aws.iot import IotAlexaVoiceService` |
| `IotAnalytics` | `from diagrams.aws.iot import IotAnalytics` |
| `IotAnalyticsChannel` | `from diagrams.aws.iot import IotAnalyticsChannel` |
| `IotAnalyticsDataSet` | `from diagrams.aws.iot import IotAnalyticsDataSet` |
| `IotAnalyticsDataStore` | `from diagrams.aws.iot import IotAnalyticsDataStore` |
| `IotAnalyticsNotebook` | `from diagrams.aws.iot import IotAnalyticsNotebook` |
| `IotAnalyticsPipeline` | `from diagrams.aws.iot import IotAnalyticsPipeline` |
| `IotBank` | `from diagrams.aws.iot import IotBank` |
| `IotBicycle` | `from diagrams.aws.iot import IotBicycle` |
| `IotBoard` | `from diagrams.aws.iot import IotBoard` |
| `IotButton` | `from diagrams.aws.iot import IotButton` |
| `IotCamera` | `from diagrams.aws.iot import IotCamera` |
| `IotCar` | `from diagrams.aws.iot import IotCar` |
| `IotCart` | `from diagrams.aws.iot import IotCart` |
| `IotCertificate` | `from diagrams.aws.iot import IotCertificate` |
| `IotCoffeePot` | `from diagrams.aws.iot import IotCoffeePot` |
| `IotCore` | `from diagrams.aws.iot import IotCore` |
| `IotDesiredState` | `from diagrams.aws.iot import IotDesiredState` |
| `IotDeviceDefender` | `from diagrams.aws.iot import IotDeviceDefender` |
| `IotDeviceGateway` | `from diagrams.aws.iot import IotDeviceGateway` |
| `IotDeviceManagement` | `from diagrams.aws.iot import IotDeviceManagement` |
| `IotDoorLock` | `from diagrams.aws.iot import IotDoorLock` |
| `IotEvents` | `from diagrams.aws.iot import IotEvents` |
| `IotFactory` | `from diagrams.aws.iot import IotFactory` |
| `IotFireTv` | `from diagrams.aws.iot import IotFireTv` |
| `IotFireTvStick` | `from diagrams.aws.iot import IotFireTvStick` |
| `IotGeneric` | `from diagrams.aws.iot import IotGeneric` |
| `IotGreengrass` | `from diagrams.aws.iot import IotGreengrass` |
| `IotGreengrassConnector` | `from diagrams.aws.iot import IotGreengrassConnector` |
| `IotHardwareBoard` | `from diagrams.aws.iot import IotHardwareBoard` |
| `IotHouse` | `from diagrams.aws.iot import IotHouse` |
| `IotHttp` | `from diagrams.aws.iot import IotHttp` |
| `IotHttp2` | `from diagrams.aws.iot import IotHttp2` |
| `IotJobs` | `from diagrams.aws.iot import IotJobs` |
| `IotLambda` | `from diagrams.aws.iot import IotLambda` |
| `IotLightbulb` | `from diagrams.aws.iot import IotLightbulb` |
| `IotMedicalEmergency` | `from diagrams.aws.iot import IotMedicalEmergency` |
| `IotMqtt` | `from diagrams.aws.iot import IotMqtt` |
| `IotOverTheAirUpdate` | `from diagrams.aws.iot import IotOverTheAirUpdate` |
| `IotPolicy` | `from diagrams.aws.iot import IotPolicy` |
| `IotPolicyEmergency` | `from diagrams.aws.iot import IotPolicyEmergency` |
| `IotReportedState` | `from diagrams.aws.iot import IotReportedState` |
| `IotRule` | `from diagrams.aws.iot import IotRule` |
| `IotSensor` | `from diagrams.aws.iot import IotSensor` |
| `IotServo` | `from diagrams.aws.iot import IotServo` |
| `IotShadow` | `from diagrams.aws.iot import IotShadow` |
| `IotSimulator` | `from diagrams.aws.iot import IotSimulator` |
| `IotSitewise` | `from diagrams.aws.iot import IotSitewise` |
| `IotThermostat` | `from diagrams.aws.iot import IotThermostat` |
| `IotThingsGraph` | `from diagrams.aws.iot import IotThingsGraph` |
| `IotTopic` | `from diagrams.aws.iot import IotTopic` |
| `IotTravel` | `from diagrams.aws.iot import IotTravel` |
| `IotUtility` | `from diagrams.aws.iot import IotUtility` |
| `IotWindfarm` | `from diagrams.aws.iot import IotWindfarm` |

### Management

**Import:** `from diagrams.aws.management import ...`

| Class Name | Import Example |
|------------|---------------|
| `AmazonDevopsGuru` | `from diagrams.aws.management import AmazonDevopsGuru` |
| `AmazonManagedGrafana` | `from diagrams.aws.management import AmazonManagedGrafana` |
| `AmazonManagedPrometheus` | `from diagrams.aws.management import AmazonManagedPrometheus` |
| `AmazonManagedWorkflowsApacheAirflow` | `from diagrams.aws.management import AmazonManagedWorkflowsApacheAirflow` |
| `AutoScaling` | `from diagrams.aws.management import AutoScaling` |
| `Chatbot` | `from diagrams.aws.management import Chatbot` |
| `Cloudformation` | `from diagrams.aws.management import Cloudformation` |
| `CloudformationChangeSet` | `from diagrams.aws.management import CloudformationChangeSet` |
| `CloudformationStack` | `from diagrams.aws.management import CloudformationStack` |
| `CloudformationTemplate` | `from diagrams.aws.management import CloudformationTemplate` |
| `Cloudtrail` | `from diagrams.aws.management import Cloudtrail` |
| `Cloudwatch` | `from diagrams.aws.management import Cloudwatch` |
| `CloudwatchAlarm` | `from diagrams.aws.management import CloudwatchAlarm` |
| `CloudwatchEventEventBased` | `from diagrams.aws.management import CloudwatchEventEventBased` |
| `CloudwatchEventTimeBased` | `from diagrams.aws.management import CloudwatchEventTimeBased` |
| `CloudwatchLogs` | `from diagrams.aws.management import CloudwatchLogs` |
| `CloudwatchRule` | `from diagrams.aws.management import CloudwatchRule` |
| `Codeguru` | `from diagrams.aws.management import Codeguru` |
| `CommandLineInterface` | `from diagrams.aws.management import CommandLineInterface` |
| `Config` | `from diagrams.aws.management import Config` |
| `ControlTower` | `from diagrams.aws.management import ControlTower` |
| `LicenseManager` | `from diagrams.aws.management import LicenseManager` |
| `ManagedServices` | `from diagrams.aws.management import ManagedServices` |
| `ManagementAndGovernance` | `from diagrams.aws.management import ManagementAndGovernance` |
| `ManagementConsole` | `from diagrams.aws.management import ManagementConsole` |
| `Opsworks` | `from diagrams.aws.management import Opsworks` |
| `OpsworksApps` | `from diagrams.aws.management import OpsworksApps` |
| `OpsworksDeployments` | `from diagrams.aws.management import OpsworksDeployments` |
| `OpsworksInstances` | `from diagrams.aws.management import OpsworksInstances` |
| `OpsworksLayers` | `from diagrams.aws.management import OpsworksLayers` |
| `OpsworksMonitoring` | `from diagrams.aws.management import OpsworksMonitoring` |
| `OpsworksPermissions` | `from diagrams.aws.management import OpsworksPermissions` |
| `OpsworksResources` | `from diagrams.aws.management import OpsworksResources` |
| `OpsworksStack` | `from diagrams.aws.management import OpsworksStack` |
| `Organizations` | `from diagrams.aws.management import Organizations` |
| `OrganizationsAccount` | `from diagrams.aws.management import OrganizationsAccount` |
| `OrganizationsOrganizationalUnit` | `from diagrams.aws.management import OrganizationsOrganizationalUnit` |
| `ParameterStore` | `from diagrams.aws.management import ParameterStore` |
| `PersonalHealthDashboard` | `from diagrams.aws.management import PersonalHealthDashboard` |
| `Proton` | `from diagrams.aws.management import Proton` |
| `SSM` | `from diagrams.aws.management import SSM` |
| `ServiceCatalog` | `from diagrams.aws.management import ServiceCatalog` |
| `SystemsManager` | `from diagrams.aws.management import SystemsManager` |
| `SystemsManagerAppConfig` | `from diagrams.aws.management import SystemsManagerAppConfig` |
| `SystemsManagerAutomation` | `from diagrams.aws.management import SystemsManagerAutomation` |
| `SystemsManagerDocuments` | `from diagrams.aws.management import SystemsManagerDocuments` |
| `SystemsManagerInventory` | `from diagrams.aws.management import SystemsManagerInventory` |
| `SystemsManagerMaintenanceWindows` | `from diagrams.aws.management import SystemsManagerMaintenanceWindows` |
| `SystemsManagerOpscenter` | `from diagrams.aws.management import SystemsManagerOpscenter` |
| `SystemsManagerParameterStore` | `from diagrams.aws.management import SystemsManagerParameterStore` |
| `SystemsManagerPatchManager` | `from diagrams.aws.management import SystemsManagerPatchManager` |
| `SystemsManagerRunCommand` | `from diagrams.aws.management import SystemsManagerRunCommand` |
| `SystemsManagerStateManager` | `from diagrams.aws.management import SystemsManagerStateManager` |
| `TrustedAdvisor` | `from diagrams.aws.management import TrustedAdvisor` |
| `TrustedAdvisorChecklist` | `from diagrams.aws.management import TrustedAdvisorChecklist` |
| `TrustedAdvisorChecklistCost` | `from diagrams.aws.management import TrustedAdvisorChecklistCost` |
| `TrustedAdvisorChecklistFaultTolerant` | `from diagrams.aws.management import TrustedAdvisorChecklistFaultTolerant` |
| `TrustedAdvisorChecklistPerformance` | `from diagrams.aws.management import TrustedAdvisorChecklistPerformance` |
| `TrustedAdvisorChecklistSecurity` | `from diagrams.aws.management import TrustedAdvisorChecklistSecurity` |
| `UserNotifications` | `from diagrams.aws.management import UserNotifications` |
| `WellArchitectedTool` | `from diagrams.aws.management import WellArchitectedTool` |

### Media

**Import:** `from diagrams.aws.media import ...`

| Class Name | Import Example |
|------------|---------------|
| `ElasticTranscoder` | `from diagrams.aws.media import ElasticTranscoder` |
| `ElementalConductor` | `from diagrams.aws.media import ElementalConductor` |
| `ElementalDelta` | `from diagrams.aws.media import ElementalDelta` |
| `ElementalLive` | `from diagrams.aws.media import ElementalLive` |
| `ElementalMediaconnect` | `from diagrams.aws.media import ElementalMediaconnect` |
| `ElementalMediaconvert` | `from diagrams.aws.media import ElementalMediaconvert` |
| `ElementalMedialive` | `from diagrams.aws.media import ElementalMedialive` |
| `ElementalMediapackage` | `from diagrams.aws.media import ElementalMediapackage` |
| `ElementalMediastore` | `from diagrams.aws.media import ElementalMediastore` |
| `ElementalMediatailor` | `from diagrams.aws.media import ElementalMediatailor` |
| `ElementalServer` | `from diagrams.aws.media import ElementalServer` |
| `KinesisVideoStreams` | `from diagrams.aws.media import KinesisVideoStreams` |
| `MediaServices` | `from diagrams.aws.media import MediaServices` |

### Migration

**Import:** `from diagrams.aws.migration import ...`

| Class Name | Import Example |
|------------|---------------|
| `ADS` | `from diagrams.aws.migration import ADS` |
| `ApplicationDiscoveryService` | `from diagrams.aws.migration import ApplicationDiscoveryService` |
| `CEM` | `from diagrams.aws.migration import CEM` |
| `CloudendureMigration` | `from diagrams.aws.migration import CloudendureMigration` |
| `DMS` | `from diagrams.aws.migration import DMS` |
| `DatabaseMigrationService` | `from diagrams.aws.migration import DatabaseMigrationService` |
| `Datasync` | `from diagrams.aws.migration import Datasync` |
| `DatasyncAgent` | `from diagrams.aws.migration import DatasyncAgent` |
| `MAT` | `from diagrams.aws.migration import MAT` |
| `MigrationAndTransfer` | `from diagrams.aws.migration import MigrationAndTransfer` |
| `MigrationHub` | `from diagrams.aws.migration import MigrationHub` |
| `SMS` | `from diagrams.aws.migration import SMS` |
| `ServerMigrationService` | `from diagrams.aws.migration import ServerMigrationService` |
| `Snowball` | `from diagrams.aws.migration import Snowball` |
| `SnowballEdge` | `from diagrams.aws.migration import SnowballEdge` |
| `Snowmobile` | `from diagrams.aws.migration import Snowmobile` |
| `TransferForSftp` | `from diagrams.aws.migration import TransferForSftp` |

### Machine Learning

**Import:** `from diagrams.aws.ml import ...`

| Class Name | Import Example |
|------------|---------------|
| `ApacheMxnetOnAWS` | `from diagrams.aws.ml import ApacheMxnetOnAWS` |
| `AugmentedAi` | `from diagrams.aws.ml import AugmentedAi` |
| `Bedrock` | `from diagrams.aws.ml import Bedrock` |
| `Comprehend` | `from diagrams.aws.ml import Comprehend` |
| `DLC` | `from diagrams.aws.ml import DLC` |
| `DeepLearningAmis` | `from diagrams.aws.ml import DeepLearningAmis` |
| `DeepLearningContainers` | `from diagrams.aws.ml import DeepLearningContainers` |
| `Deepcomposer` | `from diagrams.aws.ml import Deepcomposer` |
| `Deeplens` | `from diagrams.aws.ml import Deeplens` |
| `Deepracer` | `from diagrams.aws.ml import Deepracer` |
| `ElasticInference` | `from diagrams.aws.ml import ElasticInference` |
| `Forecast` | `from diagrams.aws.ml import Forecast` |
| `FraudDetector` | `from diagrams.aws.ml import FraudDetector` |
| `Kendra` | `from diagrams.aws.ml import Kendra` |
| `Lex` | `from diagrams.aws.ml import Lex` |
| `MachineLearning` | `from diagrams.aws.ml import MachineLearning` |
| `Personalize` | `from diagrams.aws.ml import Personalize` |
| `Polly` | `from diagrams.aws.ml import Polly` |
| `Q` | `from diagrams.aws.ml import Q` |
| `Rekognition` | `from diagrams.aws.ml import Rekognition` |
| `RekognitionImage` | `from diagrams.aws.ml import RekognitionImage` |
| `RekognitionVideo` | `from diagrams.aws.ml import RekognitionVideo` |
| `Sagemaker` | `from diagrams.aws.ml import Sagemaker` |
| `SagemakerGroundTruth` | `from diagrams.aws.ml import SagemakerGroundTruth` |
| `SagemakerModel` | `from diagrams.aws.ml import SagemakerModel` |
| `SagemakerNotebook` | `from diagrams.aws.ml import SagemakerNotebook` |
| `SagemakerTrainingJob` | `from diagrams.aws.ml import SagemakerTrainingJob` |
| `TensorflowOnAWS` | `from diagrams.aws.ml import TensorflowOnAWS` |
| `Textract` | `from diagrams.aws.ml import Textract` |
| `Transcribe` | `from diagrams.aws.ml import Transcribe` |
| `Transform` | `from diagrams.aws.ml import Transform` |
| `Translate` | `from diagrams.aws.ml import Translate` |

### Mobile

**Import:** `from diagrams.aws.mobile import ...`

| Class Name | Import Example |
|------------|---------------|
| `APIGateway` | `from diagrams.aws.mobile import APIGateway` |
| `APIGatewayEndpoint` | `from diagrams.aws.mobile import APIGatewayEndpoint` |
| `Amplify` | `from diagrams.aws.mobile import Amplify` |
| `Appsync` | `from diagrams.aws.mobile import Appsync` |
| `DeviceFarm` | `from diagrams.aws.mobile import DeviceFarm` |
| `Mobile` | `from diagrams.aws.mobile import Mobile` |
| `Pinpoint` | `from diagrams.aws.mobile import Pinpoint` |

### Network

**Import:** `from diagrams.aws.network import ...`

| Class Name | Import Example |
|------------|---------------|
| `ALB` | `from diagrams.aws.network import ALB` |
| `APIGateway` | `from diagrams.aws.network import APIGateway` |
| `APIGatewayEndpoint` | `from diagrams.aws.network import APIGatewayEndpoint` |
| `AppMesh` | `from diagrams.aws.network import AppMesh` |
| `CF` | `from diagrams.aws.network import CF` |
| `CLB` | `from diagrams.aws.network import CLB` |
| `ClientVpn` | `from diagrams.aws.network import ClientVpn` |
| `CloudFront` | `from diagrams.aws.network import CloudFront` |
| `CloudFrontDownloadDistribution` | `from diagrams.aws.network import CloudFrontDownloadDistribution` |
| `CloudFrontEdgeLocation` | `from diagrams.aws.network import CloudFrontEdgeLocation` |
| `CloudFrontStreamingDistribution` | `from diagrams.aws.network import CloudFrontStreamingDistribution` |
| `CloudMap` | `from diagrams.aws.network import CloudMap` |
| `DirectConnect` | `from diagrams.aws.network import DirectConnect` |
| `ELB` | `from diagrams.aws.network import ELB` |
| `ElasticLoadBalancing` | `from diagrams.aws.network import ElasticLoadBalancing` |
| `ElbApplicationLoadBalancer` | `from diagrams.aws.network import ElbApplicationLoadBalancer` |
| `ElbClassicLoadBalancer` | `from diagrams.aws.network import ElbClassicLoadBalancer` |
| `ElbNetworkLoadBalancer` | `from diagrams.aws.network import ElbNetworkLoadBalancer` |
| `Endpoint` | `from diagrams.aws.network import Endpoint` |
| `GAX` | `from diagrams.aws.network import GAX` |
| `GlobalAccelerator` | `from diagrams.aws.network import GlobalAccelerator` |
| `IGW` | `from diagrams.aws.network import IGW` |
| `InternetGateway` | `from diagrams.aws.network import InternetGateway` |
| `NATGateway` | `from diagrams.aws.network import NATGateway` |
| `NLB` | `from diagrams.aws.network import NLB` |
| `Nacl` | `from diagrams.aws.network import Nacl` |
| `NetworkFirewall` | `from diagrams.aws.network import NetworkFirewall` |
| `NetworkingAndContentDelivery` | `from diagrams.aws.network import NetworkingAndContentDelivery` |
| `PrivateSubnet` | `from diagrams.aws.network import PrivateSubnet` |
| `Privatelink` | `from diagrams.aws.network import Privatelink` |
| `PublicSubnet` | `from diagrams.aws.network import PublicSubnet` |
| `Route53` | `from diagrams.aws.network import Route53` |
| `Route53HostedZone` | `from diagrams.aws.network import Route53HostedZone` |
| `RouteTable` | `from diagrams.aws.network import RouteTable` |
| `SiteToSiteVpn` | `from diagrams.aws.network import SiteToSiteVpn` |
| `TGW` | `from diagrams.aws.network import TGW` |
| `TGWAttach` | `from diagrams.aws.network import TGWAttach` |
| `TransitGateway` | `from diagrams.aws.network import TransitGateway` |
| `TransitGatewayAttachment` | `from diagrams.aws.network import TransitGatewayAttachment` |
| `VPC` | `from diagrams.aws.network import VPC` |
| `VPCCustomerGateway` | `from diagrams.aws.network import VPCCustomerGateway` |
| `VPCElasticNetworkAdapter` | `from diagrams.aws.network import VPCElasticNetworkAdapter` |
| `VPCElasticNetworkInterface` | `from diagrams.aws.network import VPCElasticNetworkInterface` |
| `VPCFlowLogs` | `from diagrams.aws.network import VPCFlowLogs` |
| `VPCPeering` | `from diagrams.aws.network import VPCPeering` |
| `VPCRouter` | `from diagrams.aws.network import VPCRouter` |
| `VPCTrafficMirroring` | `from diagrams.aws.network import VPCTrafficMirroring` |
| `VpnConnection` | `from diagrams.aws.network import VpnConnection` |
| `VpnGateway` | `from diagrams.aws.network import VpnGateway` |

### Quantum

**Import:** `from diagrams.aws.quantum import ...`

| Class Name | Import Example |
|------------|---------------|
| `Braket` | `from diagrams.aws.quantum import Braket` |
| `QuantumTechnologies` | `from diagrams.aws.quantum import QuantumTechnologies` |

### Robotics

**Import:** `from diagrams.aws.robotics import ...`

| Class Name | Import Example |
|------------|---------------|
| `Robomaker` | `from diagrams.aws.robotics import Robomaker` |
| `RobomakerCloudExtensionRos` | `from diagrams.aws.robotics import RobomakerCloudExtensionRos` |
| `RobomakerDevelopmentEnvironment` | `from diagrams.aws.robotics import RobomakerDevelopmentEnvironment` |
| `RobomakerFleetManagement` | `from diagrams.aws.robotics import RobomakerFleetManagement` |
| `RobomakerSimulator` | `from diagrams.aws.robotics import RobomakerSimulator` |
| `Robotics` | `from diagrams.aws.robotics import Robotics` |

### Satellite

**Import:** `from diagrams.aws.satellite import ...`

| Class Name | Import Example |
|------------|---------------|
| `GroundStation` | `from diagrams.aws.satellite import GroundStation` |
| `Satellite` | `from diagrams.aws.satellite import Satellite` |

### Security

**Import:** `from diagrams.aws.security import ...`

| Class Name | Import Example |
|------------|---------------|
| `ACM` | `from diagrams.aws.security import ACM` |
| `AdConnector` | `from diagrams.aws.security import AdConnector` |
| `Artifact` | `from diagrams.aws.security import Artifact` |
| `CertificateAuthority` | `from diagrams.aws.security import CertificateAuthority` |
| `CertificateManager` | `from diagrams.aws.security import CertificateManager` |
| `CloudDirectory` | `from diagrams.aws.security import CloudDirectory` |
| `CloudHSM` | `from diagrams.aws.security import CloudHSM` |
| `Cloudhsm` | `from diagrams.aws.security import Cloudhsm` |
| `Cognito` | `from diagrams.aws.security import Cognito` |
| `DS` | `from diagrams.aws.security import DS` |
| `Detective` | `from diagrams.aws.security import Detective` |
| `DirectoryService` | `from diagrams.aws.security import DirectoryService` |
| `FMS` | `from diagrams.aws.security import FMS` |
| `FirewallManager` | `from diagrams.aws.security import FirewallManager` |
| `Guardduty` | `from diagrams.aws.security import Guardduty` |
| `IAM` | `from diagrams.aws.security import IAM` |
| `IAMAWSSts` | `from diagrams.aws.security import IAMAWSSts` |
| `IAMAccessAnalyzer` | `from diagrams.aws.security import IAMAccessAnalyzer` |
| `IAMPermissions` | `from diagrams.aws.security import IAMPermissions` |
| `IAMRole` | `from diagrams.aws.security import IAMRole` |
| `IdentityAndAccessManagementIam` | `from diagrams.aws.security import IdentityAndAccessManagementIam` |
| `IdentityAndAccessManagementIamAWSSts` | `from diagrams.aws.security import IdentityAndAccessManagementIamAWSSts` |
| `IdentityAndAccessManagementIamAWSStsAlternate` | `from diagrams.aws.security import IdentityAndAccessManagementIamAWSStsAlternate` |
| `IdentityAndAccessManagementIamAccessAnalyzer` | `from diagrams.aws.security import IdentityAndAccessManagementIamAccessAnalyzer` |
| `IdentityAndAccessManagementIamAddOn` | `from diagrams.aws.security import IdentityAndAccessManagementIamAddOn` |
| `IdentityAndAccessManagementIamDataEncryptionKey` | `from diagrams.aws.security import IdentityAndAccessManagementIamDataEncryptionKey` |
| `IdentityAndAccessManagementIamEncryptedData` | `from diagrams.aws.security import IdentityAndAccessManagementIamEncryptedData` |
| `IdentityAndAccessManagementIamLongTermSecurityCredential` | `from diagrams.aws.security import IdentityAndAccessManagementIamLongTermSecurityCredential` |
| `IdentityAndAccessManagementIamMfaToken` | `from diagrams.aws.security import IdentityAndAccessManagementIamMfaToken` |
| `IdentityAndAccessManagementIamPermissions` | `from diagrams.aws.security import IdentityAndAccessManagementIamPermissions` |
| `IdentityAndAccessManagementIamRole` | `from diagrams.aws.security import IdentityAndAccessManagementIamRole` |
| `IdentityAndAccessManagementIamTemporarySecurityCredential` | `from diagrams.aws.security import IdentityAndAccessManagementIamTemporarySecurityCredential` |
| `Inspector` | `from diagrams.aws.security import Inspector` |
| `InspectorAgent` | `from diagrams.aws.security import InspectorAgent` |
| `KMS` | `from diagrams.aws.security import KMS` |
| `KeyManagementService` | `from diagrams.aws.security import KeyManagementService` |
| `Macie` | `from diagrams.aws.security import Macie` |
| `ManagedMicrosoftAd` | `from diagrams.aws.security import ManagedMicrosoftAd` |
| `RAM` | `from diagrams.aws.security import RAM` |
| `ResourceAccessManager` | `from diagrams.aws.security import ResourceAccessManager` |
| `SecretsManager` | `from diagrams.aws.security import SecretsManager` |
| `SecurityHub` | `from diagrams.aws.security import SecurityHub` |
| `SecurityHubFinding` | `from diagrams.aws.security import SecurityHubFinding` |
| `SecurityIdentityAndCompliance` | `from diagrams.aws.security import SecurityIdentityAndCompliance` |
| `SecurityLake` | `from diagrams.aws.security import SecurityLake` |
| `Shield` | `from diagrams.aws.security import Shield` |
| `ShieldAdvanced` | `from diagrams.aws.security import ShieldAdvanced` |
| `SimpleAd` | `from diagrams.aws.security import SimpleAd` |
| `SingleSignOn` | `from diagrams.aws.security import SingleSignOn` |
| `WAF` | `from diagrams.aws.security import WAF` |
| `WAFFilteringRule` | `from diagrams.aws.security import WAFFilteringRule` |

### Storage

**Import:** `from diagrams.aws.storage import ...`

| Class Name | Import Example |
|------------|---------------|
| `Backup` | `from diagrams.aws.storage import Backup` |
| `CDR` | `from diagrams.aws.storage import CDR` |
| `CloudendureDisasterRecovery` | `from diagrams.aws.storage import CloudendureDisasterRecovery` |
| `EBS` | `from diagrams.aws.storage import EBS` |
| `EFS` | `from diagrams.aws.storage import EFS` |
| `EFSInfrequentaccessPrimaryBg` | `from diagrams.aws.storage import EFSInfrequentaccessPrimaryBg` |
| `EFSStandardPrimaryBg` | `from diagrams.aws.storage import EFSStandardPrimaryBg` |
| `ElasticBlockStoreEBS` | `from diagrams.aws.storage import ElasticBlockStoreEBS` |
| `ElasticBlockStoreEBSSnapshot` | `from diagrams.aws.storage import ElasticBlockStoreEBSSnapshot` |
| `ElasticBlockStoreEBSVolume` | `from diagrams.aws.storage import ElasticBlockStoreEBSVolume` |
| `ElasticFileSystemEFS` | `from diagrams.aws.storage import ElasticFileSystemEFS` |
| `ElasticFileSystemEFSFileSystem` | `from diagrams.aws.storage import ElasticFileSystemEFSFileSystem` |
| `FSx` | `from diagrams.aws.storage import FSx` |
| `Fsx` | `from diagrams.aws.storage import Fsx` |
| `FsxForLustre` | `from diagrams.aws.storage import FsxForLustre` |
| `FsxForWindowsFileServer` | `from diagrams.aws.storage import FsxForWindowsFileServer` |
| `MultipleVolumesResource` | `from diagrams.aws.storage import MultipleVolumesResource` |
| `S3` | `from diagrams.aws.storage import S3` |
| `S3AccessPoints` | `from diagrams.aws.storage import S3AccessPoints` |
| `S3Glacier` | `from diagrams.aws.storage import S3Glacier` |
| `S3GlacierArchive` | `from diagrams.aws.storage import S3GlacierArchive` |
| `S3GlacierVault` | `from diagrams.aws.storage import S3GlacierVault` |
| `S3ObjectLambdaAccessPoints` | `from diagrams.aws.storage import S3ObjectLambdaAccessPoints` |
| `SimpleStorageServiceS3` | `from diagrams.aws.storage import SimpleStorageServiceS3` |
| `SimpleStorageServiceS3Bucket` | `from diagrams.aws.storage import SimpleStorageServiceS3Bucket` |
| `SimpleStorageServiceS3BucketWithObjects` | `from diagrams.aws.storage import SimpleStorageServiceS3BucketWithObjects` |
| `SimpleStorageServiceS3Object` | `from diagrams.aws.storage import SimpleStorageServiceS3Object` |
| `SnowFamilySnowballImportExport` | `from diagrams.aws.storage import SnowFamilySnowballImportExport` |
| `Snowball` | `from diagrams.aws.storage import Snowball` |
| `SnowballEdge` | `from diagrams.aws.storage import SnowballEdge` |
| `Snowmobile` | `from diagrams.aws.storage import Snowmobile` |
| `Storage` | `from diagrams.aws.storage import Storage` |
| `StorageGateway` | `from diagrams.aws.storage import StorageGateway` |
| `StorageGatewayCachedVolume` | `from diagrams.aws.storage import StorageGatewayCachedVolume` |
| `StorageGatewayNonCachedVolume` | `from diagrams.aws.storage import StorageGatewayNonCachedVolume` |
| `StorageGatewayVirtualTapeLibrary` | `from diagrams.aws.storage import StorageGatewayVirtualTapeLibrary` |

---

## Microsoft Azure

_Complete Azure service icon catalog_ — **810 icons** across **32 categories**

### AI & Machine Learning

**Import:** `from diagrams.azure.aimachinelearning import ...`

| Class Name | Import Example |
|------------|---------------|
| `AIStudio` | `from diagrams.azure.aimachinelearning import AIStudio` |
| `AnomalyDetector` | `from diagrams.azure.aimachinelearning import AnomalyDetector` |
| `AzureAppliedAIServices` | `from diagrams.azure.aimachinelearning import AzureAppliedAIServices` |
| `AzureExperimentationStudio` | `from diagrams.azure.aimachinelearning import AzureExperimentationStudio` |
| `AzureObjectUnderstanding` | `from diagrams.azure.aimachinelearning import AzureObjectUnderstanding` |
| `AzureOpenai` | `from diagrams.azure.aimachinelearning import AzureOpenai` |
| `BatchAI` | `from diagrams.azure.aimachinelearning import BatchAI` |
| `Bonsai` | `from diagrams.azure.aimachinelearning import Bonsai` |
| `BotServices` | `from diagrams.azure.aimachinelearning import BotServices` |
| `CognitiveSearch` | `from diagrams.azure.aimachinelearning import CognitiveSearch` |
| `CognitiveServices` | `from diagrams.azure.aimachinelearning import CognitiveServices` |
| `CognitiveServicesDecisions` | `from diagrams.azure.aimachinelearning import CognitiveServicesDecisions` |
| `ComputerVision` | `from diagrams.azure.aimachinelearning import ComputerVision` |
| `ContentModerators` | `from diagrams.azure.aimachinelearning import ContentModerators` |
| `CustomVision` | `from diagrams.azure.aimachinelearning import CustomVision` |
| `FaceApis` | `from diagrams.azure.aimachinelearning import FaceApis` |
| `FormRecognizers` | `from diagrams.azure.aimachinelearning import FormRecognizers` |
| `Genomics` | `from diagrams.azure.aimachinelearning import Genomics` |
| `GenomicsAccounts` | `from diagrams.azure.aimachinelearning import GenomicsAccounts` |
| `ImmersiveReaders` | `from diagrams.azure.aimachinelearning import ImmersiveReaders` |
| `Language` | `from diagrams.azure.aimachinelearning import Language` |
| `LanguageUnderstanding` | `from diagrams.azure.aimachinelearning import LanguageUnderstanding` |
| `MachineLearning` | `from diagrams.azure.aimachinelearning import MachineLearning` |
| `MachineLearningStudioClassicWebServices` | `from diagrams.azure.aimachinelearning import MachineLearningStudioClassicWebServices` |
| `MachineLearningStudioWebServicePlans` | `from diagrams.azure.aimachinelearning import MachineLearningStudioWebServicePlans` |
| `MachineLearningStudioWorkspaces` | `from diagrams.azure.aimachinelearning import MachineLearningStudioWorkspaces` |
| `MetricsAdvisor` | `from diagrams.azure.aimachinelearning import MetricsAdvisor` |
| `Personalizers` | `from diagrams.azure.aimachinelearning import Personalizers` |
| `QnaMakers` | `from diagrams.azure.aimachinelearning import QnaMakers` |
| `ServerlessSearch` | `from diagrams.azure.aimachinelearning import ServerlessSearch` |
| `SpeechServices` | `from diagrams.azure.aimachinelearning import SpeechServices` |
| `TranslatorText` | `from diagrams.azure.aimachinelearning import TranslatorText` |

### Analytics

**Import:** `from diagrams.azure.analytics import ...`

| Class Name | Import Example |
|------------|---------------|
| `AnalysisServices` | `from diagrams.azure.analytics import AnalysisServices` |
| `AzureDataExplorerClusters` | `from diagrams.azure.analytics import AzureDataExplorerClusters` |
| `AzureDatabricks` | `from diagrams.azure.analytics import AzureDatabricks` |
| `AzureSynapseAnalytics` | `from diagrams.azure.analytics import AzureSynapseAnalytics` |
| `AzureWorkbooks` | `from diagrams.azure.analytics import AzureWorkbooks` |
| `DataExplorerClusters` | `from diagrams.azure.analytics import DataExplorerClusters` |
| `DataFactories` | `from diagrams.azure.analytics import DataFactories` |
| `DataLakeAnalytics` | `from diagrams.azure.analytics import DataLakeAnalytics` |
| `DataLakeStoreGen1` | `from diagrams.azure.analytics import DataLakeStoreGen1` |
| `Databricks` | `from diagrams.azure.analytics import Databricks` |
| `EndpointAnalytics` | `from diagrams.azure.analytics import EndpointAnalytics` |
| `EventHubClusters` | `from diagrams.azure.analytics import EventHubClusters` |
| `EventHubs` | `from diagrams.azure.analytics import EventHubs` |
| `HDInsightClusters` | `from diagrams.azure.analytics import HDInsightClusters` |
| `LogAnalyticsWorkspaces` | `from diagrams.azure.analytics import LogAnalyticsWorkspaces` |
| `PowerBiEmbedded` | `from diagrams.azure.analytics import PowerBiEmbedded` |
| `PowerPlatform` | `from diagrams.azure.analytics import PowerPlatform` |
| `PrivateLinkServices` | `from diagrams.azure.analytics import PrivateLinkServices` |
| `StreamAnalyticsJobs` | `from diagrams.azure.analytics import StreamAnalyticsJobs` |
| `SynapseAnalytics` | `from diagrams.azure.analytics import SynapseAnalytics` |

### App Services

**Import:** `from diagrams.azure.appservices import ...`

| Class Name | Import Example |
|------------|---------------|
| `AppServiceCertificates` | `from diagrams.azure.appservices import AppServiceCertificates` |
| `AppServiceDomains` | `from diagrams.azure.appservices import AppServiceDomains` |
| `AppServiceEnvironments` | `from diagrams.azure.appservices import AppServiceEnvironments` |
| `AppServicePlans` | `from diagrams.azure.appservices import AppServicePlans` |
| `AppServices` | `from diagrams.azure.appservices import AppServices` |
| `CDNProfiles` | `from diagrams.azure.appservices import CDNProfiles` |
| `CognitiveSearch` | `from diagrams.azure.appservices import CognitiveSearch` |
| `NotificationHubs` | `from diagrams.azure.appservices import NotificationHubs` |

### Azure Ecosystem

**Import:** `from diagrams.azure.azureecosystem import ...`

| Class Name | Import Example |
|------------|---------------|
| `Applens` | `from diagrams.azure.azureecosystem import Applens` |
| `AzureHybridCenter` | `from diagrams.azure.azureecosystem import AzureHybridCenter` |
| `CollaborativeService` | `from diagrams.azure.azureecosystem import CollaborativeService` |

### Azure Stack

**Import:** `from diagrams.azure.azurestack import ...`

| Class Name | Import Example |
|------------|---------------|
| `Capacity` | `from diagrams.azure.azurestack import Capacity` |
| `InfrastructureBackup` | `from diagrams.azure.azurestack import InfrastructureBackup` |
| `MultiTenancy` | `from diagrams.azure.azurestack import MultiTenancy` |
| `Offers` | `from diagrams.azure.azurestack import Offers` |
| `Plans` | `from diagrams.azure.azurestack import Plans` |
| `Updates` | `from diagrams.azure.azurestack import Updates` |
| `UserSubscriptions` | `from diagrams.azure.azurestack import UserSubscriptions` |

### Blockchain

**Import:** `from diagrams.azure.blockchain import ...`

| Class Name | Import Example |
|------------|---------------|
| `AbsMember` | `from diagrams.azure.blockchain import AbsMember` |
| `AzureBlockchainService` | `from diagrams.azure.blockchain import AzureBlockchainService` |
| `AzureTokenService` | `from diagrams.azure.blockchain import AzureTokenService` |
| `BlockchainApplications` | `from diagrams.azure.blockchain import BlockchainApplications` |
| `Consortium` | `from diagrams.azure.blockchain import Consortium` |
| `OutboundConnection` | `from diagrams.azure.blockchain import OutboundConnection` |

### Compute

**Import:** `from diagrams.azure.compute import ...`

| Class Name | Import Example |
|------------|---------------|
| `ACR` | `from diagrams.azure.compute import ACR` |
| `AKS` | `from diagrams.azure.compute import AKS` |
| `AppServices` | `from diagrams.azure.compute import AppServices` |
| `ApplicationGroup` | `from diagrams.azure.compute import ApplicationGroup` |
| `AutomanagedVM` | `from diagrams.azure.compute import AutomanagedVM` |
| `AvailabilitySets` | `from diagrams.azure.compute import AvailabilitySets` |
| `AzureComputeGalleries` | `from diagrams.azure.compute import AzureComputeGalleries` |
| `AzureSpringApps` | `from diagrams.azure.compute import AzureSpringApps` |
| `BatchAccounts` | `from diagrams.azure.compute import BatchAccounts` |
| `CitrixVirtualDesktopsEssentials` | `from diagrams.azure.compute import CitrixVirtualDesktopsEssentials` |
| `CloudServices` | `from diagrams.azure.compute import CloudServices` |
| `CloudServicesClassic` | `from diagrams.azure.compute import CloudServicesClassic` |
| `CloudsimpleVirtualMachines` | `from diagrams.azure.compute import CloudsimpleVirtualMachines` |
| `ContainerApps` | `from diagrams.azure.compute import ContainerApps` |
| `ContainerInstances` | `from diagrams.azure.compute import ContainerInstances` |
| `ContainerRegistries` | `from diagrams.azure.compute import ContainerRegistries` |
| `ContainerServicesDeprecated` | `from diagrams.azure.compute import ContainerServicesDeprecated` |
| `DiskEncryptionSets` | `from diagrams.azure.compute import DiskEncryptionSets` |
| `DiskSnapshots` | `from diagrams.azure.compute import DiskSnapshots` |
| `Disks` | `from diagrams.azure.compute import Disks` |
| `DisksClassic` | `from diagrams.azure.compute import DisksClassic` |
| `DisksSnapshots` | `from diagrams.azure.compute import DisksSnapshots` |
| `FunctionApps` | `from diagrams.azure.compute import FunctionApps` |
| `HostGroups` | `from diagrams.azure.compute import HostGroups` |
| `HostPools` | `from diagrams.azure.compute import HostPools` |
| `Hosts` | `from diagrams.azure.compute import Hosts` |
| `ImageDefinitions` | `from diagrams.azure.compute import ImageDefinitions` |
| `ImageTemplates` | `from diagrams.azure.compute import ImageTemplates` |
| `ImageVersions` | `from diagrams.azure.compute import ImageVersions` |
| `Images` | `from diagrams.azure.compute import Images` |
| `KubernetesServices` | `from diagrams.azure.compute import KubernetesServices` |
| `MaintenanceConfiguration` | `from diagrams.azure.compute import MaintenanceConfiguration` |
| `ManagedServiceFabric` | `from diagrams.azure.compute import ManagedServiceFabric` |
| `MeshApplications` | `from diagrams.azure.compute import MeshApplications` |
| `MetricsAdvisor` | `from diagrams.azure.compute import MetricsAdvisor` |
| `OsImages` | `from diagrams.azure.compute import OsImages` |
| `OsImagesClassic` | `from diagrams.azure.compute import OsImagesClassic` |
| `RestorePoints` | `from diagrams.azure.compute import RestorePoints` |
| `RestorePointsCollections` | `from diagrams.azure.compute import RestorePointsCollections` |
| `SAPHANAOnAzure` | `from diagrams.azure.compute import SAPHANAOnAzure` |
| `ServiceFabricClusters` | `from diagrams.azure.compute import ServiceFabricClusters` |
| `SharedImageGalleries` | `from diagrams.azure.compute import SharedImageGalleries` |
| `SpringCloud` | `from diagrams.azure.compute import SpringCloud` |
| `VM` | `from diagrams.azure.compute import VM` |
| `VMClassic` | `from diagrams.azure.compute import VMClassic` |
| `VMImages` | `from diagrams.azure.compute import VMImages` |
| `VMImagesClassic` | `from diagrams.azure.compute import VMImagesClassic` |
| `VMLinux` | `from diagrams.azure.compute import VMLinux` |
| `VMSS` | `from diagrams.azure.compute import VMSS` |
| `VMScaleSet` | `from diagrams.azure.compute import VMScaleSet` |
| `VMScaleSets` | `from diagrams.azure.compute import VMScaleSets` |
| `VMWindows` | `from diagrams.azure.compute import VMWindows` |
| `VirtualMachine` | `from diagrams.azure.compute import VirtualMachine` |
| `VirtualMachinesClassic` | `from diagrams.azure.compute import VirtualMachinesClassic` |
| `Workspaces` | `from diagrams.azure.compute import Workspaces` |
| `Workspaces2` | `from diagrams.azure.compute import Workspaces2` |

### Containers

**Import:** `from diagrams.azure.containers import ...`

| Class Name | Import Example |
|------------|---------------|
| `AppServices` | `from diagrams.azure.containers import AppServices` |
| `AzureRedHatOpenshift` | `from diagrams.azure.containers import AzureRedHatOpenshift` |
| `BatchAccounts` | `from diagrams.azure.containers import BatchAccounts` |
| `ContainerInstances` | `from diagrams.azure.containers import ContainerInstances` |
| `ContainerRegistries` | `from diagrams.azure.containers import ContainerRegistries` |
| `KubernetesServices` | `from diagrams.azure.containers import KubernetesServices` |
| `ServiceFabricClusters` | `from diagrams.azure.containers import ServiceFabricClusters` |

### Database

**Import:** `from diagrams.azure.database import ...`

| Class Name | Import Example |
|------------|---------------|
| `BlobStorage` | `from diagrams.azure.database import BlobStorage` |
| `CacheForRedis` | `from diagrams.azure.database import CacheForRedis` |
| `CosmosDb` | `from diagrams.azure.database import CosmosDb` |
| `DataExplorerClusters` | `from diagrams.azure.database import DataExplorerClusters` |
| `DataFactory` | `from diagrams.azure.database import DataFactory` |
| `DataLake` | `from diagrams.azure.database import DataLake` |
| `DatabaseForMariadbServers` | `from diagrams.azure.database import DatabaseForMariadbServers` |
| `DatabaseForMysqlServers` | `from diagrams.azure.database import DatabaseForMysqlServers` |
| `DatabaseForPostgresqlServers` | `from diagrams.azure.database import DatabaseForPostgresqlServers` |
| `ElasticDatabasePools` | `from diagrams.azure.database import ElasticDatabasePools` |
| `ElasticJobAgents` | `from diagrams.azure.database import ElasticJobAgents` |
| `InstancePools` | `from diagrams.azure.database import InstancePools` |
| `ManagedDatabases` | `from diagrams.azure.database import ManagedDatabases` |
| `SQL` | `from diagrams.azure.database import SQL` |
| `SQLDatabases` | `from diagrams.azure.database import SQLDatabases` |
| `SQLDatawarehouse` | `from diagrams.azure.database import SQLDatawarehouse` |
| `SQLManagedInstances` | `from diagrams.azure.database import SQLManagedInstances` |
| `SQLServerStretchDatabases` | `from diagrams.azure.database import SQLServerStretchDatabases` |
| `SQLServers` | `from diagrams.azure.database import SQLServers` |
| `SQLVM` | `from diagrams.azure.database import SQLVM` |
| `SsisLiftAndShiftIr` | `from diagrams.azure.database import SsisLiftAndShiftIr` |
| `SynapseAnalytics` | `from diagrams.azure.database import SynapseAnalytics` |
| `VirtualClusters` | `from diagrams.azure.database import VirtualClusters` |
| `VirtualDatacenter` | `from diagrams.azure.database import VirtualDatacenter` |

### Databases

**Import:** `from diagrams.azure.databases import ...`

| Class Name | Import Example |
|------------|---------------|
| `AzureCosmosDb` | `from diagrams.azure.databases import AzureCosmosDb` |
| `AzureDataExplorerClusters` | `from diagrams.azure.databases import AzureDataExplorerClusters` |
| `AzureDatabaseMariadbServer` | `from diagrams.azure.databases import AzureDatabaseMariadbServer` |
| `AzureDatabaseMigrationServices` | `from diagrams.azure.databases import AzureDatabaseMigrationServices` |
| `AzureDatabaseMysqlServer` | `from diagrams.azure.databases import AzureDatabaseMysqlServer` |
| `AzureDatabasePostgresqlServer` | `from diagrams.azure.databases import AzureDatabasePostgresqlServer` |
| `AzureDatabasePostgresqlServerGroup` | `from diagrams.azure.databases import AzureDatabasePostgresqlServerGroup` |
| `AzurePurviewAccounts` | `from diagrams.azure.databases import AzurePurviewAccounts` |
| `AzureSQL` | `from diagrams.azure.databases import AzureSQL` |
| `AzureSQLEdge` | `from diagrams.azure.databases import AzureSQLEdge` |
| `AzureSQLServerStretchDatabases` | `from diagrams.azure.databases import AzureSQLServerStretchDatabases` |
| `AzureSQLVM` | `from diagrams.azure.databases import AzureSQLVM` |
| `AzureSynapseAnalytics` | `from diagrams.azure.databases import AzureSynapseAnalytics` |
| `CacheRedis` | `from diagrams.azure.databases import CacheRedis` |
| `DataFactories` | `from diagrams.azure.databases import DataFactories` |
| `ElasticJobAgents` | `from diagrams.azure.databases import ElasticJobAgents` |
| `InstancePools` | `from diagrams.azure.databases import InstancePools` |
| `ManagedDatabase` | `from diagrams.azure.databases import ManagedDatabase` |
| `OracleDatabase` | `from diagrams.azure.databases import OracleDatabase` |
| `SQLDataWarehouses` | `from diagrams.azure.databases import SQLDataWarehouses` |
| `SQLDatabase` | `from diagrams.azure.databases import SQLDatabase` |
| `SQLElasticPools` | `from diagrams.azure.databases import SQLElasticPools` |
| `SQLManagedInstance` | `from diagrams.azure.databases import SQLManagedInstance` |
| `SQLServer` | `from diagrams.azure.databases import SQLServer` |
| `SQLServerRegistries` | `from diagrams.azure.databases import SQLServerRegistries` |
| `SsisLiftAndShiftIr` | `from diagrams.azure.databases import SsisLiftAndShiftIr` |
| `VirtualClusters` | `from diagrams.azure.databases import VirtualClusters` |

### DevOps

**Import:** `from diagrams.azure.devops import ...`

| Class Name | Import Example |
|------------|---------------|
| `APIConnections` | `from diagrams.azure.devops import APIConnections` |
| `APIManagementServices` | `from diagrams.azure.devops import APIManagementServices` |
| `ApplicationInsights` | `from diagrams.azure.devops import ApplicationInsights` |
| `Artifacts` | `from diagrams.azure.devops import Artifacts` |
| `AzureDevops` | `from diagrams.azure.devops import AzureDevops` |
| `Boards` | `from diagrams.azure.devops import Boards` |
| `ChangeAnalysis` | `from diagrams.azure.devops import ChangeAnalysis` |
| `Cloudtest` | `from diagrams.azure.devops import Cloudtest` |
| `CodeOptimization` | `from diagrams.azure.devops import CodeOptimization` |
| `Devops` | `from diagrams.azure.devops import Devops` |
| `DevopsStarter` | `from diagrams.azure.devops import DevopsStarter` |
| `DevtestLabs` | `from diagrams.azure.devops import DevtestLabs` |
| `LabAccounts` | `from diagrams.azure.devops import LabAccounts` |
| `LabServices` | `from diagrams.azure.devops import LabServices` |
| `LoadTesting` | `from diagrams.azure.devops import LoadTesting` |
| `Pipelines` | `from diagrams.azure.devops import Pipelines` |
| `Repos` | `from diagrams.azure.devops import Repos` |
| `TestPlans` | `from diagrams.azure.devops import TestPlans` |

### General

**Import:** `from diagrams.azure.general import ...`

| Class Name | Import Example |
|------------|---------------|
| `AllResources` | `from diagrams.azure.general import AllResources` |
| `Allresources` | `from diagrams.azure.general import Allresources` |
| `Azurehome` | `from diagrams.azure.general import Azurehome` |
| `Backlog` | `from diagrams.azure.general import Backlog` |
| `BizTalk` | `from diagrams.azure.general import BizTalk` |
| `BlobBlock` | `from diagrams.azure.general import BlobBlock` |
| `BlobPage` | `from diagrams.azure.general import BlobPage` |
| `Branch` | `from diagrams.azure.general import Branch` |
| `Browser` | `from diagrams.azure.general import Browser` |
| `Bug` | `from diagrams.azure.general import Bug` |
| `Builds` | `from diagrams.azure.general import Builds` |
| `Cache` | `from diagrams.azure.general import Cache` |
| `Code` | `from diagrams.azure.general import Code` |
| `Commit` | `from diagrams.azure.general import Commit` |
| `Controls` | `from diagrams.azure.general import Controls` |
| `ControlsHorizontal` | `from diagrams.azure.general import ControlsHorizontal` |
| `CostAlerts` | `from diagrams.azure.general import CostAlerts` |
| `CostAnalysis` | `from diagrams.azure.general import CostAnalysis` |
| `CostBudgets` | `from diagrams.azure.general import CostBudgets` |
| `CostManagement` | `from diagrams.azure.general import CostManagement` |
| `CostManagementAndBilling` | `from diagrams.azure.general import CostManagementAndBilling` |
| `Counter` | `from diagrams.azure.general import Counter` |
| `Cubes` | `from diagrams.azure.general import Cubes` |
| `Dashboard` | `from diagrams.azure.general import Dashboard` |
| `DevConsole` | `from diagrams.azure.general import DevConsole` |
| `Developertools` | `from diagrams.azure.general import Developertools` |
| `Download` | `from diagrams.azure.general import Download` |
| `Error` | `from diagrams.azure.general import Error` |
| `Extensions` | `from diagrams.azure.general import Extensions` |
| `FeaturePreviews` | `from diagrams.azure.general import FeaturePreviews` |
| `File` | `from diagrams.azure.general import File` |
| `Files` | `from diagrams.azure.general import Files` |
| `FolderBlank` | `from diagrams.azure.general import FolderBlank` |
| `FolderWebsite` | `from diagrams.azure.general import FolderWebsite` |
| `FreeServices` | `from diagrams.azure.general import FreeServices` |
| `Ftp` | `from diagrams.azure.general import Ftp` |
| `Gear` | `from diagrams.azure.general import Gear` |
| `GlobeError` | `from diagrams.azure.general import GlobeError` |
| `GlobeSuccess` | `from diagrams.azure.general import GlobeSuccess` |
| `GlobeWarning` | `from diagrams.azure.general import GlobeWarning` |
| `Guide` | `from diagrams.azure.general import Guide` |
| `Heart` | `from diagrams.azure.general import Heart` |
| `HelpAndSupport` | `from diagrams.azure.general import HelpAndSupport` |
| `Helpsupport` | `from diagrams.azure.general import Helpsupport` |
| `Image` | `from diagrams.azure.general import Image` |
| `Information` | `from diagrams.azure.general import Information` |
| `InputOutput` | `from diagrams.azure.general import InputOutput` |
| `JourneyHub` | `from diagrams.azure.general import JourneyHub` |
| `LaunchPortal` | `from diagrams.azure.general import LaunchPortal` |
| `Learn` | `from diagrams.azure.general import Learn` |
| `LoadTest` | `from diagrams.azure.general import LoadTest` |
| `Location` | `from diagrams.azure.general import Location` |
| `LogStreaming` | `from diagrams.azure.general import LogStreaming` |
| `ManagementGroups` | `from diagrams.azure.general import ManagementGroups` |
| `ManagementPortal` | `from diagrams.azure.general import ManagementPortal` |
| `Managementgroups` | `from diagrams.azure.general import Managementgroups` |
| `Marketplace` | `from diagrams.azure.general import Marketplace` |
| `MarketplaceManagement` | `from diagrams.azure.general import MarketplaceManagement` |
| `Media` | `from diagrams.azure.general import Media` |
| `MediaFile` | `from diagrams.azure.general import MediaFile` |
| `Mobile` | `from diagrams.azure.general import Mobile` |
| `MobileEngagement` | `from diagrams.azure.general import MobileEngagement` |
| `Module` | `from diagrams.azure.general import Module` |
| `Power` | `from diagrams.azure.general import Power` |
| `PowerUp` | `from diagrams.azure.general import PowerUp` |
| `Powershell` | `from diagrams.azure.general import Powershell` |
| `PreviewFeatures` | `from diagrams.azure.general import PreviewFeatures` |
| `ProcessExplorer` | `from diagrams.azure.general import ProcessExplorer` |
| `ProductionReadyDatabase` | `from diagrams.azure.general import ProductionReadyDatabase` |
| `QuickstartCenter` | `from diagrams.azure.general import QuickstartCenter` |
| `Quickstartcenter` | `from diagrams.azure.general import Quickstartcenter` |
| `Recent` | `from diagrams.azure.general import Recent` |
| `RegionManagement` | `from diagrams.azure.general import RegionManagement` |
| `Reservations` | `from diagrams.azure.general import Reservations` |
| `Resource` | `from diagrams.azure.general import Resource` |
| `ResourceExplorer` | `from diagrams.azure.general import ResourceExplorer` |
| `ResourceGroupList` | `from diagrams.azure.general import ResourceGroupList` |
| `ResourceGroups` | `from diagrams.azure.general import ResourceGroups` |
| `ResourceLinked` | `from diagrams.azure.general import ResourceLinked` |
| `Resourcegroups` | `from diagrams.azure.general import Resourcegroups` |
| `Scheduler` | `from diagrams.azure.general import Scheduler` |
| `Search` | `from diagrams.azure.general import Search` |
| `SearchGrid` | `from diagrams.azure.general import SearchGrid` |
| `ServerFarm` | `from diagrams.azure.general import ServerFarm` |
| `ServiceHealth` | `from diagrams.azure.general import ServiceHealth` |
| `Servicehealth` | `from diagrams.azure.general import Servicehealth` |
| `Shareddashboard` | `from diagrams.azure.general import Shareddashboard` |
| `Ssd` | `from diagrams.azure.general import Ssd` |
| `StorageAzureFiles` | `from diagrams.azure.general import StorageAzureFiles` |
| `StorageContainer` | `from diagrams.azure.general import StorageContainer` |
| `StorageQueue` | `from diagrams.azure.general import StorageQueue` |
| `Subscriptions` | `from diagrams.azure.general import Subscriptions` |
| `Support` | `from diagrams.azure.general import Support` |
| `Supportrequests` | `from diagrams.azure.general import Supportrequests` |
| `Table` | `from diagrams.azure.general import Table` |
| `Tag` | `from diagrams.azure.general import Tag` |
| `Tags` | `from diagrams.azure.general import Tags` |
| `Templates` | `from diagrams.azure.general import Templates` |
| `TfsVcRepository` | `from diagrams.azure.general import TfsVcRepository` |
| `Toolbox` | `from diagrams.azure.general import Toolbox` |
| `Troubleshoot` | `from diagrams.azure.general import Troubleshoot` |
| `Twousericon` | `from diagrams.azure.general import Twousericon` |
| `Userhealthicon` | `from diagrams.azure.general import Userhealthicon` |
| `Usericon` | `from diagrams.azure.general import Usericon` |
| `Userprivacy` | `from diagrams.azure.general import Userprivacy` |
| `Userresource` | `from diagrams.azure.general import Userresource` |
| `Versions` | `from diagrams.azure.general import Versions` |
| `WebSlots` | `from diagrams.azure.general import WebSlots` |
| `WebTest` | `from diagrams.azure.general import WebTest` |
| `WebsitePower` | `from diagrams.azure.general import WebsitePower` |
| `WebsiteStaging` | `from diagrams.azure.general import WebsiteStaging` |
| `Whatsnew` | `from diagrams.azure.general import Whatsnew` |
| `Workbooks` | `from diagrams.azure.general import Workbooks` |
| `Workflow` | `from diagrams.azure.general import Workflow` |

### Hybrid & Multi-Cloud

**Import:** `from diagrams.azure.hybridmulticloud import ...`

| Class Name | Import Example |
|------------|---------------|
| `AzureOperator5GCore` | `from diagrams.azure.hybridmulticloud import AzureOperator5GCore` |
| `AzureOperatorInsights` | `from diagrams.azure.hybridmulticloud import AzureOperatorInsights` |
| `AzureOperatorNexus` | `from diagrams.azure.hybridmulticloud import AzureOperatorNexus` |
| `AzureOperatorServiceManager` | `from diagrams.azure.hybridmulticloud import AzureOperatorServiceManager` |
| `AzureProgrammableConnectivity` | `from diagrams.azure.hybridmulticloud import AzureProgrammableConnectivity` |

### Identity

**Import:** `from diagrams.azure.identity import ...`

| Class Name | Import Example |
|------------|---------------|
| `ADB2C` | `from diagrams.azure.identity import ADB2C` |
| `ADDomainServices` | `from diagrams.azure.identity import ADDomainServices` |
| `ADIdentityProtection` | `from diagrams.azure.identity import ADIdentityProtection` |
| `ADPrivilegedIdentityManagement` | `from diagrams.azure.identity import ADPrivilegedIdentityManagement` |
| `APIProxy` | `from diagrams.azure.identity import APIProxy` |
| `AadLicenses` | `from diagrams.azure.identity import AadLicenses` |
| `AccessReview` | `from diagrams.azure.identity import AccessReview` |
| `ActiveDirectory` | `from diagrams.azure.identity import ActiveDirectory` |
| `ActiveDirectoryConnectHealth` | `from diagrams.azure.identity import ActiveDirectoryConnectHealth` |
| `AdministrativeUnits` | `from diagrams.azure.identity import AdministrativeUnits` |
| `AppRegistrations` | `from diagrams.azure.identity import AppRegistrations` |
| `AzureADB2C` | `from diagrams.azure.identity import AzureADB2C` |
| `AzureADDomainServices` | `from diagrams.azure.identity import AzureADDomainServices` |
| `AzureADIdentityProtection` | `from diagrams.azure.identity import AzureADIdentityProtection` |
| `AzureADPrivilegeIdentityManagement` | `from diagrams.azure.identity import AzureADPrivilegeIdentityManagement` |
| `AzureADPrivlegedIdentityManagement` | `from diagrams.azure.identity import AzureADPrivlegedIdentityManagement` |
| `AzureADRolesAndAdministrators` | `from diagrams.azure.identity import AzureADRolesAndAdministrators` |
| `AzureActiveDirectory` | `from diagrams.azure.identity import AzureActiveDirectory` |
| `AzureInformationProtection` | `from diagrams.azure.identity import AzureInformationProtection` |
| `ConditionalAccess` | `from diagrams.azure.identity import ConditionalAccess` |
| `CustomAzureADRoles` | `from diagrams.azure.identity import CustomAzureADRoles` |
| `EnterpriseApplications` | `from diagrams.azure.identity import EnterpriseApplications` |
| `EntraConnect` | `from diagrams.azure.identity import EntraConnect` |
| `EntraDomainServices` | `from diagrams.azure.identity import EntraDomainServices` |
| `EntraIDProtection` | `from diagrams.azure.identity import EntraIDProtection` |
| `EntraManagedIdentities` | `from diagrams.azure.identity import EntraManagedIdentities` |
| `EntraPrivlegedIdentityManagement` | `from diagrams.azure.identity import EntraPrivlegedIdentityManagement` |
| `EntraVerifiedID` | `from diagrams.azure.identity import EntraVerifiedID` |
| `ExternalIdentities` | `from diagrams.azure.identity import ExternalIdentities` |
| `GlobalSecureAccess` | `from diagrams.azure.identity import GlobalSecureAccess` |
| `Groups` | `from diagrams.azure.identity import Groups` |
| `IdentityGovernance` | `from diagrams.azure.identity import IdentityGovernance` |
| `InformationProtection` | `from diagrams.azure.identity import InformationProtection` |
| `InternetAccess` | `from diagrams.azure.identity import InternetAccess` |
| `ManagedIdentities` | `from diagrams.azure.identity import ManagedIdentities` |
| `PrivateAccess` | `from diagrams.azure.identity import PrivateAccess` |
| `Security` | `from diagrams.azure.identity import Security` |
| `TenantProperties` | `from diagrams.azure.identity import TenantProperties` |
| `UserSettings` | `from diagrams.azure.identity import UserSettings` |
| `Users` | `from diagrams.azure.identity import Users` |
| `VerifiableCredentials` | `from diagrams.azure.identity import VerifiableCredentials` |

### Integration

**Import:** `from diagrams.azure.integration import ...`

| Class Name | Import Example |
|------------|---------------|
| `APIConnections` | `from diagrams.azure.integration import APIConnections` |
| `APIForFhir` | `from diagrams.azure.integration import APIForFhir` |
| `APIManagement` | `from diagrams.azure.integration import APIManagement` |
| `APIManagementServices` | `from diagrams.azure.integration import APIManagementServices` |
| `AppConfiguration` | `from diagrams.azure.integration import AppConfiguration` |
| `AzureAPIForFhir` | `from diagrams.azure.integration import AzureAPIForFhir` |
| `AzureDataCatalog` | `from diagrams.azure.integration import AzureDataCatalog` |
| `AzureDataboxGateway` | `from diagrams.azure.integration import AzureDataboxGateway` |
| `AzureSQLServerStretchDatabases` | `from diagrams.azure.integration import AzureSQLServerStretchDatabases` |
| `AzureServiceBus` | `from diagrams.azure.integration import AzureServiceBus` |
| `AzureStackEdge` | `from diagrams.azure.integration import AzureStackEdge` |
| `DataCatalog` | `from diagrams.azure.integration import DataCatalog` |
| `DataFactories` | `from diagrams.azure.integration import DataFactories` |
| `EventGridDomains` | `from diagrams.azure.integration import EventGridDomains` |
| `EventGridSubscriptions` | `from diagrams.azure.integration import EventGridSubscriptions` |
| `EventGridTopics` | `from diagrams.azure.integration import EventGridTopics` |
| `IntegrationAccounts` | `from diagrams.azure.integration import IntegrationAccounts` |
| `IntegrationEnvironments` | `from diagrams.azure.integration import IntegrationEnvironments` |
| `IntegrationServiceEnvironments` | `from diagrams.azure.integration import IntegrationServiceEnvironments` |
| `LogicApps` | `from diagrams.azure.integration import LogicApps` |
| `LogicAppsCustomConnector` | `from diagrams.azure.integration import LogicAppsCustomConnector` |
| `PartnerNamespace` | `from diagrams.azure.integration import PartnerNamespace` |
| `PartnerRegistration` | `from diagrams.azure.integration import PartnerRegistration` |
| `PartnerTopic` | `from diagrams.azure.integration import PartnerTopic` |
| `PowerPlatform` | `from diagrams.azure.integration import PowerPlatform` |
| `Relays` | `from diagrams.azure.integration import Relays` |
| `SQLDataWarehouses` | `from diagrams.azure.integration import SQLDataWarehouses` |
| `SendgridAccounts` | `from diagrams.azure.integration import SendgridAccounts` |
| `ServiceBus` | `from diagrams.azure.integration import ServiceBus` |
| `ServiceBusRelays` | `from diagrams.azure.integration import ServiceBusRelays` |
| `ServiceCatalogManagedApplicationDefinitions` | `from diagrams.azure.integration import ServiceCatalogManagedApplicationDefinitions` |
| `SoftwareAsAService` | `from diagrams.azure.integration import SoftwareAsAService` |
| `StorsimpleDeviceManagers` | `from diagrams.azure.integration import StorsimpleDeviceManagers` |
| `SystemTopic` | `from diagrams.azure.integration import SystemTopic` |

### Intune

**Import:** `from diagrams.azure.intune import ...`

| Class Name | Import Example |
|------------|---------------|
| `AzureADRolesAndAdministrators` | `from diagrams.azure.intune import AzureADRolesAndAdministrators` |
| `ClientApps` | `from diagrams.azure.intune import ClientApps` |
| `DeviceCompliance` | `from diagrams.azure.intune import DeviceCompliance` |
| `DeviceConfiguration` | `from diagrams.azure.intune import DeviceConfiguration` |
| `DeviceEnrollment` | `from diagrams.azure.intune import DeviceEnrollment` |
| `DeviceSecurityApple` | `from diagrams.azure.intune import DeviceSecurityApple` |
| `DeviceSecurityGoogle` | `from diagrams.azure.intune import DeviceSecurityGoogle` |
| `DeviceSecurityWindows` | `from diagrams.azure.intune import DeviceSecurityWindows` |
| `Devices` | `from diagrams.azure.intune import Devices` |
| `Ebooks` | `from diagrams.azure.intune import Ebooks` |
| `ExchangeAccess` | `from diagrams.azure.intune import ExchangeAccess` |
| `Intune` | `from diagrams.azure.intune import Intune` |
| `IntuneAppProtection` | `from diagrams.azure.intune import IntuneAppProtection` |
| `IntuneForEducation` | `from diagrams.azure.intune import IntuneForEducation` |
| `Mindaro` | `from diagrams.azure.intune import Mindaro` |
| `SecurityBaselines` | `from diagrams.azure.intune import SecurityBaselines` |
| `SoftwareUpdates` | `from diagrams.azure.intune import SoftwareUpdates` |
| `TenantStatus` | `from diagrams.azure.intune import TenantStatus` |

### IoT

**Import:** `from diagrams.azure.iot import ...`

| Class Name | Import Example |
|------------|---------------|
| `AzureCosmosDb` | `from diagrams.azure.iot import AzureCosmosDb` |
| `AzureDataboxGateway` | `from diagrams.azure.iot import AzureDataboxGateway` |
| `AzureIotOperations` | `from diagrams.azure.iot import AzureIotOperations` |
| `AzureMapsAccounts` | `from diagrams.azure.iot import AzureMapsAccounts` |
| `AzureStack` | `from diagrams.azure.iot import AzureStack` |
| `DeviceProvisioningServices` | `from diagrams.azure.iot import DeviceProvisioningServices` |
| `DigitalTwins` | `from diagrams.azure.iot import DigitalTwins` |
| `EventGridSubscriptions` | `from diagrams.azure.iot import EventGridSubscriptions` |
| `EventHubClusters` | `from diagrams.azure.iot import EventHubClusters` |
| `EventHubs` | `from diagrams.azure.iot import EventHubs` |
| `FunctionApps` | `from diagrams.azure.iot import FunctionApps` |
| `IndustrialIot` | `from diagrams.azure.iot import IndustrialIot` |
| `IotCentralApplications` | `from diagrams.azure.iot import IotCentralApplications` |
| `IotEdge` | `from diagrams.azure.iot import IotEdge` |
| `IotHub` | `from diagrams.azure.iot import IotHub` |
| `IotHubSecurity` | `from diagrams.azure.iot import IotHubSecurity` |
| `LogicApps` | `from diagrams.azure.iot import LogicApps` |
| `MachineLearningStudioClassicWebServices` | `from diagrams.azure.iot import MachineLearningStudioClassicWebServices` |
| `MachineLearningStudioWebServicePlans` | `from diagrams.azure.iot import MachineLearningStudioWebServicePlans` |
| `MachineLearningStudioWorkspaces` | `from diagrams.azure.iot import MachineLearningStudioWorkspaces` |
| `Maps` | `from diagrams.azure.iot import Maps` |
| `NotificationHubNamespaces` | `from diagrams.azure.iot import NotificationHubNamespaces` |
| `NotificationHubs` | `from diagrams.azure.iot import NotificationHubs` |
| `Sphere` | `from diagrams.azure.iot import Sphere` |
| `StackHciPremium` | `from diagrams.azure.iot import StackHciPremium` |
| `StreamAnalyticsJobs` | `from diagrams.azure.iot import StreamAnalyticsJobs` |
| `TimeSeriesDataSets` | `from diagrams.azure.iot import TimeSeriesDataSets` |
| `TimeSeriesInsightsAccessPolicies` | `from diagrams.azure.iot import TimeSeriesInsightsAccessPolicies` |
| `TimeSeriesInsightsEnvironments` | `from diagrams.azure.iot import TimeSeriesInsightsEnvironments` |
| `TimeSeriesInsightsEventSources` | `from diagrams.azure.iot import TimeSeriesInsightsEventSources` |
| `TimeSeriesInsightsEventsSources` | `from diagrams.azure.iot import TimeSeriesInsightsEventsSources` |
| `Windows10CoreServices` | `from diagrams.azure.iot import Windows10CoreServices` |
| `Windows10IotCoreServices` | `from diagrams.azure.iot import Windows10IotCoreServices` |

### Management & Governance

**Import:** `from diagrams.azure.managementgovernance import ...`

| Class Name | Import Example |
|------------|---------------|
| `ActivityLog` | `from diagrams.azure.managementgovernance import ActivityLog` |
| `Advisor` | `from diagrams.azure.managementgovernance import Advisor` |
| `Alerts` | `from diagrams.azure.managementgovernance import Alerts` |
| `ApplicationInsights` | `from diagrams.azure.managementgovernance import ApplicationInsights` |
| `ArcMachines` | `from diagrams.azure.managementgovernance import ArcMachines` |
| `AutomationAccounts` | `from diagrams.azure.managementgovernance import AutomationAccounts` |
| `AzureArc` | `from diagrams.azure.managementgovernance import AzureArc` |
| `AzureLighthouse` | `from diagrams.azure.managementgovernance import AzureLighthouse` |
| `Blueprints` | `from diagrams.azure.managementgovernance import Blueprints` |
| `Compliance` | `from diagrams.azure.managementgovernance import Compliance` |
| `CostManagementAndBilling` | `from diagrams.azure.managementgovernance import CostManagementAndBilling` |
| `CustomerLockboxForMicrosoftAzure` | `from diagrams.azure.managementgovernance import CustomerLockboxForMicrosoftAzure` |
| `DiagnosticsSettings` | `from diagrams.azure.managementgovernance import DiagnosticsSettings` |
| `Education` | `from diagrams.azure.managementgovernance import Education` |
| `IntuneTrends` | `from diagrams.azure.managementgovernance import IntuneTrends` |
| `LogAnalyticsWorkspaces` | `from diagrams.azure.managementgovernance import LogAnalyticsWorkspaces` |
| `Machinesazurearc` | `from diagrams.azure.managementgovernance import Machinesazurearc` |
| `ManagedApplicationsCenter` | `from diagrams.azure.managementgovernance import ManagedApplicationsCenter` |
| `ManagedDesktop` | `from diagrams.azure.managementgovernance import ManagedDesktop` |
| `Metrics` | `from diagrams.azure.managementgovernance import Metrics` |
| `Monitor` | `from diagrams.azure.managementgovernance import Monitor` |
| `MyCustomers` | `from diagrams.azure.managementgovernance import MyCustomers` |
| `OperationLogClassic` | `from diagrams.azure.managementgovernance import OperationLogClassic` |
| `Policy` | `from diagrams.azure.managementgovernance import Policy` |
| `RecoveryServicesVaults` | `from diagrams.azure.managementgovernance import RecoveryServicesVaults` |
| `ResourceGraphExplorer` | `from diagrams.azure.managementgovernance import ResourceGraphExplorer` |
| `ResourcesProvider` | `from diagrams.azure.managementgovernance import ResourcesProvider` |
| `SchedulerJobCollections` | `from diagrams.azure.managementgovernance import SchedulerJobCollections` |
| `ServiceCatalogMad` | `from diagrams.azure.managementgovernance import ServiceCatalogMad` |
| `ServiceProviders` | `from diagrams.azure.managementgovernance import ServiceProviders` |
| `Solutions` | `from diagrams.azure.managementgovernance import Solutions` |
| `UniversalPrint` | `from diagrams.azure.managementgovernance import UniversalPrint` |
| `UserPrivacy` | `from diagrams.azure.managementgovernance import UserPrivacy` |

### Menu

**Import:** `from diagrams.azure.menu import ...`

| Class Name | Import Example |
|------------|---------------|
| `Keys` | `from diagrams.azure.menu import Keys` |

### Migrate

**Import:** `from diagrams.azure.migrate import ...`

| Class Name | Import Example |
|------------|---------------|
| `AzureDataboxGateway` | `from diagrams.azure.migrate import AzureDataboxGateway` |
| `AzureMigrate` | `from diagrams.azure.migrate import AzureMigrate` |
| `AzureStackEdge` | `from diagrams.azure.migrate import AzureStackEdge` |
| `CostManagementAndBilling` | `from diagrams.azure.migrate import CostManagementAndBilling` |
| `DataBox` | `from diagrams.azure.migrate import DataBox` |
| `RecoveryServicesVaults` | `from diagrams.azure.migrate import RecoveryServicesVaults` |

### Migration

**Import:** `from diagrams.azure.migration import ...`

| Class Name | Import Example |
|------------|---------------|
| `AzureDatabaseMigrationServices` | `from diagrams.azure.migration import AzureDatabaseMigrationServices` |
| `DataBox` | `from diagrams.azure.migration import DataBox` |
| `DataBoxEdge` | `from diagrams.azure.migration import DataBoxEdge` |
| `DatabaseMigrationServices` | `from diagrams.azure.migration import DatabaseMigrationServices` |
| `MigrationProjects` | `from diagrams.azure.migration import MigrationProjects` |
| `RecoveryServicesVaults` | `from diagrams.azure.migration import RecoveryServicesVaults` |

### Mixed Reality

**Import:** `from diagrams.azure.mixedreality import ...`

| Class Name | Import Example |
|------------|---------------|
| `RemoteRendering` | `from diagrams.azure.mixedreality import RemoteRendering` |
| `SpatialAnchorAccounts` | `from diagrams.azure.mixedreality import SpatialAnchorAccounts` |

### Machine Learning

**Import:** `from diagrams.azure.ml import ...`

| Class Name | Import Example |
|------------|---------------|
| `AzureOpenAI` | `from diagrams.azure.ml import AzureOpenAI` |
| `AzureSpeechService` | `from diagrams.azure.ml import AzureSpeechService` |
| `BatchAI` | `from diagrams.azure.ml import BatchAI` |
| `BotServices` | `from diagrams.azure.ml import BotServices` |
| `CognitiveServices` | `from diagrams.azure.ml import CognitiveServices` |
| `GenomicsAccounts` | `from diagrams.azure.ml import GenomicsAccounts` |
| `MachineLearningServiceWorkspaces` | `from diagrams.azure.ml import MachineLearningServiceWorkspaces` |
| `MachineLearningStudioWebServicePlans` | `from diagrams.azure.ml import MachineLearningStudioWebServicePlans` |
| `MachineLearningStudioWebServices` | `from diagrams.azure.ml import MachineLearningStudioWebServices` |
| `MachineLearningStudioWorkspaces` | `from diagrams.azure.ml import MachineLearningStudioWorkspaces` |

### Mobile

**Import:** `from diagrams.azure.mobile import ...`

| Class Name | Import Example |
|------------|---------------|
| `AppServiceMobile` | `from diagrams.azure.mobile import AppServiceMobile` |
| `AppServices` | `from diagrams.azure.mobile import AppServices` |
| `MobileEngagement` | `from diagrams.azure.mobile import MobileEngagement` |
| `NotificationHubs` | `from diagrams.azure.mobile import NotificationHubs` |
| `PowerPlatform` | `from diagrams.azure.mobile import PowerPlatform` |

### Monitor

**Import:** `from diagrams.azure.monitor import ...`

| Class Name | Import Example |
|------------|---------------|
| `ActivityLog` | `from diagrams.azure.monitor import ActivityLog` |
| `ApplicationInsights` | `from diagrams.azure.monitor import ApplicationInsights` |
| `AutoScale` | `from diagrams.azure.monitor import AutoScale` |
| `AzureMonitorsForSAPSolutions` | `from diagrams.azure.monitor import AzureMonitorsForSAPSolutions` |
| `AzureWorkbooks` | `from diagrams.azure.monitor import AzureWorkbooks` |
| `ChangeAnalysis` | `from diagrams.azure.monitor import ChangeAnalysis` |
| `DiagnosticsSettings` | `from diagrams.azure.monitor import DiagnosticsSettings` |
| `LogAnalyticsWorkspaces` | `from diagrams.azure.monitor import LogAnalyticsWorkspaces` |
| `Logs` | `from diagrams.azure.monitor import Logs` |
| `Metrics` | `from diagrams.azure.monitor import Metrics` |
| `Monitor` | `from diagrams.azure.monitor import Monitor` |
| `NetworkWatcher` | `from diagrams.azure.monitor import NetworkWatcher` |

### Network

**Import:** `from diagrams.azure.network import ...`

| Class Name | Import Example |
|------------|---------------|
| `ApplicationGateway` | `from diagrams.azure.network import ApplicationGateway` |
| `ApplicationSecurityGroups` | `from diagrams.azure.network import ApplicationSecurityGroups` |
| `CDNProfiles` | `from diagrams.azure.network import CDNProfiles` |
| `Connections` | `from diagrams.azure.network import Connections` |
| `DDOSProtectionPlans` | `from diagrams.azure.network import DDOSProtectionPlans` |
| `DNSPrivateZones` | `from diagrams.azure.network import DNSPrivateZones` |
| `DNSZones` | `from diagrams.azure.network import DNSZones` |
| `ExpressrouteCircuits` | `from diagrams.azure.network import ExpressrouteCircuits` |
| `Firewall` | `from diagrams.azure.network import Firewall` |
| `FrontDoors` | `from diagrams.azure.network import FrontDoors` |
| `LoadBalancers` | `from diagrams.azure.network import LoadBalancers` |
| `LocalNetworkGateways` | `from diagrams.azure.network import LocalNetworkGateways` |
| `NetworkInterfaces` | `from diagrams.azure.network import NetworkInterfaces` |
| `NetworkSecurityGroupsClassic` | `from diagrams.azure.network import NetworkSecurityGroupsClassic` |
| `NetworkWatcher` | `from diagrams.azure.network import NetworkWatcher` |
| `OnPremisesDataGateways` | `from diagrams.azure.network import OnPremisesDataGateways` |
| `PrivateEndpoint` | `from diagrams.azure.network import PrivateEndpoint` |
| `PublicIpAddresses` | `from diagrams.azure.network import PublicIpAddresses` |
| `ReservedIpAddressesClassic` | `from diagrams.azure.network import ReservedIpAddressesClassic` |
| `RouteFilters` | `from diagrams.azure.network import RouteFilters` |
| `RouteTables` | `from diagrams.azure.network import RouteTables` |
| `ServiceEndpointPolicies` | `from diagrams.azure.network import ServiceEndpointPolicies` |
| `Subnets` | `from diagrams.azure.network import Subnets` |
| `TrafficManagerProfiles` | `from diagrams.azure.network import TrafficManagerProfiles` |
| `VirtualNetworkClassic` | `from diagrams.azure.network import VirtualNetworkClassic` |
| `VirtualNetworkGateways` | `from diagrams.azure.network import VirtualNetworkGateways` |
| `VirtualNetworks` | `from diagrams.azure.network import VirtualNetworks` |
| `VirtualWans` | `from diagrams.azure.network import VirtualWans` |

### Networking

**Import:** `from diagrams.azure.networking import ...`

| Class Name | Import Example |
|------------|---------------|
| `ApplicationGateways` | `from diagrams.azure.networking import ApplicationGateways` |
| `AtmMultistack` | `from diagrams.azure.networking import AtmMultistack` |
| `AzureCommunicationsGateway` | `from diagrams.azure.networking import AzureCommunicationsGateway` |
| `AzureFirewallManager` | `from diagrams.azure.networking import AzureFirewallManager` |
| `AzureFirewallPolicy` | `from diagrams.azure.networking import AzureFirewallPolicy` |
| `Bastions` | `from diagrams.azure.networking import Bastions` |
| `CDNProfiles` | `from diagrams.azure.networking import CDNProfiles` |
| `ConnectedCache` | `from diagrams.azure.networking import ConnectedCache` |
| `Connections` | `from diagrams.azure.networking import Connections` |
| `DDOSProtectionPlans` | `from diagrams.azure.networking import DDOSProtectionPlans` |
| `DNSMultistack` | `from diagrams.azure.networking import DNSMultistack` |
| `DNSPrivateResolver` | `from diagrams.azure.networking import DNSPrivateResolver` |
| `DNSSecurityPolicy` | `from diagrams.azure.networking import DNSSecurityPolicy` |
| `DNSZones` | `from diagrams.azure.networking import DNSZones` |
| `ExpressrouteCircuits` | `from diagrams.azure.networking import ExpressrouteCircuits` |
| `Firewalls` | `from diagrams.azure.networking import Firewalls` |
| `FrontDoorAndCDNProfiles` | `from diagrams.azure.networking import FrontDoorAndCDNProfiles` |
| `IpAddressManager` | `from diagrams.azure.networking import IpAddressManager` |
| `IpGroups` | `from diagrams.azure.networking import IpGroups` |
| `LoadBalancerHub` | `from diagrams.azure.networking import LoadBalancerHub` |
| `LoadBalancers` | `from diagrams.azure.networking import LoadBalancers` |
| `LocalNetworkGateways` | `from diagrams.azure.networking import LocalNetworkGateways` |
| `Nat` | `from diagrams.azure.networking import Nat` |
| `NetworkInterfaces` | `from diagrams.azure.networking import NetworkInterfaces` |
| `NetworkSecurityGroups` | `from diagrams.azure.networking import NetworkSecurityGroups` |
| `NetworkWatcher` | `from diagrams.azure.networking import NetworkWatcher` |
| `OnPremisesDataGateways` | `from diagrams.azure.networking import OnPremisesDataGateways` |
| `PrivateLink` | `from diagrams.azure.networking import PrivateLink` |
| `PrivateLinkService` | `from diagrams.azure.networking import PrivateLinkService` |
| `PrivateLinkServices` | `from diagrams.azure.networking import PrivateLinkServices` |
| `ProximityPlacementGroups` | `from diagrams.azure.networking import ProximityPlacementGroups` |
| `PublicIpAddresses` | `from diagrams.azure.networking import PublicIpAddresses` |
| `PublicIpAddressesClassic` | `from diagrams.azure.networking import PublicIpAddressesClassic` |
| `PublicIpPrefixes` | `from diagrams.azure.networking import PublicIpPrefixes` |
| `ReservedIpAddressesClassic` | `from diagrams.azure.networking import ReservedIpAddressesClassic` |
| `ResourceManagementPrivateLink` | `from diagrams.azure.networking import ResourceManagementPrivateLink` |
| `RouteFilters` | `from diagrams.azure.networking import RouteFilters` |
| `RouteTables` | `from diagrams.azure.networking import RouteTables` |
| `ServiceEndpointPolicies` | `from diagrams.azure.networking import ServiceEndpointPolicies` |
| `SpotVM` | `from diagrams.azure.networking import SpotVM` |
| `SpotVmss` | `from diagrams.azure.networking import SpotVmss` |
| `Subnet` | `from diagrams.azure.networking import Subnet` |
| `TrafficController` | `from diagrams.azure.networking import TrafficController` |
| `TrafficManagerProfiles` | `from diagrams.azure.networking import TrafficManagerProfiles` |
| `VirtualNetworkGateways` | `from diagrams.azure.networking import VirtualNetworkGateways` |
| `VirtualNetworks` | `from diagrams.azure.networking import VirtualNetworks` |
| `VirtualNetworksClassic` | `from diagrams.azure.networking import VirtualNetworksClassic` |
| `VirtualRouter` | `from diagrams.azure.networking import VirtualRouter` |
| `VirtualWanHub` | `from diagrams.azure.networking import VirtualWanHub` |
| `VirtualWans` | `from diagrams.azure.networking import VirtualWans` |
| `WebApplicationFirewallPolicieswaf` | `from diagrams.azure.networking import WebApplicationFirewallPolicieswaf` |

### New Icons

**Import:** `from diagrams.azure.newicons import ...`

| Class Name | Import Example |
|------------|---------------|
| `AzureSustainability` | `from diagrams.azure.newicons import AzureSustainability` |
| `ConnectedVehiclePlatform` | `from diagrams.azure.newicons import ConnectedVehiclePlatform` |
| `EntraConnectHealth` | `from diagrams.azure.newicons import EntraConnectHealth` |
| `EntraConnectSync` | `from diagrams.azure.newicons import EntraConnectSync` |
| `IcmTroubleshooting` | `from diagrams.azure.newicons import IcmTroubleshooting` |
| `Osconfig` | `from diagrams.azure.newicons import Osconfig` |
| `StorageActions` | `from diagrams.azure.newicons import StorageActions` |

### Other

**Import:** `from diagrams.azure.other import ...`

| Class Name | Import Example |
|------------|---------------|
| `AadLicenses` | `from diagrams.azure.other import AadLicenses` |
| `AksIstio` | `from diagrams.azure.other import AksIstio` |
| `AppComplianceAutomation` | `from diagrams.azure.other import AppComplianceAutomation` |
| `AppRegistrations` | `from diagrams.azure.other import AppRegistrations` |
| `Aquila` | `from diagrams.azure.other import Aquila` |
| `ArcDataServices` | `from diagrams.azure.other import ArcDataServices` |
| `ArcKubernetes` | `from diagrams.azure.other import ArcKubernetes` |
| `ArcPostgresql` | `from diagrams.azure.other import ArcPostgresql` |
| `ArcSQLManagedInstance` | `from diagrams.azure.other import ArcSQLManagedInstance` |
| `ArcSQLServer` | `from diagrams.azure.other import ArcSQLServer` |
| `AvsVM` | `from diagrams.azure.other import AvsVM` |
| `AzureA` | `from diagrams.azure.other import AzureA` |
| `AzureBackupCenter` | `from diagrams.azure.other import AzureBackupCenter` |
| `AzureCenterForSAP` | `from diagrams.azure.other import AzureCenterForSAP` |
| `AzureChaosStudio` | `from diagrams.azure.other import AzureChaosStudio` |
| `AzureCloudShell` | `from diagrams.azure.other import AzureCloudShell` |
| `AzureCommunicationServices` | `from diagrams.azure.other import AzureCommunicationServices` |
| `AzureComputeGalleries` | `from diagrams.azure.other import AzureComputeGalleries` |
| `AzureDeploymentEnvironments` | `from diagrams.azure.other import AzureDeploymentEnvironments` |
| `AzureDevTunnels` | `from diagrams.azure.other import AzureDevTunnels` |
| `AzureEdgeHardwareCenter` | `from diagrams.azure.other import AzureEdgeHardwareCenter` |
| `AzureHpcWorkbenches` | `from diagrams.azure.other import AzureHpcWorkbenches` |
| `AzureLoadTesting` | `from diagrams.azure.other import AzureLoadTesting` |
| `AzureManagedGrafana` | `from diagrams.azure.other import AzureManagedGrafana` |
| `AzureMonitorDashboard` | `from diagrams.azure.other import AzureMonitorDashboard` |
| `AzureNetworkFunctionManager` | `from diagrams.azure.other import AzureNetworkFunctionManager` |
| `AzureNetworkFunctionManagerFunctions` | `from diagrams.azure.other import AzureNetworkFunctionManagerFunctions` |
| `AzureOrbital` | `from diagrams.azure.other import AzureOrbital` |
| `AzureQuotas` | `from diagrams.azure.other import AzureQuotas` |
| `AzureSphere` | `from diagrams.azure.other import AzureSphere` |
| `AzureStorageMover` | `from diagrams.azure.other import AzureStorageMover` |
| `AzureSupportCenterBlue` | `from diagrams.azure.other import AzureSupportCenterBlue` |
| `AzureVideoIndexer` | `from diagrams.azure.other import AzureVideoIndexer` |
| `AzureVirtualDesktop` | `from diagrams.azure.other import AzureVirtualDesktop` |
| `AzureVmwareSolution` | `from diagrams.azure.other import AzureVmwareSolution` |
| `Azureattestation` | `from diagrams.azure.other import Azureattestation` |
| `Azurite` | `from diagrams.azure.other import Azurite` |
| `BackupVault` | `from diagrams.azure.other import BackupVault` |
| `BareMetalInfrastructure` | `from diagrams.azure.other import BareMetalInfrastructure` |
| `CapacityReservationGroups` | `from diagrams.azure.other import CapacityReservationGroups` |
| `CentralServiceInstanceForSAP` | `from diagrams.azure.other import CentralServiceInstanceForSAP` |
| `Ceres` | `from diagrams.azure.other import Ceres` |
| `CloudServicesExtendedSupport` | `from diagrams.azure.other import CloudServicesExtendedSupport` |
| `CommunityImages` | `from diagrams.azure.other import CommunityImages` |
| `ComplianceCenter` | `from diagrams.azure.other import ComplianceCenter` |
| `ConfidentialLedgers` | `from diagrams.azure.other import ConfidentialLedgers` |
| `ContainerAppsEnvironments` | `from diagrams.azure.other import ContainerAppsEnvironments` |
| `CostExport` | `from diagrams.azure.other import CostExport` |
| `CustomIpPrefix` | `from diagrams.azure.other import CustomIpPrefix` |
| `DashboardHub` | `from diagrams.azure.other import DashboardHub` |
| `DataCollectionRules` | `from diagrams.azure.other import DataCollectionRules` |
| `DatabaseInstanceForSAP` | `from diagrams.azure.other import DatabaseInstanceForSAP` |
| `DedicatedHsm` | `from diagrams.azure.other import DedicatedHsm` |
| `DefenderCmLocalManager` | `from diagrams.azure.other import DefenderCmLocalManager` |
| `DefenderDcsController` | `from diagrams.azure.other import DefenderDcsController` |
| `DefenderDistributerControlSystem` | `from diagrams.azure.other import DefenderDistributerControlSystem` |
| `DefenderEngineeringStation` | `from diagrams.azure.other import DefenderEngineeringStation` |
| `DefenderExternalManagement` | `from diagrams.azure.other import DefenderExternalManagement` |
| `DefenderFreezerMonitor` | `from diagrams.azure.other import DefenderFreezerMonitor` |
| `DefenderHistorian` | `from diagrams.azure.other import DefenderHistorian` |
| `DefenderHmi` | `from diagrams.azure.other import DefenderHmi` |
| `DefenderIndustrialPackagingSystem` | `from diagrams.azure.other import DefenderIndustrialPackagingSystem` |
| `DefenderIndustrialPrinter` | `from diagrams.azure.other import DefenderIndustrialPrinter` |
| `DefenderIndustrialRobot` | `from diagrams.azure.other import DefenderIndustrialRobot` |
| `DefenderIndustrialScaleSystem` | `from diagrams.azure.other import DefenderIndustrialScaleSystem` |
| `DefenderMarquee` | `from diagrams.azure.other import DefenderMarquee` |
| `DefenderMeter` | `from diagrams.azure.other import DefenderMeter` |
| `DefenderPlc` | `from diagrams.azure.other import DefenderPlc` |
| `DefenderPneumaticDevice` | `from diagrams.azure.other import DefenderPneumaticDevice` |
| `DefenderProgramableBoard` | `from diagrams.azure.other import DefenderProgramableBoard` |
| `DefenderRelay` | `from diagrams.azure.other import DefenderRelay` |
| `DefenderRobotController` | `from diagrams.azure.other import DefenderRobotController` |
| `DefenderRtu` | `from diagrams.azure.other import DefenderRtu` |
| `DefenderSensor` | `from diagrams.azure.other import DefenderSensor` |
| `DefenderSlot` | `from diagrams.azure.other import DefenderSlot` |
| `DefenderWebGuidingSystem` | `from diagrams.azure.other import DefenderWebGuidingSystem` |
| `DeviceUpdateIotHub` | `from diagrams.azure.other import DeviceUpdateIotHub` |
| `DiskPool` | `from diagrams.azure.other import DiskPool` |
| `EdgeManagement` | `from diagrams.azure.other import EdgeManagement` |
| `ElasticSan` | `from diagrams.azure.other import ElasticSan` |
| `ExchangeOnPremisesAccess` | `from diagrams.azure.other import ExchangeOnPremisesAccess` |
| `ExpressRouteTrafficCollector` | `from diagrams.azure.other import ExpressRouteTrafficCollector` |
| `ExpressrouteDirect` | `from diagrams.azure.other import ExpressrouteDirect` |
| `FhirService` | `from diagrams.azure.other import FhirService` |
| `Fiji` | `from diagrams.azure.other import Fiji` |
| `HdiAksCluster` | `from diagrams.azure.other import HdiAksCluster` |
| `InstancePools` | `from diagrams.azure.other import InstancePools` |
| `InternetAnalyzerProfiles` | `from diagrams.azure.other import InternetAnalyzerProfiles` |
| `KubernetesFleetManager` | `from diagrams.azure.other import KubernetesFleetManager` |
| `LocalNetworkGateways` | `from diagrams.azure.other import LocalNetworkGateways` |
| `LogAnalyticsQueryPack` | `from diagrams.azure.other import LogAnalyticsQueryPack` |
| `ManagedInstanceApacheCassandra` | `from diagrams.azure.other import ManagedInstanceApacheCassandra` |
| `MedtechService` | `from diagrams.azure.other import MedtechService` |
| `MicrosoftDevBox` | `from diagrams.azure.other import MicrosoftDevBox` |
| `MissionLandingZone` | `from diagrams.azure.other import MissionLandingZone` |
| `MobileNetworks` | `from diagrams.azure.other import MobileNetworks` |
| `ModularDataCenter` | `from diagrams.azure.other import ModularDataCenter` |
| `NetworkManagers` | `from diagrams.azure.other import NetworkManagers` |
| `NetworkSecurityPerimeters` | `from diagrams.azure.other import NetworkSecurityPerimeters` |
| `OpenSupplyChainPlatform` | `from diagrams.azure.other import OpenSupplyChainPlatform` |
| `PeeringService` | `from diagrams.azure.other import PeeringService` |
| `Peerings` | `from diagrams.azure.other import Peerings` |
| `PrivateEndpoints` | `from diagrams.azure.other import PrivateEndpoints` |
| `ReservedCapacity` | `from diagrams.azure.other import ReservedCapacity` |
| `ResourceGuard` | `from diagrams.azure.other import ResourceGuard` |
| `ResourceMover` | `from diagrams.azure.other import ResourceMover` |
| `Rtos` | `from diagrams.azure.other import Rtos` |
| `SavingsPlans` | `from diagrams.azure.other import SavingsPlans` |
| `ScvmmManagementServers` | `from diagrams.azure.other import ScvmmManagementServers` |
| `SonicDash` | `from diagrams.azure.other import SonicDash` |
| `SshKeys` | `from diagrams.azure.other import SshKeys` |
| `StorageFunctions` | `from diagrams.azure.other import StorageFunctions` |
| `TargetsManagement` | `from diagrams.azure.other import TargetsManagement` |
| `TemplateSpecs` | `from diagrams.azure.other import TemplateSpecs` |
| `TestBase` | `from diagrams.azure.other import TestBase` |
| `UpdateManagementCenter` | `from diagrams.azure.other import UpdateManagementCenter` |
| `VMAppDefinitions` | `from diagrams.azure.other import VMAppDefinitions` |
| `VMAppVersions` | `from diagrams.azure.other import VMAppVersions` |
| `VMImageVersion` | `from diagrams.azure.other import VMImageVersion` |
| `VideoAnalyzers` | `from diagrams.azure.other import VideoAnalyzers` |
| `VirtualEnclaves` | `from diagrams.azure.other import VirtualEnclaves` |
| `VirtualInstanceForSAP` | `from diagrams.azure.other import VirtualInstanceForSAP` |
| `VirtualVisitsBuilder` | `from diagrams.azure.other import VirtualVisitsBuilder` |
| `Wac` | `from diagrams.azure.other import Wac` |
| `WebAppDatabase` | `from diagrams.azure.other import WebAppDatabase` |
| `WebJobs` | `from diagrams.azure.other import WebJobs` |
| `WindowsNotificationServices` | `from diagrams.azure.other import WindowsNotificationServices` |
| `WorkerContainerApp` | `from diagrams.azure.other import WorkerContainerApp` |

### Security

**Import:** `from diagrams.azure.security import ...`

| Class Name | Import Example |
|------------|---------------|
| `ApplicationSecurityGroups` | `from diagrams.azure.security import ApplicationSecurityGroups` |
| `AzureADAuthenticationMethods` | `from diagrams.azure.security import AzureADAuthenticationMethods` |
| `AzureADIdentityProtection` | `from diagrams.azure.security import AzureADIdentityProtection` |
| `AzureADPrivlegedIdentityManagement` | `from diagrams.azure.security import AzureADPrivlegedIdentityManagement` |
| `AzureADRiskySignins` | `from diagrams.azure.security import AzureADRiskySignins` |
| `AzureADRiskyUsers` | `from diagrams.azure.security import AzureADRiskyUsers` |
| `AzureInformationProtection` | `from diagrams.azure.security import AzureInformationProtection` |
| `AzureSentinel` | `from diagrams.azure.security import AzureSentinel` |
| `ConditionalAccess` | `from diagrams.azure.security import ConditionalAccess` |
| `Defender` | `from diagrams.azure.security import Defender` |
| `Detonation` | `from diagrams.azure.security import Detonation` |
| `ExtendedSecurityUpdates` | `from diagrams.azure.security import ExtendedSecurityUpdates` |
| `Extendedsecurityupdates` | `from diagrams.azure.security import Extendedsecurityupdates` |
| `IdentitySecureScore` | `from diagrams.azure.security import IdentitySecureScore` |
| `KeyVaults` | `from diagrams.azure.security import KeyVaults` |
| `MicrosoftDefenderEasm` | `from diagrams.azure.security import MicrosoftDefenderEasm` |
| `MicrosoftDefenderForCloud` | `from diagrams.azure.security import MicrosoftDefenderForCloud` |
| `MicrosoftDefenderForIot` | `from diagrams.azure.security import MicrosoftDefenderForIot` |
| `MultifactorAuthentication` | `from diagrams.azure.security import MultifactorAuthentication` |
| `SecurityCenter` | `from diagrams.azure.security import SecurityCenter` |
| `Sentinel` | `from diagrams.azure.security import Sentinel` |
| `UserSettings` | `from diagrams.azure.security import UserSettings` |

### Storage

**Import:** `from diagrams.azure.storage import ...`

| Class Name | Import Example |
|------------|---------------|
| `ArchiveStorage` | `from diagrams.azure.storage import ArchiveStorage` |
| `AzureDataboxGateway` | `from diagrams.azure.storage import AzureDataboxGateway` |
| `AzureFileshares` | `from diagrams.azure.storage import AzureFileshares` |
| `AzureHcpCache` | `from diagrams.azure.storage import AzureHcpCache` |
| `AzureNetappFiles` | `from diagrams.azure.storage import AzureNetappFiles` |
| `AzureStackEdge` | `from diagrams.azure.storage import AzureStackEdge` |
| `Azurefxtedgefiler` | `from diagrams.azure.storage import Azurefxtedgefiler` |
| `BlobStorage` | `from diagrams.azure.storage import BlobStorage` |
| `DataBox` | `from diagrams.azure.storage import DataBox` |
| `DataBoxEdgeDataBoxGateway` | `from diagrams.azure.storage import DataBoxEdgeDataBoxGateway` |
| `DataLakeStorage` | `from diagrams.azure.storage import DataLakeStorage` |
| `DataLakeStorageGen1` | `from diagrams.azure.storage import DataLakeStorageGen1` |
| `DataShareInvitations` | `from diagrams.azure.storage import DataShareInvitations` |
| `DataShares` | `from diagrams.azure.storage import DataShares` |
| `GeneralStorage` | `from diagrams.azure.storage import GeneralStorage` |
| `ImportExportJobs` | `from diagrams.azure.storage import ImportExportJobs` |
| `NetappFiles` | `from diagrams.azure.storage import NetappFiles` |
| `QueuesStorage` | `from diagrams.azure.storage import QueuesStorage` |
| `RecoveryServicesVaults` | `from diagrams.azure.storage import RecoveryServicesVaults` |
| `StorageAccounts` | `from diagrams.azure.storage import StorageAccounts` |
| `StorageAccountsClassic` | `from diagrams.azure.storage import StorageAccountsClassic` |
| `StorageExplorer` | `from diagrams.azure.storage import StorageExplorer` |
| `StorageSyncServices` | `from diagrams.azure.storage import StorageSyncServices` |
| `StorsimpleDataManagers` | `from diagrams.azure.storage import StorsimpleDataManagers` |
| `StorsimpleDeviceManagers` | `from diagrams.azure.storage import StorsimpleDeviceManagers` |
| `TableStorage` | `from diagrams.azure.storage import TableStorage` |

### Web

**Import:** `from diagrams.azure.web import ...`

| Class Name | Import Example |
|------------|---------------|
| `APICenter` | `from diagrams.azure.web import APICenter` |
| `APIConnections` | `from diagrams.azure.web import APIConnections` |
| `APIManagementServices` | `from diagrams.azure.web import APIManagementServices` |
| `AppServiceCertificates` | `from diagrams.azure.web import AppServiceCertificates` |
| `AppServiceDomains` | `from diagrams.azure.web import AppServiceDomains` |
| `AppServiceEnvironments` | `from diagrams.azure.web import AppServiceEnvironments` |
| `AppServicePlans` | `from diagrams.azure.web import AppServicePlans` |
| `AppServices` | `from diagrams.azure.web import AppServices` |
| `AppSpace` | `from diagrams.azure.web import AppSpace` |
| `AzureMediaService` | `from diagrams.azure.web import AzureMediaService` |
| `AzureSpringApps` | `from diagrams.azure.web import AzureSpringApps` |
| `CognitiveSearch` | `from diagrams.azure.web import CognitiveSearch` |
| `CognitiveServices` | `from diagrams.azure.web import CognitiveServices` |
| `FrontDoorAndCDNProfiles` | `from diagrams.azure.web import FrontDoorAndCDNProfiles` |
| `MediaServices` | `from diagrams.azure.web import MediaServices` |
| `NotificationHubNamespaces` | `from diagrams.azure.web import NotificationHubNamespaces` |
| `PowerPlatform` | `from diagrams.azure.web import PowerPlatform` |
| `Search` | `from diagrams.azure.web import Search` |
| `Signalr` | `from diagrams.azure.web import Signalr` |
| `StaticApps` | `from diagrams.azure.web import StaticApps` |

---

## Google Cloud Platform (GCP)

_Complete GCP service icon catalog_ — **144 icons** across **13 categories**

### Analytics

**Import:** `from diagrams.gcp.analytics import ...`

| Class Name | Import Example |
|------------|---------------|
| `BigQuery` | `from diagrams.gcp.analytics import BigQuery` |
| `Bigquery` | `from diagrams.gcp.analytics import Bigquery` |
| `Composer` | `from diagrams.gcp.analytics import Composer` |
| `DataCatalog` | `from diagrams.gcp.analytics import DataCatalog` |
| `DataFusion` | `from diagrams.gcp.analytics import DataFusion` |
| `Dataflow` | `from diagrams.gcp.analytics import Dataflow` |
| `Datalab` | `from diagrams.gcp.analytics import Datalab` |
| `Dataprep` | `from diagrams.gcp.analytics import Dataprep` |
| `Dataproc` | `from diagrams.gcp.analytics import Dataproc` |
| `Genomics` | `from diagrams.gcp.analytics import Genomics` |
| `Looker` | `from diagrams.gcp.analytics import Looker` |
| `PubSub` | `from diagrams.gcp.analytics import PubSub` |
| `Pubsub` | `from diagrams.gcp.analytics import Pubsub` |

### API

**Import:** `from diagrams.gcp.api import ...`

| Class Name | Import Example |
|------------|---------------|
| `APIGateway` | `from diagrams.gcp.api import APIGateway` |
| `Apigee` | `from diagrams.gcp.api import Apigee` |
| `Endpoints` | `from diagrams.gcp.api import Endpoints` |

### Compute

**Import:** `from diagrams.gcp.compute import ...`

| Class Name | Import Example |
|------------|---------------|
| `AppEngine` | `from diagrams.gcp.compute import AppEngine` |
| `BinaryAuthorization` | `from diagrams.gcp.compute import BinaryAuthorization` |
| `CloudRun` | `from diagrams.gcp.compute import CloudRun` |
| `ComputeEngine` | `from diagrams.gcp.compute import ComputeEngine` |
| `ContainerOptimizedOS` | `from diagrams.gcp.compute import ContainerOptimizedOS` |
| `Functions` | `from diagrams.gcp.compute import Functions` |
| `GAE` | `from diagrams.gcp.compute import GAE` |
| `GCE` | `from diagrams.gcp.compute import GCE` |
| `GCF` | `from diagrams.gcp.compute import GCF` |
| `GKE` | `from diagrams.gcp.compute import GKE` |
| `GKEOnPrem` | `from diagrams.gcp.compute import GKEOnPrem` |
| `GPU` | `from diagrams.gcp.compute import GPU` |
| `KubernetesEngine` | `from diagrams.gcp.compute import KubernetesEngine` |
| `OSConfigurationManagement` | `from diagrams.gcp.compute import OSConfigurationManagement` |
| `OSInventoryManagement` | `from diagrams.gcp.compute import OSInventoryManagement` |
| `OSPatchManagement` | `from diagrams.gcp.compute import OSPatchManagement` |
| `Run` | `from diagrams.gcp.compute import Run` |

### Database

**Import:** `from diagrams.gcp.database import ...`

| Class Name | Import Example |
|------------|---------------|
| `BigTable` | `from diagrams.gcp.database import BigTable` |
| `Bigtable` | `from diagrams.gcp.database import Bigtable` |
| `Datastore` | `from diagrams.gcp.database import Datastore` |
| `Firestore` | `from diagrams.gcp.database import Firestore` |
| `Memorystore` | `from diagrams.gcp.database import Memorystore` |
| `SQL` | `from diagrams.gcp.database import SQL` |
| `Spanner` | `from diagrams.gcp.database import Spanner` |

### Developer Tools

**Import:** `from diagrams.gcp.devtools import ...`

| Class Name | Import Example |
|------------|---------------|
| `Build` | `from diagrams.gcp.devtools import Build` |
| `CloudShell` | `from diagrams.gcp.devtools import CloudShell` |
| `Code` | `from diagrams.gcp.devtools import Code` |
| `CodeForIntellij` | `from diagrams.gcp.devtools import CodeForIntellij` |
| `ContainerRegistry` | `from diagrams.gcp.devtools import ContainerRegistry` |
| `GCR` | `from diagrams.gcp.devtools import GCR` |
| `GradleAppEnginePlugin` | `from diagrams.gcp.devtools import GradleAppEnginePlugin` |
| `IdePlugins` | `from diagrams.gcp.devtools import IdePlugins` |
| `MavenAppEnginePlugin` | `from diagrams.gcp.devtools import MavenAppEnginePlugin` |
| `SDK` | `from diagrams.gcp.devtools import SDK` |
| `Scheduler` | `from diagrams.gcp.devtools import Scheduler` |
| `ServiceCatalog` | `from diagrams.gcp.devtools import ServiceCatalog` |
| `SourceRepositories` | `from diagrams.gcp.devtools import SourceRepositories` |
| `Tasks` | `from diagrams.gcp.devtools import Tasks` |
| `TestLab` | `from diagrams.gcp.devtools import TestLab` |
| `ToolsForEclipse` | `from diagrams.gcp.devtools import ToolsForEclipse` |
| `ToolsForPowershell` | `from diagrams.gcp.devtools import ToolsForPowershell` |
| `ToolsForVisualStudio` | `from diagrams.gcp.devtools import ToolsForVisualStudio` |

### IoT

**Import:** `from diagrams.gcp.iot import ...`

| Class Name | Import Example |
|------------|---------------|
| `IotCore` | `from diagrams.gcp.iot import IotCore` |

### Management

**Import:** `from diagrams.gcp.management import ...`

| Class Name | Import Example |
|------------|---------------|
| `Billing` | `from diagrams.gcp.management import Billing` |
| `Project` | `from diagrams.gcp.management import Project` |
| `Quotas` | `from diagrams.gcp.management import Quotas` |
| `Support` | `from diagrams.gcp.management import Support` |

### Migration

**Import:** `from diagrams.gcp.migration import ...`

| Class Name | Import Example |
|------------|---------------|
| `CE` | `from diagrams.gcp.migration import CE` |
| `MigrateComputeEngine` | `from diagrams.gcp.migration import MigrateComputeEngine` |
| `TransferAppliance` | `from diagrams.gcp.migration import TransferAppliance` |

### Machine Learning

**Import:** `from diagrams.gcp.ml import ...`

| Class Name | Import Example |
|------------|---------------|
| `AIHub` | `from diagrams.gcp.ml import AIHub` |
| `AIPlatform` | `from diagrams.gcp.ml import AIPlatform` |
| `AIPlatformDataLabelingService` | `from diagrams.gcp.ml import AIPlatformDataLabelingService` |
| `AdvancedSolutionsLab` | `from diagrams.gcp.ml import AdvancedSolutionsLab` |
| `AutoML` | `from diagrams.gcp.ml import AutoML` |
| `Automl` | `from diagrams.gcp.ml import Automl` |
| `AutomlNaturalLanguage` | `from diagrams.gcp.ml import AutomlNaturalLanguage` |
| `AutomlTables` | `from diagrams.gcp.ml import AutomlTables` |
| `AutomlTranslation` | `from diagrams.gcp.ml import AutomlTranslation` |
| `AutomlVideoIntelligence` | `from diagrams.gcp.ml import AutomlVideoIntelligence` |
| `AutomlVision` | `from diagrams.gcp.ml import AutomlVision` |
| `DialogFlowEnterpriseEdition` | `from diagrams.gcp.ml import DialogFlowEnterpriseEdition` |
| `InferenceAPI` | `from diagrams.gcp.ml import InferenceAPI` |
| `JobsAPI` | `from diagrams.gcp.ml import JobsAPI` |
| `NLAPI` | `from diagrams.gcp.ml import NLAPI` |
| `NaturalLanguageAPI` | `from diagrams.gcp.ml import NaturalLanguageAPI` |
| `RecommendationsAI` | `from diagrams.gcp.ml import RecommendationsAI` |
| `STT` | `from diagrams.gcp.ml import STT` |
| `SpeechToText` | `from diagrams.gcp.ml import SpeechToText` |
| `TPU` | `from diagrams.gcp.ml import TPU` |
| `TTS` | `from diagrams.gcp.ml import TTS` |
| `TextToSpeech` | `from diagrams.gcp.ml import TextToSpeech` |
| `TranslationAPI` | `from diagrams.gcp.ml import TranslationAPI` |
| `VertexAI` | `from diagrams.gcp.ml import VertexAI` |
| `VideoIntelligenceAPI` | `from diagrams.gcp.ml import VideoIntelligenceAPI` |
| `VisionAPI` | `from diagrams.gcp.ml import VisionAPI` |

### Network

**Import:** `from diagrams.gcp.network import ...`

| Class Name | Import Example |
|------------|---------------|
| `Armor` | `from diagrams.gcp.network import Armor` |
| `CDN` | `from diagrams.gcp.network import CDN` |
| `CloudIDS` | `from diagrams.gcp.network import CloudIDS` |
| `DNS` | `from diagrams.gcp.network import DNS` |
| `DedicatedInterconnect` | `from diagrams.gcp.network import DedicatedInterconnect` |
| `ExternalIpAddresses` | `from diagrams.gcp.network import ExternalIpAddresses` |
| `FirewallRules` | `from diagrams.gcp.network import FirewallRules` |
| `IDS` | `from diagrams.gcp.network import IDS` |
| `LoadBalancing` | `from diagrams.gcp.network import LoadBalancing` |
| `NAT` | `from diagrams.gcp.network import NAT` |
| `Network` | `from diagrams.gcp.network import Network` |
| `NetworkConnectivityCenter` | `from diagrams.gcp.network import NetworkConnectivityCenter` |
| `NetworkIntelligenceCenter` | `from diagrams.gcp.network import NetworkIntelligenceCenter` |
| `NetworkSecurity` | `from diagrams.gcp.network import NetworkSecurity` |
| `NetworkTiers` | `from diagrams.gcp.network import NetworkTiers` |
| `NetworkTopology` | `from diagrams.gcp.network import NetworkTopology` |
| `PSC` | `from diagrams.gcp.network import PSC` |
| `PartnerInterconnect` | `from diagrams.gcp.network import PartnerInterconnect` |
| `PremiumNetworkTier` | `from diagrams.gcp.network import PremiumNetworkTier` |
| `PrivateServiceConnect` | `from diagrams.gcp.network import PrivateServiceConnect` |
| `Router` | `from diagrams.gcp.network import Router` |
| `Routes` | `from diagrams.gcp.network import Routes` |
| `ServiceMesh` | `from diagrams.gcp.network import ServiceMesh` |
| `StandardNetworkTier` | `from diagrams.gcp.network import StandardNetworkTier` |
| `TrafficDirector` | `from diagrams.gcp.network import TrafficDirector` |
| `VPC` | `from diagrams.gcp.network import VPC` |
| `VPN` | `from diagrams.gcp.network import VPN` |
| `VirtualPrivateCloud` | `from diagrams.gcp.network import VirtualPrivateCloud` |

### Operations

**Import:** `from diagrams.gcp.operations import ...`

| Class Name | Import Example |
|------------|---------------|
| `Logging` | `from diagrams.gcp.operations import Logging` |
| `Monitoring` | `from diagrams.gcp.operations import Monitoring` |

### Security

**Import:** `from diagrams.gcp.security import ...`

| Class Name | Import Example |
|------------|---------------|
| `ACM` | `from diagrams.gcp.security import ACM` |
| `AccessContextManager` | `from diagrams.gcp.security import AccessContextManager` |
| `AssuredWorkloads` | `from diagrams.gcp.security import AssuredWorkloads` |
| `CertificateAuthorityService` | `from diagrams.gcp.security import CertificateAuthorityService` |
| `CertificateManager` | `from diagrams.gcp.security import CertificateManager` |
| `CloudAssetInventory` | `from diagrams.gcp.security import CloudAssetInventory` |
| `IAP` | `from diagrams.gcp.security import IAP` |
| `Iam` | `from diagrams.gcp.security import Iam` |
| `KMS` | `from diagrams.gcp.security import KMS` |
| `KeyManagementService` | `from diagrams.gcp.security import KeyManagementService` |
| `ResourceManager` | `from diagrams.gcp.security import ResourceManager` |
| `SCC` | `from diagrams.gcp.security import SCC` |
| `SecretManager` | `from diagrams.gcp.security import SecretManager` |
| `SecurityCommandCenter` | `from diagrams.gcp.security import SecurityCommandCenter` |
| `SecurityHealthAdvisor` | `from diagrams.gcp.security import SecurityHealthAdvisor` |
| `SecurityScanner` | `from diagrams.gcp.security import SecurityScanner` |

### Storage

**Import:** `from diagrams.gcp.storage import ...`

| Class Name | Import Example |
|------------|---------------|
| `Filestore` | `from diagrams.gcp.storage import Filestore` |
| `GCS` | `from diagrams.gcp.storage import GCS` |
| `LocalSSD` | `from diagrams.gcp.storage import LocalSSD` |
| `PersistentDisk` | `from diagrams.gcp.storage import PersistentDisk` |
| `SSD` | `from diagrams.gcp.storage import SSD` |
| `Storage` | `from diagrams.gcp.storage import Storage` |

---

## Kubernetes

_Kubernetes resources and infrastructure_ — **69 icons** across **12 categories**

### Chaos Engineering

**Import:** `from diagrams.k8s.chaos import ...`

| Class Name | Import Example |
|------------|---------------|
| `ChaosMesh` | `from diagrams.k8s.chaos import ChaosMesh` |
| `LitmusChaos` | `from diagrams.k8s.chaos import LitmusChaos` |

### Cluster Config

**Import:** `from diagrams.k8s.clusterconfig import ...`

| Class Name | Import Example |
|------------|---------------|
| `HPA` | `from diagrams.k8s.clusterconfig import HPA` |
| `HorizontalPodAutoscaler` | `from diagrams.k8s.clusterconfig import HorizontalPodAutoscaler` |
| `LimitRange` | `from diagrams.k8s.clusterconfig import LimitRange` |
| `Limits` | `from diagrams.k8s.clusterconfig import Limits` |
| `Quota` | `from diagrams.k8s.clusterconfig import Quota` |

### Compute

**Import:** `from diagrams.k8s.compute import ...`

| Class Name | Import Example |
|------------|---------------|
| `Cronjob` | `from diagrams.k8s.compute import Cronjob` |
| `DS` | `from diagrams.k8s.compute import DS` |
| `DaemonSet` | `from diagrams.k8s.compute import DaemonSet` |
| `Deploy` | `from diagrams.k8s.compute import Deploy` |
| `Deployment` | `from diagrams.k8s.compute import Deployment` |
| `Job` | `from diagrams.k8s.compute import Job` |
| `Pod` | `from diagrams.k8s.compute import Pod` |
| `RS` | `from diagrams.k8s.compute import RS` |
| `ReplicaSet` | `from diagrams.k8s.compute import ReplicaSet` |
| `STS` | `from diagrams.k8s.compute import STS` |
| `StatefulSet` | `from diagrams.k8s.compute import StatefulSet` |

### Control Plane

**Import:** `from diagrams.k8s.controlplane import ...`

| Class Name | Import Example |
|------------|---------------|
| `API` | `from diagrams.k8s.controlplane import API` |
| `APIServer` | `from diagrams.k8s.controlplane import APIServer` |
| `CCM` | `from diagrams.k8s.controlplane import CCM` |
| `CM` | `from diagrams.k8s.controlplane import CM` |
| `ControllerManager` | `from diagrams.k8s.controlplane import ControllerManager` |
| `KProxy` | `from diagrams.k8s.controlplane import KProxy` |
| `KubeProxy` | `from diagrams.k8s.controlplane import KubeProxy` |
| `Kubelet` | `from diagrams.k8s.controlplane import Kubelet` |
| `Sched` | `from diagrams.k8s.controlplane import Sched` |
| `Scheduler` | `from diagrams.k8s.controlplane import Scheduler` |

### Ecosystem

**Import:** `from diagrams.k8s.ecosystem import ...`

| Class Name | Import Example |
|------------|---------------|
| `ExternalDns` | `from diagrams.k8s.ecosystem import ExternalDns` |
| `Helm` | `from diagrams.k8s.ecosystem import Helm` |
| `Krew` | `from diagrams.k8s.ecosystem import Krew` |
| `Kustomize` | `from diagrams.k8s.ecosystem import Kustomize` |

### Group

**Import:** `from diagrams.k8s.group import ...`

| Class Name | Import Example |
|------------|---------------|
| `NS` | `from diagrams.k8s.group import NS` |
| `Namespace` | `from diagrams.k8s.group import Namespace` |

### Infrastructure

**Import:** `from diagrams.k8s.infra import ...`

| Class Name | Import Example |
|------------|---------------|
| `ETCD` | `from diagrams.k8s.infra import ETCD` |
| `Master` | `from diagrams.k8s.infra import Master` |
| `Node` | `from diagrams.k8s.infra import Node` |

### Network

**Import:** `from diagrams.k8s.network import ...`

| Class Name | Import Example |
|------------|---------------|
| `Endpoint` | `from diagrams.k8s.network import Endpoint` |
| `Ep` | `from diagrams.k8s.network import Ep` |
| `Ing` | `from diagrams.k8s.network import Ing` |
| `Ingress` | `from diagrams.k8s.network import Ingress` |
| `Netpol` | `from diagrams.k8s.network import Netpol` |
| `NetworkPolicy` | `from diagrams.k8s.network import NetworkPolicy` |
| `SVC` | `from diagrams.k8s.network import SVC` |
| `Service` | `from diagrams.k8s.network import Service` |

### Others

**Import:** `from diagrams.k8s.others import ...`

| Class Name | Import Example |
|------------|---------------|
| `CRD` | `from diagrams.k8s.others import CRD` |
| `PSP` | `from diagrams.k8s.others import PSP` |

### Pod Config

**Import:** `from diagrams.k8s.podconfig import ...`

| Class Name | Import Example |
|------------|---------------|
| `CM` | `from diagrams.k8s.podconfig import CM` |
| `ConfigMap` | `from diagrams.k8s.podconfig import ConfigMap` |
| `Secret` | `from diagrams.k8s.podconfig import Secret` |

### RBAC

**Import:** `from diagrams.k8s.rbac import ...`

| Class Name | Import Example |
|------------|---------------|
| `CRB` | `from diagrams.k8s.rbac import CRB` |
| `CRole` | `from diagrams.k8s.rbac import CRole` |
| `ClusterRole` | `from diagrams.k8s.rbac import ClusterRole` |
| `ClusterRoleBinding` | `from diagrams.k8s.rbac import ClusterRoleBinding` |
| `Group` | `from diagrams.k8s.rbac import Group` |
| `RB` | `from diagrams.k8s.rbac import RB` |
| `Role` | `from diagrams.k8s.rbac import Role` |
| `RoleBinding` | `from diagrams.k8s.rbac import RoleBinding` |
| `SA` | `from diagrams.k8s.rbac import SA` |
| `ServiceAccount` | `from diagrams.k8s.rbac import ServiceAccount` |
| `User` | `from diagrams.k8s.rbac import User` |

### Storage

**Import:** `from diagrams.k8s.storage import ...`

| Class Name | Import Example |
|------------|---------------|
| `PV` | `from diagrams.k8s.storage import PV` |
| `PVC` | `from diagrams.k8s.storage import PVC` |
| `PersistentVolume` | `from diagrams.k8s.storage import PersistentVolume` |
| `PersistentVolumeClaim` | `from diagrams.k8s.storage import PersistentVolumeClaim` |
| `SC` | `from diagrams.k8s.storage import SC` |
| `StorageClass` | `from diagrams.k8s.storage import StorageClass` |
| `Vol` | `from diagrams.k8s.storage import Vol` |
| `Volume` | `from diagrams.k8s.storage import Volume` |

---

## On-Premise

_Self-hosted and open-source infrastructure tools_ — **211 icons** across **31 categories**

### Aggregator

**Import:** `from diagrams.onprem.aggregator import ...`

| Class Name | Import Example |
|------------|---------------|
| `Fluentd` | `from diagrams.onprem.aggregator import Fluentd` |
| `Vector` | `from diagrams.onprem.aggregator import Vector` |

### Analytics

**Import:** `from diagrams.onprem.analytics import ...`

| Class Name | Import Example |
|------------|---------------|
| `Beam` | `from diagrams.onprem.analytics import Beam` |
| `Databricks` | `from diagrams.onprem.analytics import Databricks` |
| `Dbt` | `from diagrams.onprem.analytics import Dbt` |
| `Dremio` | `from diagrams.onprem.analytics import Dremio` |
| `Flink` | `from diagrams.onprem.analytics import Flink` |
| `Hadoop` | `from diagrams.onprem.analytics import Hadoop` |
| `Hive` | `from diagrams.onprem.analytics import Hive` |
| `Metabase` | `from diagrams.onprem.analytics import Metabase` |
| `Norikra` | `from diagrams.onprem.analytics import Norikra` |
| `PowerBI` | `from diagrams.onprem.analytics import PowerBI` |
| `Powerbi` | `from diagrams.onprem.analytics import Powerbi` |
| `Presto` | `from diagrams.onprem.analytics import Presto` |
| `Singer` | `from diagrams.onprem.analytics import Singer` |
| `Spark` | `from diagrams.onprem.analytics import Spark` |
| `Storm` | `from diagrams.onprem.analytics import Storm` |
| `Superset` | `from diagrams.onprem.analytics import Superset` |
| `Tableau` | `from diagrams.onprem.analytics import Tableau` |
| `Trino` | `from diagrams.onprem.analytics import Trino` |

### Authentication

**Import:** `from diagrams.onprem.auth import ...`

| Class Name | Import Example |
|------------|---------------|
| `Boundary` | `from diagrams.onprem.auth import Boundary` |
| `BuzzfeedSso` | `from diagrams.onprem.auth import BuzzfeedSso` |
| `Oauth2Proxy` | `from diagrams.onprem.auth import Oauth2Proxy` |

### Continuous Delivery

**Import:** `from diagrams.onprem.cd import ...`

| Class Name | Import Example |
|------------|---------------|
| `Spinnaker` | `from diagrams.onprem.cd import Spinnaker` |
| `Tekton` | `from diagrams.onprem.cd import Tekton` |
| `TektonCli` | `from diagrams.onprem.cd import TektonCli` |

### Certificates

**Import:** `from diagrams.onprem.certificates import ...`

| Class Name | Import Example |
|------------|---------------|
| `CertManager` | `from diagrams.onprem.certificates import CertManager` |
| `LetsEncrypt` | `from diagrams.onprem.certificates import LetsEncrypt` |

### Continuous Integration

**Import:** `from diagrams.onprem.ci import ...`

| Class Name | Import Example |
|------------|---------------|
| `CircleCI` | `from diagrams.onprem.ci import CircleCI` |
| `Circleci` | `from diagrams.onprem.ci import Circleci` |
| `ConcourseCI` | `from diagrams.onprem.ci import ConcourseCI` |
| `Concourseci` | `from diagrams.onprem.ci import Concourseci` |
| `DroneCI` | `from diagrams.onprem.ci import DroneCI` |
| `Droneci` | `from diagrams.onprem.ci import Droneci` |
| `GithubActions` | `from diagrams.onprem.ci import GithubActions` |
| `GitlabCI` | `from diagrams.onprem.ci import GitlabCI` |
| `Gitlabci` | `from diagrams.onprem.ci import Gitlabci` |
| `Jenkins` | `from diagrams.onprem.ci import Jenkins` |
| `TC` | `from diagrams.onprem.ci import TC` |
| `Teamcity` | `from diagrams.onprem.ci import Teamcity` |
| `TravisCI` | `from diagrams.onprem.ci import TravisCI` |
| `Travisci` | `from diagrams.onprem.ci import Travisci` |
| `ZuulCI` | `from diagrams.onprem.ci import ZuulCI` |
| `Zuulci` | `from diagrams.onprem.ci import Zuulci` |

### Client

**Import:** `from diagrams.onprem.client import ...`

| Class Name | Import Example |
|------------|---------------|
| `Client` | `from diagrams.onprem.client import Client` |
| `User` | `from diagrams.onprem.client import User` |
| `Users` | `from diagrams.onprem.client import Users` |

### Compute

**Import:** `from diagrams.onprem.compute import ...`

| Class Name | Import Example |
|------------|---------------|
| `Nomad` | `from diagrams.onprem.compute import Nomad` |
| `Server` | `from diagrams.onprem.compute import Server` |

### Container

**Import:** `from diagrams.onprem.container import ...`

| Class Name | Import Example |
|------------|---------------|
| `Containerd` | `from diagrams.onprem.container import Containerd` |
| `Crio` | `from diagrams.onprem.container import Crio` |
| `Docker` | `from diagrams.onprem.container import Docker` |
| `Firecracker` | `from diagrams.onprem.container import Firecracker` |
| `Gvisor` | `from diagrams.onprem.container import Gvisor` |
| `K3S` | `from diagrams.onprem.container import K3S` |
| `LXC` | `from diagrams.onprem.container import LXC` |
| `Lxc` | `from diagrams.onprem.container import Lxc` |
| `RKT` | `from diagrams.onprem.container import RKT` |
| `Rkt` | `from diagrams.onprem.container import Rkt` |

### Database

**Import:** `from diagrams.onprem.database import ...`

| Class Name | Import Example |
|------------|---------------|
| `Cassandra` | `from diagrams.onprem.database import Cassandra` |
| `ClickHouse` | `from diagrams.onprem.database import ClickHouse` |
| `Clickhouse` | `from diagrams.onprem.database import Clickhouse` |
| `CockroachDB` | `from diagrams.onprem.database import CockroachDB` |
| `Cockroachdb` | `from diagrams.onprem.database import Cockroachdb` |
| `CouchDB` | `from diagrams.onprem.database import CouchDB` |
| `Couchbase` | `from diagrams.onprem.database import Couchbase` |
| `Couchdb` | `from diagrams.onprem.database import Couchdb` |
| `Dgraph` | `from diagrams.onprem.database import Dgraph` |
| `Druid` | `from diagrams.onprem.database import Druid` |
| `Duckdb` | `from diagrams.onprem.database import Duckdb` |
| `HBase` | `from diagrams.onprem.database import HBase` |
| `Hbase` | `from diagrams.onprem.database import Hbase` |
| `InfluxDB` | `from diagrams.onprem.database import InfluxDB` |
| `Influxdb` | `from diagrams.onprem.database import Influxdb` |
| `JanusGraph` | `from diagrams.onprem.database import JanusGraph` |
| `Janusgraph` | `from diagrams.onprem.database import Janusgraph` |
| `MSSQL` | `from diagrams.onprem.database import MSSQL` |
| `MariaDB` | `from diagrams.onprem.database import MariaDB` |
| `Mariadb` | `from diagrams.onprem.database import Mariadb` |
| `MongoDB` | `from diagrams.onprem.database import MongoDB` |
| `Mongodb` | `from diagrams.onprem.database import Mongodb` |
| `Mssql` | `from diagrams.onprem.database import Mssql` |
| `MySQL` | `from diagrams.onprem.database import MySQL` |
| `Mysql` | `from diagrams.onprem.database import Mysql` |
| `Neo4J` | `from diagrams.onprem.database import Neo4J` |
| `Oracle` | `from diagrams.onprem.database import Oracle` |
| `PostgreSQL` | `from diagrams.onprem.database import PostgreSQL` |
| `Postgresql` | `from diagrams.onprem.database import Postgresql` |
| `Qdrant` | `from diagrams.onprem.database import Qdrant` |
| `Scylla` | `from diagrams.onprem.database import Scylla` |

### DNS

**Import:** `from diagrams.onprem.dns import ...`

| Class Name | Import Example |
|------------|---------------|
| `Coredns` | `from diagrams.onprem.dns import Coredns` |
| `Powerdns` | `from diagrams.onprem.dns import Powerdns` |

### ETL

**Import:** `from diagrams.onprem.etl import ...`

| Class Name | Import Example |
|------------|---------------|
| `Embulk` | `from diagrams.onprem.etl import Embulk` |

### GitOps

**Import:** `from diagrams.onprem.gitops import ...`

| Class Name | Import Example |
|------------|---------------|
| `ArgoCD` | `from diagrams.onprem.gitops import ArgoCD` |
| `Argocd` | `from diagrams.onprem.gitops import Argocd` |
| `Flagger` | `from diagrams.onprem.gitops import Flagger` |
| `Flux` | `from diagrams.onprem.gitops import Flux` |

### Groupware

**Import:** `from diagrams.onprem.groupware import ...`

| Class Name | Import Example |
|------------|---------------|
| `Nextcloud` | `from diagrams.onprem.groupware import Nextcloud` |

### Infrastructure as Code

**Import:** `from diagrams.onprem.iac import ...`

| Class Name | Import Example |
|------------|---------------|
| `Ansible` | `from diagrams.onprem.iac import Ansible` |
| `Atlantis` | `from diagrams.onprem.iac import Atlantis` |
| `Awx` | `from diagrams.onprem.iac import Awx` |
| `Pulumi` | `from diagrams.onprem.iac import Pulumi` |
| `Puppet` | `from diagrams.onprem.iac import Puppet` |
| `Terraform` | `from diagrams.onprem.iac import Terraform` |

### Identity

**Import:** `from diagrams.onprem.identity import ...`

| Class Name | Import Example |
|------------|---------------|
| `Dex` | `from diagrams.onprem.identity import Dex` |

### In-Memory

**Import:** `from diagrams.onprem.inmemory import ...`

| Class Name | Import Example |
|------------|---------------|
| `Aerospike` | `from diagrams.onprem.inmemory import Aerospike` |
| `Hazelcast` | `from diagrams.onprem.inmemory import Hazelcast` |
| `Memcached` | `from diagrams.onprem.inmemory import Memcached` |
| `Redis` | `from diagrams.onprem.inmemory import Redis` |

### Logging

**Import:** `from diagrams.onprem.logging import ...`

| Class Name | Import Example |
|------------|---------------|
| `FluentBit` | `from diagrams.onprem.logging import FluentBit` |
| `Fluentbit` | `from diagrams.onprem.logging import Fluentbit` |
| `Graylog` | `from diagrams.onprem.logging import Graylog` |
| `Loki` | `from diagrams.onprem.logging import Loki` |
| `RSyslog` | `from diagrams.onprem.logging import RSyslog` |
| `Rsyslog` | `from diagrams.onprem.logging import Rsyslog` |
| `SyslogNg` | `from diagrams.onprem.logging import SyslogNg` |

### Messaging

**Import:** `from diagrams.onprem.messaging import ...`

| Class Name | Import Example |
|------------|---------------|
| `Centrifugo` | `from diagrams.onprem.messaging import Centrifugo` |

### MLOps

**Import:** `from diagrams.onprem.mlops import ...`

| Class Name | Import Example |
|------------|---------------|
| `Mlflow` | `from diagrams.onprem.mlops import Mlflow` |
| `Polyaxon` | `from diagrams.onprem.mlops import Polyaxon` |

### Monitoring

**Import:** `from diagrams.onprem.monitoring import ...`

| Class Name | Import Example |
|------------|---------------|
| `Cortex` | `from diagrams.onprem.monitoring import Cortex` |
| `Datadog` | `from diagrams.onprem.monitoring import Datadog` |
| `Dynatrace` | `from diagrams.onprem.monitoring import Dynatrace` |
| `Grafana` | `from diagrams.onprem.monitoring import Grafana` |
| `Humio` | `from diagrams.onprem.monitoring import Humio` |
| `Mimir` | `from diagrams.onprem.monitoring import Mimir` |
| `Nagios` | `from diagrams.onprem.monitoring import Nagios` |
| `Newrelic` | `from diagrams.onprem.monitoring import Newrelic` |
| `Prometheus` | `from diagrams.onprem.monitoring import Prometheus` |
| `PrometheusOperator` | `from diagrams.onprem.monitoring import PrometheusOperator` |
| `Sentry` | `from diagrams.onprem.monitoring import Sentry` |
| `Splunk` | `from diagrams.onprem.monitoring import Splunk` |
| `Thanos` | `from diagrams.onprem.monitoring import Thanos` |
| `Zabbix` | `from diagrams.onprem.monitoring import Zabbix` |

### Network

**Import:** `from diagrams.onprem.network import ...`

| Class Name | Import Example |
|------------|---------------|
| `Ambassador` | `from diagrams.onprem.network import Ambassador` |
| `Apache` | `from diagrams.onprem.network import Apache` |
| `Bind9` | `from diagrams.onprem.network import Bind9` |
| `Caddy` | `from diagrams.onprem.network import Caddy` |
| `CiscoRouter` | `from diagrams.onprem.network import CiscoRouter` |
| `CiscoSwitchL2` | `from diagrams.onprem.network import CiscoSwitchL2` |
| `CiscoSwitchL3` | `from diagrams.onprem.network import CiscoSwitchL3` |
| `Consul` | `from diagrams.onprem.network import Consul` |
| `ETCD` | `from diagrams.onprem.network import ETCD` |
| `Envoy` | `from diagrams.onprem.network import Envoy` |
| `Etcd` | `from diagrams.onprem.network import Etcd` |
| `Glassfish` | `from diagrams.onprem.network import Glassfish` |
| `Gunicorn` | `from diagrams.onprem.network import Gunicorn` |
| `HAProxy` | `from diagrams.onprem.network import HAProxy` |
| `Haproxy` | `from diagrams.onprem.network import Haproxy` |
| `Internet` | `from diagrams.onprem.network import Internet` |
| `Istio` | `from diagrams.onprem.network import Istio` |
| `Jbossas` | `from diagrams.onprem.network import Jbossas` |
| `Jetty` | `from diagrams.onprem.network import Jetty` |
| `Kong` | `from diagrams.onprem.network import Kong` |
| `Linkerd` | `from diagrams.onprem.network import Linkerd` |
| `Mikrotik` | `from diagrams.onprem.network import Mikrotik` |
| `Nginx` | `from diagrams.onprem.network import Nginx` |
| `OPNSense` | `from diagrams.onprem.network import OPNSense` |
| `OSM` | `from diagrams.onprem.network import OSM` |
| `Ocelot` | `from diagrams.onprem.network import Ocelot` |
| `OpenServiceMesh` | `from diagrams.onprem.network import OpenServiceMesh` |
| `Opnsense` | `from diagrams.onprem.network import Opnsense` |
| `PFSense` | `from diagrams.onprem.network import PFSense` |
| `Pfsense` | `from diagrams.onprem.network import Pfsense` |
| `Pomerium` | `from diagrams.onprem.network import Pomerium` |
| `Powerdns` | `from diagrams.onprem.network import Powerdns` |
| `Tomcat` | `from diagrams.onprem.network import Tomcat` |
| `Traefik` | `from diagrams.onprem.network import Traefik` |
| `Tyk` | `from diagrams.onprem.network import Tyk` |
| `VyOS` | `from diagrams.onprem.network import VyOS` |
| `Vyos` | `from diagrams.onprem.network import Vyos` |
| `Wildfly` | `from diagrams.onprem.network import Wildfly` |
| `Yarp` | `from diagrams.onprem.network import Yarp` |
| `Zookeeper` | `from diagrams.onprem.network import Zookeeper` |

### Proxmox

**Import:** `from diagrams.onprem.proxmox import ...`

| Class Name | Import Example |
|------------|---------------|
| `ProxmoxVE` | `from diagrams.onprem.proxmox import ProxmoxVE` |
| `Pve` | `from diagrams.onprem.proxmox import Pve` |

### Message Queue

**Import:** `from diagrams.onprem.queue import ...`

| Class Name | Import Example |
|------------|---------------|
| `ActiveMQ` | `from diagrams.onprem.queue import ActiveMQ` |
| `Activemq` | `from diagrams.onprem.queue import Activemq` |
| `Celery` | `from diagrams.onprem.queue import Celery` |
| `EMQX` | `from diagrams.onprem.queue import EMQX` |
| `Emqx` | `from diagrams.onprem.queue import Emqx` |
| `Kafka` | `from diagrams.onprem.queue import Kafka` |
| `Nats` | `from diagrams.onprem.queue import Nats` |
| `RabbitMQ` | `from diagrams.onprem.queue import RabbitMQ` |
| `Rabbitmq` | `from diagrams.onprem.queue import Rabbitmq` |
| `ZeroMQ` | `from diagrams.onprem.queue import ZeroMQ` |
| `Zeromq` | `from diagrams.onprem.queue import Zeromq` |

### Registry

**Import:** `from diagrams.onprem.registry import ...`

| Class Name | Import Example |
|------------|---------------|
| `Harbor` | `from diagrams.onprem.registry import Harbor` |
| `Jfrog` | `from diagrams.onprem.registry import Jfrog` |

### Search

**Import:** `from diagrams.onprem.search import ...`

| Class Name | Import Example |
|------------|---------------|
| `Solr` | `from diagrams.onprem.search import Solr` |

### Security

**Import:** `from diagrams.onprem.security import ...`

| Class Name | Import Example |
|------------|---------------|
| `Bitwarden` | `from diagrams.onprem.security import Bitwarden` |
| `Trivy` | `from diagrams.onprem.security import Trivy` |
| `Vault` | `from diagrams.onprem.security import Vault` |

### Storage

**Import:** `from diagrams.onprem.storage import ...`

| Class Name | Import Example |
|------------|---------------|
| `CEPH` | `from diagrams.onprem.storage import CEPH` |
| `CEPH_OSD` | `from diagrams.onprem.storage import CEPH_OSD` |
| `Ceph` | `from diagrams.onprem.storage import Ceph` |
| `CephOsd` | `from diagrams.onprem.storage import CephOsd` |
| `Glusterfs` | `from diagrams.onprem.storage import Glusterfs` |
| `Portworx` | `from diagrams.onprem.storage import Portworx` |

### Tracing

**Import:** `from diagrams.onprem.tracing import ...`

| Class Name | Import Example |
|------------|---------------|
| `Jaeger` | `from diagrams.onprem.tracing import Jaeger` |
| `Tempo` | `from diagrams.onprem.tracing import Tempo` |

### Version Control

**Import:** `from diagrams.onprem.vcs import ...`

| Class Name | Import Example |
|------------|---------------|
| `Git` | `from diagrams.onprem.vcs import Git` |
| `Gitea` | `from diagrams.onprem.vcs import Gitea` |
| `Github` | `from diagrams.onprem.vcs import Github` |
| `Gitlab` | `from diagrams.onprem.vcs import Gitlab` |
| `Svn` | `from diagrams.onprem.vcs import Svn` |

### Workflow

**Import:** `from diagrams.onprem.workflow import ...`

| Class Name | Import Example |
|------------|---------------|
| `Airflow` | `from diagrams.onprem.workflow import Airflow` |
| `Digdag` | `from diagrams.onprem.workflow import Digdag` |
| `KubeFlow` | `from diagrams.onprem.workflow import KubeFlow` |
| `Kubeflow` | `from diagrams.onprem.workflow import Kubeflow` |
| `NiFi` | `from diagrams.onprem.workflow import NiFi` |
| `Nifi` | `from diagrams.onprem.workflow import Nifi` |

---

## SaaS

_Software-as-a-Service providers_ — **42 icons** across **15 categories**

### Alerting

**Import:** `from diagrams.saas.alerting import ...`

| Class Name | Import Example |
|------------|---------------|
| `Newrelic` | `from diagrams.saas.alerting import Newrelic` |
| `Opsgenie` | `from diagrams.saas.alerting import Opsgenie` |
| `Pagerduty` | `from diagrams.saas.alerting import Pagerduty` |
| `Pushover` | `from diagrams.saas.alerting import Pushover` |
| `Xmatters` | `from diagrams.saas.alerting import Xmatters` |

### Analytics

**Import:** `from diagrams.saas.analytics import ...`

| Class Name | Import Example |
|------------|---------------|
| `Dataform` | `from diagrams.saas.analytics import Dataform` |
| `Snowflake` | `from diagrams.saas.analytics import Snowflake` |
| `Stitch` | `from diagrams.saas.analytics import Stitch` |

### Automation

**Import:** `from diagrams.saas.automation import ...`

| Class Name | Import Example |
|------------|---------------|
| `N8N` | `from diagrams.saas.automation import N8N` |

### CDN

**Import:** `from diagrams.saas.cdn import ...`

| Class Name | Import Example |
|------------|---------------|
| `Akamai` | `from diagrams.saas.cdn import Akamai` |
| `Cloudflare` | `from diagrams.saas.cdn import Cloudflare` |
| `Fastly` | `from diagrams.saas.cdn import Fastly` |
| `Imperva` | `from diagrams.saas.cdn import Imperva` |

### Chat

**Import:** `from diagrams.saas.chat import ...`

| Class Name | Import Example |
|------------|---------------|
| `Discord` | `from diagrams.saas.chat import Discord` |
| `Line` | `from diagrams.saas.chat import Line` |
| `Mattermost` | `from diagrams.saas.chat import Mattermost` |
| `Messenger` | `from diagrams.saas.chat import Messenger` |
| `RocketChat` | `from diagrams.saas.chat import RocketChat` |
| `Slack` | `from diagrams.saas.chat import Slack` |
| `Teams` | `from diagrams.saas.chat import Teams` |
| `Telegram` | `from diagrams.saas.chat import Telegram` |

### Communication

**Import:** `from diagrams.saas.communication import ...`

| Class Name | Import Example |
|------------|---------------|
| `Twilio` | `from diagrams.saas.communication import Twilio` |

### CRM

**Import:** `from diagrams.saas.crm import ...`

| Class Name | Import Example |
|------------|---------------|
| `Intercom` | `from diagrams.saas.crm import Intercom` |
| `Zendesk` | `from diagrams.saas.crm import Zendesk` |

### File Sharing

**Import:** `from diagrams.saas.filesharing import ...`

| Class Name | Import Example |
|------------|---------------|
| `Nextcloud` | `from diagrams.saas.filesharing import Nextcloud` |

### Identity

**Import:** `from diagrams.saas.identity import ...`

| Class Name | Import Example |
|------------|---------------|
| `Auth0` | `from diagrams.saas.identity import Auth0` |
| `Okta` | `from diagrams.saas.identity import Okta` |

### Logging

**Import:** `from diagrams.saas.logging import ...`

| Class Name | Import Example |
|------------|---------------|
| `DataDog` | `from diagrams.saas.logging import DataDog` |
| `Datadog` | `from diagrams.saas.logging import Datadog` |
| `NewRelic` | `from diagrams.saas.logging import NewRelic` |
| `Newrelic` | `from diagrams.saas.logging import Newrelic` |
| `Papertrail` | `from diagrams.saas.logging import Papertrail` |

### Media

**Import:** `from diagrams.saas.media import ...`

| Class Name | Import Example |
|------------|---------------|
| `Cloudinary` | `from diagrams.saas.media import Cloudinary` |

### Payment

**Import:** `from diagrams.saas.payment import ...`

| Class Name | Import Example |
|------------|---------------|
| `Adyen` | `from diagrams.saas.payment import Adyen` |
| `AmazonPay` | `from diagrams.saas.payment import AmazonPay` |
| `Paypal` | `from diagrams.saas.payment import Paypal` |
| `Stripe` | `from diagrams.saas.payment import Stripe` |

### Recommendation

**Import:** `from diagrams.saas.recommendation import ...`

| Class Name | Import Example |
|------------|---------------|
| `Recombee` | `from diagrams.saas.recommendation import Recombee` |

### Security

**Import:** `from diagrams.saas.security import ...`

| Class Name | Import Example |
|------------|---------------|
| `Crowdstrike` | `from diagrams.saas.security import Crowdstrike` |
| `Sonarqube` | `from diagrams.saas.security import Sonarqube` |

### Social

**Import:** `from diagrams.saas.social import ...`

| Class Name | Import Example |
|------------|---------------|
| `Facebook` | `from diagrams.saas.social import Facebook` |
| `Twitter` | `from diagrams.saas.social import Twitter` |

---

## Programming

_Programming languages, frameworks, and runtimes_ — **81 icons** across **4 categories**

### Flowchart

**Import:** `from diagrams.programming.flowchart import ...`

| Class Name | Import Example |
|------------|---------------|
| `Action` | `from diagrams.programming.flowchart import Action` |
| `Collate` | `from diagrams.programming.flowchart import Collate` |
| `Database` | `from diagrams.programming.flowchart import Database` |
| `Decision` | `from diagrams.programming.flowchart import Decision` |
| `Delay` | `from diagrams.programming.flowchart import Delay` |
| `Display` | `from diagrams.programming.flowchart import Display` |
| `Document` | `from diagrams.programming.flowchart import Document` |
| `InputOutput` | `from diagrams.programming.flowchart import InputOutput` |
| `Inspection` | `from diagrams.programming.flowchart import Inspection` |
| `InternalStorage` | `from diagrams.programming.flowchart import InternalStorage` |
| `LoopLimit` | `from diagrams.programming.flowchart import LoopLimit` |
| `ManualInput` | `from diagrams.programming.flowchart import ManualInput` |
| `ManualLoop` | `from diagrams.programming.flowchart import ManualLoop` |
| `Merge` | `from diagrams.programming.flowchart import Merge` |
| `MultipleDocuments` | `from diagrams.programming.flowchart import MultipleDocuments` |
| `OffPageConnectorLeft` | `from diagrams.programming.flowchart import OffPageConnectorLeft` |
| `OffPageConnectorRight` | `from diagrams.programming.flowchart import OffPageConnectorRight` |
| `Or` | `from diagrams.programming.flowchart import Or` |
| `PredefinedProcess` | `from diagrams.programming.flowchart import PredefinedProcess` |
| `Preparation` | `from diagrams.programming.flowchart import Preparation` |
| `Sort` | `from diagrams.programming.flowchart import Sort` |
| `StartEnd` | `from diagrams.programming.flowchart import StartEnd` |
| `StoredData` | `from diagrams.programming.flowchart import StoredData` |
| `SummingJunction` | `from diagrams.programming.flowchart import SummingJunction` |

### Framework

**Import:** `from diagrams.programming.framework import ...`

| Class Name | Import Example |
|------------|---------------|
| `Angular` | `from diagrams.programming.framework import Angular` |
| `Backbone` | `from diagrams.programming.framework import Backbone` |
| `Camel` | `from diagrams.programming.framework import Camel` |
| `Django` | `from diagrams.programming.framework import Django` |
| `DotNet` | `from diagrams.programming.framework import DotNet` |
| `Dotnet` | `from diagrams.programming.framework import Dotnet` |
| `Ember` | `from diagrams.programming.framework import Ember` |
| `FastAPI` | `from diagrams.programming.framework import FastAPI` |
| `Fastapi` | `from diagrams.programming.framework import Fastapi` |
| `Flask` | `from diagrams.programming.framework import Flask` |
| `Flutter` | `from diagrams.programming.framework import Flutter` |
| `GraphQL` | `from diagrams.programming.framework import GraphQL` |
| `Graphql` | `from diagrams.programming.framework import Graphql` |
| `Hibernate` | `from diagrams.programming.framework import Hibernate` |
| `Jhipster` | `from diagrams.programming.framework import Jhipster` |
| `Laravel` | `from diagrams.programming.framework import Laravel` |
| `Micronaut` | `from diagrams.programming.framework import Micronaut` |
| `NextJs` | `from diagrams.programming.framework import NextJs` |
| `Nextjs` | `from diagrams.programming.framework import Nextjs` |
| `Phoenix` | `from diagrams.programming.framework import Phoenix` |
| `Quarkus` | `from diagrams.programming.framework import Quarkus` |
| `Rails` | `from diagrams.programming.framework import Rails` |
| `React` | `from diagrams.programming.framework import React` |
| `Spring` | `from diagrams.programming.framework import Spring` |
| `Sqlpage` | `from diagrams.programming.framework import Sqlpage` |
| `Starlette` | `from diagrams.programming.framework import Starlette` |
| `Svelte` | `from diagrams.programming.framework import Svelte` |
| `Vercel` | `from diagrams.programming.framework import Vercel` |
| `Vue` | `from diagrams.programming.framework import Vue` |

### Language

**Import:** `from diagrams.programming.language import ...`

| Class Name | Import Example |
|------------|---------------|
| `Bash` | `from diagrams.programming.language import Bash` |
| `C` | `from diagrams.programming.language import C` |
| `Cpp` | `from diagrams.programming.language import Cpp` |
| `Csharp` | `from diagrams.programming.language import Csharp` |
| `Dart` | `from diagrams.programming.language import Dart` |
| `Elixir` | `from diagrams.programming.language import Elixir` |
| `Erlang` | `from diagrams.programming.language import Erlang` |
| `Go` | `from diagrams.programming.language import Go` |
| `Java` | `from diagrams.programming.language import Java` |
| `JavaScript` | `from diagrams.programming.language import JavaScript` |
| `Javascript` | `from diagrams.programming.language import Javascript` |
| `Kotlin` | `from diagrams.programming.language import Kotlin` |
| `Latex` | `from diagrams.programming.language import Latex` |
| `Matlab` | `from diagrams.programming.language import Matlab` |
| `NodeJS` | `from diagrams.programming.language import NodeJS` |
| `Nodejs` | `from diagrams.programming.language import Nodejs` |
| `PHP` | `from diagrams.programming.language import PHP` |
| `Php` | `from diagrams.programming.language import Php` |
| `Python` | `from diagrams.programming.language import Python` |
| `R` | `from diagrams.programming.language import R` |
| `Ruby` | `from diagrams.programming.language import Ruby` |
| `Rust` | `from diagrams.programming.language import Rust` |
| `Scala` | `from diagrams.programming.language import Scala` |
| `Sql` | `from diagrams.programming.language import Sql` |
| `Swift` | `from diagrams.programming.language import Swift` |
| `TypeScript` | `from diagrams.programming.language import TypeScript` |
| `Typescript` | `from diagrams.programming.language import Typescript` |

### Runtime

**Import:** `from diagrams.programming.runtime import ...`

| Class Name | Import Example |
|------------|---------------|
| `Dapr` | `from diagrams.programming.runtime import Dapr` |

---

## Elastic Stack

_Elasticsearch, Kibana, Beats, and related tools_ — **47 icons** across **8 categories**

### Agent

**Import:** `from diagrams.elastic.agent import ...`

| Class Name | Import Example |
|------------|---------------|
| `Agent` | `from diagrams.elastic.agent import Agent` |
| `Endpoint` | `from diagrams.elastic.agent import Endpoint` |
| `Fleet` | `from diagrams.elastic.agent import Fleet` |
| `Integrations` | `from diagrams.elastic.agent import Integrations` |

### Beats

**Import:** `from diagrams.elastic.beats import ...`

| Class Name | Import Example |
|------------|---------------|
| `APM` | `from diagrams.elastic.beats import APM` |
| `Auditbeat` | `from diagrams.elastic.beats import Auditbeat` |
| `Filebeat` | `from diagrams.elastic.beats import Filebeat` |
| `Functionbeat` | `from diagrams.elastic.beats import Functionbeat` |
| `Heartbeat` | `from diagrams.elastic.beats import Heartbeat` |
| `Metricbeat` | `from diagrams.elastic.beats import Metricbeat` |
| `Packetbeat` | `from diagrams.elastic.beats import Packetbeat` |
| `Winlogbeat` | `from diagrams.elastic.beats import Winlogbeat` |

### Elasticsearch

**Import:** `from diagrams.elastic.elasticsearch import ...`

| Class Name | Import Example |
|------------|---------------|
| `Alerting` | `from diagrams.elastic.elasticsearch import Alerting` |
| `Beats` | `from diagrams.elastic.elasticsearch import Beats` |
| `ElasticSearch` | `from diagrams.elastic.elasticsearch import ElasticSearch` |
| `Elasticsearch` | `from diagrams.elastic.elasticsearch import Elasticsearch` |
| `Kibana` | `from diagrams.elastic.elasticsearch import Kibana` |
| `LogStash` | `from diagrams.elastic.elasticsearch import LogStash` |
| `Logstash` | `from diagrams.elastic.elasticsearch import Logstash` |
| `LogstashPipeline` | `from diagrams.elastic.elasticsearch import LogstashPipeline` |
| `ML` | `from diagrams.elastic.elasticsearch import ML` |
| `MachineLearning` | `from diagrams.elastic.elasticsearch import MachineLearning` |
| `MapServices` | `from diagrams.elastic.elasticsearch import MapServices` |
| `Maps` | `from diagrams.elastic.elasticsearch import Maps` |
| `Monitoring` | `from diagrams.elastic.elasticsearch import Monitoring` |
| `SQL` | `from diagrams.elastic.elasticsearch import SQL` |
| `SearchableSnapshots` | `from diagrams.elastic.elasticsearch import SearchableSnapshots` |
| `SecuritySettings` | `from diagrams.elastic.elasticsearch import SecuritySettings` |
| `Stack` | `from diagrams.elastic.elasticsearch import Stack` |

### Enterprise Search

**Import:** `from diagrams.elastic.enterprisesearch import ...`

| Class Name | Import Example |
|------------|---------------|
| `AppSearch` | `from diagrams.elastic.enterprisesearch import AppSearch` |
| `Crawler` | `from diagrams.elastic.enterprisesearch import Crawler` |
| `EnterpriseSearch` | `from diagrams.elastic.enterprisesearch import EnterpriseSearch` |
| `SiteSearch` | `from diagrams.elastic.enterprisesearch import SiteSearch` |
| `WorkplaceSearch` | `from diagrams.elastic.enterprisesearch import WorkplaceSearch` |

### Observability

**Import:** `from diagrams.elastic.observability import ...`

| Class Name | Import Example |
|------------|---------------|
| `APM` | `from diagrams.elastic.observability import APM` |
| `Logs` | `from diagrams.elastic.observability import Logs` |
| `Metrics` | `from diagrams.elastic.observability import Metrics` |
| `Observability` | `from diagrams.elastic.observability import Observability` |
| `Uptime` | `from diagrams.elastic.observability import Uptime` |

### Orchestration

**Import:** `from diagrams.elastic.orchestration import ...`

| Class Name | Import Example |
|------------|---------------|
| `ECE` | `from diagrams.elastic.orchestration import ECE` |
| `ECK` | `from diagrams.elastic.orchestration import ECK` |

### SaaS

**Import:** `from diagrams.elastic.saas import ...`

| Class Name | Import Example |
|------------|---------------|
| `Cloud` | `from diagrams.elastic.saas import Cloud` |
| `Elastic` | `from diagrams.elastic.saas import Elastic` |

### Security

**Import:** `from diagrams.elastic.security import ...`

| Class Name | Import Example |
|------------|---------------|
| `Endpoint` | `from diagrams.elastic.security import Endpoint` |
| `SIEM` | `from diagrams.elastic.security import SIEM` |
| `Security` | `from diagrams.elastic.security import Security` |
| `Xdr` | `from diagrams.elastic.security import Xdr` |

---

## Firebase

_Google Firebase services_ — **23 icons** across **5 categories**

### Base

**Import:** `from diagrams.firebase.base import ...`

| Class Name | Import Example |
|------------|---------------|
| `Firebase` | `from diagrams.firebase.base import Firebase` |

### Develop

**Import:** `from diagrams.firebase.develop import ...`

| Class Name | Import Example |
|------------|---------------|
| `Authentication` | `from diagrams.firebase.develop import Authentication` |
| `Firestore` | `from diagrams.firebase.develop import Firestore` |
| `Functions` | `from diagrams.firebase.develop import Functions` |
| `Hosting` | `from diagrams.firebase.develop import Hosting` |
| `MLKit` | `from diagrams.firebase.develop import MLKit` |
| `RealtimeDatabase` | `from diagrams.firebase.develop import RealtimeDatabase` |
| `Storage` | `from diagrams.firebase.develop import Storage` |

### Extensions

**Import:** `from diagrams.firebase.extentions import ...`

| Class Name | Import Example |
|------------|---------------|
| `Extensions` | `from diagrams.firebase.extentions import Extensions` |

### Grow

**Import:** `from diagrams.firebase.grow import ...`

| Class Name | Import Example |
|------------|---------------|
| `ABTesting` | `from diagrams.firebase.grow import ABTesting` |
| `AppIndexing` | `from diagrams.firebase.grow import AppIndexing` |
| `DynamicLinks` | `from diagrams.firebase.grow import DynamicLinks` |
| `FCM` | `from diagrams.firebase.grow import FCM` |
| `InAppMessaging` | `from diagrams.firebase.grow import InAppMessaging` |
| `Invites` | `from diagrams.firebase.grow import Invites` |
| `Messaging` | `from diagrams.firebase.grow import Messaging` |
| `Predictions` | `from diagrams.firebase.grow import Predictions` |
| `RemoteConfig` | `from diagrams.firebase.grow import RemoteConfig` |

### Quality

**Import:** `from diagrams.firebase.quality import ...`

| Class Name | Import Example |
|------------|---------------|
| `AppDistribution` | `from diagrams.firebase.quality import AppDistribution` |
| `CrashReporting` | `from diagrams.firebase.quality import CrashReporting` |
| `Crashlytics` | `from diagrams.firebase.quality import Crashlytics` |
| `PerformanceMonitoring` | `from diagrams.firebase.quality import PerformanceMonitoring` |
| `TestLab` | `from diagrams.firebase.quality import TestLab` |

---

## DigitalOcean

_DigitalOcean cloud platform services_ — **25 icons** across **4 categories**

### Compute

**Import:** `from diagrams.digitalocean.compute import ...`

| Class Name | Import Example |
|------------|---------------|
| `Containers` | `from diagrams.digitalocean.compute import Containers` |
| `Docker` | `from diagrams.digitalocean.compute import Docker` |
| `Droplet` | `from diagrams.digitalocean.compute import Droplet` |
| `DropletConnect` | `from diagrams.digitalocean.compute import DropletConnect` |
| `DropletSnapshot` | `from diagrams.digitalocean.compute import DropletSnapshot` |
| `K8SCluster` | `from diagrams.digitalocean.compute import K8SCluster` |
| `K8SNode` | `from diagrams.digitalocean.compute import K8SNode` |
| `K8SNodePool` | `from diagrams.digitalocean.compute import K8SNodePool` |

### Database

**Import:** `from diagrams.digitalocean.database import ...`

| Class Name | Import Example |
|------------|---------------|
| `DbaasPrimary` | `from diagrams.digitalocean.database import DbaasPrimary` |
| `DbaasPrimaryStandbyMore` | `from diagrams.digitalocean.database import DbaasPrimaryStandbyMore` |
| `DbaasReadOnly` | `from diagrams.digitalocean.database import DbaasReadOnly` |
| `DbaasStandby` | `from diagrams.digitalocean.database import DbaasStandby` |

### Network

**Import:** `from diagrams.digitalocean.network import ...`

| Class Name | Import Example |
|------------|---------------|
| `Certificate` | `from diagrams.digitalocean.network import Certificate` |
| `Domain` | `from diagrams.digitalocean.network import Domain` |
| `DomainRegistration` | `from diagrams.digitalocean.network import DomainRegistration` |
| `Firewall` | `from diagrams.digitalocean.network import Firewall` |
| `FloatingIp` | `from diagrams.digitalocean.network import FloatingIp` |
| `InternetGateway` | `from diagrams.digitalocean.network import InternetGateway` |
| `LoadBalancer` | `from diagrams.digitalocean.network import LoadBalancer` |
| `ManagedVpn` | `from diagrams.digitalocean.network import ManagedVpn` |
| `Vpc` | `from diagrams.digitalocean.network import Vpc` |

### Storage

**Import:** `from diagrams.digitalocean.storage import ...`

| Class Name | Import Example |
|------------|---------------|
| `Folder` | `from diagrams.digitalocean.storage import Folder` |
| `Space` | `from diagrams.digitalocean.storage import Space` |
| `Volume` | `from diagrams.digitalocean.storage import Volume` |
| `VolumeSnapshot` | `from diagrams.digitalocean.storage import VolumeSnapshot` |

---

## IBM Cloud

_IBM Cloud and Watson services_ — **180 icons** across **14 categories**

### Analytics

**Import:** `from diagrams.ibm.analytics import ...`

| Class Name | Import Example |
|------------|---------------|
| `Analytics` | `from diagrams.ibm.analytics import Analytics` |
| `DataIntegration` | `from diagrams.ibm.analytics import DataIntegration` |
| `DataRepositories` | `from diagrams.ibm.analytics import DataRepositories` |
| `DeviceAnalytics` | `from diagrams.ibm.analytics import DeviceAnalytics` |
| `StreamingComputing` | `from diagrams.ibm.analytics import StreamingComputing` |

### Applications

**Import:** `from diagrams.ibm.applications import ...`

| Class Name | Import Example |
|------------|---------------|
| `ActionableInsight` | `from diagrams.ibm.applications import ActionableInsight` |
| `Annotate` | `from diagrams.ibm.applications import Annotate` |
| `ApiDeveloperPortal` | `from diagrams.ibm.applications import ApiDeveloperPortal` |
| `ApiPolyglotRuntimes` | `from diagrams.ibm.applications import ApiPolyglotRuntimes` |
| `AppServer` | `from diagrams.ibm.applications import AppServer` |
| `ApplicationLogic` | `from diagrams.ibm.applications import ApplicationLogic` |
| `EnterpriseApplications` | `from diagrams.ibm.applications import EnterpriseApplications` |
| `Index` | `from diagrams.ibm.applications import Index` |
| `IotApplication` | `from diagrams.ibm.applications import IotApplication` |
| `Microservice` | `from diagrams.ibm.applications import Microservice` |
| `MobileApp` | `from diagrams.ibm.applications import MobileApp` |
| `Ontology` | `from diagrams.ibm.applications import Ontology` |
| `OpenSourceTools` | `from diagrams.ibm.applications import OpenSourceTools` |
| `RuntimeServices` | `from diagrams.ibm.applications import RuntimeServices` |
| `SaasApplications` | `from diagrams.ibm.applications import SaasApplications` |
| `ServiceBroker` | `from diagrams.ibm.applications import ServiceBroker` |
| `SpeechToText` | `from diagrams.ibm.applications import SpeechToText` |
| `VisualRecognition` | `from diagrams.ibm.applications import VisualRecognition` |
| `Visualization` | `from diagrams.ibm.applications import Visualization` |

### Blockchain

**Import:** `from diagrams.ibm.blockchain import ...`

| Class Name | Import Example |
|------------|---------------|
| `Blockchain` | `from diagrams.ibm.blockchain import Blockchain` |
| `BlockchainDeveloper` | `from diagrams.ibm.blockchain import BlockchainDeveloper` |
| `CertificateAuthority` | `from diagrams.ibm.blockchain import CertificateAuthority` |
| `ClientApplication` | `from diagrams.ibm.blockchain import ClientApplication` |
| `Communication` | `from diagrams.ibm.blockchain import Communication` |
| `Consensus` | `from diagrams.ibm.blockchain import Consensus` |
| `Event` | `from diagrams.ibm.blockchain import Event` |
| `EventListener` | `from diagrams.ibm.blockchain import EventListener` |
| `ExistingEnterpriseSystems` | `from diagrams.ibm.blockchain import ExistingEnterpriseSystems` |
| `HyperledgerFabric` | `from diagrams.ibm.blockchain import HyperledgerFabric` |
| `KeyManagement` | `from diagrams.ibm.blockchain import KeyManagement` |
| `Ledger` | `from diagrams.ibm.blockchain import Ledger` |
| `Membership` | `from diagrams.ibm.blockchain import Membership` |
| `MembershipServicesProviderApi` | `from diagrams.ibm.blockchain import MembershipServicesProviderApi` |
| `MessageBus` | `from diagrams.ibm.blockchain import MessageBus` |
| `Node` | `from diagrams.ibm.blockchain import Node` |
| `Services` | `from diagrams.ibm.blockchain import Services` |
| `SmartContract` | `from diagrams.ibm.blockchain import SmartContract` |
| `TransactionManager` | `from diagrams.ibm.blockchain import TransactionManager` |
| `Wallet` | `from diagrams.ibm.blockchain import Wallet` |

### Compute

**Import:** `from diagrams.ibm.compute import ...`

| Class Name | Import Example |
|------------|---------------|
| `BareMetalServer` | `from diagrams.ibm.compute import BareMetalServer` |
| `ImageService` | `from diagrams.ibm.compute import ImageService` |
| `Instance` | `from diagrams.ibm.compute import Instance` |
| `Key` | `from diagrams.ibm.compute import Key` |
| `PowerInstance` | `from diagrams.ibm.compute import PowerInstance` |

### Data

**Import:** `from diagrams.ibm.data import ...`

| Class Name | Import Example |
|------------|---------------|
| `Caches` | `from diagrams.ibm.data import Caches` |
| `Cloud` | `from diagrams.ibm.data import Cloud` |
| `ConversationTrainedDeployed` | `from diagrams.ibm.data import ConversationTrainedDeployed` |
| `DataServices` | `from diagrams.ibm.data import DataServices` |
| `DataSources` | `from diagrams.ibm.data import DataSources` |
| `DeviceIdentityService` | `from diagrams.ibm.data import DeviceIdentityService` |
| `DeviceRegistry` | `from diagrams.ibm.data import DeviceRegistry` |
| `EnterpriseData` | `from diagrams.ibm.data import EnterpriseData` |
| `EnterpriseUserDirectory` | `from diagrams.ibm.data import EnterpriseUserDirectory` |
| `FileRepository` | `from diagrams.ibm.data import FileRepository` |
| `GroundTruth` | `from diagrams.ibm.data import GroundTruth` |
| `Model` | `from diagrams.ibm.data import Model` |
| `TmsDataInterface` | `from diagrams.ibm.data import TmsDataInterface` |

### DevOps

**Import:** `from diagrams.ibm.devops import ...`

| Class Name | Import Example |
|------------|---------------|
| `ArtifactManagement` | `from diagrams.ibm.devops import ArtifactManagement` |
| `BuildTest` | `from diagrams.ibm.devops import BuildTest` |
| `CodeEditor` | `from diagrams.ibm.devops import CodeEditor` |
| `CollaborativeDevelopment` | `from diagrams.ibm.devops import CollaborativeDevelopment` |
| `ConfigurationManagement` | `from diagrams.ibm.devops import ConfigurationManagement` |
| `ContinuousDeploy` | `from diagrams.ibm.devops import ContinuousDeploy` |
| `ContinuousTesting` | `from diagrams.ibm.devops import ContinuousTesting` |
| `Devops` | `from diagrams.ibm.devops import Devops` |
| `Provision` | `from diagrams.ibm.devops import Provision` |
| `ReleaseManagement` | `from diagrams.ibm.devops import ReleaseManagement` |

### General

**Import:** `from diagrams.ibm.general import ...`

| Class Name | Import Example |
|------------|---------------|
| `CloudMessaging` | `from diagrams.ibm.general import CloudMessaging` |
| `CloudServices` | `from diagrams.ibm.general import CloudServices` |
| `Cloudant` | `from diagrams.ibm.general import Cloudant` |
| `CognitiveServices` | `from diagrams.ibm.general import CognitiveServices` |
| `DataSecurity` | `from diagrams.ibm.general import DataSecurity` |
| `Enterprise` | `from diagrams.ibm.general import Enterprise` |
| `GovernanceRiskCompliance` | `from diagrams.ibm.general import GovernanceRiskCompliance` |
| `IBMContainers` | `from diagrams.ibm.general import IBMContainers` |
| `IBMPublicCloud` | `from diagrams.ibm.general import IBMPublicCloud` |
| `IdentityAccessManagement` | `from diagrams.ibm.general import IdentityAccessManagement` |
| `IdentityProvider` | `from diagrams.ibm.general import IdentityProvider` |
| `InfrastructureSecurity` | `from diagrams.ibm.general import InfrastructureSecurity` |
| `Internet` | `from diagrams.ibm.general import Internet` |
| `IotCloud` | `from diagrams.ibm.general import IotCloud` |
| `MicroservicesApplication` | `from diagrams.ibm.general import MicroservicesApplication` |
| `MicroservicesMesh` | `from diagrams.ibm.general import MicroservicesMesh` |
| `Monitoring` | `from diagrams.ibm.general import Monitoring` |
| `MonitoringLogging` | `from diagrams.ibm.general import MonitoringLogging` |
| `ObjectStorage` | `from diagrams.ibm.general import ObjectStorage` |
| `OfflineCapabilities` | `from diagrams.ibm.general import OfflineCapabilities` |
| `Openwhisk` | `from diagrams.ibm.general import Openwhisk` |
| `PeerCloud` | `from diagrams.ibm.general import PeerCloud` |
| `RetrieveRank` | `from diagrams.ibm.general import RetrieveRank` |
| `Scalable` | `from diagrams.ibm.general import Scalable` |
| `ServiceDiscoveryConfiguration` | `from diagrams.ibm.general import ServiceDiscoveryConfiguration` |
| `TextToSpeech` | `from diagrams.ibm.general import TextToSpeech` |
| `TransformationConnectivity` | `from diagrams.ibm.general import TransformationConnectivity` |

### Infrastructure

**Import:** `from diagrams.ibm.infrastructure import ...`

| Class Name | Import Example |
|------------|---------------|
| `Channels` | `from diagrams.ibm.infrastructure import Channels` |
| `CloudMessaging` | `from diagrams.ibm.infrastructure import CloudMessaging` |
| `Dashboard` | `from diagrams.ibm.infrastructure import Dashboard` |
| `Diagnostics` | `from diagrams.ibm.infrastructure import Diagnostics` |
| `EdgeServices` | `from diagrams.ibm.infrastructure import EdgeServices` |
| `EnterpriseMessaging` | `from diagrams.ibm.infrastructure import EnterpriseMessaging` |
| `EventFeed` | `from diagrams.ibm.infrastructure import EventFeed` |
| `InfrastructureServices` | `from diagrams.ibm.infrastructure import InfrastructureServices` |
| `InterserviceCommunication` | `from diagrams.ibm.infrastructure import InterserviceCommunication` |
| `LoadBalancingRouting` | `from diagrams.ibm.infrastructure import LoadBalancingRouting` |
| `MicroservicesMesh` | `from diagrams.ibm.infrastructure import MicroservicesMesh` |
| `MobileBackend` | `from diagrams.ibm.infrastructure import MobileBackend` |
| `MobileProviderNetwork` | `from diagrams.ibm.infrastructure import MobileProviderNetwork` |
| `Monitoring` | `from diagrams.ibm.infrastructure import Monitoring` |
| `MonitoringLogging` | `from diagrams.ibm.infrastructure import MonitoringLogging` |
| `PeerServices` | `from diagrams.ibm.infrastructure import PeerServices` |
| `ServiceDiscoveryConfiguration` | `from diagrams.ibm.infrastructure import ServiceDiscoveryConfiguration` |
| `TransformationConnectivity` | `from diagrams.ibm.infrastructure import TransformationConnectivity` |

### Management

**Import:** `from diagrams.ibm.management import ...`

| Class Name | Import Example |
|------------|---------------|
| `AlertNotification` | `from diagrams.ibm.management import AlertNotification` |
| `ApiManagement` | `from diagrams.ibm.management import ApiManagement` |
| `CloudManagement` | `from diagrams.ibm.management import CloudManagement` |
| `ClusterManagement` | `from diagrams.ibm.management import ClusterManagement` |
| `ContentManagement` | `from diagrams.ibm.management import ContentManagement` |
| `DataServices` | `from diagrams.ibm.management import DataServices` |
| `DeviceManagement` | `from diagrams.ibm.management import DeviceManagement` |
| `InformationGovernance` | `from diagrams.ibm.management import InformationGovernance` |
| `ItServiceManagement` | `from diagrams.ibm.management import ItServiceManagement` |
| `Management` | `from diagrams.ibm.management import Management` |
| `MonitoringMetrics` | `from diagrams.ibm.management import MonitoringMetrics` |
| `ProcessManagement` | `from diagrams.ibm.management import ProcessManagement` |
| `ProviderCloudPortalService` | `from diagrams.ibm.management import ProviderCloudPortalService` |
| `PushNotifications` | `from diagrams.ibm.management import PushNotifications` |
| `ServiceManagementTools` | `from diagrams.ibm.management import ServiceManagementTools` |

### Network

**Import:** `from diagrams.ibm.network import ...`

| Class Name | Import Example |
|------------|---------------|
| `Bridge` | `from diagrams.ibm.network import Bridge` |
| `DirectLink` | `from diagrams.ibm.network import DirectLink` |
| `Enterprise` | `from diagrams.ibm.network import Enterprise` |
| `Firewall` | `from diagrams.ibm.network import Firewall` |
| `FloatingIp` | `from diagrams.ibm.network import FloatingIp` |
| `Gateway` | `from diagrams.ibm.network import Gateway` |
| `InternetServices` | `from diagrams.ibm.network import InternetServices` |
| `LoadBalancer` | `from diagrams.ibm.network import LoadBalancer` |
| `LoadBalancerListener` | `from diagrams.ibm.network import LoadBalancerListener` |
| `LoadBalancerPool` | `from diagrams.ibm.network import LoadBalancerPool` |
| `LoadBalancingRouting` | `from diagrams.ibm.network import LoadBalancingRouting` |
| `PublicGateway` | `from diagrams.ibm.network import PublicGateway` |
| `Region` | `from diagrams.ibm.network import Region` |
| `Router` | `from diagrams.ibm.network import Router` |
| `Rules` | `from diagrams.ibm.network import Rules` |
| `Subnet` | `from diagrams.ibm.network import Subnet` |
| `TransitGateway` | `from diagrams.ibm.network import TransitGateway` |
| `Vpc` | `from diagrams.ibm.network import Vpc` |
| `VpnConnection` | `from diagrams.ibm.network import VpnConnection` |
| `VpnGateway` | `from diagrams.ibm.network import VpnGateway` |
| `VpnPolicy` | `from diagrams.ibm.network import VpnPolicy` |

### Security

**Import:** `from diagrams.ibm.security import ...`

| Class Name | Import Example |
|------------|---------------|
| `ApiSecurity` | `from diagrams.ibm.security import ApiSecurity` |
| `BlockchainSecurityService` | `from diagrams.ibm.security import BlockchainSecurityService` |
| `DataSecurity` | `from diagrams.ibm.security import DataSecurity` |
| `Firewall` | `from diagrams.ibm.security import Firewall` |
| `Gateway` | `from diagrams.ibm.security import Gateway` |
| `GovernanceRiskCompliance` | `from diagrams.ibm.security import GovernanceRiskCompliance` |
| `IdentityAccessManagement` | `from diagrams.ibm.security import IdentityAccessManagement` |
| `IdentityProvider` | `from diagrams.ibm.security import IdentityProvider` |
| `InfrastructureSecurity` | `from diagrams.ibm.security import InfrastructureSecurity` |
| `PhysicalSecurity` | `from diagrams.ibm.security import PhysicalSecurity` |
| `SecurityMonitoringIntelligence` | `from diagrams.ibm.security import SecurityMonitoringIntelligence` |
| `SecurityServices` | `from diagrams.ibm.security import SecurityServices` |
| `TrustendComputing` | `from diagrams.ibm.security import TrustendComputing` |
| `Vpn` | `from diagrams.ibm.security import Vpn` |

### Social

**Import:** `from diagrams.ibm.social import ...`

| Class Name | Import Example |
|------------|---------------|
| `Communities` | `from diagrams.ibm.social import Communities` |
| `FileSync` | `from diagrams.ibm.social import FileSync` |
| `LiveCollaboration` | `from diagrams.ibm.social import LiveCollaboration` |
| `Messaging` | `from diagrams.ibm.social import Messaging` |
| `Networking` | `from diagrams.ibm.social import Networking` |

### Storage

**Import:** `from diagrams.ibm.storage import ...`

| Class Name | Import Example |
|------------|---------------|
| `BlockStorage` | `from diagrams.ibm.storage import BlockStorage` |
| `ObjectStorage` | `from diagrams.ibm.storage import ObjectStorage` |

### User

**Import:** `from diagrams.ibm.user import ...`

| Class Name | Import Example |
|------------|---------------|
| `Browser` | `from diagrams.ibm.user import Browser` |
| `Device` | `from diagrams.ibm.user import Device` |
| `IntegratedDigitalExperiences` | `from diagrams.ibm.user import IntegratedDigitalExperiences` |
| `PhysicalEntity` | `from diagrams.ibm.user import PhysicalEntity` |
| `Sensor` | `from diagrams.ibm.user import Sensor` |
| `User` | `from diagrams.ibm.user import User` |

---

## Oracle Cloud Infrastructure (OCI)

_Oracle Cloud services_ — **152 icons** across **9 categories**

### Compute

**Import:** `from diagrams.oci.compute import ...`

| Class Name | Import Example |
|------------|---------------|
| `Autoscale` | `from diagrams.oci.compute import Autoscale` |
| `AutoscaleWhite` | `from diagrams.oci.compute import AutoscaleWhite` |
| `BM` | `from diagrams.oci.compute import BM` |
| `BMWhite` | `from diagrams.oci.compute import BMWhite` |
| `BareMetal` | `from diagrams.oci.compute import BareMetal` |
| `BareMetalWhite` | `from diagrams.oci.compute import BareMetalWhite` |
| `Container` | `from diagrams.oci.compute import Container` |
| `ContainerEngine` | `from diagrams.oci.compute import ContainerEngine` |
| `ContainerEngineWhite` | `from diagrams.oci.compute import ContainerEngineWhite` |
| `ContainerWhite` | `from diagrams.oci.compute import ContainerWhite` |
| `Functions` | `from diagrams.oci.compute import Functions` |
| `FunctionsWhite` | `from diagrams.oci.compute import FunctionsWhite` |
| `InstancePools` | `from diagrams.oci.compute import InstancePools` |
| `InstancePoolsWhite` | `from diagrams.oci.compute import InstancePoolsWhite` |
| `OCIR` | `from diagrams.oci.compute import OCIR` |
| `OCIRWhite` | `from diagrams.oci.compute import OCIRWhite` |
| `OCIRegistry` | `from diagrams.oci.compute import OCIRegistry` |
| `OCIRegistryWhite` | `from diagrams.oci.compute import OCIRegistryWhite` |
| `OKE` | `from diagrams.oci.compute import OKE` |
| `OKEWhite` | `from diagrams.oci.compute import OKEWhite` |
| `VM` | `from diagrams.oci.compute import VM` |
| `VMWhite` | `from diagrams.oci.compute import VMWhite` |
| `VirtualMachine` | `from diagrams.oci.compute import VirtualMachine` |
| `VirtualMachineWhite` | `from diagrams.oci.compute import VirtualMachineWhite` |

### Connectivity

**Import:** `from diagrams.oci.connectivity import ...`

| Class Name | Import Example |
|------------|---------------|
| `Backbone` | `from diagrams.oci.connectivity import Backbone` |
| `BackboneWhite` | `from diagrams.oci.connectivity import BackboneWhite` |
| `CDN` | `from diagrams.oci.connectivity import CDN` |
| `CDNWhite` | `from diagrams.oci.connectivity import CDNWhite` |
| `CustomerDatacenter` | `from diagrams.oci.connectivity import CustomerDatacenter` |
| `CustomerDatacntrWhite` | `from diagrams.oci.connectivity import CustomerDatacntrWhite` |
| `CustomerPremises` | `from diagrams.oci.connectivity import CustomerPremises` |
| `CustomerPremisesWhite` | `from diagrams.oci.connectivity import CustomerPremisesWhite` |
| `DNS` | `from diagrams.oci.connectivity import DNS` |
| `DNSWhite` | `from diagrams.oci.connectivity import DNSWhite` |
| `DisconnectedRegions` | `from diagrams.oci.connectivity import DisconnectedRegions` |
| `DisconnectedRegionsWhite` | `from diagrams.oci.connectivity import DisconnectedRegionsWhite` |
| `FastConnect` | `from diagrams.oci.connectivity import FastConnect` |
| `FastConnectWhite` | `from diagrams.oci.connectivity import FastConnectWhite` |
| `NATGateway` | `from diagrams.oci.connectivity import NATGateway` |
| `NATGatewayWhite` | `from diagrams.oci.connectivity import NATGatewayWhite` |
| `VPN` | `from diagrams.oci.connectivity import VPN` |
| `VPNWhite` | `from diagrams.oci.connectivity import VPNWhite` |

### Database

**Import:** `from diagrams.oci.database import ...`

| Class Name | Import Example |
|------------|---------------|
| `ADB` | `from diagrams.oci.database import ADB` |
| `ADBWhite` | `from diagrams.oci.database import ADBWhite` |
| `Autonomous` | `from diagrams.oci.database import Autonomous` |
| `AutonomousWhite` | `from diagrams.oci.database import AutonomousWhite` |
| `BigdataService` | `from diagrams.oci.database import BigdataService` |
| `BigdataServiceWhite` | `from diagrams.oci.database import BigdataServiceWhite` |
| `DBService` | `from diagrams.oci.database import DBService` |
| `DBServiceWhite` | `from diagrams.oci.database import DBServiceWhite` |
| `DMS` | `from diagrams.oci.database import DMS` |
| `DMSWhite` | `from diagrams.oci.database import DMSWhite` |
| `DatabaseService` | `from diagrams.oci.database import DatabaseService` |
| `DatabaseServiceWhite` | `from diagrams.oci.database import DatabaseServiceWhite` |
| `DataflowApache` | `from diagrams.oci.database import DataflowApache` |
| `DataflowApacheWhite` | `from diagrams.oci.database import DataflowApacheWhite` |
| `Dcat` | `from diagrams.oci.database import Dcat` |
| `DcatWhite` | `from diagrams.oci.database import DcatWhite` |
| `Dis` | `from diagrams.oci.database import Dis` |
| `DisWhite` | `from diagrams.oci.database import DisWhite` |
| `Science` | `from diagrams.oci.database import Science` |
| `ScienceWhite` | `from diagrams.oci.database import ScienceWhite` |
| `Stream` | `from diagrams.oci.database import Stream` |
| `StreamWhite` | `from diagrams.oci.database import StreamWhite` |

### DevOps

**Import:** `from diagrams.oci.devops import ...`

| Class Name | Import Example |
|------------|---------------|
| `APIGateway` | `from diagrams.oci.devops import APIGateway` |
| `APIGatewayWhite` | `from diagrams.oci.devops import APIGatewayWhite` |
| `APIService` | `from diagrams.oci.devops import APIService` |
| `APIServiceWhite` | `from diagrams.oci.devops import APIServiceWhite` |
| `ResourceMgmt` | `from diagrams.oci.devops import ResourceMgmt` |
| `ResourceMgmtWhite` | `from diagrams.oci.devops import ResourceMgmtWhite` |

### Governance

**Import:** `from diagrams.oci.governance import ...`

| Class Name | Import Example |
|------------|---------------|
| `Audit` | `from diagrams.oci.governance import Audit` |
| `AuditWhite` | `from diagrams.oci.governance import AuditWhite` |
| `Compartments` | `from diagrams.oci.governance import Compartments` |
| `CompartmentsWhite` | `from diagrams.oci.governance import CompartmentsWhite` |
| `Groups` | `from diagrams.oci.governance import Groups` |
| `GroupsWhite` | `from diagrams.oci.governance import GroupsWhite` |
| `Logging` | `from diagrams.oci.governance import Logging` |
| `LoggingWhite` | `from diagrams.oci.governance import LoggingWhite` |
| `OCID` | `from diagrams.oci.governance import OCID` |
| `OCIDWhite` | `from diagrams.oci.governance import OCIDWhite` |
| `Policies` | `from diagrams.oci.governance import Policies` |
| `PoliciesWhite` | `from diagrams.oci.governance import PoliciesWhite` |
| `Tagging` | `from diagrams.oci.governance import Tagging` |
| `TaggingWhite` | `from diagrams.oci.governance import TaggingWhite` |

### Monitoring

**Import:** `from diagrams.oci.monitoring import ...`

| Class Name | Import Example |
|------------|---------------|
| `Alarm` | `from diagrams.oci.monitoring import Alarm` |
| `AlarmWhite` | `from diagrams.oci.monitoring import AlarmWhite` |
| `Email` | `from diagrams.oci.monitoring import Email` |
| `EmailWhite` | `from diagrams.oci.monitoring import EmailWhite` |
| `Events` | `from diagrams.oci.monitoring import Events` |
| `EventsWhite` | `from diagrams.oci.monitoring import EventsWhite` |
| `HealthCheck` | `from diagrams.oci.monitoring import HealthCheck` |
| `HealthCheckWhite` | `from diagrams.oci.monitoring import HealthCheckWhite` |
| `Notifications` | `from diagrams.oci.monitoring import Notifications` |
| `NotificationsWhite` | `from diagrams.oci.monitoring import NotificationsWhite` |
| `Queue` | `from diagrams.oci.monitoring import Queue` |
| `QueueWhite` | `from diagrams.oci.monitoring import QueueWhite` |
| `Search` | `from diagrams.oci.monitoring import Search` |
| `SearchWhite` | `from diagrams.oci.monitoring import SearchWhite` |
| `Telemetry` | `from diagrams.oci.monitoring import Telemetry` |
| `TelemetryWhite` | `from diagrams.oci.monitoring import TelemetryWhite` |
| `Workflow` | `from diagrams.oci.monitoring import Workflow` |
| `WorkflowWhite` | `from diagrams.oci.monitoring import WorkflowWhite` |

### Network

**Import:** `from diagrams.oci.network import ...`

| Class Name | Import Example |
|------------|---------------|
| `Drg` | `from diagrams.oci.network import Drg` |
| `DrgWhite` | `from diagrams.oci.network import DrgWhite` |
| `Firewall` | `from diagrams.oci.network import Firewall` |
| `FirewallWhite` | `from diagrams.oci.network import FirewallWhite` |
| `InternetGateway` | `from diagrams.oci.network import InternetGateway` |
| `InternetGatewayWhite` | `from diagrams.oci.network import InternetGatewayWhite` |
| `LoadBalancer` | `from diagrams.oci.network import LoadBalancer` |
| `LoadBalancerWhite` | `from diagrams.oci.network import LoadBalancerWhite` |
| `RouteTable` | `from diagrams.oci.network import RouteTable` |
| `RouteTableWhite` | `from diagrams.oci.network import RouteTableWhite` |
| `SecurityLists` | `from diagrams.oci.network import SecurityLists` |
| `SecurityListsWhite` | `from diagrams.oci.network import SecurityListsWhite` |
| `ServiceGateway` | `from diagrams.oci.network import ServiceGateway` |
| `ServiceGatewayWhite` | `from diagrams.oci.network import ServiceGatewayWhite` |
| `Vcn` | `from diagrams.oci.network import Vcn` |
| `VcnWhite` | `from diagrams.oci.network import VcnWhite` |

### Security

**Import:** `from diagrams.oci.security import ...`

| Class Name | Import Example |
|------------|---------------|
| `CloudGuard` | `from diagrams.oci.security import CloudGuard` |
| `CloudGuardWhite` | `from diagrams.oci.security import CloudGuardWhite` |
| `DDOS` | `from diagrams.oci.security import DDOS` |
| `DDOSWhite` | `from diagrams.oci.security import DDOSWhite` |
| `Encryption` | `from diagrams.oci.security import Encryption` |
| `EncryptionWhite` | `from diagrams.oci.security import EncryptionWhite` |
| `IDAccess` | `from diagrams.oci.security import IDAccess` |
| `IDAccessWhite` | `from diagrams.oci.security import IDAccessWhite` |
| `KeyManagement` | `from diagrams.oci.security import KeyManagement` |
| `KeyManagementWhite` | `from diagrams.oci.security import KeyManagementWhite` |
| `MaxSecurityZone` | `from diagrams.oci.security import MaxSecurityZone` |
| `MaxSecurityZoneWhite` | `from diagrams.oci.security import MaxSecurityZoneWhite` |
| `Vault` | `from diagrams.oci.security import Vault` |
| `VaultWhite` | `from diagrams.oci.security import VaultWhite` |
| `WAF` | `from diagrams.oci.security import WAF` |
| `WAFWhite` | `from diagrams.oci.security import WAFWhite` |

### Storage

**Import:** `from diagrams.oci.storage import ...`

| Class Name | Import Example |
|------------|---------------|
| `BackupRestore` | `from diagrams.oci.storage import BackupRestore` |
| `BackupRestoreWhite` | `from diagrams.oci.storage import BackupRestoreWhite` |
| `BlockStorage` | `from diagrams.oci.storage import BlockStorage` |
| `BlockStorageClone` | `from diagrams.oci.storage import BlockStorageClone` |
| `BlockStorageCloneWhite` | `from diagrams.oci.storage import BlockStorageCloneWhite` |
| `BlockStorageWhite` | `from diagrams.oci.storage import BlockStorageWhite` |
| `Buckets` | `from diagrams.oci.storage import Buckets` |
| `BucketsWhite` | `from diagrams.oci.storage import BucketsWhite` |
| `DataTransfer` | `from diagrams.oci.storage import DataTransfer` |
| `DataTransferWhite` | `from diagrams.oci.storage import DataTransferWhite` |
| `ElasticPerformance` | `from diagrams.oci.storage import ElasticPerformance` |
| `ElasticPerformanceWhite` | `from diagrams.oci.storage import ElasticPerformanceWhite` |
| `FileStorage` | `from diagrams.oci.storage import FileStorage` |
| `FileStorageWhite` | `from diagrams.oci.storage import FileStorageWhite` |
| `ObjectStorage` | `from diagrams.oci.storage import ObjectStorage` |
| `ObjectStorageWhite` | `from diagrams.oci.storage import ObjectStorageWhite` |
| `StorageGateway` | `from diagrams.oci.storage import StorageGateway` |
| `StorageGatewayWhite` | `from diagrams.oci.storage import StorageGatewayWhite` |

---

## OpenStack

_OpenStack cloud infrastructure services_ — **54 icons** across **19 categories**

### API Proxies

**Import:** `from diagrams.openstack.apiproxies import ...`

| Class Name | Import Example |
|------------|---------------|
| `EC2API` | `from diagrams.openstack.apiproxies import EC2API` |

### Application Lifecycle

**Import:** `from diagrams.openstack.applicationlifecycle import ...`

| Class Name | Import Example |
|------------|---------------|
| `Freezer` | `from diagrams.openstack.applicationlifecycle import Freezer` |
| `Masakari` | `from diagrams.openstack.applicationlifecycle import Masakari` |
| `Murano` | `from diagrams.openstack.applicationlifecycle import Murano` |
| `Solum` | `from diagrams.openstack.applicationlifecycle import Solum` |

### Bare Metal

**Import:** `from diagrams.openstack.baremetal import ...`

| Class Name | Import Example |
|------------|---------------|
| `Cyborg` | `from diagrams.openstack.baremetal import Cyborg` |
| `Ironic` | `from diagrams.openstack.baremetal import Ironic` |

### Billing

**Import:** `from diagrams.openstack.billing import ...`

| Class Name | Import Example |
|------------|---------------|
| `CloudKitty` | `from diagrams.openstack.billing import CloudKitty` |
| `Cloudkitty` | `from diagrams.openstack.billing import Cloudkitty` |

### Compute

**Import:** `from diagrams.openstack.compute import ...`

| Class Name | Import Example |
|------------|---------------|
| `Nova` | `from diagrams.openstack.compute import Nova` |
| `Qinling` | `from diagrams.openstack.compute import Qinling` |
| `Zun` | `from diagrams.openstack.compute import Zun` |

### Container Services

**Import:** `from diagrams.openstack.containerservices import ...`

| Class Name | Import Example |
|------------|---------------|
| `Kuryr` | `from diagrams.openstack.containerservices import Kuryr` |

### Deployment

**Import:** `from diagrams.openstack.deployment import ...`

| Class Name | Import Example |
|------------|---------------|
| `Ansible` | `from diagrams.openstack.deployment import Ansible` |
| `Charms` | `from diagrams.openstack.deployment import Charms` |
| `Chef` | `from diagrams.openstack.deployment import Chef` |
| `Helm` | `from diagrams.openstack.deployment import Helm` |
| `Kolla` | `from diagrams.openstack.deployment import Kolla` |
| `KollaAnsible` | `from diagrams.openstack.deployment import KollaAnsible` |
| `TripleO` | `from diagrams.openstack.deployment import TripleO` |
| `Tripleo` | `from diagrams.openstack.deployment import Tripleo` |

### Frontend

**Import:** `from diagrams.openstack.frontend import ...`

| Class Name | Import Example |
|------------|---------------|
| `Horizon` | `from diagrams.openstack.frontend import Horizon` |

### Monitoring

**Import:** `from diagrams.openstack.monitoring import ...`

| Class Name | Import Example |
|------------|---------------|
| `Monasca` | `from diagrams.openstack.monitoring import Monasca` |
| `Telemetry` | `from diagrams.openstack.monitoring import Telemetry` |

### Multi-Region

**Import:** `from diagrams.openstack.multiregion import ...`

| Class Name | Import Example |
|------------|---------------|
| `Tricircle` | `from diagrams.openstack.multiregion import Tricircle` |

### Networking

**Import:** `from diagrams.openstack.networking import ...`

| Class Name | Import Example |
|------------|---------------|
| `Designate` | `from diagrams.openstack.networking import Designate` |
| `Neutron` | `from diagrams.openstack.networking import Neutron` |
| `Octavia` | `from diagrams.openstack.networking import Octavia` |

### NFV

**Import:** `from diagrams.openstack.nfv import ...`

| Class Name | Import Example |
|------------|---------------|
| `Tacker` | `from diagrams.openstack.nfv import Tacker` |

### Optimization

**Import:** `from diagrams.openstack.optimization import ...`

| Class Name | Import Example |
|------------|---------------|
| `Congress` | `from diagrams.openstack.optimization import Congress` |
| `Rally` | `from diagrams.openstack.optimization import Rally` |
| `Vitrage` | `from diagrams.openstack.optimization import Vitrage` |
| `Watcher` | `from diagrams.openstack.optimization import Watcher` |

### Orchestration

**Import:** `from diagrams.openstack.orchestration import ...`

| Class Name | Import Example |
|------------|---------------|
| `Blazar` | `from diagrams.openstack.orchestration import Blazar` |
| `Heat` | `from diagrams.openstack.orchestration import Heat` |
| `Mistral` | `from diagrams.openstack.orchestration import Mistral` |
| `Senlin` | `from diagrams.openstack.orchestration import Senlin` |
| `Zaqar` | `from diagrams.openstack.orchestration import Zaqar` |

### Packaging

**Import:** `from diagrams.openstack.packaging import ...`

| Class Name | Import Example |
|------------|---------------|
| `LOCI` | `from diagrams.openstack.packaging import LOCI` |
| `Puppet` | `from diagrams.openstack.packaging import Puppet` |
| `RPM` | `from diagrams.openstack.packaging import RPM` |

### Shared Services

**Import:** `from diagrams.openstack.sharedservices import ...`

| Class Name | Import Example |
|------------|---------------|
| `Barbican` | `from diagrams.openstack.sharedservices import Barbican` |
| `Glance` | `from diagrams.openstack.sharedservices import Glance` |
| `Karbor` | `from diagrams.openstack.sharedservices import Karbor` |
| `Keystone` | `from diagrams.openstack.sharedservices import Keystone` |
| `Searchlight` | `from diagrams.openstack.sharedservices import Searchlight` |

### Storage

**Import:** `from diagrams.openstack.storage import ...`

| Class Name | Import Example |
|------------|---------------|
| `Cinder` | `from diagrams.openstack.storage import Cinder` |
| `Manila` | `from diagrams.openstack.storage import Manila` |
| `Swift` | `from diagrams.openstack.storage import Swift` |

### User

**Import:** `from diagrams.openstack.user import ...`

| Class Name | Import Example |
|------------|---------------|
| `OpenStackClient` | `from diagrams.openstack.user import OpenStackClient` |
| `Openstackclient` | `from diagrams.openstack.user import Openstackclient` |

### Workload Provisioning

**Import:** `from diagrams.openstack.workloadprovisioning import ...`

| Class Name | Import Example |
|------------|---------------|
| `Magnum` | `from diagrams.openstack.workloadprovisioning import Magnum` |
| `Sahara` | `from diagrams.openstack.workloadprovisioning import Sahara` |
| `Trove` | `from diagrams.openstack.workloadprovisioning import Trove` |

---

## Outscale

_Outscale cloud provider services_ — **12 icons** across **4 categories**

### Compute

**Import:** `from diagrams.outscale.compute import ...`

| Class Name | Import Example |
|------------|---------------|
| `Compute` | `from diagrams.outscale.compute import Compute` |
| `DirectConnect` | `from diagrams.outscale.compute import DirectConnect` |

### Network

**Import:** `from diagrams.outscale.network import ...`

| Class Name | Import Example |
|------------|---------------|
| `ClientVpn` | `from diagrams.outscale.network import ClientVpn` |
| `InternetService` | `from diagrams.outscale.network import InternetService` |
| `LoadBalancer` | `from diagrams.outscale.network import LoadBalancer` |
| `NatService` | `from diagrams.outscale.network import NatService` |
| `Net` | `from diagrams.outscale.network import Net` |
| `SiteToSiteVpng` | `from diagrams.outscale.network import SiteToSiteVpng` |

### Security

**Import:** `from diagrams.outscale.security import ...`

| Class Name | Import Example |
|------------|---------------|
| `Firewall` | `from diagrams.outscale.security import Firewall` |
| `IdentityAndAccessManagement` | `from diagrams.outscale.security import IdentityAndAccessManagement` |

### Storage

**Import:** `from diagrams.outscale.storage import ...`

| Class Name | Import Example |
|------------|---------------|
| `SimpleStorageService` | `from diagrams.outscale.storage import SimpleStorageService` |
| `Storage` | `from diagrams.outscale.storage import Storage` |

---

## Alibaba Cloud

_Alibaba Cloud (Aliyun) services_ — **131 icons** across **10 categories**

### Analytics

**Import:** `from diagrams.alibabacloud.analytics import ...`

| Class Name | Import Example |
|------------|---------------|
| `AnalyticDb` | `from diagrams.alibabacloud.analytics import AnalyticDb` |
| `ClickHouse` | `from diagrams.alibabacloud.analytics import ClickHouse` |
| `DataLakeAnalytics` | `from diagrams.alibabacloud.analytics import DataLakeAnalytics` |
| `ElaticMapReduce` | `from diagrams.alibabacloud.analytics import ElaticMapReduce` |
| `OpenSearch` | `from diagrams.alibabacloud.analytics import OpenSearch` |

### Application

**Import:** `from diagrams.alibabacloud.application import ...`

| Class Name | Import Example |
|------------|---------------|
| `ApiGateway` | `from diagrams.alibabacloud.application import ApiGateway` |
| `BeeBot` | `from diagrams.alibabacloud.application import BeeBot` |
| `BlockchainAsAService` | `from diagrams.alibabacloud.application import BlockchainAsAService` |
| `CloudCallCenter` | `from diagrams.alibabacloud.application import CloudCallCenter` |
| `CodePipeline` | `from diagrams.alibabacloud.application import CodePipeline` |
| `DirectMail` | `from diagrams.alibabacloud.application import DirectMail` |
| `LogService` | `from diagrams.alibabacloud.application import LogService` |
| `MNS` | `from diagrams.alibabacloud.application import MNS` |
| `MessageNotificationService` | `from diagrams.alibabacloud.application import MessageNotificationService` |
| `NodeJsPerformancePlatform` | `from diagrams.alibabacloud.application import NodeJsPerformancePlatform` |
| `OpenSearch` | `from diagrams.alibabacloud.application import OpenSearch` |
| `PTS` | `from diagrams.alibabacloud.application import PTS` |
| `PerformanceTestingService` | `from diagrams.alibabacloud.application import PerformanceTestingService` |
| `RdCloud` | `from diagrams.alibabacloud.application import RdCloud` |
| `SCA` | `from diagrams.alibabacloud.application import SCA` |
| `SLS` | `from diagrams.alibabacloud.application import SLS` |
| `SmartConversationAnalysis` | `from diagrams.alibabacloud.application import SmartConversationAnalysis` |
| `Yida` | `from diagrams.alibabacloud.application import Yida` |

### Communication

**Import:** `from diagrams.alibabacloud.communication import ...`

| Class Name | Import Example |
|------------|---------------|
| `DirectMail` | `from diagrams.alibabacloud.communication import DirectMail` |
| `MobilePush` | `from diagrams.alibabacloud.communication import MobilePush` |

### Compute

**Import:** `from diagrams.alibabacloud.compute import ...`

| Class Name | Import Example |
|------------|---------------|
| `AutoScaling` | `from diagrams.alibabacloud.compute import AutoScaling` |
| `BatchCompute` | `from diagrams.alibabacloud.compute import BatchCompute` |
| `ContainerRegistry` | `from diagrams.alibabacloud.compute import ContainerRegistry` |
| `ContainerService` | `from diagrams.alibabacloud.compute import ContainerService` |
| `ECI` | `from diagrams.alibabacloud.compute import ECI` |
| `ECS` | `from diagrams.alibabacloud.compute import ECS` |
| `EHPC` | `from diagrams.alibabacloud.compute import EHPC` |
| `ESS` | `from diagrams.alibabacloud.compute import ESS` |
| `ElasticComputeService` | `from diagrams.alibabacloud.compute import ElasticComputeService` |
| `ElasticContainerInstance` | `from diagrams.alibabacloud.compute import ElasticContainerInstance` |
| `ElasticHighPerformanceComputing` | `from diagrams.alibabacloud.compute import ElasticHighPerformanceComputing` |
| `ElasticSearch` | `from diagrams.alibabacloud.compute import ElasticSearch` |
| `FC` | `from diagrams.alibabacloud.compute import FC` |
| `FunctionCompute` | `from diagrams.alibabacloud.compute import FunctionCompute` |
| `OOS` | `from diagrams.alibabacloud.compute import OOS` |
| `OperationOrchestrationService` | `from diagrams.alibabacloud.compute import OperationOrchestrationService` |
| `ROS` | `from diagrams.alibabacloud.compute import ROS` |
| `ResourceOrchestrationService` | `from diagrams.alibabacloud.compute import ResourceOrchestrationService` |
| `SAE` | `from diagrams.alibabacloud.compute import SAE` |
| `SAS` | `from diagrams.alibabacloud.compute import SAS` |
| `SLB` | `from diagrams.alibabacloud.compute import SLB` |
| `ServerLoadBalancer` | `from diagrams.alibabacloud.compute import ServerLoadBalancer` |
| `ServerlessAppEngine` | `from diagrams.alibabacloud.compute import ServerlessAppEngine` |
| `SimpleApplicationServer` | `from diagrams.alibabacloud.compute import SimpleApplicationServer` |
| `WAS` | `from diagrams.alibabacloud.compute import WAS` |
| `WebAppService` | `from diagrams.alibabacloud.compute import WebAppService` |

### Database

**Import:** `from diagrams.alibabacloud.database import ...`

| Class Name | Import Example |
|------------|---------------|
| `ApsaradbCassandra` | `from diagrams.alibabacloud.database import ApsaradbCassandra` |
| `ApsaradbHbase` | `from diagrams.alibabacloud.database import ApsaradbHbase` |
| `ApsaradbMemcache` | `from diagrams.alibabacloud.database import ApsaradbMemcache` |
| `ApsaradbMongodb` | `from diagrams.alibabacloud.database import ApsaradbMongodb` |
| `ApsaradbOceanbase` | `from diagrams.alibabacloud.database import ApsaradbOceanbase` |
| `ApsaradbPolardb` | `from diagrams.alibabacloud.database import ApsaradbPolardb` |
| `ApsaradbPostgresql` | `from diagrams.alibabacloud.database import ApsaradbPostgresql` |
| `ApsaradbPpas` | `from diagrams.alibabacloud.database import ApsaradbPpas` |
| `ApsaradbRedis` | `from diagrams.alibabacloud.database import ApsaradbRedis` |
| `ApsaradbSqlserver` | `from diagrams.alibabacloud.database import ApsaradbSqlserver` |
| `DBS` | `from diagrams.alibabacloud.database import DBS` |
| `DMS` | `from diagrams.alibabacloud.database import DMS` |
| `DRDS` | `from diagrams.alibabacloud.database import DRDS` |
| `DTS` | `from diagrams.alibabacloud.database import DTS` |
| `DataManagementService` | `from diagrams.alibabacloud.database import DataManagementService` |
| `DataTransmissionService` | `from diagrams.alibabacloud.database import DataTransmissionService` |
| `DatabaseBackupService` | `from diagrams.alibabacloud.database import DatabaseBackupService` |
| `DisributeRelationalDatabaseService` | `from diagrams.alibabacloud.database import DisributeRelationalDatabaseService` |
| `GDS` | `from diagrams.alibabacloud.database import GDS` |
| `GraphDatabaseService` | `from diagrams.alibabacloud.database import GraphDatabaseService` |
| `HybriddbForMysql` | `from diagrams.alibabacloud.database import HybriddbForMysql` |
| `RDS` | `from diagrams.alibabacloud.database import RDS` |
| `RelationalDatabaseService` | `from diagrams.alibabacloud.database import RelationalDatabaseService` |

### IoT

**Import:** `from diagrams.alibabacloud.iot import ...`

| Class Name | Import Example |
|------------|---------------|
| `IotInternetDeviceId` | `from diagrams.alibabacloud.iot import IotInternetDeviceId` |
| `IotLinkWan` | `from diagrams.alibabacloud.iot import IotLinkWan` |
| `IotMobileConnectionPackage` | `from diagrams.alibabacloud.iot import IotMobileConnectionPackage` |
| `IotPlatform` | `from diagrams.alibabacloud.iot import IotPlatform` |

### Network

**Import:** `from diagrams.alibabacloud.network import ...`

| Class Name | Import Example |
|------------|---------------|
| `CEN` | `from diagrams.alibabacloud.network import CEN` |
| `Cdn` | `from diagrams.alibabacloud.network import Cdn` |
| `CloudEnterpriseNetwork` | `from diagrams.alibabacloud.network import CloudEnterpriseNetwork` |
| `EIP` | `from diagrams.alibabacloud.network import EIP` |
| `ElasticIpAddress` | `from diagrams.alibabacloud.network import ElasticIpAddress` |
| `ExpressConnect` | `from diagrams.alibabacloud.network import ExpressConnect` |
| `NatGateway` | `from diagrams.alibabacloud.network import NatGateway` |
| `SLB` | `from diagrams.alibabacloud.network import SLB` |
| `ServerLoadBalancer` | `from diagrams.alibabacloud.network import ServerLoadBalancer` |
| `SmartAccessGateway` | `from diagrams.alibabacloud.network import SmartAccessGateway` |
| `VPC` | `from diagrams.alibabacloud.network import VPC` |
| `VirtualPrivateCloud` | `from diagrams.alibabacloud.network import VirtualPrivateCloud` |
| `VpnGateway` | `from diagrams.alibabacloud.network import VpnGateway` |

### Security

**Import:** `from diagrams.alibabacloud.security import ...`

| Class Name | Import Example |
|------------|---------------|
| `ABS` | `from diagrams.alibabacloud.security import ABS` |
| `AS` | `from diagrams.alibabacloud.security import AS` |
| `AntiBotService` | `from diagrams.alibabacloud.security import AntiBotService` |
| `AntiDdosBasic` | `from diagrams.alibabacloud.security import AntiDdosBasic` |
| `AntiDdosPro` | `from diagrams.alibabacloud.security import AntiDdosPro` |
| `AntifraudService` | `from diagrams.alibabacloud.security import AntifraudService` |
| `BastionHost` | `from diagrams.alibabacloud.security import BastionHost` |
| `CFW` | `from diagrams.alibabacloud.security import CFW` |
| `CM` | `from diagrams.alibabacloud.security import CM` |
| `CloudFirewall` | `from diagrams.alibabacloud.security import CloudFirewall` |
| `CloudSecurityScanner` | `from diagrams.alibabacloud.security import CloudSecurityScanner` |
| `ContentModeration` | `from diagrams.alibabacloud.security import ContentModeration` |
| `CrowdsourcedSecurityTesting` | `from diagrams.alibabacloud.security import CrowdsourcedSecurityTesting` |
| `DES` | `from diagrams.alibabacloud.security import DES` |
| `DataEncryptionService` | `from diagrams.alibabacloud.security import DataEncryptionService` |
| `DbAudit` | `from diagrams.alibabacloud.security import DbAudit` |
| `GameShield` | `from diagrams.alibabacloud.security import GameShield` |
| `IdVerification` | `from diagrams.alibabacloud.security import IdVerification` |
| `ManagedSecurityService` | `from diagrams.alibabacloud.security import ManagedSecurityService` |
| `SecurityCenter` | `from diagrams.alibabacloud.security import SecurityCenter` |
| `ServerGuard` | `from diagrams.alibabacloud.security import ServerGuard` |
| `SslCertificates` | `from diagrams.alibabacloud.security import SslCertificates` |
| `WAF` | `from diagrams.alibabacloud.security import WAF` |
| `WebApplicationFirewall` | `from diagrams.alibabacloud.security import WebApplicationFirewall` |

### Storage

**Import:** `from diagrams.alibabacloud.storage import ...`

| Class Name | Import Example |
|------------|---------------|
| `CloudStorageGateway` | `from diagrams.alibabacloud.storage import CloudStorageGateway` |
| `FileStorageHdfs` | `from diagrams.alibabacloud.storage import FileStorageHdfs` |
| `FileStorageNas` | `from diagrams.alibabacloud.storage import FileStorageNas` |
| `HBR` | `from diagrams.alibabacloud.storage import HBR` |
| `HDFS` | `from diagrams.alibabacloud.storage import HDFS` |
| `HDR` | `from diagrams.alibabacloud.storage import HDR` |
| `HybridBackupRecovery` | `from diagrams.alibabacloud.storage import HybridBackupRecovery` |
| `HybridCloudDisasterRecovery` | `from diagrams.alibabacloud.storage import HybridCloudDisasterRecovery` |
| `Imm` | `from diagrams.alibabacloud.storage import Imm` |
| `NAS` | `from diagrams.alibabacloud.storage import NAS` |
| `OSS` | `from diagrams.alibabacloud.storage import OSS` |
| `OTS` | `from diagrams.alibabacloud.storage import OTS` |
| `ObjectStorageService` | `from diagrams.alibabacloud.storage import ObjectStorageService` |
| `ObjectTableStore` | `from diagrams.alibabacloud.storage import ObjectTableStore` |

### Web

**Import:** `from diagrams.alibabacloud.web import ...`

| Class Name | Import Example |
|------------|---------------|
| `Dns` | `from diagrams.alibabacloud.web import Dns` |
| `Domain` | `from diagrams.alibabacloud.web import Domain` |

---

## GIS (Geospatial)

_Geospatial Information Systems tools and libraries_ — **65 icons** across **15 categories**

### CLI

**Import:** `from diagrams.gis.cli import ...`

| Class Name | Import Example |
|------------|---------------|
| `Gdal` | `from diagrams.gis.cli import Gdal` |
| `Imposm` | `from diagrams.gis.cli import Imposm` |
| `Lastools` | `from diagrams.gis.cli import Lastools` |
| `Mapnik` | `from diagrams.gis.cli import Mapnik` |
| `Mdal` | `from diagrams.gis.cli import Mdal` |
| `Pdal` | `from diagrams.gis.cli import Pdal` |

### C++

**Import:** `from diagrams.gis.cplusplus import ...`

| Class Name | Import Example |
|------------|---------------|
| `Mapnik` | `from diagrams.gis.cplusplus import Mapnik` |

### Data

**Import:** `from diagrams.gis.data import ...`

| Class Name | Import Example |
|------------|---------------|
| `BAN` | `from diagrams.gis.data import BAN` |
| `Here` | `from diagrams.gis.data import Here` |
| `IGN` | `from diagrams.gis.data import IGN` |
| `Openstreetmap` | `from diagrams.gis.data import Openstreetmap` |
| `Overturemaps` | `from diagrams.gis.data import Overturemaps` |

### Database

**Import:** `from diagrams.gis.database import ...`

| Class Name | Import Example |
|------------|---------------|
| `Postgis` | `from diagrams.gis.database import Postgis` |

### Desktop

**Import:** `from diagrams.gis.desktop import ...`

| Class Name | Import Example |
|------------|---------------|
| `Maptunik` | `from diagrams.gis.desktop import Maptunik` |
| `QGIS` | `from diagrams.gis.desktop import QGIS` |

### Format

**Import:** `from diagrams.gis.format import ...`

| Class Name | Import Example |
|------------|---------------|
| `Geopackage` | `from diagrams.gis.format import Geopackage` |
| `Geoparquet` | `from diagrams.gis.format import Geoparquet` |

### Geocoding

**Import:** `from diagrams.gis.geocoding import ...`

| Class Name | Import Example |
|------------|---------------|
| `Addok` | `from diagrams.gis.geocoding import Addok` |
| `Gisgraphy` | `from diagrams.gis.geocoding import Gisgraphy` |
| `Nominatim` | `from diagrams.gis.geocoding import Nominatim` |
| `Pelias` | `from diagrams.gis.geocoding import Pelias` |

### Java

**Import:** `from diagrams.gis.java import ...`

| Class Name | Import Example |
|------------|---------------|
| `Geotools` | `from diagrams.gis.java import Geotools` |

### JavaScript

**Import:** `from diagrams.gis.javascript import ...`

| Class Name | Import Example |
|------------|---------------|
| `Cesium` | `from diagrams.gis.javascript import Cesium` |
| `Geostyler` | `from diagrams.gis.javascript import Geostyler` |
| `Keplerjs` | `from diagrams.gis.javascript import Keplerjs` |
| `Leaflet` | `from diagrams.gis.javascript import Leaflet` |
| `Maplibre` | `from diagrams.gis.javascript import Maplibre` |
| `OlExt` | `from diagrams.gis.javascript import OlExt` |
| `Openlayers` | `from diagrams.gis.javascript import Openlayers` |
| `Turfjs` | `from diagrams.gis.javascript import Turfjs` |

### Mobile

**Import:** `from diagrams.gis.mobile import ...`

| Class Name | Import Example |
|------------|---------------|
| `Mergin` | `from diagrams.gis.mobile import Mergin` |
| `Qfield` | `from diagrams.gis.mobile import Qfield` |
| `Smash` | `from diagrams.gis.mobile import Smash` |

### OGC

**Import:** `from diagrams.gis.ogc import ...`

| Class Name | Import Example |
|------------|---------------|
| `OGC` | `from diagrams.gis.ogc import OGC` |
| `WFS` | `from diagrams.gis.ogc import WFS` |
| `WMS` | `from diagrams.gis.ogc import WMS` |

### Organization

**Import:** `from diagrams.gis.organization import ...`

| Class Name | Import Example |
|------------|---------------|
| `Osgeo` | `from diagrams.gis.organization import Osgeo` |

### Python

**Import:** `from diagrams.gis.python import ...`

| Class Name | Import Example |
|------------|---------------|
| `Geopandas` | `from diagrams.gis.python import Geopandas` |
| `Pysal` | `from diagrams.gis.python import Pysal` |

### Routing

**Import:** `from diagrams.gis.routing import ...`

| Class Name | Import Example |
|------------|---------------|
| `Graphhopper` | `from diagrams.gis.routing import Graphhopper` |
| `Osrm` | `from diagrams.gis.routing import Osrm` |
| `Pgrouting` | `from diagrams.gis.routing import Pgrouting` |
| `Valhalla` | `from diagrams.gis.routing import Valhalla` |

### Server

**Import:** `from diagrams.gis.server import ...`

| Class Name | Import Example |
|------------|---------------|
| `Actinia` | `from diagrams.gis.server import Actinia` |
| `Baremaps` | `from diagrams.gis.server import Baremaps` |
| `Deegree` | `from diagrams.gis.server import Deegree` |
| `G3WSuite` | `from diagrams.gis.server import G3WSuite` |
| `Geohealthcheck` | `from diagrams.gis.server import Geohealthcheck` |
| `Geomapfish` | `from diagrams.gis.server import Geomapfish` |
| `Geomesa` | `from diagrams.gis.server import Geomesa` |
| `Geonetwork` | `from diagrams.gis.server import Geonetwork` |
| `Geonode` | `from diagrams.gis.server import Geonode` |
| `Georchestra` | `from diagrams.gis.server import Georchestra` |
| `Geoserver` | `from diagrams.gis.server import Geoserver` |
| `Geowebcache` | `from diagrams.gis.server import Geowebcache` |
| `Kepler` | `from diagrams.gis.server import Kepler` |
| `Mapproxy` | `from diagrams.gis.server import Mapproxy` |
| `Mapserver` | `from diagrams.gis.server import Mapserver` |
| `Mapstore` | `from diagrams.gis.server import Mapstore` |
| `Mviewer` | `from diagrams.gis.server import Mviewer` |
| `Pg_Tileserv` | `from diagrams.gis.server import Pg_Tileserv` |
| `Pycsw` | `from diagrams.gis.server import Pycsw` |
| `Pygeoapi` | `from diagrams.gis.server import Pygeoapi` |
| `QGISServer` | `from diagrams.gis.server import QGISServer` |
| `Zooproject` | `from diagrams.gis.server import Zooproject` |

---

## Custom Icons

Use any local PNG/JPG image as a node icon:

```python
from diagrams.custom import Custom

# Use any local image file
my_service = Custom("My Service", "./path/to/icon.png")
```

---

## C4 Model Diagrams

The library also supports C4 model diagrams:

```python
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship
```

| Class | Description |
|-------|-------------|
| `Person` | A person (user, actor) |
| `Container` | A software container (app, service) |
| `Database` | A database |
| `System` | A software system |
| `SystemBoundary` | Boundary grouping containers |
| `Relationship` | Connection between elements |

---

*Auto-generated from the installed `diagrams` Python package.*
