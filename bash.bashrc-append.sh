curl "http://localhost:8080/newShell" \
-H "Accept: application/json" \
-H "Content-Type:application/json" \
--data @<(cat <<EOF
{
  "user": "$USER",
  "PID": $$
  }
EOF
)