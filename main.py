import argparse
import json
import logging
import os
import subprocess
import sys
from typing import Dict, List

import jsonschema
import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class ConfigHardener:
    """
    A class for hardening configuration files based on JSON schema policies.
    """

    def __init__(self, config_file: str, policy_file: str, dry_run: bool = False):
        """
        Initializes the ConfigHardener.

        Args:
            config_file: Path to the configuration file to harden.
            policy_file: Path to the JSON schema policy file.
            dry_run: If True, only show changes without applying them.
        """
        self.config_file = config_file
        self.policy_file = policy_file
        self.dry_run = dry_run
        self.config_data = None
        self.policy_schema = None

    def load_config(self) -> None:
        """
        Loads the configuration file (YAML or JSON).
        """
        try:
            with open(self.config_file, "r") as f:
                if self.config_file.endswith((".yaml", ".yml")):
                    self.config_data = yaml.safe_load(f)
                elif self.config_file.endswith(".json"):
                    self.config_data = json.load(f)
                else:
                    raise ValueError(
                        "Unsupported configuration file format. Only YAML and JSON are supported."
                    )
        except FileNotFoundError:
            logging.error(f"Configuration file not found: {self.config_file}")
            sys.exit(1)
        except yaml.YAMLError as e:
            logging.error(f"Error parsing YAML configuration: {e}")
            sys.exit(1)
        except json.JSONDecodeError as e:
            logging.error(f"Error parsing JSON configuration: {e}")
            sys.exit(1)
        except Exception as e:
            logging.error(f"Error loading configuration file: {e}")
            sys.exit(1)

    def load_policy(self) -> None:
        """
        Loads the JSON schema policy file.
        """
        try:
            with open(self.policy_file, "r") as f:
                self.policy_schema = json.load(f)
        except FileNotFoundError:
            logging.error(f"Policy file not found: {self.policy_file}")
            sys.exit(1)
        except json.JSONDecodeError as e:
            logging.error(f"Error parsing JSON policy: {e}")
            sys.exit(1)
        except Exception as e:
            logging.error(f"Error loading policy file: {e}")
            sys.exit(1)

    def validate_config(self) -> List[str]:
        """
        Validates the configuration against the policy schema.

        Returns:
            A list of validation errors.
        """
        try:
            jsonschema.validate(instance=self.config_data, schema=self.policy_schema)
            return []  # No errors
        except jsonschema.ValidationError as e:
            return [str(e)]
        except Exception as e:
            logging.error(f"Error during validation: {e}")
            return [str(e)]

    def remediate_config(self) -> None:
        """
        Remediates non-compliant settings based on the policy. This is a placeholder.
        In a real-world scenario, this would contain logic to modify the
        configuration file based on the validation errors and the remediation
        strategies defined in the policy. For example, it might update specific
        values, add missing keys, or remove insecure settings.

        This simplified version just prints remediation suggestions.
        """
        errors = self.validate_config()
        if errors:
            logging.warning(
                "Configuration validation failed. Remediation suggestions:"
            )
            for error in errors:
                logging.warning(f"  - {error}")
                # In a real implementation, apply changes here based on the error
                # and the policy's remediation instructions.
                # Example:
                #   if "required property 'secure_setting'" in error:
                #       self.config_data["secure_setting"] = True
                #   ...
        else:
            logging.info("Configuration is compliant with the policy.")

        if self.dry_run:
            logging.info("Dry run: No changes will be applied.")
            logging.info("Remediation suggestions (if any) are for informational purposes.")
        else:
            if errors: # only write if there were errors
                logging.info("Applying changes (simulated in this example).")
                # In a real implementation, write the modified configuration back to file
                # with open(self.config_file, "w") as f:
                #    yaml.dump(self.config_data, f)  # or json.dump(self.config_data, f)
            else:
                logging.info("No changes needed.")

    def run(self) -> None:
        """
        Runs the hardening process.
        """
        self.load_config()
        self.load_policy()
        self.remediate_config()


def setup_argparse() -> argparse.ArgumentParser:
    """
    Sets up the command-line argument parser.

    Returns:
        An argparse.ArgumentParser object.
    """
    parser = argparse.ArgumentParser(
        description="Applies security hardening recommendations to configuration files."
    )
    parser.add_argument(
        "-c",
        "--config",
        dest="config_file",
        required=True,
        help="Path to the configuration file (YAML or JSON).",
    )
    parser.add_argument(
        "-p",
        "--policy",
        dest="policy_file",
        required=True,
        help="Path to the JSON schema policy file.",
    )
    parser.add_argument(
        "-n",
        "--dry-run",
        dest="dry_run",
        action="store_true",
        help="Perform a dry run (show changes without applying them).",
    )
    return parser


def main() -> None:
    """
    Main function to parse arguments and run the config hardener.
    """
    parser = setup_argparse()
    args = parser.parse_args()

    # Input validation - basic file existence check
    if not os.path.exists(args.config_file):
        logging.error(f"Config file does not exist: {args.config_file}")
        sys.exit(1)

    if not os.path.exists(args.policy_file):
        logging.error(f"Policy file does not exist: {args.policy_file}")
        sys.exit(1)

    hardener = ConfigHardener(args.config_file, args.policy_file, args.dry_run)
    hardener.run()


if __name__ == "__main__":
    main()

# Example usage:
# 1. Create a sample config.yaml:
#
# secure_setting: false
# insecure_setting: "unsafe_value"
#
# 2. Create a sample policy.json:
#
# {
#   "type": "object",
#   "properties": {
#     "secure_setting": { "type": "boolean", "const": true },
#     "insecure_setting": { "type": "string", "const": "safe_value" }
#   },
#   "required": ["secure_setting", "insecure_setting"]
# }
#
# 3. Run the script:
# python your_script_name.py -c config.yaml -p policy.json
#
# 4. Run in dry-run mode:
# python your_script_name.py -c config.yaml -p policy.json -n

# Example of offensive tools integration (simulated):
# In a real-world scenario, after hardening, you could run tools like:
# - Lynis: To perform a security audit and verify the hardening.
# - CIS Benchmarks: To assess compliance with CIS security standards.
# These tools would be executed using `subprocess`, and their output
# would be parsed to identify any remaining vulnerabilities.