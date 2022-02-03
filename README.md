# config_deployer

Generating interfaces config from jinja2 template and upload to the box. Based on [nornir](https://github.com/nornir-automation/nornir) framework with [scrali](https://github.com/carlmontanari/scrapli) for device communication.

inventory/defaults.yml - credentials
inventory/groups.yml - connection parameters
inventory/hosts.yml - device list with variables for using durinig template generation
