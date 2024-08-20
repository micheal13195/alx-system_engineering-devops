/Users/michealaderibigbe/Downloads/debug\ image.jpg 

Issue Summary

Duration of the Outage: The outage started at 03:30 AM and was resolved by 5:00 PM West African Time.

Effects:

The site was not listening on port 80, causing all users to be unable to access the website.

Root Cause:

The Nginx server's site settings were not properly linked. Specifically, the sites-available configuration was not linked to sites-enabled, meaning the configuration was correct but not activated, preventing users from accessing the site.

Timeline

03:30 AM: The issue was detected when ALX (the platform) attempted to access the website and found it unresponsive.

04:40 AM: ALX monitoring alerts indicated that the site was down, and the issue was escalated to me.

05:00 AM: Initial investigation focused on checking the Nginx configuration files for errors, but no errors were found in the configuration itself.

10:15 PM: Further investigation led to checking which service was listening on port 80. It was then discovered that the Nginx configuration in sites-available was not linked to sites-enabled.

11:30 PM: The default configuration was correctly linked in sites-enabled, and Nginx was restarted to apply the changes.

12:00 AM: The issue was resolved, and the site was back online.

Root Cause and Resolution

Root Cause:

The root cause was the failure to link the sites-available configuration to sites-enabled, meaning the Nginx server configuration was not active despite being correct.

Solution:

The issue was resolved by linking the default configuration from sites-available to sites-enabled and restarting the Nginx service.

Corrective and Preventative Measures

Improvements:

Ensuring that after any configuration changes, a script or automated check is run to confirm that the necessary configurations are linked and active. Improve the monitoring system to detect such issues earlier.

Task List:

Create and execute a script to link the sites-available configuration to sites-enabled after each configuration change. Add a monitoring check to ensure that Nginx is correctly listening on port 80.

Example Script

Here is the script i mentioned to ensure the configuration is always active:

[bash] (Copy code) #!/usr/bin/env bash

Ensure Nginx is properly configured and listening on port 80

cat /etc/nginx/sites-available/default > /etc/nginx/sites-enabled/default sudo service nginx restart

This script ensures that the correct configuration is enabled and restarts Nginx to apply the changes.


