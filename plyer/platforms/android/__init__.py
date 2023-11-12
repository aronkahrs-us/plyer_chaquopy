from os import environ
from java import jclass as autoclass

ANDROID_VERSION = autoclass('android.os.Build$VERSION')
SDK_INT = ANDROID_VERSION.SDK_INT
	@@ -14,6 +48,6 @@
    PythonService = autoclass(ns + '.PythonService')
    activity = PythonService.mService
else:
    PythonActivity = autoclass(ns + '.PythonActivity')
    print(dir(PythonActivity))
    activity = PythonActivity
