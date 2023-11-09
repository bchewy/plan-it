# Plan-IT

![deploy to frontend](https://github.com/bchewy/plan-it/actions/workflows/deploy-to-s3.yml/badge.svg)
![deploy to backend](https://github.com/bchewy/plan-it/actions/workflows/deploy-flask-to-ec2.yml/badge.svg)

### What is Plan-it?
Plan-it is a sustainable travel routing web-app built on Google Maps to help users consciously keep track of their carbon emissions savings when commuting.

### What's the purpose?
To encourage green choices, we will implement gamification features like rewards and social sharing for selecting low-carbon routes. The app will also provide tools for tracking carbon footprint over time, optimized route planning based on sustainability, and a community forum for knowledge sharing around sustainable transportation. 

### Test account details (Google account)
Username: planituser27@gmail.com
Password: planit123

### ENV Configuration:
`frontend/`
```env
VITE_GMAPS_API_KEY=XYZ
VITE_GIFY_API_KEY=XYZ
VITE_AUTH0_DOMAIN=XYZ
VITE_AUTH0_CLIENTID=XYZ
VITE_API_KEY=XYZ
```
`backend/`
```env
MONGO_URI="mongodb_connection_string"
API_KEY="XYZ"
```
