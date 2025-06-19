# Earthquake_Notification_System-Global-
A simple Python-based system that monitors live earthquake data feeds (USGS) and sends real-time SMS alerts for new earthquake events. The project uses Flask for the server, threading for continuous data polling, and integrates with an SMS service Twilio to notify users of significant seismic activity.

#Customization
Polling Interval: You can adjust how often the system checks for new events (poll_interval in seconds).
Feed URL: Currently using USGS feed you can modify for regional sources.

#Future Improvements
1)User preferences for magnitude thresholds and region filtering
2)Logging and dashboard
3)Support for other disaster alerts (floods, storms, etc.)
