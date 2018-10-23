
cat input | perl -p -E's/(.)\1{3,}/\1 \1/g' | ack -v "\[[a-z ]*([a-z])([a-z])\2\1[a-z ]*\]" | ack "([a-z])([a-z])\2\1" | wc -l
