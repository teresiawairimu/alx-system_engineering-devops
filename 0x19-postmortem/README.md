Postmortem: Apache 500 Error Due to Typo in WordPress Configuration
---

Issue Summary
1. Duration of Outage: 16-08-2024, 08:10PM - 08:30PM EAT (25 minutes)
2. Impact: The Apache Web server returned HTTP 500 Internal Server Error for all requests, causing the primary WordPress site to be inaccessible 100% of users were unable to access the site during the outage.
3.  Root Cause: The root cause was a typo in the 'wp-settings.php' file where a file extension was mistakenly written as '.phpp' instead of '.php'. This caused the 'require_once' function to fail, leading to the PHP script crashing and returning a 500 error.

---

Timeline

08:10PM EAT: Monitoring systems detected an increase in HTTP 500 errors from the Apache server, trigerring an alert.

08:13PM EAT: The on-call engineer received the alert and immediately began investigating by checking the Apache error logs, which pointed to a PHP issue.

08:15PM EAT: Upon activating WordPress debugging mode by modifying the 'wp-config.php' file, the engineer identified the exact error in the 'wp-settings.php' file, specifically a typo that caused a php warning.

08:17PM EAT: The engineer fixed the typo using a 'sed' command to replace '.phpp' with '.php' in the 'wp-settings.php' file.

08:19PM EAT: To ensure the issue wouldn't recur, the engineer created a Puppet manifest to automate the typo fix in case of future occurrences.

08:22PM EAT: The engineer tested PHP functionality by creating an 'info.php' file and confirmed the server was processing PHP file correctly.

08:25PM EAT: The engineer checked teh WordPress debug log to verify no other errors were present.

08:30PM EAT: The site was fully restored, and the incident was resolved.

Root Cause and Resolution

The 500 error was caused by a typo in the 'wp-settings.php' file, where teh 'require_once' statement attempted to include a non-existent file with the '.phpp' extension. This typo caused a fatal PHP error, resulting in the Apache server returning a 500 error.
The issue was resolved by running a 'sed' command to correct the extension from '.php'. This command was incorporated into a Puppet manifest to automate the fix and prevent future occurrences of similar issues. The successful execution of the Puppet script ensured that the typo was corrected and normal functionality was restored.

Corrective and Preventative Measures
Improvements/Fixes:
1. Implement a review process for critical configuration files to catch typos and errors before they go live
2. Use automation tools like Puppet to apply fixes consistently across environments and prevent manual errors.
3. Regularly activate and monitor WordPress debugging to catch potential issues early.

Tasks:
1. Deploy the Puppet Manifest to automatically correct the typo if it appears again.
2. Conduct a code review of all critical WordPress configuration files to identify and correct any other potential issues.
3. Add a pre-deployment script that checks for common typos and errors in WordPress files before deployment.
4. Enhance monitoring to alert on specific php errors that could lead to a 500 error, allowing for quicker detection and resolution
