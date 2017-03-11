.. currentmodule:: pyb
.. _pyb.Pin:

class Pin -- control I/O pins
=============================

A pin is the basic object to control I/O pins. It has methods to set the mode
of the pin (input, output, etc) and methods to get and set the digital logic
level. For analog control of a pin, see the :ref:`ADC <pyb.ADC>` class.

Usage Model:

.. only:: port_pyboard

    All board pins are predefined as ``pyb.Pin.board.<name>``::

        x1_pin = pyb.Pin.board.X1

        g = pyb.Pin(pyb.Pin.board.X1, pyb.Pin.IN)

    CPU pins which correspond to the board pins are available as
    ``pyb.cpu.<name>``. For the CPU pins, the names are the port letter
    followed by the pin number. On the PYBv1.0, ``pyb.Pin.board.X1`` and
    ``pyb.Pin.cpu.A0`` are the same pin.

    You can also use strings::

        g = pyb.Pin('X1', pyb.Pin.OUT_PP)

    Users can add their own names::

        MyMapperDict = {'LeftMotorDir': pyb.Pin.cpu.C12}
        pyb.Pin.dict(MyMapperDict)
        g = pyb.Pin("LeftMotorDir", pyb.Pin.OUT_OD)

    and can query mappings::

        pin = pyb.Pin("LeftMotorDir")

    Users can also add their own mapping function::

        def MyMapper(pin_name):
            if pin_name == "LeftMotorDir":
                return pyb.Pin.cpu.A0

        pyb.Pin.mapper(MyMapper)

    So, if you were to call: ``pyb.Pin("LeftMotorDir", pyb.Pin.OUT_PP)`` then
    ``"LeftMotorDir"`` is passed directly to the mapper function.

    To summarise, the following order determines how things get mapped into an
    ordinal pin number:

    1. Directly specify a pin object
    2. User supplied mapping function
    3. User supplied mapping (object must be usable as a dictionary key)
    4. Supply a string which matches a board pin
    5. Supply a string which matches a CPU port/pin

    You can set ``pyb.Pin.debug(True)`` to get some debug information about how
    a particular object gets mapped to a pin.

    When a pin has the ``Pin.PULL_UP`` or ``Pin.PULL_DOWN`` pull-mode enabled,
    that pin has an effective 40k Ohm resistor pulling it to 3V3 or GND
    respectively (except pin Y5 which has 11k Ohm resistors).

Constructors
------------

.. class:: pyb.Pin(id, ...)

    Create a new Pin object associated with the id.

    If additional arguments are given, they are used to initialise the pin. See
    :meth:`Pin.init`.

.. only:: port_pyboard

    Class methods
    -------------

    .. classmethod:: Pin.debug([state])

        Get or set the debugging state (``True`` or ``False`` for on or off).

    .. classmethod:: Pin.dict([dict])

        Get or set the pin mapper dictionary.

    .. classmethod:: Pin.mapper([fun])

        Get or set the pin mapper function.

Methods
-------

.. only:: port_pyboard

    .. method:: Pin.init(mode, pull=Pin.PULL_NONE, af=-1)

        Initialise the pin:

        - ``mode`` can be one of:

            - ``Pin.IN`` - configure the pin for input;
            - ``Pin.OUT_PP`` - configure the pin for output, with push-pull control;
            - ``Pin.OUT_OD`` - configure the pin for output, with open-drain control;
            - ``Pin.AF_PP`` - configure the pin for alternate function, pull-pull;
            - ``Pin.AF_OD`` - configure the pin for alternate function, open-drain;
            - ``Pin.ANALOG`` - configure the pin for analog.

        - ``pull`` can be one of:

            - ``Pin.PULL_NONE`` - no pull up or down resistors;
            - ``Pin.PULL_UP`` - enable the pull-up resistor;
            - ``Pin.PULL_DOWN`` - enable the pull-down resistor.

        - when mode is ``Pin.AF_PP`` or ``Pin.AF_OD``, then ``af`` can be the
          index or name of one of the alternate functions associated with a
          pin.

       Returns: ``None``.

.. method:: Pin.value([value])

    Get or set the digital logic level of the pin:

    - With no argument, return 0 or 1 depending on the logic level of the pin.
    - With ``value`` given, set the logic level of the pin.  ``value`` can be
      anything that converts to a boolean.  If it converts to ``True``, the pin
      is set high, otherwise it is set low.

.. only:: port_pyboard

    .. method:: Pin.__str__()

        Return a string describing the pin object.

    .. method:: Pin.af()

        Return the currently configured alternate function of the pin.

        The integer returned will match one of the allowed constants for the
        ``af`` argument to the :meth:`init <Pin.init>` function.

    .. method:: Pin.af_list()

        Return an array of alternate functions available for this pin.

    .. method:: Pin.high()

        Set the digital logic level of the pin to high.

        Equivalent to :meth:`Pin.value(True) <Pin.value>`.

    .. method:: Pin.gpio()

        Return the base address of the GPIO block associated with this pin.

    .. method:: Pin.low()

        Set the digital logic level of the pin to low.

        Equivalent to :meth:`Pin.value(False) <Pin.value>`.

    .. method:: Pin.mode()

        Return the currently configured mode of the pin.

        The integer returned will match one of the allowed constants for the
        ``mode`` argument to the :meth:init <Pin.init>` function.

    .. method:: Pin.name()

        Get the pin name.

    .. method:: Pin.names()

        Return the CPU and board names for this pin.

    .. method:: Pin.pin()

        Get the pin number.

    .. method:: Pin.port()

        Get the pin GPIO port number.

.. method:: Pin.pull()

    Return the currently configured pull of the pin.

    The integer returned will match one of the allowed constants for the pull
    argument to the :meth:init <Pin.init>` function.

Constants
---------

.. only:: port_pyboard

    .. data:: Pin.AF_OD

       Initialise the pin to alternate function mode with an open-drain drive.

    .. data:: Pin.AF_PP

       Initialise the pin to alternate function mode with a push-pull drive.

    .. data:: Pin.ANALOG

       Initialise the pin to analog mode.

    .. data:: Pin.IN

       Initialise the pin to input mode.

    .. data:: Pin.OUT

       Alias for ``Pin.OUT_PP``.

    .. data:: Pin.OUT_OD

       Initialise the pin to output mode with an open-drain drive.

    .. data:: Pin.OUT_PP

       Initialise the pin to output mode with a push-pull drive.

    .. data:: Pin.PULL_DOWN

       Enable the pull-down resistor on the pin.

    .. data:: Pin.PULL_NONE

       Don't enable any pull up or down resistors on the pin.

    .. data:: Pin.PULL_UP

       Enable the pull-up resistor on the pin.

.. only:: port_pyboard

    class PinAF -- Pin Alternate Functions
    ======================================

    A Pin represents a physical pin on the microprocessor. Each pin can have a
    variety of functions (GPIO, I2C SDA, etc). Each ``PinAF`` object represents
    a particular function for a pin.

    Usage Model::

        x3 = pyb.Pin.board.X3
        x3_af = x3.af_list()

    ``x3_af`` will now contain an array of ``PinAF`` objects which are
    available on pin X3.

    For the pyboard, ``x3_af`` would contain::

        [Pin.AF1_TIM2, Pin.AF2_TIM5, Pin.AF3_TIM9, Pin.AF7_USART2]

    Normally, each peripheral would configure the alternate function
    automatically, but sometimes the same function is available on multiple
    pins, and having more control is desired.

    To configure pin X3 to expose ``TIM2_CH3``, you could use::

        pin = pyb.Pin(pyb.Pin.board.X3, mode=pyb.Pin.AF_PP, af=pyb.Pin.AF1_TIM2)

    where the constant ``pyb.Pin.AF1_TIM2`` holds the same value as that
    returned by the :meth:`index <PinAF.index>` method of the corresponding
    ``PinAF`` instance ``Pin.AF1_TIM2`` in ``x3_af[0]``. So the above call is
    equivalent to::

        pin = pyb.Pin(pyb.Pin.board.X3, mode=pyb.Pin.AF_PP, af=x3_af[0].index())

    or::

        pin = pyb.Pin(pyb.Pin.board.X3, mode=pyb.Pin.AF_PP, af=1)


    Methods
    -------

    .. method:: PinAF.index()

       Return the alternate function index.

    .. method:: PinAF.name()

       Return the name of the alternate function.

    .. method:: PinAF.reg()

       Return the base register associated with the peripheral assigned to this
       alternate function. For example, if the alternate function were
       ``TIM2_CH3`` this would return ``stm.TIM2``.
