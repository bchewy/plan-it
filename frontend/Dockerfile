# Use the official Node.js 14 image as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install the dependencies
RUN npm install --legacy-peer-deps

# Copy the rest of the frontend files to the container
COPY . .

# Build the frontend
RUN npm run build

# Expose the port that the frontend will run on
EXPOSE 4173

# Start the frontend
CMD ["npm", "run", "preview"]