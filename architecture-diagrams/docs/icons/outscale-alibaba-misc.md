# Cloud Provider Icons - Outscale, Alibaba & Misc

Outscale, Alibaba Cloud, GIS, Custom icons, and C4 model components.

**Total:** ~220 icons + C4 components

**Import pattern:** `from diagrams.<provider>.<category> import <ClassName>`

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
