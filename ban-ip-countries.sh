COUNTRIES=('cn' 'tw' 'ru' 'in' 'br')
ipset flush countries
for i in "${COUNTRIES[@]}"; do
    echo "Ban IP of country ${i}"

    for IP in $(wget --no-check-certificate -O - https://www.ipdeny.com/ipblocks/data/countries/${i}.zone)
    do
        ipset add countries $IP;
    done
done
