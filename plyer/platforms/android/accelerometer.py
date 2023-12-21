'''
Android accelerometer
---------------------
'''

from plyer.facades import Accelerometer
from java import dynamic_proxy
from java import jclass as autoclass
from java import cast as cast
from java import method as java_method
from plyer.platforms.android import activity
from android.hardware import SensorEventListener

Context = autoclass('android.content.Context')
Sensor = autoclass('android.hardware.Sensor')
SensorManager = autoclass('android.hardware.SensorManager')

class AccelerometerSensorListener(dynamic_proxy(SensorEventListener)):
    __javainterfaces__ = ['android/hardware/SensorEventListener']

    def __init__(self):
        super(AccelerometerSensorListener, self).__init__()
        self.SensorManager = cast(
            autoclass('android.hardware.SensorManager'),
            activity.getSystemService(Context.SENSOR_SERVICE)
        )
        self.sensor = self.SensorManager.getDefaultSensor(
            Sensor.TYPE_LINEAR_ACCELERATION
        )
        self.sensor2 = self.SensorManager.getDefaultSensor(
            Sensor.TYPE_GYROSCOPE
        )

        self.values = [None, None, None]
        self.values2 = [None, None, None]

    def enable(self):
        self.SensorManager.registerListener(
            self, self.sensor,
            SensorManager.SENSOR_DELAY_FASTEST
        )
        self.SensorManager.registerListener(
            self, self.sensor2,
            SensorManager.SENSOR_DELAY_FASTEST
        )

    def disable(self):
        self.SensorManager.unregisterListener(self, self.sensor)
        self.SensorManager.unregisterListener(self, self.sensor2)
        
    def onSensorChanged(self, event):
        if event.sensor.getType() == Sensor.TYPE_LINEAR_ACCELERATION:
            self.values = event.values[:3]
        elif event.sensor.getType() == Sensor.TYPE_GYROSCOPE:
            self.values2 = event.values[:3]

    def onAccuracyChanged(self, sensor, accuracy):
        # Maybe, do something in future?
        pass


class AndroidAccelerometer(Accelerometer):
    def __init__(self):
        super().__init__()
        self.bState = False

    def _enable(self):
        if (not self.bState):
            self.listener = AccelerometerSensorListener()
            self.listener.enable()
            self.bState = True

    def _disable(self):
        if (self.bState):
            self.bState = False
            self.listener.disable()
            del self.listener

    def _get_acceleration(self):
        if (self.bState):
            return tuple(self.listener.values)
        else:
            return (None, None, None)

    def __del__(self):
        if self.bState:
            self._disable()
        super().__del__()


def instance():
    return AndroidAccelerometer()
