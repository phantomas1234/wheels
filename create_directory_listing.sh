#!/bin/bash

echo "<ol>" > index.html
for i in `ls *.whl`; do echo "<li><a href='$i'>$i</a></li>" >> index.html; done
echo "</ol>" >> index.html