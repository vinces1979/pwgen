pwgen
===

A simple implementation of pwgen in python

Installation
---------

    pip install pwgen
    easy_install install pwgen

Basic Usage:
------------------

    from pwgen import pwgen
    pwgen()
    >> '[^%6JK<&Lb}{.T#eYY+
    pwgen(10, no_symbols=True)
    >> ujr20YVkH3
    pwgen(50, 10, no_symbols=True, no_capitalize=True)
    >>['ra8xymzct6e9fmmwen0ejvae6x5pyjvdlptxz8da69e4fivvs4',
        'v4hj1v1a3wwr765xvlsorn9rdfe8vk9pf2fnqdr891ztvrc7wd',
        'zpowwedvv2l2ka747weuijejqetnquga8w6eixuaeuoerpjvp2',
        'mz3hwplg0rlq9aplq0b42qgnk89t4g0fnuy9clopoh4omyzg3l',
        'caoll9osyhr09geao192u82tjhw7nlbsbbvlvpisa34jz2u68d',
        'zmx9a8df2i2shmozy03j0ss36z8omcmuxl8xvlegj96f7vhw0n',
        'nl0rfitjwle86qcm5iefehezqnsgfj4ndyq8290ux5ha64nrqk',
        'limpalwibi0ndvi5rtr7f5vd5bximoiihid9lgr4rx4os6x63i',
        '824jxymdzst8vxlivdqdg99b7q3kt0l05i0jczg5gjga566xyg',
        'ptfh1g6ks4ff25oxcpluhogdvgqnozwb385shedrpw6s603yl7']
