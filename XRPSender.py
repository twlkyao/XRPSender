#!/usr/bin/env python

""" Script to send XRP to the public address of your choice """

__author__      = "Hurukan"
__copyright__   = "Copyright 2013, XRP Talk"

import json
import requests
import sys


##############
# XRP Sender #
##############

def XRPSender(service, secret, account, destination, amount):

    # Service

    if not service:
        print "[XRPSender]{error} No service"
        return False

    # Secret

    if not secret:
        print "[XRPSender]{error} No secret key"
        return False

    # Account - From

    if not account:
        print "[XRPSender]{error} No account"
        return False

    # Destination - To

    if not destination:
        print "[XRPSender]{error} No destination"
        return False

    # Amount

    if not amount:
        print "[XRPSender]{error} No amount"
        return False

    try:
        normalized_amount = float(amount) * 1000000
        normalized_amount = str(int(normalized_amount))
    except Exception, err:
        print "[XRPSender]{exception} Invalid amount: %s" % err
        return False

    # Create a Signed Request

    signed_request = { "method" : "sign", 
                       "params": [ { "secret": secret,
                                     "tx_json" : {
                                        "TransactionType" : "Payment",
                                        "Account" : account,
                                        "Destination" : destination,
                                        "Amount" : normalized_amount
                                        },
                             } ]
                      }
    
    # Send the Signed Request to the Service

    try:
        response = requests.post(service, data=json.dumps(signed_request))
        signed_response = json.loads(response.text)
    except Exception, err:
        print "[XRPSender]{exception} %s" % err
        return False

    # Result

    if not "result" in signed_response:
        print "[XRPSender]{error} No result in the signed response"
        return False

    # Status

    if not "status" in signed_response["result"]:
        print "[XRPSender]{error} No status in the signed response"
        return False

    if signed_response["result"]["status"] != "success":
        if "error_message" in signed_response["result"]:
            print "[XRPSender]{error} Error in the signed response: %s" % signed_response["result"]["error_message"]
        else:
            print "[XRPSender]{error} Error in the signed response"      
        return False

    # Tx Blob

    if not "tx_blob" in signed_response["result"]:
        print "[XRPSender]{error} No Tx Blob"
        return False

    tx_blob = signed_response["result"]["tx_blob"]

    # Validation

    print "You're going to send %s XRP to %s" % (amount, destination)

    while True:
        validation = raw_input("Do you confirm this transaction? [yes/no] ")
        if validation in ('y', 'ye', 'yes'):
            break
        if validation in ('n', 'no'):
            return False

    # Create a Submit Tx

    submit_tx = { "method" : "submit", "params": [ { "tx_blob": tx_blob } ] }    

    # Send the Submit Tx

    try:
        response = requests.post(service, data=json.dumps(submit_tx))
        submitted_response = json.loads(response.text)
    except Exception, e:
        print "[XRPSender]{exception} %s" % e
        return False

    if submitted_response["result"]["status"] != "success":
        if "error_message" in submitted_response["result"]:
            print "[XRPSender]{error} Error in the submitted response: %s" % submitted_response["result"]["error_message"]
        else:
            print "[XRPSender]{error} Error in the submitted response"      
        return False

    print "XRP sent ;)"

    return True


########
# Main #
########

if __name__ == "__main__":

    # Usage

    if len(sys.argv) != 6:
        print ""
        print "Usage:"
        print "------"
        print ""
        print "    * python XRPSender.py [service] [secret] [from_addr] [to_addr] [amount]"
        print ""
        print "Variables:"
        print "----------"
        print ""
        print "    * service   = https://s1.ripple.com:51234/"
        print "    * secret    = spz7x7vjAgU1JuBcgabx8MmgNzLg7"
        print "    * from_addr = rMmTCjGFRWPz8S2zAUUoNVSQHxtRQD4eCx"
        print "    * to_addr   = rKjGXUc8uyY8FCkMXdqfDNVeJFnJVqabkw"
        print "    * amount    = 1000"
        print ""
        sys.exit(1)

    XRPSender(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
