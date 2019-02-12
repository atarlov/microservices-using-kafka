#!/bin/bash

for i in {1..100}

 do docker exec -it bbc3a614b879 python prod.py -p 9092 -t new -m something$i
 echo $i

done
