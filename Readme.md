# BOFA 2022 (GMOT)
## Requirements
Only need docker compose installed on your system (tested on v2.6.1). Make sure you have the docker daemon running before you begin.

## Configuration
Database configuration details are found in database.env, which you can change as needed.

## Setup
Javascript files are renamed with the .myjs extension for transfer via email. Before starting the project, rename them back by running ```for /R %x in (*.myjs) do ren "%x" *.js```

## Instructions
From the root of the project, run ```docker compose up --build``` to build and start all the components of the system. The frontend will be available at localhost:3000 after a short delay.