ranges=$(awk '{match($0, /[0-9]+\.[0-9]+\.[0-9]+\.*[0-9]+\/[0-9]+/); print substr($0, RSTART, RLENGTH)}' $1)
for range in $ranges; do
echo "scanning range "$range" for "$1;
nam=$(echo ${range::-3})
nmap -p443 --script $1 -Pn -v -oX $nam.txt $range
done
