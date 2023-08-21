# Route Obstruction Detection Module - Readme

This repository contains an Object Oriented Programming (OOP) based solution for the task of calculating and detecting obstructions in a route between two locations within the context of a scientific exhibition project. The purpose of this module is to assist explorers in determining the best route to follow while digging to the core of the earth. The module will assess whether there are any impenetrable obstructions between two given locations and provide relevant information based on the calculated expected time and the actual time duration.
Table of Contents

    Introduction
    Class Documentation
    Example Usage
    Assumptions

## Introduction

In this project, I have implemented an OOP solution that adheres to the guidelines provided. The Route Obstruction Detection Module is designed to receive two location points and evaluate whether there are any obstructions between them. The primary objective is to determine if there are impenetrable obstructions based on the expected time and the actual time taken to travel between the two points.
Usage

    Clone this repository to your local machine.
    Use the provided classes and methods to integrate the Route Obstruction Detection Module into your project.
    Ensure that you have access to the TimeDuration module, which calculates the time taken to travel between two points.
    Use the RouteObstructionDetector class to detect obstructions and impenetrable obstructions between two locations.

## Class Documentation
### RouteObstructionDetector

A class that implements the route obstruction detection functionality.
Methods

    __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b
        self.speed = 0.7
        self.distance = self.distance()
        self.exp_time = self.distance / self.speed
        self.obs_time = TimeDurationModule().sim_time
## Example Usage

### python

###  create the Obstruction object and usee the check_result method to determine the result
    y = RouteObstructionDetector(point_a = [53.5872,-2.4138], point_b = [53.474,-2.2388])
    print(y.check_result())
    True

## Assumptions

    The TimeDuration module is provided and simulates the time taken to travel between two locations.
    The speed, distance, and expected time are provided as parameters to the RouteObstructionDetector class.
    The actual time taken is provided for obstruction detection.
    The speed, distance, and expected time are not hardcoded within the module to ensure flexibility for various scenarios.