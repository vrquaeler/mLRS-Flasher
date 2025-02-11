#!/usr/bin/env python
#*******************************************************
# Copyright (c) MLRS project
# GPL3
# https://www.gnu.org/licenses/gpl-3.0.de.html
# OlliW @ www.olliw.eu
#*******************************************************
# mLRS Meta Data for mLRS Flahser Desktop App
# 11. Feb. 2025 001
#********************************************************


# this is easy enough to maintain by hand for the moment
#
# fname: holds a string which appears in the firmware file name and which allows to uniquely get the device type/brand
# chipset: we assume currently that a device type/brand does not use mixed chips

g_txModuleExternalDeviceTypeDict = {
    'MatekSys' :       { 'fname' : 'matek',       'chipset' : 'stm32' },
    'FrSky R9' :       { 'fname' : 'R9',          'chipset' : 'stm32' },
    'FlySky FRM 303' : { 'fname' : 'FRM303',      'chipset' : 'stm32' },
    'Wio E5' :         { 'fname' : 'Wio-E5',      'chipset' : 'stm32' },
    'E77 MBL Kit' :    { 'fname' : 'E77-MBLKit',  'chipset' : 'stm32' },
    'Easysolder' :     { 'fname' : 'easysolder',  'chipset' : 'stm32' },
    'RadioMaster' :    { 'fname' : 'radiomaster', 'chipset' : 'esp32' },
    'BetaFPV' :        { 'fname' : 'betafpv',     'chipset' : 'esp32' },
}


g_receiverDeviceTypeDict = {
    'MatekSys' :       { 'fname' : 'matek',       'chipset' : 'stm32' },
    'FrSky R9' :       { 'fname' : 'R9',          'chipset' : 'stm32' },
    'FlySky FRM 303' : { 'fname' : 'FRM303',      'chipset' : 'stm32' },
    'Wio E5' :         { 'fname' : 'Wio-E5',      'chipset' : 'stm32' },
    'E77 MBL Kit' :    { 'fname' : 'E77-MBLKit',  'chipset' : 'stm32' },
    'Easysolder' :     { 'fname' : 'easysolder',  'chipset' : 'stm32' },
}


g_txModuleInternalDeviceTypeDict = {
    'Jumper T20, T20 V2, T15, T14, T-Pro S' :        { 'fname' : 'jumper-internal',            'chipset' : 'esp32' },
    'RadioMaster TX16S, TX12, MT12, Zorro, Pocket' : { 'fname' : 'radiomaster-internal-2400',  'chipset' : 'esp32' },
    'RadioMaster Boxer' :                            { 'fname' : 'radiomaster-internal-boxer', 'chipset' : 'esp32' },
}


'''--------------------------------------------------
-- Target/firmware specific
--------------------------------------------------'''
# things which are target and/or firmware specific

g_targetsDict = {
    #-- tx modules
    # stm32 defaults:
    # - 'flashmethod' : 'stlink'
    'tx-matek-' : {
        'flashmethod' : 'dfu',
        'description' : 'flash method is DFU',
    },
    'tx-E77-MBLKit-' : {},
    'tx-easysolder-' : {},
    'tx-FRM303-' : {},
    'tx-R9' : {},
    'tx-Wio-E5-' : {},

    # esp32 tx module defaults
    # - 'flashmethod' : esptool with 'esp32' 
    'tx-betafpv-' : {
        'tx-betafpv-micro-1w-2400' : {
            'description' : 'For flashing the dip switches need to be set as follow:\n- blabla\n- blabla',
            'wireless' : {
                'description' : 'Notes for flashing the wireless-bridge:',
            },
        },
    },
    'tx-radiomaster-' : {
        'tx-radiomaster-bandit-' : {
            'wireless' : {},
        },
        'tx-radiomaster-rp4td-' : {},
    },

    # esp32 internal tx module defaults
    # - 'flashmethod' : ...
    # - wireless-bridge: these currently all use a esp8285 backpack, and use the same wirelesss-bridge flash method
    'tx-jumper-internal-' : {},
    'tx-radiomaster-internal-' : {
        'tx-radiomaster-internal-2400-' : {},
        'tx-radiomaster-internal-boxer-' : {},
    },

    #-- receivers
    # stm32 defaults:
    # - 'flashmethod' : 'stlink'
    'rx-matek-' : {
        'flashmethod' : 'dfu',
        'rx-matek-mr900-22-' : {
            'flashmethod' : 'stlink'
        },
    },
    'rx-E77-MBLKit-' : {},
    'rx-easysolder-' : {},
    'rx-FRM303-' : {},
    'rx-R9' : {},
    'rx-Wio-E5-' : {},
    
    # esp defaults:
    # - 'flashmethod' : ??
    'rx-bayck-' : {},
    'rx-betafpv-' : {},
    'rx-generic-' : {},
    'rx-generic-c3-lr1121-' : {},
    'rx-radiomaster-' : {},
    'rx-speedybee-' : {},
}

