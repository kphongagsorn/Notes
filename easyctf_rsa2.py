
#!/usr/bin/env python
# install libnum:
# apt-get install openssl
# apt-get install pyopenssl
# https://github.com/hellman/libnum, python setup.py install


import libnum

n = 266965481915457805187702917726550329693157 #find p and q; http://factordb.com/index.php?query=266965481915457805187702917726550329693157
p = 458070420083487550883
q = 582804455845022449879
e = 65537
c = 78670065603555615007383828728708393504251

n=p*q
phi=(p-1)*(q-1)
d = libnum.modular.invmod(e, phi)

print libnum.n2s(pow(c, d, n))
