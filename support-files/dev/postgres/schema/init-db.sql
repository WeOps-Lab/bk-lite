-- 创建所需的数据库
CREATE DATABASE cmdb;
CREATE DATABASE metis;
CREATE DATABASE monitor;
CREATE DATABASE node_mgmt;
CREATE DATABASE "ops-console";
CREATE DATABASE system_mgmt;
CREATE DATABASE bklite;
CREATE DATABASE opspilot;


-- 为每个数据库设置默认用户权限
GRANT ALL PRIVILEGES ON DATABASE cmdb TO postgres;
GRANT ALL PRIVILEGES ON DATABASE metis TO postgres;
GRANT ALL PRIVILEGES ON DATABASE monitor TO postgres;
GRANT ALL PRIVILEGES ON DATABASE node_mgmt TO postgres;
GRANT ALL PRIVILEGES ON DATABASE "ops-console" TO postgres;
GRANT ALL PRIVILEGES ON DATABASE system_mgmt TO postgres;
GRANT ALL PRIVILEGES ON DATABASE bklite TO postgres;
GRANT ALL PRIVILEGES ON DATABASE opspilot TO postgres;
