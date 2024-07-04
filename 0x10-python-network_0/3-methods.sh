#!/bin/bash
# prend une URL en entrée et affiche toutes les méthodes HTTP que le serveur accepte
curl -s -I "$1" | grep "Allow:" | cut -d " " -f 2-
