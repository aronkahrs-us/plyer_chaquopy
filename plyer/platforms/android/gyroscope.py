'''
Android Gyroscope
-----------------
'''

from plyer.facades import Gyroscope
from java import dynamic_proxy
from java import jclass as autoclass
from java import cast as cast
from java import method as java_method
from plyer.platforms.android import activity
from android.hardware import SensorEventListener

Context = autoclass('android.content.Context')
Sensor = autoclass('android.hardware.Sensor')
SensorManager = autoclass('android.hardware.SensorManager')


class GyroscopeSensorListener(dynamic_proxy(SensorEventListener)):
    __javainterfaces__ = ['android/hardware/SensorEventListener']

    def __init__(self):
        super(GyroscopeSensorListener, self).__init__()
        self.SensorManager = cast(
            autoclass('android.hardware.SensorManager'),
            activity.getSystemService(Context.SENSOR_SERVICE)
        )
        self.sensor = self.SensorManager.getDefaultSensor(
            Sensor.TYPE_GYROSCOPE
        )

        self.values = [None, None, None]

    def enable(self):
        self.SensorManager.registerListener(
            self, self.sensor,
            SensorManager.SENSOR_DELAY_FASTEST
        )

    def disable(self):
        self.SensorManager.unregisterListener(self, self.sensor)

    def onSensorChanged(self, event):
        if event.sensor.getType == Sensor.TYPE_GYROSCOPE:
            self.values = event.values[:3]
            print('GYRO: ',self.values[:3])

    def onAccuracyChanged(self, sensor, accuracy):
        # Maybe, do something in future?
        pass


class GyroUncalibratedSensorListener(dynamic_proxy(SensorEventListener)):
    __javainterfaces__ = ['android/hardware/SensorEventListener']

    def __init__(self):
        super(GyroUncalibratedSensorListener, self).__init__()
        service = activity.getSystemService(Context.SENSOR_SERVICE)
        self.SensorManager = cast(autoclass('android.hardware.SensorManager'), service)

        self.sensor = self.SensorManager.getDefaultSensor(
            Sensor.TYPE_GYROSCOPE_UNCALIBRATED)
        self.values = [None, None, None, None, None, None]

    def enable(self):
        self.SensorManager.registerListener(
            self, self.sensor,
            SensorManager.SENSOR_DELAY_NORMAL
        )

    def disable(self):
        self.SensorManager.unregisterListener(self, self.sensor)

    def onSensorChanged(self, event):
        self.values = event.values[:6]

    def onAccuracyChanged(self, sensor, accuracy):
        pass


class AndroidGyroscope(Gyroscope):
    def __init__(self):
        super().__init__()
        self.bState = False

    def _enable(self):
        if (not self.bState):
            self.listenerg = GyroscopeSensorListener()
            self.listenergu = GyroUncalibratedSensorListener()
            self.listenerg.enable()
            self.listenergu.enable()
            self.bState = True

    def _disable(self):
        if (self.bState):
            self.bState = False
            self.listenerg.disable()
            self.listenergu.disable()
            del self.listenerg
            del self.listenergu

    def _get_orientation(self):
        if (self.bState):
            return tuple(self.listenerg.values)
        else:
            return (None, None, None)

    def _get_rotation_uncalib(self):
        if (self.bState):
            return tuple(self.listenergu.values)
        else:
            return (None, None, None, None, None, None)

    def __del__(self):
        if self.bState:
            self._disable()
        super().__del__()


def instance():
    return AndroidGyroscope()
