#!/usr/bin/env python3
#Autor:  Carlos Romaña
import argparse
import json
import requests
import sys

def add_emoji_to_subject(subject):
    """Agrega emojis al INICIO del subject según el estado"""
    subject_upper = subject.upper()
    if "RECOVERY" in subject_upper or "UP" in subject_upper or "OK" in subject_upper:
        return "✅ " + subject
    elif "PROBLEM" in subject_upper and ("DOWN" in subject_upper or "CRITICAL" in subject_upper):
        return "❌ " + subject
    elif "WARNING" in subject_upper:
        return "⚠️ " + subject
    else:
        return "ℹ️ " + subject

def create_message(url, subject, output, long_message=None):
    """Crea el diccionario para la tarjeta de Teams"""
    message = {}

    # Agrega emoji al inicio del título
    subject_with_emoji = add_emoji_to_subject(subject)

    message['summary'] = subject_with_emoji
    message['title'] = subject_with_emoji
    message['text'] = output

    if long_message:
        message['text'] += '\n\n' + long_message

    message['@type'] = 'MessageCard'
    message['@context'] = 'https://schema.org/extensions'

    return message

def send_to_teams(url, message_json):
    """Envía la tarjeta a Teams vía webhook"""
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, data=message_json, headers=headers)
    if r.status_code == requests.codes.ok:
        print('success')
        return True
    else:
        print('failure')
        return False

def main(args):
    url = args.get('url')
    if url is None:
        print('error no url')
        exit(2)

    subject = args.get('subject')
    output = args.get('output')
    long_message = args.get('long_message')

    message_dict = create_message(url, subject, output, long_message)
    message_json = json.dumps(message_dict)

    send_to_teams(url, message_json)

if __name__ == '__main__':
    args = {}

    parser = argparse.ArgumentParser()
    parser.add_argument('subject', action='store', help='message subject')
    parser.add_argument('output', action='store', help='output of the check')
    parser.add_argument('url', action='store', help='teams connector webhook url')

    parsedArgs = parser.parse_args()

    args['subject'] = parsedArgs.subject
    args['url'] = parsedArgs.url
    args['output'] = parsedArgs.output

    if not sys.stdin.isatty():
        stdin_data = sys.stdin.read().strip()
        if stdin_data:
            args['long_message'] = stdin_data

    main(args)
