from datetime import datetime
import random

class MeasurementLog:
    def __init__(self):
        self.measurements = []

    def __len__(self):
        return len(self.measurements)

    def __repr__(self):
        measurements_names_list= [measurement["name"] for measurement in self.measurements]
        measurements_names = set(measurements_names_list)
        return f"Total measurements - {len(self.measurements)}, Measurements name {measurements_names}"

    def add(self, name, value, unit):
        measurement = {
            "name": name,
            "value": value,
            "unit": unit,
            "timestamp": datetime.now()
        }
        self.measurements.append(measurement)

    def get_latest(self, name):
        matching = [measurement for measurement in self.measurements if measurement["name"] == name]
        if matching:
            return matching[-1]
        return None

    def stats(self, name):
        values = [measurement["value"] for measurement in self.measurements if measurement["name"] == name]
        if not values:
            return None
        return {
            "min": min(values),
            "max": max(values),
            "avg": sum(values) / len(values)
        }

    def failures(self, limits):
        result = [] # New list for failures

        for measurement in self.measurements:
            name = measurement["name"]
            if name in limits:
                low, high = limits[name]
                if not low <= measurement["value"] <= high:
                    result.append(measurement) # add the failed measurement
        return result

    def clear(self):
        self.measurements = []


class MockInstrument:
    def __init__(self, nominal):
        self.nominal = nominal

    def measure(self):
        noise = random.uniform(-0.1,0.1)

        return self.nominal + noise





#log.add("RX_Power", 11.8, "dBm")
#log.add("TX_Power", 12.0, "dBm")

# print(log.measurements)
# print(type(log.measurements))

# print(log.get_latest("RX_Gain"))
# print(log.get_latest("TX_Power"))

# print(log.stats("TX_Power"))



# Mock instrument
mock_inst = MockInstrument(nominal=12.5)

# Logger
log = MeasurementLog()

# Get 10 measurements
for i in range(10):
    mock_inst_value = mock_inst.measure()
    log.add("TX_Power", mock_inst_value, "dBm")

display_rounded_stats = log.stats("TX_Power")
print(f"min = {display_rounded_stats['min']:.2f}, max = {display_rounded_stats['max']:.2f}, avg = {display_rounded_stats['avg']:.2f}")



limits = {"TX_Power": (12.0, 12.5)}
print(log.failures(limits))
