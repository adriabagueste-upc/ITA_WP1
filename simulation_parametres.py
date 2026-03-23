# ---Aircraft Parameters---
aircraft_params = {
    "B767-300ER": {
        "MW": 204.10,     # (t)
        "mW": 103.20,     # (t)
        "RW": 158.80,     # (t)
        "MP": 46.50,      # (t)
        "S": 283.50,      # (m^2)

        "CD0": 0.0207,
        "CD2": 0.0483,
        "CD0_ic": 0.0140,
        "CD2_ic": 0.0490,
        "CD0_clean": 0.0174,
        "CD2_clean": 0.0459,

        "CT1": 0.35167e6,   # (N)
        "CT2": 0.44673e5,   # (ft)
        "CT3": 0.10129e-9,  # (1/ft^2)

        "CF1": 0.54005,     # (kg/(min·kN))
        "CF2": 0.55782e3    # (kt)
    },

    "B777-300": {
        "MW": 299.30,     # (t)
        "mW": 159.60,     # (t)
        "RW": 237.60,     # (t)
        "MP": 64.90,      # (t)
        "S": 428.04,      # (m^2)

        "CD0": 0.0175,
        "CD2": 0.0525,
        "CD0_ic": 0.0173,
        "CD2_ic": 0.0484,
        "CD0_clean": 0.0157,
        "CD2_clean": 0.0420,

        "CT1": 0.42577e6,   # (N)
        "CT2": 0.48987e5,   # (ft)
        "CT3": 0.66146e-10, # (1/ft^2)

        "CF1": 0.87843,     # (kg/(min·kN))
        "CF2": 0.36897e4    # (kt)
    },

    "B737": {
        "MW": 70.80,      # (t)
        "mW": 38.28,      # (t)
        "RW": 60.00,      # (t)
        "MP": 16.92,      # (t)
        "S": 124.65,      # (m^2)

        "CD0": 0.0333,
        "CD2": 0.0428,
        "CD0_ic": 0.0270,
        "CD2_ic": 0.0441,
        "CD0_clean": 0.0235,
        "CD2_clean": 0.0445,

        "CT1": 0.14573e6,   # (N)
        "CT2": 0.55638e5,   # (ft)
        "CT3": 0.14200e-10, # (1/ft^2)

        "CF1": 0.94680,     # (kg/(min·kN))
        "CF2": 0.10000e15   # (kt)
    },

    "A320-212": {
        "MW": 77.00,      # (t)
        "mW": 39.00,      # (t)
        "RW": 64.00,      # (t)
        "MP": 21.50,      # (t)
        "S": 122.60,      # (m^2)

        "CD0": 0.0390,
        "CD2": 0.0396,
        "CD0_ic": 0.0242,
        "CD2_ic": 0.0469,
        "CD0_clean": 0.0240,
        "CD2_clean": 0.0375,

        "CT1": 0.13605e6,   # (N)
        "CT2": 0.52238e5,   # (ft)
        "CT3": 0.26637e-10, # (1/ft^2)

        "CF1": 0.94000,     # (kg/(min·kN))
        "CF2": 0.10000e6    # (kt)
    },

    "A319-131": {
        "MW": 70.00,      # (t)
        "mW": 40.00,      # (t)
        "RW": 60.00,      # (t)
        "MP": 17.00,      # (t)
        "S": 122.60,      # (m^2)

        "CD0": 0.0445,
        "CD2": 0.0328,
        "CD0_ic": 0.0284,
        "CD2_ic": 0.0376,
        "CD0_clean": 0.0280,
        "CD2_clean": 0.0310,

        "CT1": 0.13900e6,   # (N)
        "CT2": 0.58900e5,   # (ft)
        "CT3": 0.57200e-14, # (1/ft^2)

        "CF1": 0.68800,     # (kg/(min·kN))
        "CF2": 0.16700e4    # (kt)
    }
}

#---Simulation parametres---
simulation_parametres = {
    'Atmospheric': {
        'MSL_pressure': 101325, # (Pa)
        'MSL_air_density': 1.225, # (kg/m^3)
        'MSL_temperature': 288.15, # (K)
        'MSL_speed_of_sound': 340.294, # (m/s)
        'MSL_gravity_acceleration': 9.80665, # (m/s^2)
        'Real_gas_constant': 287.04, # (m^2/Ks^2)
        'Tropopause_height': 11000, # (m)
        'Tropopause_temperature': 216.65 # (K)
    },

    'Conversion': {
        'm/ft_coefficient': 0.3048 # (m/ft)
    },

    'Simulation': {
        'Delta_t': 1.0, # (s)
        'Max_height': 14000, # (m)
        'Max_iteration': 50000, # (number of iterations)
        'Initial_altitude': 35 # (ft)
    }
}

if __name__ == "__main__":
    print("Aircraft parameters")