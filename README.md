![Banner](banner.png)

# cha-SysctlHardener
Validates a YAML or JSON configuration file against a hardening policy written as a JSON schema, and reports every setting that does not comply, with the schema failure for each one. It does not rewrite the configuration file: the report is the output, and a non-compliant configuration exits with status 1 so scripts can gate on it.

## Install
`git clone https://github.com/ShadowGuard-AI/cha-sysctlhardener`

## Usage
`python3 main.py -c CONFIG_FILE -p POLICY_FILE [-n]`

## Parameters
- `-h`: Show help message and exit
- `-c`, `--config`: Path to the configuration file (YAML or JSON). Required.
- `-p`, `--policy`: Path to the JSON schema policy file. Required.
- `-n`, `--dry-run`: Perform a dry run (show changes without applying them). Every run of this tool is report only, so this flag does not change the output or the exit code: a non-compliant configuration still exits 1 with this flag.

## Verified behavior
- A compliant configuration exits 0.
- A non-compliant configuration exits 1 and reports the schema failure for each setting.
- A missing configuration file exits 1.

## License
See LICENSE.
