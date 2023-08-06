## Project description
 
Python package for personal development

## Install

```
pip install PyAase
```

## Usage

```
from PyAase import ead

# Change the sequence of strings after base64 encryption
temp1 = ead.enc_base64('Aase')
print(temp1)  # QWFzZQ==
temp2 = ead.dec_base64(temp1)
print(temp2)  # Aase

# clo: A with Z(lowercase and so on) and 0 with 9...
clo_temp1 = ead.clo(temp1)
print(clo_temp1)  # JDUaAJ==

clo_temp2 = ead.clo(clo_temp1)
print(clo_temp2)  # QWFzZQ==
```



This is a simple package. There are still many imperfections.

Please give us your advice. I wish you all the best.
