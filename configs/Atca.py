## System states
##   state can change to next state in 2 ways:
##   - a process emits a GotoSystemState signal with state name to goto
##   - objects specified in EXIT_STATE_DEPEND have started
SYSTEM_STATES = [
	'BASE_APPS',
	'BMC_STARTING',
	'BMC_READY',
	'HOST_POWERING_ON',
	'HOST_POWERED_ON',
	'HOST_BOOTING',
	'HOST_BOOTED',
	'HOST_POWERED_OFF',
]

EXIT_STATE_DEPEND = {
	'BASE_APPS' : {
		'/org/openbmc/sensors': 0,
	},
	'BMC_STARTING' : {
		'/org/openbmc/control/chassis0': 0,
		'/org/openbmc/control/power0' : 0,
		'/org/openbmc/control/led/identify' : 0,
		'/org/openbmc/control/host0' : 0,
		'/org/openbmc/control/flash/bios' : 0,
	}
}

FRU_INSTANCES = {
	'<inventory_root>/system' : { 'fru_type' : 'SYSTEM','is_fru' : True, },
	'<inventory_root>/system/chassis' : { 'fru_type' : 'SYSTEM','is_fru' : True, },
	'<inventory_root>/system/chassis/motherboard' : { 'fru_type' : 'MAIN_PLANAR','is_fru' : True, },

	'<inventory_root>/system/chassis/fan0' : { 'fru_type' : 'FAN','is_fru' : True, },
	'<inventory_root>/system/chassis/fan1' : { 'fru_type' : 'FAN','is_fru' : True, },
	'<inventory_root>/system/chassis/fan2' : { 'fru_type' : 'FAN','is_fru' : True, },
	'<inventory_root>/system/chassis/fan3' : { 'fru_type' : 'FAN','is_fru' : True, },
	'<inventory_root>/system/chassis/fan4' : { 'fru_type' : 'FAN','is_fru' : True, },

	'<inventory_root>/system/chassis/motherboard/bmc' : { 'fru_type' : 'BMC','is_fru' : False, 
			'manufacturer' : 'ASPEED' },
	'<inventory_root>/system/chassis/motherboard/cpu0' : { 'fru_type' : 'CPU', 'is_fru' : True, },
	'<inventory_root>/system/chassis/motherboard/cpu0/core0' : { 'fru_type' : 'CORE', 'is_fru' : False, },
	'<inventory_root>/system/chassis/motherboard/cpu0/core1' : { 'fru_type' : 'CORE', 'is_fru' : False, },
	'<inventory_root>/system/chassis/motherboard/cpu0/core2' : { 'fru_type' : 'CORE', 'is_fru' : False, },
	'<inventory_root>/system/chassis/motherboard/cpu0/core3' : { 'fru_type' : 'CORE', 'is_fru' : False, },
	'<inventory_root>/system/chassis/motherboard/cpu0/core4' : { 'fru_type' : 'CORE', 'is_fru' : False, },
	'<inventory_root>/system/chassis/motherboard/cpu0/core5' : { 'fru_type' : 'CORE', 'is_fru' : False, },
	'<inventory_root>/system/chassis/motherboard/cpu0/core6' : { 'fru_type' : 'CORE', 'is_fru' : False, },
	'<inventory_root>/system/chassis/motherboard/cpu0/core7' : { 'fru_type' : 'CORE', 'is_fru' : False, },
	'<inventory_root>/system/chassis/motherboard/cpu0/core8' : { 'fru_type' : 'CORE', 'is_fru' : False, },
	'<inventory_root>/system/chassis/motherboard/cpu0/core9' : { 'fru_type' : 'CORE', 'is_fru' : False, },
	'<inventory_root>/system/chassis/motherboard/cpu0/core10' : { 'fru_type' : 'CORE', 'is_fru' : False, },
	'<inventory_root>/system/chassis/motherboard/cpu0/core11' : { 'fru_type' : 'CORE', 'is_fru' : False, },

	
	'<inventory_root>/system/chassis/motherboard/membuf0' : { 'fru_type' : 'MEMORY_BUFFER', 'is_fru' : False, },

	'<inventory_root>/system/chassis/motherboard/dimm0' : { 'fru_type' : 'DIMM', 'is_fru' : True,},
	'<inventory_root>/system/chassis/motherboard/dimm1' : { 'fru_type' : 'DIMM', 'is_fru' : True,},
	'<inventory_root>/system/chassis/motherboard/dimm2' : { 'fru_type' : 'DIMM', 'is_fru' : True,},
	'<inventory_root>/system/chassis/motherboard/dimm3' : { 'fru_type' : 'DIMM', 'is_fru' : True,},

	'<inventory_root>/system/chassis/io_board/pcie_slot0' : { 'fru_type' : 'PCIE_CARD', 'is_fru' : True,},
	'<inventory_root>/system/chassis/io_board/pcie_slot1' : { 'fru_type' : 'PCIE_CARD', 'is_fru' : True,},

	'<inventory_root>/system/systemevent'                  : { 'fru_type' : 'SYSTEM_EVENT', 'is_fru' : False, },
	'<inventory_root>/system/chassis/motherboard/refclock' : { 'fru_type' : 'MAIN_PLANAR', 'is_fru' : False, },
	'<inventory_root>/system/chassis/motherboard/pcieclock': { 'fru_type' : 'MAIN_PLANAR', 'is_fru' : False, },
	'<inventory_root>/system/chassis/motherboard/todclock' : { 'fru_type' : 'MAIN_PLANAR', 'is_fru' : False, },
	'<inventory_root>/system/chassis/motherboard/apss'     : { 'fru_type' : 'MAIN_PLANAR', 'is_fru' : False, },
}

ID_LOOKUP = {
	'FRU' : {
		0x0d : '<inventory_root>/system/chassis',
		0x34 : '<inventory_root>/system/chassis/motherboard',
		0x01 : '<inventory_root>/system/chassis/motherboard/cpu',
		0x02 : '<inventory_root>/system/chassis/motherboard/membuf',
		0x03 : '<inventory_root>/system/chassis/motherboard/dimm0',
		0x04 : '<inventory_root>/system/chassis/motherboard/dimm1',
		0x05 : '<inventory_root>/system/chassis/motherboard/dimm2',
		0x06 : '<inventory_root>/system/chassis/motherboard/dimm3',
		0x35 : '<inventory_root>/system',
	},
	'FRU_STR' : {
		'PRODUCT_15' : '<inventory_root>/system',
		'CHASSIS_2' : '<inventory_root>/system/chassis',
		'BOARD_1'   : '<inventory_root>/system/chassis/motherboard/cpu',
		'BOARD_2'   : '<inventory_root>/system/chassis/motherboard/membuf',
		'BOARD_14'   : '<inventory_root>/system/chassis/motherboard',
		'PRODUCT_3'   : '<inventory_root>/system/chassis/motherboard/dimm0',
		'PRODUCT_4'   : '<inventory_root>/system/chassis/motherboard/dimm1',
		'PRODUCT_5'   : '<inventory_root>/system/chassis/motherboard/dimm2',
		'PRODUCT_6'   : '<inventory_root>/system/chassis/motherboard/dimm3',
	},
	'SENSOR' : {
		0x34 : '<inventory_root>/system/chassis/motherboard',
		0x37 : '<inventory_root>/system/chassis/motherboard/refclock',
		0x38 : '<inventory_root>/system/chassis/motherboard/pcieclock',
		0x39 : '<inventory_root>/system/chassis/motherboard/todclock',
		0x3A : '<inventory_root>/system/chassis/apss',
		0x2f : '<inventory_root>/system/chassis/motherboard/cpu',
		0x22 : '<inventory_root>/system/chassis/motherboard/cpu/core1',
		0x23 : '<inventory_root>/system/chassis/motherboard/cpu/core2',
		0x24 : '<inventory_root>/system/chassis/motherboard/cpu/core3',
		0x25 : '<inventory_root>/system/chassis/motherboard/cpu/core4',
		0x26 : '<inventory_root>/system/chassis/motherboard/cpu/core5',
		0x27 : '<inventory_root>/system/chassis/motherboard/cpu/core6',
		0x28 : '<inventory_root>/system/chassis/motherboard/cpu/core9',
		0x29 : '<inventory_root>/system/chassis/motherboard/cpu/core10',
		0x2a : '<inventory_root>/system/chassis/motherboard/cpu/core11',
		0x2b : '<inventory_root>/system/chassis/motherboard/cpu/core12',
		0x2c : '<inventory_root>/system/chassis/motherboard/cpu/core13',
		0x2d : '<inventory_root>/system/chassis/motherboard/cpu/core14',
		0x2e : '<inventory_root>/system/chassis/motherboard/membuf',
		0x1e : '<inventory_root>/system/chassis/motherboard/dimm0',
		0x1f : '<inventory_root>/system/chassis/motherboard/dimm1',
		0x20 : '<inventory_root>/system/chassis/motherboard/dimm2',
		0x21 : '<inventory_root>/system/chassis/motherboard/dimm3',
		0x09 : '/org/openbmc/sensors/host/BootCount',
		0x05 : '/org/openbmc/sensors/host/BootProgress',
		0x32 : '/org/openbmc/sensors/host/OperatingSystemStatus',
	},
	'GPIO_PRESENT' : {
		'SLOT0_PRESENT' : '<inventory_root>/system/chassis/motherboard/pciecard_x16',
		'SLOT1_PRESENT' : '<inventory_root>/system/chassis/motherboard/pciecard_x8',
	}
}

GPIO_CONFIG = {}
GPIO_CONFIG['FSI_CLK']    =   { 'gpio_pin': 'A4', 'direction': 'out' }
GPIO_CONFIG['FSI_DATA']   =   { 'gpio_pin': 'A5', 'direction': 'out' }
GPIO_CONFIG['FSI_ENABLE'] =   { 'gpio_pin': 'D0', 'direction': 'out' }
GPIO_CONFIG['POWER_PIN']  =   { 'gpio_pin': 'F3', 'direction': 'out'  } # change from E1
GPIO_CONFIG['CRONUS_SEL'] =   { 'gpio_pin': 'A6', 'direction': 'out'  }
GPIO_CONFIG['PGOOD']      =   { 'gpio_pin': 'J0', 'direction': 'in'  } # change from C7
GPIO_CONFIG['BMC_THROTTLE'] = { 'gpio_pin': 'J3', 'direction': 'out' }
# GPIO_CONFIG['IDBTN']       = { 'gpio_pin': 'Q7', 'direction': 'out' } # delete
GPIO_CONFIG['POWER_BUTTON'] = { 'gpio_pin': 'R6', 'direction': 'both' } # change from E0, R6 is void
# GPIO_CONFIG['PCIE_RESET']   = { 'gpio_pin': 'B5', 'direction': 'out' } # function done in cpld
GPIO_CONFIG['PCIE_RESET']   = { 'gpio_pin': 'B6', 'direction': 'out' } # function done in cpld
# GPIO_CONFIG['USB_RESET']    = { 'gpio_pin': 'B6', 'direction': 'out' }
GPIO_CONFIG['SLOT0_RISER_PRESENT'] =   { 'gpio_pin': 'N0', 'direction': 'in' }
GPIO_CONFIG['SLOT1_RISER_PRESENT'] =   { 'gpio_pin': 'N1', 'direction': 'in' }
GPIO_CONFIG['SLOT2_RISER_PRESENT'] =   { 'gpio_pin': 'N2', 'direction': 'in' }
GPIO_CONFIG['SLOT0_PRESENT'] =         { 'gpio_pin': 'N3', 'direction': 'in' }
GPIO_CONFIG['SLOT1_PRESENT'] =         { 'gpio_pin': 'N4', 'direction': 'in' }
GPIO_CONFIG['SLOT2_PRESENT'] =         { 'gpio_pin': 'N5', 'direction': 'in' }
GPIO_CONFIG['MEZZ0_PRESENT'] =         { 'gpio_pin': 'O0', 'direction': 'in' }
GPIO_CONFIG['MEZZ1_PRESENT'] =         { 'gpio_pin': 'O1', 'direction': 'in' }
GPIO_CONFIG['CHECKSTOP']      =   { 'gpio_pin': 'H0', 'direction': 'falling' } # change from P5

GPIO_CONFIGS = {
    'power_config' : {
        'power_good_in' : 'PGOOD',
        'power_up_outs' : [
            ('POWER_PIN', False),
        ],
        'reset_outs' : [
#            ('USB_RESET', False),
        ],
        'pci_reset_outs': [
            # net name, polarity, reset hold
            ('PCIE_RESET', False, True),
        ],
    },
    'hostctl_config' : {
        'fsi_data' : 'FSI_DATA',
        'fsi_clk' : 'FSI_CLK',
        'fsi_enable' : 'FSI_ENABLE',
        'cronus_sel' : 'CRONUS_SEL',
        'optionals' : [
            ('BMC_THROTTLE', True),
#            ('IDBTN', False),
        ],
    },
}

# Miscellaneous non-poll sensor with system specific properties.
# The sensor id is the same as those defined in ID_LOOKUP['SENSOR'].
MISC_SENSORS = {
	0x09 : { 'class' : 'BootCountSensor' },
	0x05 : { 'class' : 'BootProgressSensor' },
	0x32 : { 'class' : 'OperatingSystemStatusSensor' },
}

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
