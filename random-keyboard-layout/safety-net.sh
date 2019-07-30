#!/bin/bash

COMMAND="setxkbmap de"

echo "Press ENTER to run '$COMMAND'"
echo "Interrupt (CTRL-C) 3 times to stop!"

trapped=0
trap_fn () {
  trapped="$((trapped+1))"
  echo "$trapped"
  if [ "$trapped" -ge 3 ]; then
    echo "bye"
    trap SIGINT
    exit 0
  fi
}
trap "trap_fn" SIGINT

while read _; do
  echo "$COMMAND"
  $COMMAND

done
