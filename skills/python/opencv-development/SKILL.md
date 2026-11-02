---
name: opencv-development
description: Develop and debug OpenCV image or video processing in Python. Use for cv2 pipelines, camera input, color conversion or image-processing correctness.
---

# Opencv development

Inspect input source, shape, dtype, color space, value range and expected output. Obtain a small representative image or clip and preserve it for comparison where permitted. Distinguish algorithm errors from input/codec/backend failures.

Make BGR/RGB, grayscale and alpha conversions explicit. Check coordinate conventions, resize interpolation, contour/mask dimensions and integer overflow. Check capture/read return values and release camera/video resources. Avoid GUI dependencies in headless environments; choose one compatible OpenCV package variant.

Use deterministic synthetic inputs to verify geometric or numeric transformations where useful. Evaluate real samples across relevant lighting, scale and motion conditions. Measure latency/throughput before optimizing; do not assume acceleration is available.

Report input assumptions, verified behavior, package/backend requirements and limits. Avoid claiming robustness from a single favorable frame.
