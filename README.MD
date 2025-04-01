

**Cron Script for Sending Periodic GET Requests**
=====================================================

**Overview**
------------

This script sends periodic GET requests to a specified URL at a configurable interval. It is designed to be run as a cron job to ensure continuous monitoring of the target URL.

**Configuration**
-----------------

The script uses the following configuration variables:

* `URL`: The target URL to send GET requests to.
* `INTERVAL_MINUTES`: The interval in minutes between requests.
* `INTERVAL_SECONDS`: The interval in seconds between requests (calculated from `INTERVAL_MINUTES`).

**Usage**
---------

1. Set the `URL` variable to the desired target URL.
2. Set the `INTERVAL_MINUTES` variable to the desired interval between requests.
3. Save the script and make it executable (e.g., `chmod +x cron1.py`).
4. Add the script to your system's cron table to run at the desired interval (e.g., `crontab -e`).

**Example Cron Entry**
----------------------

To run the script every 5 minutes, add the following line to your cron table:
```bash
*/5 * * * * python /path/to/cron1.py
```
**Script Output**
-----------------

The script will print the timestamp and status of each request to the console. In case of errors, it will print an error message with the corresponding status code.

**Requirements**
---------------

* Python 3.x
* `requests` library (install with `pip install requests`)

**Notes**
-------

* The script uses a timeout of 15 seconds for each request. You can adjust this value by modifying the `timeout` parameter in the `requests.get()` call.
* The script catches and prints errors that occur during the request. You can modify the error handling to suit your needs.
