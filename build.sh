#!/bin/sh
pex --disable-cache -r requirements.txt -v -e main -M main -P remindme -o build/remindme.pex