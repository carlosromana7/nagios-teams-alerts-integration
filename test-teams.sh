#!/bin/bash

# Script para probar notificaciones a Teams manualmente
WEBHOOK_URL="https://tu-webhook-url"
SUBJECT=$1
OUTPUT=$2

if [ -z "$SUBJECT" ] || [ -z "$OUTPUT" ]; then
    echo "Uso: $0 \"SUBJECT\" \"OUTPUT\""
    exit 1
fi

/usr/local/nagios/libexec/notify-teams.py "$SUBJECT" "$OUTPUT" "$WEBHOOK_URL"
