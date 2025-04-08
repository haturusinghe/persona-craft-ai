# PersonaCraft.AI Project

## Installation

1. Install dependencies:
    - Partial installation:  
      poetry install --without aws  
    - Full installation:  
      poetry install

2. Install Poe plugin (one-time per system):
    poetry self add 'poethepoet[poetry_plugin]'

3. Test Poe with a sample task:
    - Run the task:
      poetry poe run-sample-hello  
    Expected output: hello poe is working
