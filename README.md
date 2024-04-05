# Simple Klipper Power Loss Recovery

I am currently working on a more complex approach of [Power Loss Recovery](https://klipper.discourse.group/t/wip-power-loss-recovery/14478), but while working on that, I made this simple power loss recovery script in Python, that can recover any print by the last recorded Z height. It works as follows:
1. Slicer's start G-Code ends with `; POWER_PANIC_PRESERVE`
2. Slicer's layer change G-Code will invoke `UPDATE_Z Z=` to set the z height
3. `UPDATE_Z` will save the variable to `variables.cfg`
4. When power is lost, you still have to manually heat up the bed
5. You can get the last recorded z from `variables.cfg`
6. Run the script: `python3 /path/to/script.py <Z HEIGHT FROM PREVIOUS STEP> <NAME OF GCODE FILE>`
7. Look in your G-Codes folder, and there should be a G-Code file that starts with `RECOVER-SOFT-`
8. Use `SET_KINEMATIC_POSITION Z=` to set the z height without homing Z
9. Use the move panel to move Z 10mm up
10. Run `G28 X Y` to home X and Y
11. For now, you will still need to edit your recovered G-Code to remove any homing G-Code from the start G-Code.
12. Set your velocity limit to something slow e.g. 20mm
13. Start the recovery G-Code and make sure your print doesn't fall off the bed.
14. Increase print speed slowly to avoid knocking the print off the bed.

[Config](https://github.com/3DCoded/klipper-simple-power-loss-recovery/blob/main/powerloss.cfg)

[Python Script](https://github.com/3DCoded/klipper-simple-power-loss-recovery/blob/main/powerloss.py)

Add the following to the end of your slicer's start G-Code (NOT in your `PRINT_START` macro if you have one)
```
; POWER_PANIC_PRESERVE
```

Add the following to your slicer's after layer change G-Code (this syntax is for PrusaSlicer)
```
UPDATE_Z Z=[layer_z]
```

If anyone finds this helpful or has ideas to improve it, please let me know [here](https://klipper.discourse.group/t/simple-power-loss-recovery/15534/1).
