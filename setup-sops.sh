#!/bin/bash
# setup
# run source setup-sops.sh arg1
# arg1 should be age public key

# Check for required arg1
if [ $# -eq 0 ]
    then
        echo "No arguments supplied"
        echo "example:\nsource setup-sops.sh age1ExampleRecipientPublicKey1"
fi

# Set SOPS age key file for decryption
unset SOPS_AGE_KEY_FILE
export SOPS_AGE_KEY_FILE=~/sops-key.txt

# Set SOPs age public key for encryption
unset SOPS_AGE_RECIPIENTS
export SOPS_AGE_RECIPIENTS=$1
