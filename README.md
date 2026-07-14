# Python Instrument Logger

A Python toolkit that simulates an Automated Test Equipment (ATE) 
measurement environment. It models a measurement instrument with 
realistic noise, logs readings, computes statistics (min/max/avg), 
and flags measurements that fall outside defined pass/fail limits.

## Features

- **MockInstrument** — simulates a measurement device returning 
  readings around a nominal value with random noise.
- **MeasurementLog** — stores measurements and provides:
  - Latest reading lookup by name
  - Statistics (min, max, average) per parameter
  - Pass/fail checking against defined limits

## Usage

```python
# Create a simulated instrument and a logger
instrument = MockInstrument(nominal=12.5)
log = MeasurementLog()

# Take 10 measurements
for _ in range(10):
    reading = instrument.measure()
    log.add("TX_Power", reading, "dBm")

# Get statistics
print(log.stats("TX_Power"))

# Check against limits
limits = {"TX_Power": (12.0, 13.0)}
print(log.failures(limits))
```

## Requirements

- Python 3.12+

## Roadmap

- Replace MockInstrument with real hardware control (Signal Hound SA44B)
- Add PyVISA support for standard test instruments