#!/bin/bash
for f in loop/*.tex; do
    if [ -f "$f" ]; then
        tectonic -o loop "$f"
    fi
done
