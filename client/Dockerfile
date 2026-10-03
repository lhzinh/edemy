FROM dhi.io/bun:1-alpine-dev AS base

# Set working directory
WORKDIR /app


FROM base AS dependencies
WORKDIR /app

# Copy package-related files first to leverage Docker's caching mechanism
COPY package.json bun.lock* ./

RUN bun install --frozen-lockfile


FROM base AS development
WORKDIR /app

# Copy project dependencies from dependencies stage
COPY --from=dependencies /app/node_modules ./node_modules
COPY . .

ENV WATCHPACK_POLLING=true
ENV HOSTNAME="0.0.0.0"
ENV NODE_ENV=development

EXPOSE 3000

CMD ["bun", "dev"]


FROM base AS builder
WORKDIR /app

COPY --from=dependencies /app/node_modules ./node_modules
COPY . .

ENV NODE_ENV=production

RUN bun run build


FROM dhi.io/nginx:1.28.0-alpine3.21-dev AS production

# Copy custom Nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the static build output from the build stage to Nginx's default HTML serving directory
COPY --chown=nginx:nginx --from=builder /app/out /usr/share/nginx/html

# Non-root user for security best practices
USER nginx

# Expose port 8080 to allow HTTP traffic
EXPOSE 8080

# # Start Nginx directly with custom config
ENTRYPOINT ["nginx", "-c", "/etc/nginx/nginx.conf"]
CMD ["-g", "daemon off;"]
