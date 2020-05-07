# Snapshotalyzer

Manage AWS EC2 snapshots

# About

This project uses boto3 to manage AWS EC2 instance Snapshots

# Configuring

Shotty uses the configuration files created by the AWS Cli. e.g.
'aws configure --profile shotty'

# Running 

'Pipenv run "python shotty/shotty.py <command> <subcommand> <--project=PROJECT>"'

*command* is instances, volumes, or snapshots.
*subcommand* depends on command
*project* is optional
