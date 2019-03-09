Google Authenticator Extract Tool
=================================

This tool extracts a page of TOTP QR codes (and other information)
from a Google Authenticator database file.

Acquiring a database file
-------------------------

The file is `/data/data/com.google.android.apps.authenticator2/databases/databases`
on your Android device, but it is not accessible by regular means.

* On an unrooted, unmodified device there's essentially no way to get at it.

* On an unrooted, unlocked device you can install the TWRP recovery, use Advanced > File Manager to copy the file into `/sdcard`.  You can then pull it using `adb pull`, or manage it using your device's file manager.

* On a rooted device, you can simply `adb root` and `adb pull` the file.

Usage
-----

* Install Python 3.6+, the `qrcode` library and the PIL library.
* Run `python extract.py databases > otp.html` (or if you've renamed the database file, adapt accordingly).
* Open `otp.html` for a listing of QR codes you can use to set up other OTP apps.
