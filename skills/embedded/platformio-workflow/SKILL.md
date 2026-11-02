---
name: platformio-workflow
description: Build, test and troubleshoot PlatformIO firmware projects. Use for platformio.ini environments, board dependencies, firmware builds, device upload or serial monitoring.
---

# Platformio workflow

Read platformio.ini, project instructions, board details and existing environments. Identify the exact board, framework, platform/toolchain version and intended environment; inspect installed CLI help when needed.

Keep environment-specific build flags, libraries, partitions and upload settings explicit. Preserve known-compatible pins. Build the selected environment and run available host/embedded tests, distinguishing simulation from hardware results.

Before upload, confirm the physical device and serial/debug port, firmware target and authorization. Do not choose an arbitrary connected device or erase flash/fuses as a routine retry. Consider persistent settings, partition changes and a recovery path for bootloader or OTA changes.

After upload, inspect bounded serial output and the relevant device behavior. Report the environment, build/test results and hardware verification separately. If hardware is unavailable, state that flashing and runtime behavior remain unverified.
