'''
Android MULTI
---------------------
'''

from plyer.facades import MULTI
from java import dynamic_proxy
from java import jclass as autoclass
from java import cast as cast
from java import method as java_method
from plyer.platforms.android import activity
from android.hardware import SensorEventListener

Context = autoclass('android.content.Context')
Sensor = autoclass('android.hardware.Sensor')
SensorManager = autoclass('android.hardware.SensorManager')

class MULTISensorListener(dynamic_proxy(SensorEventListener)):
    __javainterfaces__ = ['android/hardware/SensorEventListener']

    def __init__(self):
        super(AccelerometerSensorListener, self).__init__()
        self.SensorManager = cast(
            autoclass('android.hardware.SensorManager'),
            activity.getSystemService(Context.SENSOR_SERVICE)
        )
        self.sensor_acc = self.SensorManager.getDefaultSensor(
            Sensor.TYPE_LINEAR_ACCELERATION
        )
        self.sensor_gyro = self.SensorManager.getDefaultSensor(
            Sensor.TYPE_GYROSCOPE
        )

        self.acc = [None, None, None]
        self.gyro = [None, None, None]

    def enable(self):
        self.SensorManager.registerListener(
            self, self.sensor_acc,
            SensorManager.SENSOR_DELAY_FASTEST
        )
        self.SensorManager.registerListener(
            self, self.sensor_gyro,
            SensorManager.SENSOR_DELAY_FASTEST
        )

    def disable(self):
        self.SensorManager.unregisterListener(self, self.sensor_acc)
        self.SensorManager.unregisterListener(self, self.sensor_gyro)
        
    def onSensorChanged(self, event):
        if event.sensor.getType() == Sensor.TYPE_ACCELEROMETER:
            self.acc = event.values[:3]
        elif event.sensor.getType() == Sensor.TYPE_GYROSCOPE:
            self.gyro = event.values[:3]

    def onAccuracyChanged(self, sensor, accuracy):
        # Maybe, do something in future?
        pass


class AndroidMULTI(MULTI):
    def __init__(self):
        super().__init__()
        self.bState = False

    def _enable(self):
        if (not self.bState):
            self.listener = MULTISensorListener()
            self.listener.enable()
            self.bState = True

    def _disable(self):
        if (self.bState):
            self.bState = False
            self.listener.disable()
            del self.listener

    def _get_acceleration(self):
        if (self.bState):
            return tuple(self.listener.acc)
        else:
            return (None, None, None)
            
    def _get_orientation(self):
        if (self.bState):
            return tuple(self.listener.gyro)
        else:
            return (None, None, None)

    def __del__(self):
        if self.bState:
            self._disable()
        super().__del__()


def instance():
    return AndroidMULTI()
