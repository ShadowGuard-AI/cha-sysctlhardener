![Banner](banner.png)

# cha-SysctlHardener
Validates a YAML or JSON configuration file against a hardening policy written as a JSON schema, and reports every setting that does not comply, with the schema failure for each one. It does not rewrite the configuration file: the report is the output, and a non-compliant configuration exits with status 1 so scripts can gate on it.

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
