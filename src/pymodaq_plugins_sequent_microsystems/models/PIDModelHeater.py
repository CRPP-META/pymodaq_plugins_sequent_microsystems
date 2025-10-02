import numpy as np

from pymodaq.extensions.pid.utils import PIDModelGeneric, DataToActuatorPID, main
from pymodaq_data.data import DataToExport, DataCalculated

from pymodaq.utils.data import DataActuator

from typing import List


def some_function_to_convert_the_pid_outputs(outputs: List[float], dt: float, stab=True):
    """ Should be replaced here or in the model class to process the outputs """
    print(outputs)
    value = outputs[0]
    output = 0 if value < 0 else 100 if value > 100 else value
    return [output]

def some_function_to_convert_the_data(measurements: DataToExport):
    """ Should be replaced here or in the model class to process the measurement """
    a = 0
    return a


class PIDModelHeater(PIDModelGeneric):
    limits = dict(max=dict(state=False, value=10),
                  min=dict(state=False, value=-10),)
    konstants = dict(kp=30, ki=3, kd=0.01)

    setpoint_ini = [30]  # number and values of initial setpoints
    # setpoints_names = ['Temperature']  # number and names of setpoints

    actuators_name = ["OD"]  # names of actuator's control modules involved in the PID
    detectors_name = ["RTD"]  # names of detector's control modules involved in the PID

    # params = []  # list of dict to initialize specific Parameters

    def __init__(self, pid_controller):
        super().__init__(pid_controller)

    def update_settings(self, param):
        """
        Get a parameter instance whose value has been modified by a user on the UI
        Parameters
        ----------
        param: (Parameter) instance of Parameter object
        """
        if param.name() == '':
            pass

    def ini_model(self):
        super().ini_model()
        # self.get_mod_from_name('RTD', 'det').settings.child('main_settings', 'wait_time').setValue(0)

        # add here other specifics initialization if needed

    def convert_input(self, measurements: DataToExport):
        """
        Convert the measurements in the units to be fed to the PID (same dimensionality as the setpoint)
        Parameters
        ----------
        measurements: DataToExport
            Data from the declared detectors from which the model extract a value of the same units as the setpoint

        Returns
        -------
        InputFromDetector: the converted input in the setpoints units

        """
        x = measurements.get_data_from_dim('Data0D').data[0][0][0]
        return DataToExport('pid inputs',
                            data=[DataCalculated('pid calculated',
                                                 data=[np.array([x])])])

    def convert_output(self, outputs: List[float], dt: float, stab=True) -> DataToActuatorPID:
        """
        Convert the output of the PID in units to be fed into the actuator
        Parameters
        ----------
        outputs: List of float
            output value from the PID from which the model extract a value of the same units as the actuator
        dt: float
            Ellapsed time since the last call to this function
        stab: bool

        Returns
        -------
        OutputToActuator: the converted output

        """
        outputs = some_function_to_convert_the_pid_outputs(outputs, dt, stab)
        print(outputs[0])
        return DataToActuatorPID('pid outputs',
                                mode='abs',
                                data=[DataActuator(self.actuators_name[0], data=outputs[0])])


if __name__ == '__main__':
    main("PDRC_PID.xml")  # some preset configured with the right actuators and detectors


