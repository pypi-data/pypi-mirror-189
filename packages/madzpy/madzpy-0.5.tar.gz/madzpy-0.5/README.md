# madz-py
madzpy is a rpc and api wrapper.

First, install it:
```
python3 setup.py install
```

All commands interfacing with the node need to use an Instance of `madz()`

To create a new instance, run:
```
import madzpy

madz = madzpy.madz()
```
Here are some commands you can use:
```
#                      Private key               From            To            Amount
print(madz.transaction("XXXXXXXXXXXXXXXXXXXXXX", "0x4ba...b313", "0xbd...164", 1))
# returns False 

#                  Address
print(madz.balance("0x4ba...b313"))

#                     Address
print(madz.is_address("0x4ba...b313"))

```

Better docs soon™

If you face any issues, file a issue on Github.

If you want to support the developer, send, Madz, BNB, MATIC or ETH to the following address:
```0xAFDfedC5311218B636EEbe3837C489c3BeAcFfB4```

This code is released under MIT License.
