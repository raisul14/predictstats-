FROM node:18-alpine

WORKDIR /app
COPY frontend/package*.json ./
RUN npm ci

COPY frontend/ .

RUN npm run build

CMD ["npm", "start"]
