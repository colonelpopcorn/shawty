#!/usr/bin/env bash

# Build the client app
cd $(pwd)/clientapp
npm install
npm run prod

# Run the database migrations
cd ..

