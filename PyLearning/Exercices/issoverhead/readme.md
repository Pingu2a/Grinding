# ISS Overhead Notifier
This project is an automated tracking and notification system designed to alert you when the International Space Station (ISS) is flying over your current location. It fetches real-time orbital data and local astronomical times to dispatch an email notification only if the ISS is visible (overhead and during nighttime).

This project focuses on API integration, geographical coordinate validation, and implementing the SMTP protocol for automated network alerts.

## Sources:
[Open Notify ISS API](http://open-notify.org/Open-Notify-API/)

[Sunrise Sunset API](https://sunrise-sunset.org/api)

[Python smtplib documentation](https://docs.python.org/3/library/smtplib.html)

## How to try
Ensure you have the `requests` library installed in your virtual environment. Update the `MY_LAT`, `MY_LONG`, `MY_EMAIL`, and `MY_PASSWORD` variables with your specific coordinates and credentials, then run the script.

**Result**: The script will run in the background, checking every 60 seconds. If the ISS is within +5/-5 degrees of your position and it is currently dark outside at your location, an email will be sent to your inbox.

## Logic
**1. Real-Time API Data Fetching**

The script uses the `requests` library to communicate with external APIs. It performs a `GET` request to retrieve the current latitude and longitude of the ISS in a **JSON** format, which is then parsed into Python floats for comparison.

**2. Coordinate Proximity Validation**

A custom function, `is_iss_overhead()`, calculates if the user's position is within a specific range (+5 or -5 degrees) of the ISS. This creates a virtual "window" in the sky, ensuring the notification only triggers when the station is reasonably close to the observer.

**3. Astronomical Time Comparison**

By querying the Sunrise-Sunset API with local coordinates, the script retrieves the exact UTC times for dawn and dusk. It uses `.split()` and string slicing to isolate the hour, allowing the script to determine if the current time qualifies as "night," a requirement for spotting the ISS with the naked eye.

**4. Automated Polling Loop**

The script implements a `while True` loop combined with `time.sleep(60)`. This ensures the program constantly monitors the sky without overwhelming the APIs or the CPU, checking for the required conditions once every minute.

**5. Secure SMTP Connection**

For the notification phase, the script initiates an **SMTP** session with Gmail's servers. It utilizes `connection.starttls()` to secure the transmission via **TLS** (Transport Layer Security) before performing the login and dispatching the payload.

**6. Conditional Execution Logic**

The email is only sent if a double boolean check returns `True`: the ISS must be overhead AND it must be night. This prevents unnecessary emails during the day when the ISS is invisible due to sunlight.