'''
Multiple Sensors
============

'''


class MULTI:
    '''
    Multi facade.
    '''

    @property
    def acceleration(self):
        '''
        Property that returns values of the current acceleration
        sensors, as a (x, y, z) tuple. Returns (None, None, None)
        if no data is currently available.
        '''
        return self.get_acceleration()
      
    @property
    def rotation(self):
        '''
        Property that returns the rate of rotation around the device's local
        X, Y and Z axis.

        Along x-axis: angular speed around the X axis
        Along y-axis: angular speed around the Y axis
        Along z-axis: angular speed around the Z axis

        Returns (None, None, None) if no data is currently available.
        '''
        return self.get_orientation()

    @property
    def orientation(self):
        '''
        WARNING:: This property is deprecated after API Level 8.
        Use `gyroscope.rotation` instead.

        Property that returns values of the current Gyroscope sensors, as
        a (x, y, z) tuple. Returns (None, None, None) if no data is currently
        available.
        '''
        return self.get_orientation()

    def enable(self):
        '''
        Activate the accelerometer sensor. Throws an error if the
        hardware is not available or not implemented on.
        '''
        self._enable()

    def disable(self):
        '''
        Disable the accelerometer sensor.
        '''
        self._disable()

    def get_acceleration(self):
        return self._get_acceleration()

    def get_orientation(self):
        return self._get_orientation()


    # private

    def _enable(self):
        raise NotImplementedError()

    def _disable(self):
        raise NotImplementedError()

    def _get_acceleration(self):
        raise NotImplementedError()

    def _get_orientation(self):
        raise NotImplementedError()
