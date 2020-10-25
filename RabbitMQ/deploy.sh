#!/bin/bash
chromium http://localhost:15672/
xterm -hold -e "docker-compose -f docker-compose-data.yml up" &
docker-compose -f docker-compose.yml up



