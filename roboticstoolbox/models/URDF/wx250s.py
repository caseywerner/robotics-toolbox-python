#!/usr/bin/env python

import numpy as np
import roboticstoolbox as rp
from roboticstoolbox.robot.ETS import ETS
from pathlib import Path


class wx250s(ETS):

    def __init__(self):

        mpath = Path(rp.__file__).parent
        fpath = mpath / 'models' / 'xacro' / 'interbotix_descriptions' / 'urdf'
        fname = 'wx250s.urdf.xacro'

        args = super(wx250s, self).urdf_to_ets_args(
            (fpath / fname).as_posix())

        super(wx250s, self).__init__(
            args[0],
            name=args[1])

        self.manufacturer = 'Interbotix'

        self._qz = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self._qr = np.array([0, -0.3, 0, -2.2, 0, 2.0, np.pi/4, 0, 0])

    @property
    def qz(self):
        return self._qz

    @property
    def qr(self):
        return self._qr
