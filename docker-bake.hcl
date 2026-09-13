variable "IMAGE_NAMESPACE" {
  default = "edemy"
}

variable "IMAGE_TAG" {
  default = "local"
}

variable "IMAGE_SHA" {
  default = "sha-local"
}

variable "IMAGE_CHANNEL" {
  default = "local"
}

variable "GIT_SHA" {
  default = "local"
}

target "client" {
  context    = "./client"
  dockerfile = "Dockerfile"
  target     = "production"
  tags = [
    "${IMAGE_NAMESPACE}/edemy-client:${IMAGE_TAG}",
    "${IMAGE_NAMESPACE}/edemy-client:${IMAGE_SHA}",
    "${IMAGE_NAMESPACE}/edemy-client:${IMAGE_CHANNEL}",
  ]
  labels = {
    "org.opencontainers.image.title"    = "Edemy client"
    "org.opencontainers.image.vendor"   = "Edemy"
    "org.opencontainers.image.revision" = GIT_SHA
  }
  cache-from = ["type=gha,scope=client"]
  cache-to   = ["type=gha,mode=max,scope=client"]
}

target "server" {
  context    = "./server"
  dockerfile = "Dockerfile"
  target     = "production"
  tags = [
    "${IMAGE_NAMESPACE}/edemy-server:${IMAGE_TAG}",
    "${IMAGE_NAMESPACE}/edemy-server:${IMAGE_SHA}",
    "${IMAGE_NAMESPACE}/edemy-server:${IMAGE_CHANNEL}",
  ]
  labels = {
    "org.opencontainers.image.title"    = "Edemy server"
    "org.opencontainers.image.vendor"   = "Edemy"
    "org.opencontainers.image.revision" = GIT_SHA
  }
  cache-from = ["type=gha,scope=server"]
  cache-to   = ["type=gha,mode=max,scope=server"]
}

group "default" {
  targets = ["client", "server"]
}