from os import environ
from java import dynamic_proxy, jboolean, jvoid, Override, static_proxy
from java import jclass as autoclass
from androidx.appcompat.app import AppCompatActivity
from android.os import Bundle
from android.graphics.drawable import ColorDrawable
from android.view import Menu, MenuItem, View
from com.ak.geosmartphone.geosmartphone import R
class UIDemoActivity(static_proxy(AppCompatActivity)):
    @Override(jvoid, [Bundle])
    def onCreate(self, state):
        AppCompatActivity.onCreate(self, state)
        if state is None:
            state = Bundle()

    @Override(jvoid, [Bundle])
    def onSaveInstanceState(self, state):
        state.putInt("source_visibility", self.wvSource.getVisibility())
        state.putInt("title_color", self.title_drawable.getColor())

    @Override(jboolean, [Menu])
    def onCreateOptionsMenu(self, menu):
        self.getMenuInflater().inflate(R.menu.view_source, menu)
        return True

    @Override(jboolean, [MenuItem])
    def onOptionsItemSelected(self, item):
        id = item.getItemId()
        if id == R.id.menu_source:
            vis = self.wvSource.getVisibility()
            new_vis = View.VISIBLE if (vis == View.GONE) else View.GONE
            self.wvSource.setVisibility(new_vis)
            return True
        else:
            return False


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
    PythonActivity = UIDemoActivity()
    print(dir(PythonActivity))
    activity = PythonActivity
