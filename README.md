![A quiet table after the last performance: a retired monkey cap on a folded programme, a ticket roll, carbon copies under a stamp pad, and a saucer of brass buttons, with no lettering anywhere](intro-banner.png)

> Day book entry treatment noted first: a ruled day book page, Baloo Chettan 2 in uniform navy on paper.

# cha-sysctlhardener

![A small navy monkey cap with a pale peak edge and one brass button at the side](logo.png)

![A table at the end of a day with the day book open at the front carrying the title as an entry](banner.png)

![A tabletop in three depths: the wall still, the day book turning one page at a long interval, and lamplight shifting from one brass button to its neighbour](scene.svg)


# cha-SysctlHardener
Validates a YAML or JSON configuration file against a hardening policy written as a JSON schema, and reports every setting that does not comply, with the schema failure for each one. It does not rewrite the configuration file: the report is the output, and a non-compliant configuration exits with status 1 so scripts can gate on it.

## Install
`git clone https://github.com/ShadowGuard-AI/cha-sysctlhardener`


![A major divider: a measuring tape unreeling across the full page width](sep-heavy.svg)

## Usage

> Carbon copy slip: Report Only, Never Rewritten. Every run reports and leaves the configuration file untouched, and a non compliant configuration exits 1 so scripts can gate on it.

`python3 main.py -c CONFIG_FILE -p POLICY_FILE [-n]`


![A minor divider: a centred short length of measuring tape](sep-light.svg)

## Parameters

> Carbon copy slip: The Dry Run Changes Nothing. The dry run flag does not change the output or the exit code, as the parameter line below states in full.

- `-h`: Show help message and exit
- `-c`, `--config`: Path to the configuration file (YAML or JSON). Required.
- `-p`, `--policy`: Path to the JSON schema policy file. Required.
- `-n`, `--dry-run`: Perform a dry run (show changes without applying them). Every run of this tool is report only, so this flag does not change the output or the exit code: a non-compliant configuration still exits 1 with this flag.


![A major divider: a measuring tape unreeling across the full page width](sep-heavy.svg)

## Verified behavior
- A compliant configuration exits 0.
- A non-compliant configuration exits 1 and reports the schema failure for each setting.
- A missing configuration file exits 1.


![A minor divider: a centred short length of measuring tape](sep-light.svg)

## License
See LICENSE.
