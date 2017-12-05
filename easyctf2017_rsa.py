#!/usr/bin/env python
# install libnum:
# apt-get install openssl
# apt-get install pyopenssl
# https://github.com/hellman/libnum, python setup.py install

import libnum

p = 33499881069427614105926941260008415630190853527846401734073924527104092366847259
q = 34311544767652906613104559081988349779622789386528780506962212898921316785995851
e = 65537
c = 43465248299278658712013216049003172427898782261990372316282214376041873514481386908793943532363461126240609464283533882761307749486816342864113338277082746552

n=p*q
phi=(p-1)*(q-1)
d = libnum.modular.invmod(e, phi)
print libnum.n2s(pow(c, d, n))


#easyctf{wh3n_y0u_h4ve_p&q_RSA_iz_ez_7829d89f}

rsa2.py
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
