#!/bin/bash

echo "🔁 Building Tex for RunPod (linux/amd64)..."
docker buildx build --platform linux/amd64 -t vortexblack/tex:latest . --push

echo "✅ Build + push complete. Restart your RunPod pod to apply changes."