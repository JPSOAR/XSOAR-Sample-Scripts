##Simple Ping Example
import json

ping_args = {
    "address" : "google.com"
}
ping_result = demisto.executeCommand("Ping", ping_args)

#Uncomment to print the Ping Command's response object.
#print(json.dumps(ping_result,indent=4))

#Capture just the IP from Ping Command's response object
ip = ping_result[0]["Contents"]["destination_ip"]

#print IP to warroom/playground
print(ip)

#Set the IP to context
demisto.setContext("CustomPing.IP",ip)