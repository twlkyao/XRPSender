About
=====

Script to send XRP to the public address of your choice.
You need python and requests installed ;)

Usage
=====


    Usage:
    ------
    
        * python XRPSender.py [service] [secret] [from_addr] [to_addr] [amount]
    
    Variables:
    ----------
    
        * service   = https://s1.ripple.com:51234/
        * secret    = spz7x7vjAgU1JuBcgabx8MmgNzLg7
        * from_addr = rMmTCjGFRWPz8S2zAUUoNVSQHxtRQD4eCx
        * to_addr   = rKjGXUc8uyY8FCkMXdqfDNVeJFnJVqabkw
        * amount    = 1000

    $ python XRPSender.py https://s1.ripple.com:51234/ spz7x7vjAgU1JuBcgabx8MmgNzLg7 rMmTCjGFRWPz8S2zAUUoNVSQHxtRQD4eCx rBYJAUMJN4di2EZUTHZ52TfCfzszAEXTG8 100000
    You're going to send 100000 XRP to rBYJAUMJN4di2EZUTHZ52TfCfzszAEXTG8
    Do you confirm this transaction? [yes/no] y
    XRP sent ;)
