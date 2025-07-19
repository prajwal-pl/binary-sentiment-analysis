FROM node:24-alpine3.21

WORKDIR /app

# Copy package.json and package-lock.json to leverage Docker caching
COPY package*.json ./

# Install dependencies and a simple HTTP server for reliable static file serving
RUN npm install && npm install -g serve

# Copy the rest of the application
COPY . .

# Create .env file with API URL pointing to the backend
RUN echo "VITE_API_URL=http://localhost:8000" > .env

# Build the application
RUN npm run build

# Expose port 3000
EXPOSE 3000

# Command to run the application using serve instead of Vite preview
# serve is more reliable for production-like environments
CMD ["serve", "-s", "dist", "-l", "3000", "-n"]