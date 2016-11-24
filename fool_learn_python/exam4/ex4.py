#!/usr/bin/env python
# coding=utf-8

cars = 100
space_in_car = 4.0
drivers = 30
passenger = 90
cars_not_driven = cars - drivers
cars_driver = drivers
carpool_capacity = cars_driver * space_in_car
average_passengers_per_car = passenger / cars_driver


print ("There are",cars,"cars available")
print ("There are only ",drivers,"drivers available.")
print ("There will be ",cars_not_driven,"empty cars today.")
print ("We can transport",carpool_capacity,"people today.")
print ("We have",passenger,"to carpool today.")
print ("We need to put about",average_passengers_per_car,"in each car.")
