#!/usr/bin/env python
__author__ = 'Aaron Otillar'
Version = 1.0

import math
import sys
from random import *
import numpy
from NameGenerator import generate_name

#sys.stdout = open('C:\\Users\\aotillar\Desktop\SolarSystem_01.txt', 'w')

G = 6.67259 * 10 ** -11


def roll_dice(N, S):
    '''Sum of N dice with S sides'''
    value = 0
    for i in range(N):
        value += randrange(0, S + 1)
    return value


class Star:
    '''This class defines what a star is. It has all of the attributes necessary to describe a star, as well as methods
    to give it a name, randomly generate its stats, and cassify it according to modern classification systems.'''

    def __init__(self):
        self.mass = 0
        self.radius = 0
        self.luminosity = 0
        self.temperature = 0
        self.classification = ''
        self.color = ''
        self.name = ''
        self.habitable_upper = 0
        self.habitable_lower = 0

    def description(self):
        """Returns the Description of this star."""
        return str('This Star is a', self.classification, ' star.')

    def generatename(self):
        """Assigns a name to the star, so it is not just a string of letters and numbers."""
        letters = 'abcdefghijklmnopqrstuvqxyz'
        numbers = '0123456789'
        name = generate_name()
        self.name += name
        self.name += ' '

        for i in range(2):
            letter = letters[randrange(0, len(letters) - 1)].capitalize()
            number = numbers[randrange(0, len(numbers) - 1)]

            self.name += number
            self.name += letter

    def generatestats(self):
        '''Rolls 7, 4 sided dice and adds them up. Classifies a star according to surface temperature
        based on the value of the roll. If the value is higher than 18, a second roll is used.

        This is obviosduly built from a table of values that bases luminosity, radius, and mass based off temperature.
        '''
        roll1 = roll_dice(7, 4)
        roll2 = -1
        if 15 <= roll1 < 18:
            self.temperature = uniform(5200.0, 6000.0)
        if 13 <= roll1 <= 15:
            self.temperature = uniform(3700.0, 5200.0)
        if 11 <= roll1 <= 13:
            self.temperature = uniform(2400.0, 3700.0)
        if 11 > roll1 or roll1 >= 18:
            roll2 = uniform(0.0, 1.0)

        if 0.0 <= roll2 <= 0.25:
            self.temperature = uniform(6000.0, 7500.0)
        if 0.25 <= roll2 <= 0.5:
            self.temperature = uniform(7500.0, 10000.0)
        if 0.5 <= roll2 <= 0.75:
            self.temperature = uniform(10000.0, 30000.0)
        if 0.75 <= roll2 <= 1.0:
            self.temperature = uniform(30000, 31000.0)

        if 2400.0 < self.temperature < 3700.0:
            self.mass = uniform(0.08, 0.45)
            self.radius = uniform(0.0, 0.7)
            self.luminosity = uniform(0.0, 0.08)
            self.classification = 'M'

        if 3700.0 < self.temperature < 5200.0:
            self.mass = uniform(0.45, 0.8)
            self.radius = uniform(0.7, 0.96)
            self.luminosity = uniform(0.08, 0.6)
            self.classification = 'K'
        if 5200.0 < self.temperature < 6000.0:
            self.mass = uniform(0.8, 1.04)
            self.radius = uniform(0.96, 1.15)
            self.luminosity = uniform(0.6, 1.5)
            self.classification = 'G'
        if 6000.0 < self.temperature < 7500.0:
            self.mass = uniform(1.04, 1.4)
            self.radius = uniform(1.15, 1.4)
            self.luminosity = uniform(1.5, 5)
            self.classification = 'F'
        if 7500.0 < self.temperature < 10000.0:
            self.mass = uniform(1.4, 2.1)
            self.radius = uniform(1.4, 1.8)
            self.luminosity = uniform(5.0, 25.0)
            self.classification = 'A'
        if 10000.0 < self.temperature < 30000.0:
            self.mass = uniform(2.1, 16.0)
            self.radius = uniform(1.8, 6.6)
            self.luminosity = uniform(25, 30000.00)
            self.classification = 'B'
        if 30000.0 < self.temperature:
            self.mass = uniform(16.0, 10000.00)
            self.radius = uniform(6.6, 10000.00)
            self.luminosity = uniform(30000.0, 250000.0)
            self.classification = 'O'

    def ri(self):
        ''' Sets the habitable upper bound for a star in AU. This is as far out from a star a planet can be
        that water could hypothetically be liquid '''
        upperbound = math.sqrt(self.luminosity / 1.1)
        self.habitable_upper = upperbound

    def ro(self):
        '''Sets the habitable lower bound for a star in AU. This is as far out from a star a planet can be
        that water could hypothetically be liquid'''
        lowerbound = math.sqrt(self.luminosity / 0.53)
        self.habitable_lower = lowerbound


class Planet:
    '''A Class that determines all of the characteristics of a randomly generated planet. It also houses all
    of the necessary fields for orbit calculations, however these are left blank until more learning can be done
    on the subject of simulated orbits.'''

    def __init__(self):
        self.name = ''
        self.mass_kg = 0
        self.mass_earth = 0
        self.equitorial_Diameter = 0
        self.radius_m = 0
        self.radius_earth = 0
        self.orbital_period = 0
        self.rotation_period = 0
        self.moons = 0
        self.axial_tilt = 0
        self.atmosphere = False
        self.habitable = False

        self.eccentricity = 0
        self.semi_major_axis = 0
        self.semi_minor_axis = 0
        self.apogee = 0
        self.perigee = 0
        self.inclination = 0
        self.longitude_ascending_node = 0
        self.argument_of_periapsis = 0
        self.mean_anonomly = 0

        self.surface_area = 0
        self.density = 0
        self.volume = 0

    def generate_name(self, starname):
        '''Same as star name generator, except it uses the Stars Name as the base for all planet names. '''
        letters = 'abcdefghijklmnopqrstuvqxyz'
        numbers = '0123456789'
        self.name += starname
        self.name += ' '

        for i in range(2):
            letter = letters[randrange(0, len(letters) - 1)].capitalize()
            number = numbers[randrange(0, len(numbers) - 1)]
            self.name += number
            self.name += letter

    def generate_stats(self, upperlimit):
        '''This Function generates the random characteristics for the planet. It starts out by randomly assigning
        a mass in Earth masses to the planet. Then it converts that mass into kg. It randomizes the
        semi-major axis of the planets orbit based on its parents star habitable upper bound of life, times 10.
        This function also asigns moons to the planet, which will be described and formed in a separate function.'''
        # MASS
        #
        # What is needed now is to simulate the fact that planets are much smaller the closer they are to the sun, and
        # much larger the farther away they are from the sun. This might mean basing the mass and radius first on
        # distance from the sun, then on their relationship to one another.
        """Another consideration for this function is to calculate mass and radius based"""

        mass = uniform(0.05, 315.0)
        self.mass_earth = mass
        self.mass_kg = mass * (5.79219 * 10 ** 24)

        # Radius -
        # This Calculation uses a table to create radius based on Real solar system ratios of Mass to Radii
        # This Table will hopefully be updated as more information is gatthered. Units are in Earth Mass and Radius
        #
        # Mass < 1 <-> r < 1
        # 150 > mass > 1  <->  10 > r > 1
        # mass > 150 <-> r > 10
        #
        # After more research, maybe we should generate the radius and then base the mass off the radius.

        if self.mass_earth < 1.0:
            self.radius_earth = uniform(0.5, 1.0)
        if 150 > self.mass_earth > 1:
            self.radius_earth = uniform(1, 10.00)
        if self.mass_earth > 150.00:
            self.radius_earth = uniform(10.00, 60.00)

        # Here we convert from Earth Radii to Radii in M

        self.radius_m = self.radius_earth * (6.3781 * 10 ** 6)

        # Eccentricity

        self.eccentricity = abs(numpy.random.normal(.08, .09, 1)[0])

        # Semi-Major-Axis

        self.semi_major_axis = uniform(0.25, upperlimit * 10)

        # Semi Minor axis
        # The equation is b = a(sqrt(1-e^2))
        e2 = self.eccentricity ** 2
        b = 1 - e2
        self.semi_minor_axis = self.semi_major_axis * math.sqrt(b)

        # Apogee and Perigee
        a = 1 + self.eccentricity
        b = 1 - self.eccentricity
        self.apogee = self.semi_major_axis * a
        self.perigee = self.semi_major_axis * b

        # Volume
        self.volume = (4 / 3) * math.pi * self.radius_m ** 2

        # Surface Area
        self.surface_area = 4 * math.pi * self.radius_m ** 2

        # Density
        self.density = self.mass_kg / self.volume

        # Moons
        # roll1 = roll_dice(2, 4)
        # roll2 = roll_dice(2, 4)
        # self.moons = min(roll1, roll2)
        self.moons = math.floor(numpy.random.uniform(0, 8))

    def calculate_orbital_period(self, sMass):
        '''This function calculates orbital period. I will get back to you on the math.

        2022 Here: This formula is based off of keplers third law and newtons law of gravitation.
        Substituting newtons law into Keplers law leaves us with an equation
        T^2 = k*a^3 where k = 4pi^2*a^3/GM where G is the universal gravitational constant and M is the
        larger mass, typically the sun. This equation can also work for satelites, and moons of planets.
        In almost all cases in space where the larger mass is typically tens of orders of magnitude larger than
        the smaller mass, (earth and an artifical satelite) the smaller mass is neglagible.
        '''
        # Convert all numbers into like units
        starMass = sMass * (1.98855 * 10 ** 30)
        a = self.semi_major_axis * (1.4960 * 10 ** 11)

        # Calculate Gravitational Constant
        u = G * (starMass + self.mass_kg)

        # Calculate T in seconds
        t = 2 * math.pi * (math.sqrt((a ** 3) / u))

        thour = t / 3600
        tday = thour / 24
        tyear = tday / 365
        self.orbital_period = tyear


class SolarSystem:
    '''This class houses containers for a parent star, and its planetary children. This Class Randomly generates a star
    and then randomly generates, planet(s) for that parent star. It uses the functions contained in all of the children
    classes, to determine all of the stats for each of the celestial bodies.'''

    # After we generate the planets distance and sort them out, we then need to calculate all of their stats, with regards
    # to their parent star and their distance away from that star. If we have an interval of distance from 0-100 Au, there
    # needs to be a distribution function that determines mass, and radius based on the where the planet falls in that
    # interval
    # Something like
    # 0-5 AU = radius = .5 Earth Radii - 1.5 earth Radii
    # 5-30 AU = Radius = 3.0 Earth Radii - 15 Earth Radii
    #
    # Then after we calculate the radius of the planet, we can then calculate the mass of the planet followed by all
    # of the other parameters.
    #
    #
    #

    def __init__(self):
        self.stars = []
        self.planets = []
        self.habitable = 0

    def generate_stars(self, n):
        '''Assigns a star to variable a, calls the parent functions of the star class, generate name, generate stats,
        upper bound, lower bound. Then appends the star to the Solar Systems class container of stars.'''
        for star in range(n):
            a = Star()
            a.generatename()
            a.generatestats()
            a.ri()
            a.ro()
            self.stars.append(a)

    def generate_planets(self, planet_limit):
        '''This function generates planets for each solar system class object. It uses a bound of planet limit,
         that is set later on in the program to determine the maximum number of planets a solar system can have.
         Then it creates an instance of the planet class and assigns it to variable P. Then it proceeds to call out
         the various parent functions of the Planet class to randomly generate stats for each planet.Finally
         it uses a loop to call out each of the planets in the planet list, checks to see if each planets
         semi major axis lies within the upper and lower bounds of the habitable zone of the planet, and then assigns
         each planets Habitable tag to true or false'''
        for i in range(0, randrange(0, planet_limit)):
            p = Planet()
            p.generate_name(self.stars[0].name)
            p.generate_stats(self.stars[0].habitable_upper)
            p.calculate_orbital_period(self.stars[0].mass)
            if self.stars[0].habitable_upper <= p.semi_major_axis <= self.stars[0].habitable_lower:
                p.habitable = True
            self.planets.append(p)

    def sort_planets(self):
        '''This function uses a lambda function to sort all of the planets from closest to the sun,
        to farthest away from the sun'''
        a = sorted(self.planets, key=lambda planet: planet.semi_major_axis)
        self.planets = a

    def calculate_habitable(self):
        '''This Function ccles through all of the planets and creates a Habitable Planet Stat that allows the user
        to esil identify if this solar system has any habitable planets or not.'''

        for i in range(len(self.planets)):
            if self.planets[i].habitable:
                self.habitable += 1


class Cluster:
    '''This Class is just a test dummy to put all of the classes to work, and to visualize the information
    in a visual manner. It Houses a container of Solar Systems. A few static variables that give the reader
    information about the number of planets. It also houses a number of functions for Actually creating Stars and
    their planets.'''

    def __init__(self):
        self.localcluster = []
        self.total_planets = 0
        self.habitable = 0
        self.star_classes = {}

    def generate_stars(self, star_amount, planet_amount):
        '''Star Ammount, Planet Amount'''
        for i in range(star_amount):
            a = SolarSystem()
            a.generate_stars(1)
            a.generate_planets(planet_amount)
            a.sort_planets()
            a.calculate_habitable()
            self.localcluster.append(a)

    def clear_cluster(self):
        self.localcluster = []

    def calculate_star_stats(self):
        '''Generate Stats for all stars in the cluster'''
        self.star_classes["m"] = 0
        self.star_classes["k"] = 0
        self.star_classes["g"] = 0
        self.star_classes["f"] = 0
        self.star_classes["a"] = 0
        self.star_classes["b"] = 0
        self.star_classes["o"] = 0
        for star in range(len(self.localcluster)):
            if self.localcluster[star].stars[0].classification == 'M':
                self.star_classes["m"] += 1
            if self.localcluster[star].stars[0].classification == 'K':
                self.star_classes["k"] += 1
            if self.localcluster[star].stars[0].classification == 'G':
                self.star_classes["g"] += 1
            if self.localcluster[star].stars[0].classification == 'F':
                self.star_classes["f"] += 1
            if self.localcluster[star].stars[0].classification == 'A':
                self.star_classes["a"] += 1
            if self.localcluster[star].stars[0].classification == 'B':
                self.star_classes["b"] += 1
            if self.localcluster[star].stars[0].classification == 'O':
                self.star_classes["o"] += 1

        for system in range(len(self.localcluster)):
            self.habitable += self.localcluster[system].habitable
            self.total_planets += len(self.localcluster[system].planets)

        print(' Star Class Totals for this Cluster')
        print(' M:', self.star_classes["m"], 'K:', self.star_classes["k"], 'G:', self.star_classes["g"],
              'F:', self.star_classes["f"], 'A:', self.star_classes["a"], 'B:', self.star_classes["b"],
              'O:', self.star_classes["o"])
        print()
        print(' Total Number of Habitable Planets in this Cluster')
        print(' ', self.habitable, ' Out of ', self.total_planets, ' total.')

        for system in range(len(self.localcluster)):
            print()
            print('Solar System:', system)
            print('Habitable Planets in this System:', self.localcluster[system].habitable,
                  ' Out of ', len(self.localcluster[system].planets), ' Total Planets')
            print('Star Name', self.localcluster[system].stars[0].name)
            print('     Classification', self.localcluster[system].stars[0].classification)
            print('     Temperature', self.localcluster[system].stars[0].temperature, ' Kelvin')
            print('     Mass', self.localcluster[system].stars[0].mass, 'Solar Mssses',
                  self.localcluster[system].stars[0].mass * (1.98855 * 10 ** 30), ' Kilograms')
            print('     Radius', self.localcluster[system].stars[0].radius, 'Solar Radii',
                  self.localcluster[system].stars[0].radius * (6.955 * 10 ** 30), ' Meters')
            print('     Luminosity', self.localcluster[system].stars[0].luminosity)
            print('     Habitable Zone Upper Bound', self.localcluster[system].stars[0].habitable_upper, ' AU')
            print('     Habitable Zone Lower Bound', self.localcluster[system].stars[0].habitable_lower, ' AU')
            print('------------------------------------------------------------------------------')
            for planet in range(len(self.localcluster[system].planets)):
                print()
                print('         Planet Name', self.localcluster[system].planets[planet].name)
                print('         Semi Major Axis', self.localcluster[system].planets[planet].semi_major_axis, ' AU')
                print('         Semi Minor Axis', self.localcluster[system].planets[planet].semi_minor_axis, ' AU')
                print('         Apogee', self.localcluster[system].planets[planet].apogee, ' AU')
                print('         Perigee', self.localcluster[system].planets[planet].perigee, ' AU')
                print('         Eccentricity', self.localcluster[system].planets[planet].eccentricity)
                print('         Volume', self.localcluster[system].planets[planet].volume, 'm^3'),
                print('         Density', self.localcluster[system].planets[planet].density),
                print('         Surface Area', self.localcluster[system].planets[planet].surface_area, 'm^2'),
                print('         Mass', self.localcluster[system].planets[planet].mass_kg, ' Kg',
                      self.localcluster[system].planets[planet].mass_earth, ' Earth Masses')
                print('         Radius', self.localcluster[system].planets[planet].radius_m, 'Meters',
                      self.localcluster[system].planets[planet].radius_earth, 'Earth Radii')
                print('         Orbital Period', self.localcluster[system].planets[planet].orbital_period,
                      'Earth Years')
                print('         Moons', self.localcluster[system].planets[planet].moons)
                print('         Habitable', self.localcluster[system].planets[planet].habitable)
        print('---------------------------------------------------')


aaron = Cluster()
aaron.generate_stars(5, 5)
aaron.calculate_star_stats()
aaron_dict = vars(aaron)
