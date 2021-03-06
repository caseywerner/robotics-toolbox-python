#!/usr/bin/env python

import numpy as np
from roboticstoolbox.robot.ETS import ETS
from roboticstoolbox.robot.ET import ET
from roboticstoolbox.robot.ELink import ELink


class Frankie(ETS):
    """
    A class representing the Franka Emika Panda robot arm. ETS taken from [1]
    based on https://frankaemika.github.io/docs/control_parameters.html

    :param et_list: List of elementary transforms which represent the robot
        kinematics
    :type et_list: list of etb.robot.et
    :param q_idx: List of indexes within the ets_list which correspond to
        joints
    :type q_idx: list of int
    :param name: Name of the robot
    :type name: str, optional
    :param manufacturer: Manufacturer of the robot
    :type manufacturer: str, optional
    :param base: Location of the base is the world frame
    :type base: float np.ndarray(4,4), optional
    :param tool: Offset of the flange of the robot to the end-effector
    :type tool: float np.ndarray(4,4), optional
    :param qz: The zero joint angle configuration of the robot
    :type qz: float np.ndarray(7,)
    :param qr: The ready state joint angle configuration of the robot
    :type qr: float np.ndarray(7,)

    References: [1] Kinematic Derivatives using the Elementary Transform
        Sequence, J. Haviland and P. Corke
    """
    def __init__(self):

        deg = np.pi/180
        mm = 1e-3
        tool_offset = (103)*mm

        b0 = ELink(
            ET.rz(),
            name='base0',
            parent=None
        )

        b1 = ELink(
            ET.tx(),
            name='base1',
            parent=b0
        )

        l0 = ELink(
            ET.tz(0.333) * ET.rz(),
            name='link0',
            parent=b1
        )

        l1 = ELink(
            ET.rx(-90*deg) * ET.rz(),
            name='link1',
            parent=l0
        )

        l2 = ELink(
            ET.rx(90*deg) * ET.tz(0.316) * ET.rz(),
            name='link2',
            parent=l1
        )

        l3 = ELink(
            ET.tx(0.0825) * ET.rx(90*deg) * ET.rz(),
            name='link3',
            parent=l2
        )

        l4 = ELink(
            ET.tx(-0.0825) * ET.rx(-90*deg) * ET.tz(0.384) * ET.rz(),
            name='link4',
            parent=l3
        )

        l5 = ELink(
            ET.rx(90*deg) * ET.rz(),
            name='link5',
            parent=l4
        )

        l6 = ELink(
            ET.tx(0.088) * ET.rx(90*deg) * ET.tz(0.107) * ET.rz(),
            name='link6',
            parent=l5
        )

        ee = ELink(
            ET.tz(tool_offset) * ET.rz(-np.pi/4),
            name='ee',
            parent=l6
        )

        ets = [b0, b1, l0, l1, l2, l3, l4, l5, l6, ee]

        super(Frankie, self).__init__(
            ets,
            name='Frankie',
            manufacturer='Franka Emika, Omron')

        self._qz = np.array([0, 0, 0, 0, 0, 0, 0, 0])
        self._qr = np.array([0, 0, -90, -90, 90, 0, -90, 90]) * deg

    @property
    def qz(self):
        return self._qz

    @property
    def qr(self):
        return self._qr
