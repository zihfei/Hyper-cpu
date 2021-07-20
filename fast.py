print("fast")
Acpu = int(input("Enter Acpu"))
print(Acpu)
ALimt = int(input("Enter ALimt"))
print(ALimt)
Bcpu = int(input("Enter Bcpu"))
print(Bcpu)
BLimt = int(input("Enter BLimt"))
print(BLimt)
Ccpu = int(input("Enter Ccpu"))
print(Ccpu)
CLimt = int(input("Enter CLimt"))
print(CLimt)
if Bcpu > BLimt :
    if Acpu < ALimt:
        ALimt = ALimt - Bcpu  + BLimt - Acpu
        if ALimt > 0 :
            print(ALimt)
            print("bcpu use alimt")
        else:
            ALimt = ALimt + CLimt - Ccpu 
            print(ALimt)
            print("bcpu use alimt and climt")
    else:
        CLimt = CLimt - Bcpu  + BLimt - Ccpu
        if CLimt > 0 :
            print(CLimt)
            print("bcpu use climt")
        else:
            print("bcpu use base")
elif Acpu > ALimt:
    if Bcpu < BLimt:
        BLimt = BLimt - Acpu  + ALimt
        if BLimt > 0 :
            print(BLimt)
            print("acpu use blimt")
        else:
            BLimt = BLimt + CLimt - Ccpu
            print(BLimt)
            print("acpu use blimt and climt")
    else:
        CLimt = CLimt - Acpu  + ALimt
        if CLimt > 0 :
            print(CLimt)
            print("acpu use climt")
        else:
            print("acpu use base")
elif Ccpu > CLimt:
    if Bcpu < BLimt:
        BLimt = BLimt - Ccpu  + CLimt
        if BLimt > 0 :
            print(BLimt)
            print("ccpu use blimt")
        else:
            BLimt = BLimt + ALimt - Acpu
            print(BLimt)
            print("ccpu use blimt and alimt")
    else:
        ALimt = ALimt - Ccpu  + CLimt
        if ALimt > 0 :
            print(ALimt)
            print("ccpu use alimt")
        else:
            print("ccpu use base")
else:
    print("every one good")