# Home Assistant CPU Temp

A simple script to query a Linux server for its current CPU temperature and report it to Home Assistant.

This repository contains 2 files:

- `cputemp.py` - This is the Python script that handles the collection of CPU temperature data and reporting to Home Assistant.
- `ha.yml` - This is an example Home Assistant Entity (to be placed in your HA's `configuration.yaml`) defintion for the CPU temperature entity.

## Setup

Before using the script, you must first obtain a long-lived token from your Home Assistant instance. See [this article](https://community.home-assistant.io/t/how-to-get-long-lived-access-token/162159/2) for details. 

Once the access token is acquired, you can setup the script. Modify the following lines in `cputemp.py`, replacing each with your Home Assistant URL and access token respectfully. 

```python
url = "http://hostname:8123/api/states/input_number.cpu_temp"
```

```python
# Replace ABCDEFG with your Long-lived access token
headers = {
  "Authorization": "Bearer ABCDEFG",
  "content-type": "application/json"
}
```

It is recommended to setup a cronjob to periodically report this information automatically, rather than running it manually. An (extremely rudimentary) example is provided below:

```
* * * * * /opt/cputemp.py
* * * * * (sleep 30 ; /opt/cputemp.py)
```

## Usage

```bash
./cputemp.py
```