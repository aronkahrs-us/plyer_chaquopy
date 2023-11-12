from os import environ
from java import jclass as autoclass

ANDROID_VERSION = autoclass('android.os.Build$VERSION')
SDK_INT = ANDROID_VERSION.SDK_INT

PythonActivity = autoclass('org.beeware.android.PythonActivity')
print(dir(PythonActivity))
activity = PythonActivity
