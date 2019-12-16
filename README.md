# CircuitPython Adapter

This library aims to provide a translation layer from SMBus calls to CircuitPython i2c calls, to allow pre-existing code to run on CircuitPython with little to no modifications.

## Currently implements:

* `write_i2c_block_data`
* `read_i2c_block_data`
* `readfrom_mem`

# Example

Original Code:
```python
from smbus import SMBus
i2c_bus = SMBus(1)
```

Using CircuitPython Adapter:
```python
from pimoroni_circuitpython_adapter import not_SMBus as SMBus
i2c_bus = SMBus(1)
```