## Project description
 
Python package for personal development

## Install

```
pip install venus-tools
```

## Usage

```
from PyAase import ead


# Change the sequence of strings after base64 encryption

enc_str = 'VmVudXM='

# _desc: A with Z(lowercase and so on) and 0 with 9...
re_enc_str = ead.clo(enc_str) 

print(re_enc_str) # EnEfwCN=

```



This is a simple package. There are still many imperfections.

Please give us your advice. I wish you all the best.
