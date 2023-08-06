## Usage

**A good tool for checking host, has 24+ servers from different countries to check. Using check-host.net**

```python
#ping server www.google.com
>>> from hostcheck import *
>>> host.ping("www.google.com")
saved as: check-host.json
>>> 

#check http server www.google.com
>>> from hostcheck import *
>>> host.http("www.google.com")
saved as: check-host.json
>>> 

#check tcp server 3.125.102.39:13352
>>> from hostcheck import *
>>> host.tcp("3.125.102.39:13352")
saved as: check-host.json
>>> 

```

**all results are automatically saved to the check-host file in json format.  You can read it using the json module.**

## Installation

```basb
pip install hostcheck

```

## Maybe will be in new versions

 - dns checker 
 - udp checker

