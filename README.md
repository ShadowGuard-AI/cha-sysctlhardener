# cha-SysctlHardener
Applies secure sysctl settings based on a target operating system profile and a custom-defined hardening policy. Leverages `subprocess` to execute sysctl commands and `PyYAML` to define the hardening policy. - Focused on Applies security hardening recommendations to configuration files (e.g., YAML, JSON, INI).  Uses a library of security policies defined as JSON schemas.  Validates configuration files against these policies and provides remediation suggestions for non-compliant settings.  Supports version control integration (e.g., Git) to track changes and revert to previous states. Generates reports detailing configuration deviations and their potential security impact. Example use case: Hardening Linux systemd configurations.

## Install
`git clone https://github.com/ShadowStrikeHQ/cha-sysctlhardener`

## Usage
`./cha-sysctlhardener [params]`

## Parameters
- `-h`: Show help message and exit
- `-c`: No description provided
- `-p`: Path to the JSON schema policy file.
- `-n`: No description provided

## License
Copyright (c) ShadowStrikeHQ
