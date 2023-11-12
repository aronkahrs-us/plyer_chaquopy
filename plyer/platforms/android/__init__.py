from os import environ
from java import jclass as autoclass
from com.ak.geosmartphone.geosmartphone import R;

ANDROID_VERSION = autoclass('android.os.Build$VERSION')
SDK_INT = ANDROID_VERSION.SDK_INT

try:
    from android import config
    ns = config.JAVA_NAMESPACE
except (ImportError, AttributeError):
    ns = 'org.beeware.android'

if 'PYTHON_SERVICE_ARGUMENT' in environ:
    PythonService = autoclass(ns + '.PythonService')
    activity = PythonService.mService
else:
    PythonActivity = autoclass(ns + '.PythonActivity')
    activity = PythonActivity.mActivity
    print(PythonActivity,activity)
    print(activity)
    print(dir(PythonActivity))
