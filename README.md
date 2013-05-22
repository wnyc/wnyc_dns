WNYC_DNS
========

A very simple utility to perform bulk changes against Rackspace's DNS
service.

wnyc_dns will support multiple subcommands; currently only update_ip_addresses is implemented

Bulk IP Address Change
----------------------

To change all of the IP addresses from 1.2.3.4 to 4.3.2.1 while excluding any definitions whose names starta with host1, host2 or host3

    wnyc_dns --live --username=<username> --apikey=<secret>    update_ip_addresses A:1.2.3.4 A:4.3.2.1  host1 host2 host3




