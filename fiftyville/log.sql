-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Theft took place on July 28
-- Theft was at Chamberlin Street
-- Who is the thief?
-- Where did the thief escape to?
-- Who is the thief's accomplice who helped them escape?

-- Start by looking at crime_scene_reports table, since we know day and location
-- Find out what the description is
SELECT description
FROM crime_scene_reports
WHERE day = 28 AND month = 7 AND year = 2021
AND street = "Humphrey Street";
-- Two incidents happened that day. One was the theft of the CS50 duck, other was littering
-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time
-- Each of their interview transcripts mentions the bakery.
-- Find the transcript and names of those who gave interviews
SELECT name, transcript
FROM interviews
WHERE day = 28
AND month = 7
AND year = 2021
AND transcript LIKE "%bakery%";
-- Ruth: Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.
-- Eugene: I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
-- Raymond: As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.

-- Start by checking the bakery security logs for those who exited within 10 minutes of the crime
SELECT license_plate
FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute <= 25
AND minute >= 15
AND activity = "exit";
-- Gives us a list of 8 license plates: 8 suspects.
-- Let's find the list of people's names. This will begin our running list of suspects.

SELECT name
FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute <= 25
AND minute >= 15
AND activity = "exit";

-- Running list of suspects: Vanessa, Bruce, Barry, Luca, Sofia, Iman, Diana, Kelsey

-- Get a list of people who used the ATM that morning, since the thief was seen using the ATM at Leggett Street before the incident
SELECT name
FROM people
JOIN bank_accounts
ON people.id = bank_accounts.person_id
JOIN atm_transactions
ON atm_transactions.account_number = bank_accounts.account_number
WHERE year = 2021
AND day = 28
AND month = 7
AND atm_location = "Leggett Street"
AND transaction_type = "withdraw";

-- List of names for those who withdrew money that day: Bruce, Diana, Brooke, Kenny, Iman, Luca, Taylor, Benista
-- Those who fit on both lists: Bruce, Diana, Iman, Luca

-- Find a log of people who made phone calls at the time:
SELECT name
FROM people
JOIN phone_calls
ON people.phone_number = phone_calls.caller
WHERE year = 2021
AND month = 7
AND day = 28
AND duration <= 60;
-- Names of those who MADE calls less than a minute: Sofia, Kelsey, Bruce, Kathryn, Kelsey, Taylor, Diana, Carina, Kenny, Benista
-- Names of those on all 3 lists: Bruce, Diana

-- Get list of receivers' names (possible accomplices:)
SELECT name
FROM people
JOIN phone_calls
ON people.phone_number = phone_calls.receiver
WHERE year = 2021
AND month = 7
AND day = 28
AND duration <= 60;
-- Receiver's names: Jack, Larry, Robin, Luca, Melissa, James, Philip, Jacqueline, Doris, Anna

-- The thief asked someone to book the first flight out of fiftyville the next morning
SELECT abbreviation, full_name, city
FROM airports
WHERE city = "Fiftyville";
-- CSF airport
SELECT abbreviation, full_name, city
FROM airports
JOIN flights
ON flights.destination_airport_id = airports.id
WHERE origin_airport_id IN (
    SELECT id
    FROM airports
    WHERE city = "Fiftyville"
)
AND year = 2021
AND month = 7
AND day = 29
ORDER BY hour, minute;

-- The earliest flight is the one from Fiftyville to LaGuardia
-- Who was on the flight?

SELECT name
FROM people
JOIN passengers
ON people.passport_number = passengers.passport_number
JOIN flights
ON passengers.flight_id = flights.id
JOIN airports
ON airports.id = flights.destination_airport_id
WHERE people.passport_number IN (
    SELECT passport_number
    FROM passengers
    WHERE flight_id
    IN (
        SELECT id
        FROM flights
        WHERE destination_airport_id IN (
            SELECT id
            FROM airports
            WHERE abbreviation = "LGA"
        )
    )
)
ORDER BY name;

-- Bruce must be the person who committed the crime since he is the only person on all four of these lists
-- Bruce was seen exiting the bakery within 10 minutes of the crime
-- He made an ATM transaction at Leggett Street
-- He had a phone call less than 1 minute
-- He was on a flight the next day to NYC.
-- Bruce escaped to Laguardia airport in NYC

-- Who is the accomplice?

SELECT name
FROM people
JOIN phone_calls
ON people.phone_number = phone_calls.receiver
WHERE year = 2021
AND month = 7
AND day = 28
AND duration <= 60
AND caller IN (
    SELECT phone_number
    FROM people
    WHERE name = "Bruce"
);

-- Robin is the accomplice, since this is the person Bruce called on 7/28 to book his flight to LGA>