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
    activity = PythonActivity
    print(PythonActivity)
    print(dir(PythonActivity))
    Context = autoclass("android.content.Context")
    vibrator_service = activity.getSystemService(Context.VIBRATOR_SERVICE)
    vibrator = cast("android.os.Vibrator", vibrator_service)
    print(Context)
    print(vibrator_service)
    print(vibrator)
