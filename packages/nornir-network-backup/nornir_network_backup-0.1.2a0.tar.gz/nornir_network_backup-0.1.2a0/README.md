# nornir-network-backup

A nornir playbook to store network equipment config backups and relevant "show" command facts.

You can define the main configuration backup command or fact commands per device type.

This backup tool uses Netmiko for connecting to devices and Textfsm to parse facts.

Requirements:

- nornir
- nornir-utils
- nornir-netmiko

> This is a beta version. Extra options and documentation will follow soon !

## Function

- take the running config of 1 or more hosts and save it to a file
  - the file will be overwritten every day
  - optional take a diff of the previous file and save it as well
- run "show" commands and save each output to a separate file in a facts folder
  - files will be overwritten every time
  - all files in a single facts folder
  - save a file with meta data: info about the last backup time, commands executed, failed + successful commands
  - the commands may change depending on vendor or hw type or software
  - commands which can be parsed with textfsm will be saved as YAML, if they cannot be parsed then it will be .config text files
- it should be possible to run the backup file for a single host
- or run agains a complete file
- generate an overall report with:
  - last run time
  - hosts succeeded
  - hosts failed
  - hosts skipped

## Output folder structure

```text
|- backup folder
|  |-- facts folder
|  |-- reports folder  
```

## Commands

```shell
nnb backup
nnb backup-single-host
```

## Usage

```shell
poetry run nnb backup-single-host
```

## Environment Variables

Used by nornir_utils.plugins.inventory.load_credentials transform function, in case username + password are not defined by CLI

NORNIR_USERNAME

NORNIR_PASSWORD
