from simulation_parametres import aircraft_params, simulation_parametres
import math

# This program is meant to be the equation library for "The impact of implementing CCO in departures from Málaga –Costa del Sol airport (LEMG)

# Author: Adrià Bagüeste
# Subject: ITA (Infraestructures del transport aeri)
# Polytechnic University of Catalonia

# Notes:
# 1- meter calculations prefered over meters
# 2- BADA standard Atmospheric equations and constants

class Equations:

    def __init__(self): 

        # - International Standard Atmosphere, Mean Sea Level conditions -
        
        #  Initial conditions
        self.P0 = simulation_parametres['Atmospheric']['MSL_pressure'] #Pressure (N/m^2)
        self.rho0 = simulation_parametres['Atmospheric']['MSL_air_density'] #Air density (kg/m^3)
        self.T0 = simulation_parametres['Atmospheric']['MSL_temperature'] #Temperature (K)
        self.a0 = simulation_parametres['Atmospheric']['MSL_speed_of_sound'] #Speed of sound (m/s)
        self.g0 = simulation_parametres['Atmospheric']['MSL_gravity_acceleration'] #Acceleration of gravity (m/s^2)

        # Constants
        self.R = simulation_parametres['Atmospheric']['Real_gas_constant'] #Real gas constant (m^2/Ks^2)

        # - Unit convertion Parameters -
        self.m_over_ft = simulation_parametres['Conversion']['m/ft_coefficient'] #ft to m
        
        # Conditional values
        self.h_tropopause = simulation_parametres['Atmospheric']['Tropopause_height'] # meters
        self.TT = simulation_parametres['Atmospheric']['Tropopause_temperature'] #Temperature above troposphere (36089 ft / 11000 m)

        # - Simulation parameters -
        self.delta_t = simulation_parametres['Simulation']['Delta_t'] # (s)
        self.h0 = self.ft_to_m(simulation_parametres['Simulation']['Initial_altitude']) # (m)
        self.hf = self.ft_to_m(simulation_parametres['Simulation']['Max_height']) # (m)
        self.Max_iteration = simulation_parametres['Simulation']['Max_iteration'] #Maximum iteration steps for the simulation

    # - Simulation methods - 

    # Unit conversion
    def ft_to_m(self, h_ft:float) -> float:
        return h_ft * self.m_over_ft

    # Atmospheric conditions equations
    def Temp(self, h:float) -> float : #h: Height in m, returns temperature 
        if h < self.h_tropopause:
            T = self.T0 - 6.5*(h/1000)
        else: T = 216.65
        return T
    def p(self,h:float) -> float:
        base = max(1 - 0.0065*h/self.T0, 0.0)
        return self.P0 * (base**5.2561)
    def rho(self,p:float, T:float) -> float: #p: Pressure in Pascal, T: Temperature in Kelvin, returns rho (density) in kg/m^3
        return max((p)/(self.R*T),0.0)

    # Aerodynamic equations
    @staticmethod
    def CD(CD0:float, CD2:float, CD0_ic:float, CD2_ic:float, CD0_clean:float, CD2_clean:float, CL:float, h:float) -> float: #CD0 and CD2 change as a function of the altitude in order to simulate the change in the flap configuration
        if h < 1500:
            CD = CD0 + CD2 * (CL**2)
        elif 1500 < h < 2500:
            CD = CD0_ic + CD2_ic * (CL**2)
        else:
            CD = CD0_clean + CD2_clean * (CL**2)
        return CD
    def CL(self, M:float, rho:float, S:float, V:float) -> float:
        return 2*((M*self.g0)/(rho*(V**2)*S))
    
    # Main forces Equations
    @staticmethod
    def Tmax(CT1:float, CT2:float, CT3:float, h:float) -> float: #Thrust: Engine thrust is assumed always to its maximum
        return max((CT1*(1-(h/CT2)+CT3*((h)**2))),0)
    @staticmethod
    def D(rho:float, S:float, CD:float, V:float) -> float: #Drag
        return ((1/2)*rho*S*CD*(V)**2)

    # Derived Equaions
    def V_ROC(self, M:float, rho:float, S:float, T:float, CD0:float, CD2:float) -> float: #Minimum velocity for a given thrust, mass, drag and lift
        term_1 = 1/(3*rho*S*CD0)
        term_2 = math.sqrt((T**2)+12*CD2*((M*self.g0)**2)*CD0)
        return math.sqrt(max(term_1*(T+term_2), 0))
    def V_Gamma(self, M:float, rho:float, S:float, CD0:float, CD2:float) -> float: #Minimum velocity for a given climb angle, mass, drag and lift
        term_1 = 4*CD2*((M*self.g0)**2)
        term_2 = (rho**2)*(S**2)*CD0
        return (max(term_1/term_2, 0))**(0.25)
    def ROC(self,V:float, T:float, D:float, M:float) -> float: #Rate of climb, as a function of the velocity, thrust, drag and mass
        return max((V*((T-D)/(M*self.g0))),0)

    #Extra equations
    @staticmethod
    def eta(CF1:float, CF2:float, v:float) -> float: #Fuel consumption, as a function of the velocity, with two parameters that depend on the engine type
        return (CF1*(1+(v/CF2)))
    
    # - Simulation -

    def getCCO(self, ac_type: str, MTOW_percent: float, V_type: str): #Returns [x,y] to plot
        Max_iteration = self.Max_iteration
        current_height = self.h0
        current_x = 0
        current_t = 0

        M = (aircraft_params[ac_type]["MW"]) * MTOW_percent * 1000 #meters
        S = aircraft_params[ac_type]["S"]

        CT1 = aircraft_params[ac_type]["CT1"] 
        CT2 = aircraft_params[ac_type]["CT2"] * (self.m_over_ft)
        CT3 = aircraft_params[ac_type]["CT3"] * (self.m_over_ft)**2

        CD0 = aircraft_params[ac_type]["CD0"]
        CD2 = aircraft_params[ac_type]["CD2"]

        CD0_ic = aircraft_params[ac_type]["CD0_ic"]
        CD2_ic = aircraft_params[ac_type]["CD2_ic"]

        CD0_clean = aircraft_params[ac_type]["CD0_clean"]
        CD2_clean = aircraft_params[ac_type]["CD2_clean"]

        x = [0]
        y = [current_height]
        t = [0]

        while current_x < 350000:

            p = self.p(current_height)
            Temp = self.Temp(current_height)
            rho = self.rho(p, Temp)
            Th = self.Tmax(CT1, CT2, CT3, current_height)

            if V_type == 'ROC':
                Vmin = self.V_ROC(M, rho, S, Th, CD0, CD2)
            elif V_type == 'Gamma':
                Vmin = self.V_Gamma(M, rho, S, CD0, CD2)

            CL = self.CL(M, rho, S, Vmin)

            CD = self.CD(CD0, CD2, CD0_ic, CD2_ic, CD0_clean, CD2_clean, CL, current_height)

            D = self.D(rho, S, CD, Vmin)

            RoC = self.ROC(Vmin, Th, D, M)

            delta_h = RoC*self.delta_t
            delta_x = Vmin * self.delta_t

            current_height += delta_h
            current_x += delta_x
            current_t += self.delta_t

            y.append(current_height)
            x.append(current_x)
            t.append(current_t)

#            print('- DEBUG -')
#            print(f'Pressure: {p}')
#            print(f'Temperature: {Temp}')
#            print(f'Air density (rho): {rho}')
#            print(f'Velocity: {Vmin}')
#            print(f'Thrust: {Th}')
#
#            print(Vmin)
#            print(RoC)
#            print(Th)
#            print(D)
#
        return(x, y)
    
#ES STARS TE UN LIMIT MASSA BAIX I LA TRAJECTORIA COINCIDEIX